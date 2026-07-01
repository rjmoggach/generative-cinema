---
name: location-pack
description: >-
  Build or refresh a location/set reference — spec file plus a folder of locked plates —
  that keeps a setting consistent as the camera moves and the light changes. Trigger
  phrases: "scout this location", "build a location pack", "lock this environment",
  "master plate + coverage", "time-of-day variants", "establishing plate for X", "keep
  this place consistent across shots", "give me this location at night / in the rain".
  Produces a master establishing plate, multi-angle coverage (including the reverse
  angle), and time-of-day / weather variants all derived from the locked geometry anchor.
  The output is the reference that shot-prompt and image-edit carry to hold the set's
  geometry and light logic consistent across every shot.
---

# Location-Pack Assistant

Build a persistent, multi-angle location reference. The geometry anchor lives in the
asset; downstream prompts carry only change. When `shot-prompt` or `image-edit` needs to
carry a set into a new shot angle or lighting state, it attaches the master plate and
restates the continuity table verbatim. This skill calls `image-edit` as its derive
engine — every coverage angle and time-of-day / weather variant is an i2i operation
driven from the locked master plate.

## When to use

Whenever a location must read as the same place across more than one shot — or when the
user requests establishing plates, a location pack, or time-of-day / weather variants of
an existing setting. If the spec file already exists (`set-{show}-{name}.md`), refine it
in place: update only the changed coverage or variant and re-export the affected images.
Do not rebuild from scratch unless the location's production design has fundamentally
changed.

## Core principle: master plate, then fan out

Generate one clean **master plate** first — a wide establishing view in base-state light
(neutral time of day, settled weather) that locks the location's geometry: sight lines,
horizon, architectural anchors, background elements, and practical light positions. Then
derive every coverage angle and time-of-day / weather variant *from it* via reference
conditioning and `image-edit`. Never generate coverage or variants independently;
siblings built without a shared anchor diverge in geometry and dressing immediately and
cannot be reliably re-anchored later. A weak master plate — badly lit, under-resolved,
or compositionally ambiguous — poisons everything downstream. Lock it right before
fanning out.

## Step 1 — Load craft

Read these before writing any prompt:

- [`references/reference-craft-artdept.md`](references/reference-craft-artdept.md) —
  the creative foundation: environment class, design language, material palette, era,
  and production intent (principal set / background / extension).
- [`references/guide-location-pack.md`](references/guide-location-pack.md) —
  master-plate discipline, coverage-angle rules, reverse-angle landmark continuity, and
  time-of-day / weather variant logic.
- [`references/guide-asset-reference.md`](references/guide-asset-reference.md) —
  anchor-then-fan-out, reference counts and strength, multi-reference composition, and
  the asset naming taxonomy (§9).
- [`references/guide-image-editing.md`](references/guide-image-editing.md) —
  the i2i mechanics used to derive coverage angles and lighting variants from the anchor.

If the user names a show code, read `project-context-{show}.md` (and
`art-bible-{show}.md` if present) and inherit the Standard Prompt Prefix, palette hex
codes, CMF lexicon, style reference, lighting vocabulary, grade, lens specs, atmosphere,
and forbidden terms; construct prompts from those fields. Hold these consistently across
the master plate, all coverage, and all variants.

## Step 2 — Master plate

Generate the **master plate**: the widest, most spatially informative view of the
location in base-state light — neutral time of day (typically late morning or early
afternoon), settled weather, full-depth geometry visible. Neutral grade, no heavy
atmosphere effects. The goal is maximum spatial and architectural information with minimum
distraction from transient light or weather.

Once the master plate is approved:

1. **Write the identity block** — 50–80 words, hex-pinned: environment class, era,
   primary materials and finishes with hex, dominant spatial axes (long axis of the
   space, sight line to horizon or background wall, key landmark), practical light
   sources and their positions, and any critical atmospheric or grade note. This block
   is pasted verbatim into every downstream shot prompt — vague language here becomes
   spatial drift everywhere downstream.
2. **Note the base-state light logic:** key direction (compass or clock position), colour
   temp with hex, hard or soft quality, and approximate time of day. This entry becomes
   the `Base` row of the continuity table.
3. Save as `assets/set/{name}/set-{name}-plate.png` in the user's working folder.

## Step 3 — Coverage

Using the master plate as the locked reference, derive **coverage angles** via
`image-edit` — one angle at a time, each pinned to the same geometry and dressing.
Coverage should account for the angles the scene actually requires; always include the
reverse angle.

- Main coverage: `set-{name}-cov-01.png`, `set-{name}-cov-02.png`, etc.
- Reverse angle: `set-{name}-cov-reverse.png` — looking back along the master plate's
  primary sight line. The reverse is where geometry drift first becomes visible; verify
  landmark continuity explicitly before moving on.

For each coverage angle: note which real or implied architectural landmark (window frame,
doorway, distant structure, horizon break, practicals) appears in both the master plate
and the coverage view. These landmarks are the continuity anchors for this location
across shots and must be held consistent.

Hold apparent scale, lens character, and background dressing constant across all coverage
angles — a change in any of these reads as a different set, not a different camera
position. Derive each angle from the master plate; never cross-derive angles from sibling
coverage, as that compounds drift.

## Step 4 — Time-of-day / weather variants

