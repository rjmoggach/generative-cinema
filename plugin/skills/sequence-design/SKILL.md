---
name: sequence-design
description: >-
  Plan a scene or sequence before any shots are generated: choose coverage,
  staging, screen direction, the visual intensity arc, and a shot list — then hand
  it to the shot-prompt skill. Use this whenever a user wants to plan, break down,
  block, or storyboard a scene/sequence rather than a single shot — phrases like
  "plan this scene", "break down the sequence", "how should I cover this", "design
  the coverage", "build a shot list for", "block this scene", or "what shots do I
  need". Sits between project-context (the look) and shot-prompt (each shot); load
  a project-context-{show-code}.md first so the plan inherits the visual language.
---

# Sequence Design Assistant

Operate at the **scene level**. Turn a dramatic beat into a coverage plan — a shot
list with sizes, lenses, moves, screen geometry, and an intensity arc — that the
`shot-prompt` skill then renders shot by shot. You are the director planning the
day, not the prompt engineer writing each frame.

## Where this sits

```
project-context  ->  sequence-design  ->  shot-prompt  ->  prompts
   (the look)        (the scene plan)      (each shot)
```

## When to use

Any request to plan/break down/block/storyboard a scene or sequence. For a single
shot, skip straight to `shot-prompt`.

## Step 1 — Load the look

If a `project-context-<show-code>.md` exists, read it and inherit the standard
prompt prefix, palette, lighting, lens signature, and forbidden terms. If none
exists, offer `project-context` first, or proceed noting the plan won't be
consistency-locked.

## Step 2 — Define the dramatic beat

State, with the user, in one or two lines each:
- **Where/when** (location, time, light).
- **Who wants what** (the characters and their objective in the scene).
- **The turn** — the single beat where something changes. This is the scene's pivot.
- **Exit feeling** — how the audience should feel leaving.

## Step 3 — Choose the coverage mode

Per [`references/guide-sequence-construction.md`](${CLAUDE_PLUGIN_ROOT}/context/guide-sequence-construction.md):
- **Master + coverage** (default; safest for AI) — establish geography, then matched angles.
- **Fragmented** (no master) — subjective/tense; continuity rules matter more.
- **Oner** — one designed move; keep within the model's strong duration.

## Step 4 — Set staging and the line

Pick a staging pattern (A/I/L) and fix **screen positions, the 180° axis, eyelines,
and motion vectors** per
[`references/guide-continuity-rules.md`](${CLAUDE_PLUGIN_ROOT}/context/guide-continuity-rules.md).
Write these down — they must stay constant across every shot for the cut to read.

## Step 5 — Plan the intensity arc

Using [`references/guide-visual-structure.md`](${CLAUDE_PLUGIN_ROOT}/context/guide-visual-structure.md),
map the scene's dramatic arc to a *visual* one: open lower-intensity (wider, flatter,
slower, more affinity), escalate into the turn (tighter, deeper, faster, more
contrast/saturation), resolve. Decide which components carry the build.

## Step 6 — Write the shot list

Produce a numbered shot list. For each shot specify: label, size, angle, lens,
movement, the beat it serves, and its target intensity. Choose sizes/coverage via
[`references/guide-shot-selection.md`](${CLAUDE_PLUGIN_ROOT}/context/guide-shot-selection.md) and lenses
via [`references/guide-lens-language.md`](${CLAUDE_PLUGIN_ROOT}/context/guide-lens-language.md). Use the
project's `<show-code>` and a sequence number for labels (e.g., `S2-03`).

Output format:

```
SEQUENCE <code>-S<n>: <scene name>
Beat: <where/who/turn/exit>   Coverage: <mode>   Staging: <A/I/L>
Line/direction: <A left looking right; B right looking left; travel L→R>
Intensity arc: <open → peak at the turn → resolve>

S<n>-01  Establishing — <size>, <angle>, <lens>, <move> — serves <beat> — intensity <low/med/high>
S<n>-02  Master — ...
S<n>-03  Coverage CU — ...
...
```

## Step 7 — Hand off to shot-prompt

State the target model(s) and pass the shot list to `shot-prompt`, which renders
each line into a model-optimized prompt using the locked prefix and continuity
cues. Remind the user to review the result **as a cut**, not as stills.

## Critical rules

1. Plan the **turn** first; design coverage and the intensity peak around it.
2. Lock screen direction, eyelines, and motion vectors **before** generating.
3. Inherit the `project-context` look; never invent a conflicting one.
4. Output a concrete, numbered shot list — no `[PLACEHOLDERS]`.
5. Keep oners and clip lengths within the chosen model's strong duration.
