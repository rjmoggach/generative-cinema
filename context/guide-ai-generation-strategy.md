# AI Generation Strategy — Craft Under Current Model Limits

The connective tissue between film craft and what today's generative models can
actually do. The other guides describe ideal cinematic intent; this one keeps that
intent achievable given how 2026 image/video models behave. Used by `shot-prompt`
(how to realize a shot) and `model-docs` (what to document). Pair with
`model-currency-2026-06.md` for per-model specifics.

Format: **Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

> Models change monthly. Treat capability claims as "as of June 2026" and
> re-check the currency file.

---

## 1. Aim for perceptual continuity, not pixel-perfect identity

- **Use when:** any multi-shot sequence with a recurring character or location.
- **Because:** current systems don't hold a fixed identity model — they
  reconstruct the subject each generation from prompt, references, and context.
  Some drift is inherent. The realistic, achievable goal is that the viewer
  *recognizes the same person/place* across shots even as expression, angle, and
  light change — not identical pixels.
- **Prompt translation:** lock the high-salience identity cues (silhouette,
  hair, key wardrobe color, distinctive features) and accept variation in the
  rest; review a sequence as a *cut*, asking "does this read as the same person?"
- **Watch-outs:** chasing pixel-perfection wastes iterations; design shots so
  small drifts are hidden (cut on movement, change size+angle together).

---

## 2. Reference images beat text "character bibles"

- **Use when:** holding a character/object/location across shots.
- **Because:** text can *describe* a subject but can't pin a face; as of 2026 the
  efficient method is a firm visual anchor — a clear reference image, a locked
  style, and (for video) defined first/last frames — rather than ever-longer
  text DNA blocks.
- **Prompt translation:** generate one strong "hero" reference still first, then
  drive subsequent shots from it (image-to-image / character-reference features);
  keep the text prompt for *changes only*, letting the reference carry identity.
- **Watch-outs:** still restate the standard prompt prefix (look identity) even
  when using a reference image; the reference pins *who*, the prefix pins *the look*.

---

## 3. Lock what must not change

- **Use when:** every shot in a consistency-critical sequence.
- **Because:** the fewer free variables, the less drift. Pin style, palette,
  lighting direction, lens/grain, and (video) endpoints; vary only the shot's
  intent.
- **Prompt translation:** reuse the `project-context` standard prompt prefix
  verbatim; hold a fixed **seed** where supported; set first/last frames for video;
  keep light direction + color identical across coverage (see
  `guide-continuity-rules.md`).

---

## 4. Sequence shots to each model's strengths

- **Use when:** choosing which model renders which shot.
- **Because:** the field is multi-polar — no model wins everything. Play to
  strengths: a strong stills model for the hero/establishing frame; a
  character-consistent video model for coverage; an audio-native model for
  dialogue; an HDR/physics model for VFX elements.
- **Prompt translation:** per `model-currency-2026-06.md`, route shots — e.g.,
  establishing/hero still on the best image model, motion coverage on the
  strongest character-lock video model, dialogue on the audio-native one — then
  match grade in post.
- **Watch-outs:** switching models mid-sequence risks look mismatch; reconcile
  with a consistent grade and the shared prompt prefix.

---

## 5. The 5-10-1 iteration loop (cost-efficient)

- **Use when:** converging on a hero shot without burning budget.
- **Because:** premium renders are expensive; most exploration doesn't need them.
- **Prompt translation:** (1) make ~5 cheap/fast variations to find direction,
  (2) pick the best, (3) do ~10 refinements on it, (4) one final render on the
  premium model. Iterate the *prompt*, changing one variable at a time.
- **Watch-outs:** match duration to the beat (don't request 10s for a 4s action);
  over-long clips strain coherence.

---

## 6. Fight drift with craft, not just prompting

- Cut **on action** and pair a **30°+ angle change with a size change** so minor
  identity shifts read as new coverage, not errors (see `guide-continuity-rules.md`).
- Prefer **slow, motivated** camera moves (see `guide-creative-approaches.md`) —
  they render cleaner and hold identity better than fast/erratic motion.
- State **screen direction, gaze, and motion vectors every shot** — the model has
  no memory of the previous clip.
- Use **edits and inserts** (cutaways, details) to bridge shots that won't
  cleanly match — a classic editorial fix that also hides generation seams.

---

## 7. Quick application

1. Pick the **hero reference** first; let it carry identity.
2. **Lock** prefix, palette, light direction, seed, endpoints.
3. **Route** each shot to the model that does it best (currency file).
4. **Iterate 5-10-1**, one variable at a time.
5. Hide residual drift with **continuity craft and edits**; judge as a cut.

Companion: `model-currency-2026-06.md`, `guide-continuity-rules.md`,
`guide-sequence-construction.md`, and each `models/model-*.md`.
