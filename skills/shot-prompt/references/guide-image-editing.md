# Image Editing (Image-to-Image)

Decision rules for **editing a still the user already has** rather than generating
one from scratch: preserve what makes it recognizable, change only what they ask.
This is the image-to-image (i2i) discipline — the still sibling of
`guide-footage-transformation.md` (video-to-video). It is model-agnostic — FLUX.2 /
FLUX.1 Kontext, Nano Banana (Gemini Image), and Seedream all do i2i — so the craft
below is written neutrally; the per-model *syntax* (how you pass the source image,
reference limits, denoise/strength controls, mask/inpaint support) lives in each
model doc. Use this with the `image-edit` skill, which orchestrates source → model →
prompt. It is also the **engine** the asset skills (`character-sheet`,
`prop-turntable`, `location-pack`) call to derive views and states from a locked
anchor — pair it with `guide-asset-reference.md`.

Each entry uses the library's decision-unit format:
**Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The core idea: preserve, then change one thing

An edit prompt has two jobs that pull against each other: **lock** everything that
makes the source recognizable (the subject, face, wardrobe, framing, lens, light-key
direction), and **change** only the named element. Under-specify the lock and the
model re-rolls the face or the whole frame, and the edit stops matching the original.
So every prompt states **both halves explicitly** — a constant **identity block** and
a variable **edit instruction** — and restates the most fragile guardrail (usually
*"face and identity unchanged; everything else identical to the source"*) at the end.

- **Use when:** a real photo or generated still is the starting point and only part
  of it should change.
- **Because:** i2i models will happily regenerate the whole frame; what you don't
  lock, you lose.
- **Prompt translation:** open by naming what to preserve *exactly*, name the single
  change concretely, close with the lock-down clause.
- **Watch-outs:** vague locks ("keep it similar") drift; name the specific attributes.
- **Anchors:** compositing first principles — match, then integrate, then sell.

## 2. Inspect the source first

Before writing, **look at the still**: subject, framing, wardrobe, palette, time of
day, and the **light-key direction** (name it — screen-left or screen-right). Build
the edit from what the image actually shows, not the user's one-line summary. If no
source still is described, ask what they're starting from before writing.

---

## 3. Pick the edit mechanism

Four mechanisms, lowest-risk first. Choose before you write — each changes the prompt.

### A. Conversational / partial-denoise edit (one attribute)
- **Use when:** changing a single attribute (shirt color, add glasses, open the eyes)
  while keeping the rest pixel-stable.
- **Because:** models with partial denoising (e.g. Nano Banana) edit the named region
  while preserving the facial "fingerprint"; lowest identity risk.
- **Prompt translation:** name only the change ("change the jacket to deep navy
  #1b2a4a; keep everything else identical"); rely on the model to hold the rest.

### B. Masked inpaint (a bounded region)
- **Use when:** the change is spatially contained (remove an object, fix a hand, add a
  scar at a specific spot) and you can mask it.
- **Because:** a mask confines regeneration to the region, leaving the rest untouched.
- **Prompt translation:** describe only what belongs *inside* the mask; state how it
  should integrate with the surrounding light and surface.

### C. Full-frame i2i with a denoise dial (restyle / relight / reworld)
- **Use when:** the change is global (regrade, relight, swap the world around a
  subject, restyle).
- **Because:** the **denoise strength** sets how far the result departs from the
  source — low keeps structure, high invents freely.
- **Prompt translation:** set strength deliberately (see §4); preserve subject + light
  explicitly so a global change doesn't mutate identity.

### D. Multi-reference composition (compose locked assets)
- **Use when:** placing a locked subject into a new background wearing a locked
  costume/prop — the art-department use case.
- **Because:** each reference carries one locked element; the prompt directs the
  composition. See `guide-asset-reference.md` §5.
- **Prompt translation:** assign every reference an explicit role ("Image 1 = this
  exact person, keep face and features; Image 2 = background; Image 3 = costume"), then
  state the scene.

## 4. The denoise-strength dial

The central control for full-frame i2i. Low values preserve; high values reinvent.

- **~0.2–0.35** — light touch: regrade, subtle relight, clean-up, small fixes;
  structure and identity stay locked. Use for continuity progressions.
- **~0.4–0.6** — moderate: restyle, change materials/wardrobe, swap a background while
  keeping subject pose; identity at moderate risk — lock it explicitly.
- **~0.7+** — heavy: near-regeneration; only when you want the source as loose
  inspiration. Expect identity drift; pin it hard or use a reference feature instead.

When unsure, start low and raise only if the change didn't take — overshooting denoise
is the most common "it doesn't look like them anymore" failure.

## 5. Lighting & integration

Whenever you add or swap an element, it only reads as real if it obeys the frame's
light and optics. The full integration craft — key direction, environmental bounce,
optics/atmosphere matching, edges and grounding, photoreal element/texture-reference
technique — is identical to v2v and lives in `guide-footage-transformation.md` §4–5.
The one-line version: **color matching alone is not enough** — match light direction,
softness, shadow density, lens character, haze, depth of field, and grain, and remove
hard cut-out edges. Hold the source's light-key direction unless the edit *is* a
relight.

## 6. Common edit types

- **Recolor / material change:** name the exact target (hex for color; "brushed
  steel," "worn leather" for material); mechanism A or B; keep silhouette and form.
- **Swap the world around a subject:** preserve subject + pose + light-key; mechanism
  C at moderate denoise or D; relight the subject into the new world (warm directional
  daylight is safest for identity; night/neon forces a fuller relight — flag it).
- **Add / progress a wound, scar, blood, dirt:** mechanism B; pin **position + side +
  size + hex**; progress by editing the *previous* state (fresh → scabbed → scarred),
  not regenerating.
- **Age a face:** treat the aged result as a *new* anchor reference; low-moderate
  denoise; state age cues concretely ("mid-50s, deep nasolabial lines, grey-streaked
  hair"); lock as its own reference if it recurs.
- **Relight / regrade:** mechanism C, low denoise; name the new key direction and grade.
- **Remove / clean up:** mechanism B; describe what should fill the gap, matching
  surrounding surface and light.
- **Restyle (render style/medium):** mechanism C; inherit the show's global style ref
  (`art-bible`) so the restyle stays on-world.

## 7. Multi-reference composition (brief)

Putting a locked character into a new plate wearing a locked costume is the art-dept
spine; the full method (role assignment, effective reference counts, identity-block
vs scene-block) is in `guide-asset-reference.md`. Here, just remember: **identity
lives in the reference; change lives in the prompt** — restate the identity block
verbatim even when a reference carries the face.

## 8. Iterating

Change **only the named thing** ("warmer grade," "scar a touch lower," "navy not
black," "keep the original crop") and keep the rest of the prompt stable — re-rolling
the whole prompt loses what already worked. **Edit the chosen result** (pass it back
as the base) rather than starting over; for any progression, edit from the previous
stage.

---

## Structure patterns to internalize (durable across i2i models)

- **One-attribute edit:** `identity block (preserve all)` → `the single change, with
  exact value` → `lock-down clause`.
- **World swap around a subject:** `identity block (subject + pose + light-key)` →
  `new world + relight to match` → `denoise ~0.4–0.6` → `lock-down`.
- **Wound progression:** `identity + prior state` → `the one new change at
  position/side/size` → `masked inpaint, low denoise` → `lock-down`.
- **Compose locked assets:** `Image 1 = locked subject` + `Image 2 = location` +
  `Image 3 = costume/prop` → `scene direction (camera, light, action)` → `lock-down`.
