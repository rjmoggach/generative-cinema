---
name: character-sheet
description: >-
  Build or refresh the single most load-bearing asset in the pipeline: a persistent
  character reference — spec file plus a folder of locked reference images — that holds
  a character's face, body, wardrobe, and makeup/hair consistent across every shot.
  Trigger phrases: "build a character sheet", "lock this character", "make a turnaround
  / model sheet", "create the hero reference for X", "keep this person consistent across
  shots", "design this character". Produces the three facets — identity (casting),
  turnaround + wardrobe (costume), and HMU states (makeup-hair) — as one unified asset.
  The output is the reference that shot-prompt and image-edit carry to maintain identity
  across shots and states.
---

# Character-Sheet Assistant

Build the single most load-bearing asset in the pipeline: a unified, persistent
character reference. Identity lives in this asset; downstream prompts carry only change.
When `shot-prompt` or `image-edit` needs to carry a character into a new scene or
state, it attaches the outputs of this skill and pastes the descriptor block verbatim.
This skill calls `image-edit` as its derive engine — every view and state fan-out is
an i2i operation driven from the locked anchor.

## When to use

Whenever a character will recur across more than one shot, or when the user requests a
turnaround, model sheet, or hero reference — even for a single scene if consistency
matters. If the spec file already exists (`char-{show}-{name}.md`), refine it in place:
update only the changed facet and re-export the affected images. Do not rebuild from
scratch unless the creative direction has fundamentally changed.

## Core principle: anchor, then fan out

Generate one clean **hero identity reference** first — front-facing, evenly lit,
neutral background, high-res, frame-filling — then derive every other view and state
*from it* via reference conditioning and `image-edit`. Never generate views
independently; siblings built without a shared anchor diverge immediately and cannot be
reliably re-anchored later. A weak anchor — angled, expressive, low-res, or
background-cluttered — poisons everything downstream. Get it right before fanning out.

## Step 1 — Load craft

Read these before writing any prompt:

- [`references/reference-craft-character.md`](references/reference-craft-character.md) —
  the creative foundation: casting (typage, presence, ensemble chemistry), costume
  (silhouette, materiality, palette), HMU (state logic, injury grammar, aging rhythm).
- [`references/guide-character-consistency.md`](references/guide-character-consistency.md) —
  technical identity lock: descriptor blocks, two-block prompting, identity-vs-scene split.
- [`references/guide-turnaround-sheets.md`](references/guide-turnaround-sheets.md) —
  alignment-line discipline, view angles, companion expression and pose sheets.
- [`references/guide-asset-reference.md`](references/guide-asset-reference.md) —
  anchor-then-fan-out, reference counts and strength, multi-reference composition,
  the asset naming taxonomy (§9).
- [`references/guide-image-editing.md`](references/guide-image-editing.md) —
  the i2i mechanics used to derive views and progress states from the anchor.

If the user names a show code, read `project-context-{show}.md` (and
`art-bible-{show}.md` if present) and inherit the Standard Prompt Prefix, palette hex
codes, lighting, lens specs, atmosphere, and forbidden terms. Hold these consistently
across all three facets.

## Step 2 — Identity (casting)

Generate the **hero identity reference**: front portrait, neutral background, even fill
light, no shadow drama — the anchor from which every view and state derives.

Once the anchor is approved:

1. Fan out a **multi-angle bundle** — ¾-left, side-left, side-right, ¾-right, back —
   by driving each view through `image-edit` with the anchor as the locked reference.
   Align every view on the **eye / shoulder / waist / knee / foot** guide lines
   (guide-turnaround-sheets).
2. **Write the descriptor block** — 50–80 words, hex-pinned: face structure, hair color
   and texture, skin tone with hex, body build, distinctive marks, default wardrobe note.
   This block is pasted verbatim into every downstream prompt; vague language here
   becomes drift everywhere downstream.
3. **Call the reference-vs-LoRA gate** (guide-asset-reference §3):
   - One scene or quick turnaround → reference images only (~65–75% consistency).
   - Recurring hero across many shots or episodes → reference + trained LoRA + fixed
     descriptor block (~85–92%); record the `LoRA trigger word:` in the spec file.

## Step 3 — Turnaround + wardrobe (costume)

Using the front anchor as the locked reference, derive the **full turnaround set** via
`image-edit`: `-turn-front`, `-turn-side-l`, `-turn-side-r`, `-turn-back`, `-turn-3q-l`,
`-turn-3q-r`. Hold the eye / shoulder / waist / knee / foot alignment lines consistent
across all views (guide-turnaround-sheets).

