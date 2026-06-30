# Footage Transformation (Video-to-Video)

Decision rules for **editing a clip the user already has** rather than building a
scene from scratch: keep a real subject and the real camera move, change only what
they ask for. This is the video-to-video (v2v) discipline. It is model-agnostic —
Seedance, Runway, Kling, Wan, and Veo all do v2v — so the craft below is written
neutrally; the per-model *syntax* (how you declare the source clip, input limits,
audio flags) lives in each model doc. Use this with the `footage-transform` skill,
which orchestrates source → model → prompt.

Each entry uses the library's decision-unit format:
**Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The core idea: preserve, then change one thing

A transformation prompt has two jobs that pull against each other: **lock**
everything that makes the source recognizable (identity, face, wardrobe,
performance, framing, lens, and camera motion), and **change** only the named
element. Under-specify the lock and the model re-rolls the face or the camera, and
the edit stops matching the original. So every prompt states **both halves
explicitly**, and repeats the most fragile guardrail — usually *"face and identity
unchanged"* — at the end of the action.

- **Use when:** any time a real clip is the starting point and only part of it
  should change.
- **Because:** v2v models will happily regenerate the whole frame; what you don't
  lock, you lose.
- **Prompt translation:** open with a source declaration that names what to
  preserve *exactly* and what single thing to change; close with a lock-down
  clause restating the fragile guardrail.
- **Watch-outs:** vague locks ("keep it similar") drift; name the specific
  attributes (identity, wardrobe, framing, camera move).
- **Anchors:** compositing first principles — match, then integrate, then sell.

## 2. Inspect the source before you write

Before writing the source declaration for a clip you can open, **probe it**: read
duration / fps / aspect and extract a few frames. Build the declaration and the
runtime from what the footage actually shows — subject, wardrobe, framing, camera
move, time of day, key direction — not from the user's one-line summary. Default
the output duration to the probed runtime. If no source clip is described, ask what
footage they're starting from before writing anything.

---

## 3. Two transformation modes

### A. Add an element to the footage

Set a head on fire, transform a hand, make a limb invisible, perch a creature on a
landmark. Keep the whole plate; layer the effect in.

- **Use when:** the plate stays, something new appears inside it.
- **Because:** an added element only reads as real if it obeys the plate's physics
  and light — presence alone looks pasted on.
