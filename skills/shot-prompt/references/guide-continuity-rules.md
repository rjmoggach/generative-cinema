# Continuity & Spatial Logic

The rules that keep a multi-shot scene legible: the audience always knows *where
everyone is* and *who is looking at whom*. These are absent from the library as
actionable rules — and they matter **doubly for AI generation**, where shot-to-
shot space is fragile and must be pinned explicitly in prompts.

Format: **Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The axis of action (the "line") and the 180° rule

- **Rule:** imagine a line through the two subjects (or the direction of action).
  Keep the camera on **one side** of that line for all shots in the scene.
- **Use when:** any scene with two or more people relating, or directional motion.
- **Because:** staying on one side keeps screen direction consistent — Character A
  stays frame-left looking right, B stays frame-right looking left. Cross the line
  and they suddenly appear to look the same way or swap sides, disorienting the cut.
- **Prompt translation:** bake screen position + gaze into every shot of the
  scene: "A on left looking screen-right, B on right looking screen-left". Keep
  these constant across the establishing, OTS, and CU prompts.
- **Watch-outs (AI):** models don't track an off-screen geometry between separate
  generations — *you* are the continuity supervisor. State left/right and gaze
  direction explicitly in each prompt or singles will mismatch.
- **Anchors:** Arijon (the line, triangle system); Mascelli (continuity).

### Crossing the line on purpose

- **Use when:** you want to signal a shift — a turning point, a power reversal,
  disorientation, or a new "round" of a fight.
- **Because:** a deliberate line-cross jars; used knowingly it marks change.
- **Prompt translation:** flip the screen positions intentionally and let the
  edit land on a story beat; don't do it by accident.

---

## 2. The 30° rule (and avoiding the jump cut)

- **Rule:** when cutting to a new angle of the same subject, move the camera at
  least **30°** around it (and ideally change size too).
- **Because:** less than ~30° looks like the subject twitched rather than the
  camera moved — an unintended jump cut.
- **Prompt translation:** between two coverage shots of one subject, change angle
  by 30°+ *and* shot size (e.g., MS front → CU 3/4). 
- **Watch-outs:** for clean continuity in AI sequences, pair an angle change with
  a size change — it both satisfies the rule and hides identity drift between gens.

### Jump cut on purpose

- **Use when:** you want time to lurch, energy/anxiety, or a stylistic stamp
  (Godard, music-video, montage of an activity).
- **Because:** the discontinuity *is* the effect — compressed time, restlessness.

---

## 3. Eyeline match

- **Rule:** where a character looks in shot A must be consistent with the angle of
  what they see in shot B. Looking screen-left → the seen object is on the right
  side of the relationship, framed accordingly.
- **Use when:** any look-then-see, or reaction-to-thing pairing.
- **Because:** the matched eyeline stitches two separate shots into one space and
  one mind; a mismatched eyeline breaks the illusion that they share a room.
- **Prompt translation:** in the looker's shot specify gaze direction and angle
  (slightly off-lens, screen-left, downward); in the POV/object shot match the
  reverse angle and height (a child's POV looks *up*).
- **Anchors:** eyeline match is the partner of the 180° rule.

---

## 4. Screen direction & continuity of motion

- **Rule:** a subject exiting frame-right should enter the next shot frame-left
  (continuing left-to-right travel). Keep consistent travel direction across a
  journey unless a turnaround is shown.
- **Use when:** chases, walks, journeys, anything moving across cuts.
- **Because:** consistent direction = continuous travel; reversing it implies
  turning back or a new direction.
- **Prompt translation:** state motion vector each shot ("moving left to right");
  for a destination approach, keep the vector constant shot to shot.
- **Watch-outs (AI):** specify direction every shot — an i2v/t2v model has no
  memory of the previous clip's vector.

---

## 5. Match on action & entrances/exits

- **Match on action:** cut during a movement (a rise, a reach, a door opening) so
  the motion carries across the cut and hides it.
  - *Prompt translation:* generate the outgoing shot ending mid-motion and the
    incoming shot beginning mid-motion at a matching point; cut at the overlap.
- **Clean entrances/exits:** let a subject clear frame before cutting, or enter
  into a held frame, to give the editor clean handles and preserve geography.

---

## 6. The AI continuity checklist (per scene)

Because current models reconstruct space each generation, lock these *in the
prompts*, not just in your head:

1. **Screen positions** — who is left, who is right (keep constant).
2. **Gaze directions** — each character's eyeline, every shot.
3. **Motion vectors** — travel direction, every shot.
4. **Lighting key direction & color** — from the `project-context` (so cuts match).
5. **Lens + grain + palette** — the standard prompt prefix (identity of the look).
6. **Angle+size change of 30°+** between coverage of the same subject.

Aim for **perceptual continuity** (the viewer reads it as one space and the same
people), not pixel-perfect identity — that's the realistic target with today's
models. See `guide-ai-generation-strategy.md` (planned) and `model-currency-*.md`.

Pairs with `guide-sequence-construction.md`, which sets the coverage these rules
keep coherent.
