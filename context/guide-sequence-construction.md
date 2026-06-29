# Sequence & Scene Construction

How to build a *scene*, not just a shot. This is the level above `shot-prompt`:
decide the coverage, the staging pattern, the screen geometry, and the intensity
arc — then generate the individual shots to fill it. Pairs tightly with
`guide-shot-selection.md`, `guide-lens-language.md`, and `guide-continuity-rules.md`.

Format: **Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The scene as a unit

A scene has a *dramatic shape*: an entry state, a turn (the beat where something
changes), and an exit state. Design coverage around the **turn** — that's where
your tightest, most lavish shots go; everything else serves it. Before generating
shots, name: *Where are we? Who wants what? What is the turning beat? How should
the audience feel leaving?*

---

## 2. Coverage strategy — three ways to build a scene

### Master + coverage (classic, safest for AI)

- **Use when:** dialogue, most narrative scenes, when you need editorial freedom.
- **Because:** a master establishes geography and lighting as ground truth; matched
  coverage (OTS, singles, inserts) lets you cut to the right emotion at the right
  moment while staying spatially legible.
- **Prompt translation:** generate the master first; reuse its lighting, palette,
  lens, and screen positions as the locked basis for every coverage prompt.
- **Watch-outs:** match light direction and color across all coverage or cuts
  will flicker; hold a seed where the model supports it.
- **Anchors:** standard continuity coverage; Mascelli.

### Fragmented (no master)

- **Use when:** subjective, tense, disorienting, or stylized scenes.
- **Because:** building only from fragments (details, CUs, partial views) denies
  the audience a stable map — intimate or anxious by design.
- **Prompt translation:** skip the wide; sequence CUs/inserts with strong eyeline
  and direction cues so it still reads as one space.
- **Watch-outs:** without a master, continuity rules matter *more*, not less.

### The oner (single continuous shot)

- **Use when:** real-time tension, immersion, virtuosic reveals.
- **Because:** unbroken time builds pressure and presence; the camera move *is*
  the edit.
- **Prompt translation:** one shot with a designed move (Layer 3) that re-frames
  to do the job of several cuts — e.g., push from two-shot to CU on the turn.
- **Watch-outs:** longest single takes strain AI duration/coherence; keep within
  the model's strong duration and design the move simply.
- **Anchors:** Cuarón, Iñárritu (see `reference-visual-*.md`).

---

## 3. Staging patterns (Katz: A, I, L)

Katz reduces the hundreds of staging choices to three relationships between actors
and camera. Pick one as the scene's spine:

- **A-pattern (depth/wedge):** actors arranged toward/away from camera along a
  diagonal — strong depth, clear foreground/background hierarchy. *Use for* power
  imbalance, staging in depth, deep-focus scenes.
- **I-pattern (lateral line):** actors across the frame on a line parallel to
  camera — flat, frontal, confrontational or formal. *Use for* face-offs, symmetry,
  Wes-Anderson-style frontality.
- **L-pattern (right angle):** one actor faces camera-ish, another at 90° — natural
  conversational asymmetry, easy OTS coverage. *Use for* most dialogue.
- **Prompt translation:** describe actor placement and facing in the master prompt
  per the chosen pattern; keep it consistent through coverage.
- **Anchors:** Katz, *Film Directing: Shot by Shot*.

---

## 4. The intensity arc (pair with Bruce Block — see planned `guide-visual-structure.md`)

- **Use when:** any multi-shot scene; especially a sequence with a climax.
- **Because:** the *visual* intensity should rise and fall *with the story*.
  Tighter sizes, more contrast, more movement, longer lenses, faster cutting all
  raise intensity; their opposites lower it. Plan the curve so the peak beat also
  peaks visually.
- **Prompt translation:** map shots to an intensity curve — open lower-intensity
  (wide, static, deeper focus, slower cuts), escalate into the turn (tighter,
  shallow, moving, faster), then resolve. Encode this per-shot.
- **Watch-outs:** if everything is max intensity, nothing is — reserve the peak.

---

## 5. Rhythm & pacing across cuts

- **Shot duration sets pace:** long held shots = contemplative; short shots =
  energetic/chaotic. Vary deliberately; cut faster into a climax.
- **Cut on action** to hide the join; **cut on a look/reaction** to pass attention.
- **Intercut (parallel)** two lines of action to build suspense or draw a
  comparison; the cutting rhythm itself creates meaning (montage).
- **Prompt translation:** for video models, match clip duration to the beat's
  energy (don't request 10s for a 4s beat); for sequence models, specify shot
  order and relative lengths.
- **Anchors:** Arijon (cutting patterns), Spottiswoode (rhythmic montage).

---

## 6. Scene-build workflow (hand-off to `shot-prompt`)

1. **State the beat:** location, who/wants, the turn, exit feeling.
2. **Choose coverage mode** (master+coverage / fragmented / oner).
3. **Pick the staging pattern** (A/I/L) and set screen positions + the line.
4. **Plan the intensity arc** and assign each shot a size + lens + move.
5. **Lock continuity** (screen direction, eyelines, light direction) per
   `guide-continuity-rules.md`.
6. **Generate** establishing → master → coverage with `shot-prompt`, reusing the
   standard prompt prefix and matched lighting throughout.
7. **Review as a cut**, not as stills: do the directions, eyelines, and intensity
   curve hold across the sequence?

This is the natural home of a future `sequence-design` skill; until then, run this
checklist before invoking `shot-prompt` for a full scene.
