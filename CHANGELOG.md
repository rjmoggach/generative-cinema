# Changelog

All notable changes to the Generative AI Context Library will be documented in this file.

## v0.9.0 - 2026-07-01

### New: Asset integration & QC (art department, Phase 4 - roadmap complete)

- Added the `refs:` attachment notation (`context/guide-asset-reference.md` §10): each shot line names its assets by spec-stem (`char-{name}`, `prop-{name}`, `set-{name}`).
- `sequence-design` + `first-ad` now attach `refs:` to each shot line; `shot-prompt` + `cinematographer` consume them - loading each asset's anchor image and restating its identity block verbatim (identity = reference, change = prompt), inheriting the art-bible palette/CMF.
- `script-supervisor` now audits asset continuity: missing/wrong reference, costume/HMU/prop state drift, and location geometry mismatch, alongside its screen-direction/eyeline checks.
- Added per-model reference-count/strength caveats to `model-currency-2026-06.md` and a new end-to-end guide `docs/05-asset-pipeline.md`.
- Also in this release: the `model-image-luma-uni-1.md` doc (Luma Uni-1 unified image model). Sources: Pat P. Miller, Script Supervising and Film Continuity.

## v0.8.0 - 2026-07-01

### New: Production Designer / world bible (art department, Phase 3)

- Added the `art-direction` skill - a PD interview that produces `art-bible-{show}.md`: the show's global palette (named + hex), material/CMF lexicon, era/genre, a global style reference, and an index of every character/prop/set asset. Inherits the look from `project-context`; written to the user's working folder.
- Added the `production-designer` agent - the art-department counterpart to `director`: sets the world and delegates to casting, costume, makeup-hair, propmaster, and location-scout.
- Added the technical guide `context/guide-art-direction.md` and expanded the Production Design creative section in `reference-craft-artdept.md` (anchored to Ken Adam, Hannah Beachler, Patrice Vermette, and peers).
- Retrofitted the asset skills (`character-sheet`, `prop-turntable`, `location-pack`, `image-edit`) to inherit palette/CMF/style from `art-bible-{show}.md` when present.
- Wired into `skills/build.py` + `plugin/assemble.py`; docs updated to ten skills / eleven agents; crew flow now runs director -> production-designer -> art-dept sub-roles; sources added to `knowledge-base/Miscellaneous-Sources.md`.

## v0.7.0 - 2026-07-01

### New: Props & Locations (art department, Phase 2)

- Added the `prop-turntable` skill — build a persistent prop reference (hero anchor, orthographic ring, detail views, state variants/multiples) written to your working folder; uses `image-edit` as the derive engine.
- Added the `location-pack` skill — build a location/set reference (master establishing plate, coverage incl. the reverse angle, time-of-day/weather variants from locked geometry) with a continuity table.
- Added two art-department agents: `propmaster` (prop turntables) and `location-scout` (location packs).
- Added creative craft `context/reference-craft-artdept.md` (props + locations/sets artistry with real-master anchors) and technical guides `guide-prop-turntable.md` + `guide-location-pack.md`. 3D-assist (Blender) is noted as a deferred technique.
- Extended the asset naming taxonomy in `guide-asset-reference.md` §9 with prop facets (`hero`/`ortho`/`detail`/`360`), location facets (`plate`/`cov`/`tod`), and `top`/`bottom` views. Environment asset type is `set`.
- Wired into `skills/build.py` + `plugin/assemble.py`; docs updated to nine skills / ten agents; sources added to `knowledge-base/Miscellaneous-Sources.md`.

## v0.6.0 - 2026-06-30

### New: Character pipeline (art department, Phase 1)

- Added the `character-sheet` skill — build a persistent, re-attachable character reference (hero identity + descriptor block, turnaround/model sheet, wardrobe states, makeup/hair states) that downstream shots carry identity from. Anchor-then-fan-out; uses `image-edit` as the derive engine; output written to the user's working folder.
- Added three art-department agents: `casting-director` (identity), `costume-designer` (turnaround + wardrobe), `makeup-hair` (HMU states) — facets of one `char-{show}-{name}.md` asset.
- Added creative craft `context/reference-craft-character.md` (casting/costume/makeup-hair artistry with real-master anchors) and technical guides `guide-character-consistency.md` + `guide-turnaround-sheets.md`.
- Added the typed asset naming taxonomy to `guide-asset-reference.md` (`{type}-{show}-{name}.md`, `assets/{type}/{name}/`; codes char/prop/set/veh/cam/light/style/fx).
- Wired into `skills/build.py` + `plugin/assemble.py`; docs updated to seven skills; sources added to `knowledge-base/Miscellaneous-Sources.md`.

## v0.5.1 - 2026-06-30

### New skill: image-edit (image-to-image) — closes the i2i coverage gap