For each **costume state** (day-1, day-2-wet, formal, etc.):

- Lock the garment by **name + silhouette + primary hex** — never describe wardrobe
  with vague adjectives such as "dark" or "casual."
- Note the state explicitly: clean / soiled / wet / torn.
- Derive wet or damaged versions by editing from the clean fit image at low denoise
  rather than regenerating from the identity anchor.
- Save as `char-{name}-fit-{label}.png` (e.g., `char-eli-fit-day1.png`,
  `char-eli-fit-day2-wet.png`).
- Add expression or pose companion sheets if a mood or action range is requested.

## Step 4 — HMU states (makeup-hair)

Build a **state library** — at minimum: `clean`, `aged`, `wounded`, `wet`. Each state
must be independently lockable so `image-edit` can derive further progressions from any
of them without reverting to the identity anchor.

For wound and injury states:

- Pin every wound by **position + side + size + hex** — e.g., "3 cm laceration,
  right cheekbone, fresh blood `#C0392B`, sutured edge."
- Progress wound stages by editing from the preceding stage at low denoise (~0.15–0.25),
  not by regenerating — this preserves the wound fingerprint and keeps the progression
  continuous across stages.

For aging states: edit from the clean base; hold the light-key direction; do not
regenerate the face from scratch.

Save as `char-{name}-hmu-{label}.png` (e.g., `char-eli-hmu-clean.png`,
`char-eli-hmu-wound-01.png`).

## Step 5 — Model + references

Identify the target model for all i2i work in this session (ask once if unstated;
prefer the model already in use for the project). Load the model doc for
source/reference syntax, per-model reference-image limits, and denoise/strength controls:

- FLUX.1 Kontext: [`references/models/model-editing-flux-kontext.md`](references/models/model-editing-flux-kontext.md)
- Gemini Flash (Nano Banana): [`references/models/model-image-gemini-flash.md`](references/models/model-image-gemini-flash.md)
- Seedream 4: [`references/models/model-image-seedream-4.md`](references/models/model-image-seedream-4.md)
- FLUX.1 Pro: [`references/models/model-image-flux-pro.md`](references/models/model-image-flux-pro.md)

Before quoting reference counts or strength values, check
[`references/model-currency-2026-06.md`](references/model-currency-2026-06.md) for the
current version and per-model limits — these change monthly. The general sweet spot is
**4–6 reference images at strength ~0.7** (guide-asset-reference §4), but verify the
hard limits per model before advising any specific count.

## Step 6 — Output

Write all outputs to the **user's working folder** — never to the plugin repo.

**Spec file:** `char-{show}-{name}.md`, filled from
[`references/character-template.md`](references/character-template.md). State the
descriptor block prominently at the top of the Identity section so `shot-prompt` and
`image-edit` can locate and paste it verbatim without scanning the whole document.

**Image folder:** `assets/char/{name}/` — use the asset taxonomy filenames exactly
(guide-asset-reference §9):

- Identity: `char-{name}-id-front.png`, `char-{name}-id-3q-l.png`, etc.
- Turnaround: `char-{name}-turn-front.png`, `-turn-side-l`, `-turn-side-r`,
  `-turn-back`, `-turn-3q-l`, `-turn-3q-r`
- Wardrobe: `char-{name}-fit-{label}.png`
- HMU: `char-{name}-hmu-{label}.png`

All filenames are lowercase ASCII kebab-case. A version suffix (`-v02`, etc.) is
optional but recommended once the asset enters shot production. Confirm the output
paths aloud before saving — the user's working folder, not the repo.

## Critical rules

1. **Anchor before fan-out.** No view or state generates until the front hero reference
   is approved.
2. **Descriptor block verbatim.** Write it once in the spec file; paste it unchanged
   into every downstream prompt. Do not paraphrase or condense.
3. **Pin hex, garment name, wound spec.** Vague language drifts — "dark jacket" and
   "3 cm laceration, right cheekbone, `#C0392B`" are not equivalent.
4. **Hold the light-key.** The dominant key direction locked in the anchor carries
   through every view and state unless the edit *is* a relight.
5. **Edit, don't regenerate, for progressions.** Wound stages, aging, soiling — always
   edit from the prior state at low denoise; regenerating loses the fingerprint.
6. **Binaries to the user's folder only.** Images and spec files go to the user's
   working folder; nothing writes to the plugin repo.
7. **Verify counts vs currency.** Reference count and strength limits are
   version-sensitive — check `model-currency` before advising any specific value.