Derive time-of-day and weather variants from the **locked master plate** via `image-edit`
— one variable changed per variant, using the master plate (or the nearest prior variant)
as the source. Never vary more than one axis simultaneously; stacking time and weather in
a single generation step compounds uncontrolled drift.

Standard variant set (generate only what the project requires):

- Dawn: `set-{name}-tod-dawn.png` — low-east light, cool colour cast
- Golden hour: `set-{name}-tod-golden.png` — low-west warm key, long shadows
- Dusk: `set-{name}-tod-dusk.png` — transitional blue-to-amber, practicals coming on
- Night: `set-{name}-tod-night.png` — overhead minimal ambient, practical-dominant
- Overcast: `set-{name}-tod-overcast.png` — flat top light, desaturated
- Rain: `set-{name}-tod-rain.png` — wet surfaces, rain haze, overcast modifier
- Fog: `set-{name}-tod-fog.png` — near-distance falloff, diffused ambient

For each variant: state the single variable changed, the new light direction and colour
temp with hex, and the atmosphere descriptor. These values populate the continuity table
and are restated verbatim in every shot prompt that uses this variant.

## Step 5 — Continuity table

Compile the continuity table from the master plate and each completed variant. This table
is carried into the spec file (`set-template.md`) and restated verbatim in every shot
prompt that places action in this location — it is the mechanism by which the location
stays coherent across the cut.

| Variant | Key direction | Colour | Atmosphere |
|---------|--------------|--------|------------|
| Base (day) | {e.g., overhead south, hard} | neutral `#FFF5E4` | clear |
| Dawn | {low east, soft} | cool `#B8D4E8` | light mist |
| Golden | {low west, hard} | warm amber `#FFB347` | long shadows |
| Night | {overhead, practical-key} | cool blue-black `#1A1F2E` | deep shadow |
| Rain | {top, diffuse} | grey-green `#B8C4B0` | rain haze, wet surfaces |

Add or trim rows to match the variants actually generated. Hex-pin every Colour entry —
vague descriptors ("warm", "cool") drift across prompting sessions.

## Step 6 — Model + references

Identify the target model for all i2i work in this session (ask once if unstated; prefer
the model already in use for the project). Load the model doc for source/reference
syntax, per-model reference-image limits, and denoise/strength controls:

- FLUX.1 Kontext: [`references/models/model-editing-flux-kontext.md`](references/models/model-editing-flux-kontext.md)
- Gemini Flash (Nano Banana): [`references/models/model-image-gemini-flash.md`](references/models/model-image-gemini-flash.md)
- Seedream 4: [`references/models/model-image-seedream-4.md`](references/models/model-image-seedream-4.md)
- FLUX.1 Pro: [`references/models/model-image-flux-pro.md`](references/models/model-image-flux-pro.md)

Before quoting reference counts or strength values, check
[`references/model-currency-2026-06.md`](references/model-currency-2026-06.md) for the
current version and per-model limits — these change monthly. The general sweet spot is
**4–6 reference images at strength ~0.7** (guide-asset-reference §4), but verify the
hard limits per model before advising any specific count.

## Step 7 — Output

Write all outputs to the **user's working folder** — never to the plugin repo.

**Spec file:** `set-{show}-{name}.md`, filled from
[`references/set-template.md`](references/set-template.md). The crew role for this
workflow is `location-scout`, but the asset type in the taxonomy is `set` — spec
filenames follow `set-{show}-{name}.md` (not `location-…`) and the image folder is
`assets/set/{name}/`.

**Image folder:** `assets/set/{name}/` — use the asset taxonomy filenames exactly
(guide-asset-reference §9):

- Master plate: `set-{name}-plate.png`
- Coverage: `set-{name}-cov-01.png`, `set-{name}-cov-02.png`, `set-{name}-cov-reverse.png`
- Time-of-day / weather: `set-{name}-tod-dawn.png`, `-tod-golden.png`, `-tod-night.png`,
  `-tod-rain.png`, etc.

All filenames are lowercase ASCII kebab-case. Image filenames carry **no `{show}`
prefix** — the show code lives only in the spec filename. A version suffix (`-v02`, etc.)
is optional but recommended once the asset enters shot production. Confirm the output
paths aloud before saving — the user's working folder, not the repo.

## Critical rules

1. **Anchor before fan-out.** No coverage angle or time-of-day variant generates until
   the master plate is approved.
2. **Derive from the master plate.** Coverage and variants are i2i operations from the
   locked master — never generate independently; divergence cannot be re-anchored.
3. **One variable per variant.** Each time-of-day or weather variant changes exactly one
   axis from the master plate or the nearest prior variant; stacking changes loses
   control of the result.
4. **Lock reverse-angle landmarks.** The reverse angle is the first place geometry
   inconsistency surfaces — verify that shared architectural landmarks read consistently
   in both directions before continuing.
5. **Hex-pin the continuity table.** Colour temp and atmosphere without hex values will
   drift across sessions; pin every entry before writing it into the spec file.
6. **Binaries to the user's folder only.** Images and spec files go to the user's
   working folder; nothing writes to the plugin repo.
7. **Verify counts vs currency.** Reference count and strength limits are
   version-sensitive — check `model-currency-2026-06` before advising any specific value.