- Added `image-edit` skill — the still sibling of `footage-transform`: write/refine i2i prompts that preserve a real photo or generated still and change one thing (recolor/material, swap the background/crowd/world around a preserved subject, add or progress a wound, age a face, relight/regrade, remove/clean up, or compose locked references into a new scene). Trigger phrases include "change this image to X", "swap the crowd/background/wardrobe", "make these fans Moroccan instead of Dutch", "recolor this costume". Previously these requests had no home — `footage-transform` is v2v-only.
- Added foundation craft guide `context/guide-image-editing.md` (preserve-then-change, the four edit mechanisms, the denoise-strength dial, lighting integration, common edit types).
- Added foundation craft guide `context/guide-asset-reference.md` (anchor-then-fan-out, identity-block vs scene-block, reference-vs-LoRA decision gate, effective reference counts, multi-reference composition) — the shared spine for the upcoming art-department asset layer (v0.6+).
- Wired `image-edit` into `skills/build.py` and `plugin/assemble.py`; docs updated to six skills.
- Added `ROADMAP.md` (and staged stub crew/skills under `roadmap/`) planning the v0.6+ art department: Production Designer, casting, costume, makeup/hair, propmaster, location scout — character sheets, prop turntables, and location packs.

## v0.5.0 - 2026-06-30

### New skill: footage-transform (video-to-video)

- Added `footage-transform` skill — write/refine v2v prompts that preserve a real source clip and change one thing (add a VFX element, swap the environment, drop in a photoreal creature, sync a camera move to a spoken line, generate a transformed start frame).
- Added model-agnostic craft guide `context/guide-footage-transformation.md` (preserve-then-change, lighting/optics integration, timed moves with dual anchors, prepended-intro duration budget, first-frame workflow).
- Refreshed `context/model-video-seedance-pro.md` to Seedance 2.x: video-to-video `@source`/`@creature` input grammar, NON-IP guardrail, SFX-line convention, and 2.x input limits.
- Wired the new skill into `skills/build.py` and `plugin/assemble.py`; docs updated to five skills.

## v0.4.1 - 2026-06-30

### Distribution fix

- Ship a prebuilt `generative-cinema.plugin` at the repo root so Cowork users can install without building it.
- `plugin/assemble.py --package` now writes the artifact to the repo root (was a hardcoded session path).
- Un-ignored the committed root `generative-cinema.plugin` in `.gitignore`.
- README Cowork install now links the prebuilt file; maintenance note covers rebuilding/committing it on release.

## v0.2 - 2026-06-29

### Model currency refresh (June 2026)

- Added `context/model-currency-2026-06.md` as the single source of truth for current model versions.
- Added a currency callout to each of the 9 original model docs (FLUX.2, Nano Banana 2, Midjourney v8.1, Seedream 5, Seedance 2.5, Runway Gen-4.5, Veo 3.1, Luma Ray3.2).

### New model docs (12 models total)

- `model-video-kling-3.md` - Kling 3.0 (native 4K, fluid motion, Motion Control/Brush).
- `model-video-sora-2.md` - Sora 2 / 2 Pro (multi-shot storytelling, native dialogue; API sunset Sep 24 2026).
- `model-video-wan-2-6.md` - Wan 2.6 (open-weights, native audio/lip-sync, self-hostable).

### Cinematic craft guides (decision-support)

Heuristic-format guides (Decision / Use when / Because / Prompt translation / Watch-outs / Anchors):

- `guide-shot-selection.md`, `guide-lens-language.md`, `guide-continuity-rules.md`, `guide-sequence-construction.md` (P0).
- `guide-visual-structure.md`, `guide-color-story.md`, `guide-creative-approaches.md` (P1).
- `guide-ai-generation-strategy.md` (P2 - craft under current model limits).
- See `docs/history/CRAFT-EXPANSION-PROPOSAL.md` for the original roadmap.

### Agent skills (`skills/`)

Evolved the Custom GPT prompts into self-contained, progressively-disclosed skills:

- `project-context` (visual DNA interview), `sequence-design` (scene/coverage planning), `shot-prompt` (six-layer prompt generation), `model-docs` (document/refresh a model).
- `skills/build.py` syncs `context/` into each skill's bundled `references/` and packages installable `.skill` files to `skills/dist/` (git-ignored).
- Pipeline: project-context -> sequence-design -> shot-prompt -> prompts.

## v0.1 - 2025-11-07

### Initial Release

**9 Production-Ready Models:**
- Image Generation (4): FLUX.1 Pro, Gemini Flash, Midjourney v7, Seedream 4.0
- Video Generation (4): Seedance Pro, Runway Gen-4 Turbo, Google Veo 3.1, Luma Ray3
- Image Editing (1): FLUX.1 Kontext

**Show Context System:**
- Meta-generator for creating show context documents (20 essential questions)
- Template for manual creation
- Complete example: luxury automotive commercial

**Custom GPT Integration:**
- Meta-generator for system prompts
- Generic template for quick setup
- Complete deployment guide

**Documentation:**
- 9 model documentation files (consistent template structure)
- Setup guide for Custom GPT deployment
- Common workflow examples
- Model selection decision guide
- Universal prompting principles

**Process Tools:**
- Meta-generator for show contexts
- Meta-generator for system prompts
- Model documentation template
- All files follow `meta-generator-[TYPE]-[SUBTYPE].md` naming convention

**File Structure:**
- `context/` - 9 model documentation files
- `docs/` - Setup guides, workflows, model selection
- `prompts/` - 7 meta-generators and templates