- **Prompt translation:** describe the effect's **behavior over time** (where it
  starts, how it spreads, what light it throws), and make it **interact with the
  plate** (firelight flickering on a face and spilling onto nearby surfaces; a
  glassy invisible arm refracting the background; a giant creature casting a real
  soft-edged contact shadow on what it grips). State **scale explicitly** for giant
  creatures or the model renders them life-size ("enormous, dwarfing the structure,
  clearly colossal"). The subject usually stays **oblivious / unfazed**, mid-action
  — that contrast is often the point; say so.
- **Watch-outs:** "fire" with no behavior reads flat — specify ignition, spread,
  flicker. Forgetting scale yields a normal-sized creature.
- **Anchors:** effects animation (physics over presence); plate interaction.

### B. Replace the environment around a preserved subject

Keep the person, their vehicle, the seatbelt, the camera rig and its move; swap the
whole world.

- **Use when:** subject and camera stay, the world changes.
- **Because:** a new world only sits behind a real subject if it **streams past
  with parallax** consistent with the original motion.
- **Prompt translation:** preserve subject + vehicle + rig + motion; describe the
  new world rushing past at the original speed with matching parallax; relight to
  match (see §4).
- **Watch-outs:** **warm, directional daylight worlds are safer** for identity than
  night or neon, which force a full relight of the subject and raise drift risk.
  Flag the tradeoff and bake the relight instruction in when the user wants
  night/neon anyway.
- **Anchors:** background plate replacement; parallax continuity.

---

## 4. Lighting integration — the part that makes or breaks it

First decide the fork with the user; it changes everything:

- **Preserve the subject's light, grade only the new elements.** Light and grade the
  added creature/environment to match the existing key on the subject. **Lowest
  identity risk.**
- **Relight the whole frame under one look** (subject included). For a unified
  cinematic/commercial grade. **Higher risk to the face** — keep
  identity/expression/wardrobe explicitly locked while only lighting and grade
  change.

Color matching alone is **not enough** to make a preserved subject sit in a new
world — that's the most common "looks pasted in" failure. Go beyond color:

- **Light:** same key direction (name it — screen-left or screen-right), same
  softness, same shadow density and direction across the subject.
- **Environmental bounce:** let the world spill onto the subject — cool skylight
  from above, a warm bounce from sunlit ground/foliage, subtle ambient occlusion
  where forms meet.
- **Optics & atmosphere:** match lens character and micro-contrast; add a touch of
  the scene's haze over the subject so they aren't unnaturally crisp against a hazy
  background; match depth of field, focus falloff, and grain to the rest of frame.
- **Edges & grounding:** remove hard cut-out edges, halos, and mismatched rims;
  ground the subject with believable depth so they occupy the same space.

State time of day and key direction concretely ("soft, diffused midday daylight,
key from screen-right"). "Softer" = a larger, more diffuse source: gentle
soft-edged shadows, low contrast, smooth highlight rolloff, light haze.

## 5. Photoreal element / creature integration

When an added element must read as real:

- Demand documentary/practical realism explicitly: "fully photoreal, real fur with
  depth and individual strands (or true scale detail / brushed metal), true anatomy,
  **never CG, plastic, or cartoonish**."
- Tie it into the plate: same sun direction and color temperature as the subject,
  real soft-edged contact shadow on what it touches, same haze and depth as the far
  background.
- If it still reads as CG after a take, the reliable fix is a **second input** — a
  reference photo of the real animal/material — declared as a **texture-only**
  reference (appearance only; ignore its background and lighting). Repoint the
  element at it.
- **Behavior must match the species/material:** a sloth shifts slow heavy weight; a
  chimp is alert and twitchy; a snake's coils tighten and a forked tongue tastes the
  air (and snakes don't blink — use an unblinking stare, not a blink, for a reptile
  payoff).

---

## 6. Timed camera moves synced to dialogue

A crash zoom or smooth push-in landing on a beat is a recurring payoff. Anchor it
**two ways at once** so it lands even if the model's internal timing drifts:

- **Semantic:** `On the line "<exact words>," the camera <snaps into a hard crash
  zoom | begins a smooth, steady push-in>…`. Requires the model's "keep source
  dialogue" audio mode so the talk track survives.
- **Numeric:** `At about <T> seconds… the camera…`. Get `T` by measuring the source
  audio.
- **Crash zoom** = fast hard punch-in; **smooth push-in** = slow steady glide, no
  snap. Match the user's word exactly.
- If a landmark or subject must stay visible **through** the move, say so ("the tower
  stays in frame throughout, never cropped").
- Leave enough **tail** after the trigger for the payoff to play (a creature slowly
  turning to camera needs ~2–3s). On a short clip, fire on the *first word* rather
  than after the line.

### Reveal pull-back (the outward move)

The mirror of the push-in: open tight on the *added* element in isolation — a
long-telephoto, compressed framing with the subject out of frame — then move outward
to land on the real plate. Match the user's word: **hard/snap zoom-out** (fast punch
outward) vs **smooth pull-back** (slow decompression). Anchor the landing the same
two ways, and demand a **100% match of the source composition** at the landing —
name the matched attributes (angle, headroom, horizon, lens character) or the model
lands on a near-miss framing that no longer cuts against the original. After the
landing, hand off to the preserved take and keep the source's own camera motion.

### Preserving lip-sync to a known line

Quote the line **verbatim** and anchor it twice: inside the action ("…lips matching
the source exactly, saying clearly: '<line>'…") and in the audio/dialogue line.
Require the model's keep-source-dialogue mode and add "lips matching the source
exactly" to the lock-down clause. Then check the line against the surviving dialogue
window (see §7) — a line that runs ~6s cannot sit in a 5s tail. If it doesn't fit,
resolve the runtime before delivering; don't ship a prompt that can't lip-sync.

---

## 7. Duration discipline

Default to the source clip's exact runtime. When the user changes the runtime,
**recompute** any numeric zoom timing and tell them the new mark. When a long hold
lands on a static element, add small "living" micro-movements (a slow blink, jaw
shift, steady breath) so it doesn't look frozen.

### Prepended-intro budget: intro + remaining = total

When you prepend a beat (a reveal, a telephoto hold, an establishing shot) to footage
you must preserve, the preserved take does not get longer — it gets *pushed back*.
State the arithmetic every time and flag what falls off:

`total runtime − intro length = surviving window for the source performance`

If the source take is longer than that window, some of it cannot play. Say so, and
offer the three resolutions in order of fidelity:

1. **Extend the total** so the full source fits. Highest fidelity, longest clip.
2. **Start the source earlier** — sacrifice the clip's own quiet lead-in so the
   dialogue still lands. Keeps total fixed, keeps the words, loses pre-roll.
3. **Accept truncation** — the first N seconds won't appear. Only safe if the dropped
   head has no dialogue.

Never promise "100% lip-sync" *and* a prepended intro on a fixed total without doing
this subtraction first. Recompute and re-flag on *every* change to either number.

## 8. First / start-frame workflow

Before spending video credits, it's often worth generating the **transformed opening
still** as an image, locking the look, then animating from it. Generate the
transformed first frame with an image model, confirm the look with the user, then
hand the chosen still back to the v2v model as the start frame. When refining a
generated still, edit the chosen result (pass it back as the base) and fix only
what's off rather than starting over.

## 9. Iterating

Users iterate fast and in small steps ("softer light," "from the right," "bigger
snowier mountains," "make the creature huge," "a beat before the zoom," "keep the
original runtime"). Change **only the named thing** and keep the rest of the prompt
stable — re-rolling the whole prompt loses what already worked.

---

## Structure patterns to internalize (durable across v2v models)

- **Add-element:** `source (preserve all, add effect)` → `specs + guardrails` →
  `continuous shot, preserved performance, effect igniting/creeping with plate
  interaction, subject unfazed` → `lock-down clause` → `audio`.
- **Environment-swap:** `source (preserve subject + vehicle + rig + motion, replace
  world)` → `specs + grade for the new world` → `continuous shot from the same rig,
  new world streaming past with parallax, relight to match or relight-all` →
  `lock-down` → `audio`.
- **Element-on-landmark with timed zoom:** `source` + `texture reference` → `specs +
  keep source dialogue` → `continuous locked shot, giant photoreal element
  integrated, subject delivering to camera` → `at ~T / on the line "…", smooth
  push-in keeping the landmark in frame, element turns to camera` → `lock-down` →
  `audio + dialogue`.
- **Prepended reveal intro:** `source (preserve subject + performance + lip-sync +
  framing, add element, prepend telephoto intro)` + `texture reference` → `specs +
  keep source dialogue` → `open tight on the element in isolation, zoom-out at ~T
  landing on a 100% match of the source composition, then the preserved take plays
  with exact lip-sync to the quoted line while the element continues behind` →
  `budget check (intro + remaining = total)` → `lock-down` → `audio + dialogue`.
