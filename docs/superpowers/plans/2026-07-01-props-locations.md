# Props & Locations (Phase 2) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship v0.7.0 — a props & locations asset pipeline: the `prop-turntable` and `location-pack` skills, the `propmaster` and `location-scout` agents, and the craft library (creative + technical) they read, with the taxonomy extended for objects/environments and full build wiring.

**Architecture:** `context/` is the single source of truth; `skills/build.py` bundles context files into each skill's `references/` and zips `.skill`s; `plugin/assemble.py` regenerates `plugin/context/` + `plugin/skills/` (repointing `](references/…)` links to `${CLAUDE_PLUGIN_ROOT}/context/`) and **validates** dead links + agent YAML. No unit-test framework — the gate is `python plugin/assemble.py` printing `VALIDATE: OK` and `python skills/build.py` running clean. Mirrors the Phase 1 (character) pipeline exactly.

**Tech Stack:** Markdown (library + skills + agents), Python 3 stdlib build scripts, JSON manifests. Spec: `docs/superpowers/specs/2026-07-01-props-locations-design.md`.

## Global Constraints

- **Target version:** `0.7.0` — set verbatim in `plugin/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` (both `metadata.version` and the plugin-entry `version`), and README banners.
- **Library format for `guide-*.md`:** heuristic decision-unit — `**Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**`
- **Library format for `reference-*.md`:** knowledge catalog with anchor tables (sibling of `reference-craft-character.md`).
- **House style:** match existing `context/guide-*.md` / `reference-*.md` — em-dashes (—) and rich prose ARE the house style; straight quotes; no emojis; technical terms in `` `code` ``. (The "no em-dashes" rule is model-doc-only; no model docs here.) No `[PLACEHOLDER]` in shipped files.
- **Asset naming taxonomy:** environment asset type is `set` (NOT `loc`). Spec files `prop-{show}-{name}.md` / `set-{show}-{name}.md`; folders `assets/prop/{name}/` / `assets/set/{name}/`. **Image filenames carry NO `{show}`** — only the `.md` spec name does. New facets: props `hero`/`ortho`/`detail`/`360`; locations `plate`/`cov`/`tod`. New views: `top`/`bottom`. All lowercase kebab.
- **Asset binaries live in the user's working folder only** — never committed to the plugin repo.
- **3D-assist is deferred** — do NOT create `guide-3d-assist.md`; each technical guide carries a one-line forward-pointer only.
- **Agent frontmatter (strict YAML, required keys):** `name`, `description`, `model`, `color`, `tools`. Use `model: inherit`, `tools: ["Read", "Grep", "Glob"]`. No raw `<…>` tags in frontmatter (assemble.py rejects them). Colors: `propmaster` = pink, `location-scout` = cyan.
- **Commits:** OMIT the `Co-Authored-By` trailer (project preference). Branch: `feat/props-locations` (already created).
- **Build hygiene (Phase 1 lesson):** editing `context/guide-asset-reference.md` re-syncs EVERY skill that bundles it (`image-edit`, `character-sheet`, and the new skills). After `build.py` runs, commit ALL regenerated bundle copies so the tree is clean.

---

### Task 1: Extend the asset taxonomy (§9) for props & locations

**Files:**
- Modify: `context/guide-asset-reference.md` (§9 "Naming & storage")

**Interfaces:**
- Produces: the prop/location facet+view codes that Tasks 2-7 reference. No code symbols.

- [ ] **Step 1: Read §9** of `context/guide-asset-reference.md` to see the current facet line, view line, and the example table (it currently has `char` rows and facets `id/turn/fit/hmu/expr/pose/palette`, views `front/back/side-l/side-r/3q-l/3q-r`).

- [ ] **Step 2: Extend the facet list** — append the new facets to the existing facet line, preserving its exact separator style:
`hero` (prop hero view), `ortho` (orthographic ring member), `detail` (macro/detail), `360` (turntable step), `plate` (location master plate), `cov` (location coverage angle), `tod` (time-of-day/weather variant).

- [ ] **Step 3: Extend the view list** — append `top` and `bottom` to the existing views line (for objects/environments).

- [ ] **Step 4: Add prop + set example rows** to the §9 example block, mirroring the `char` examples, exactly:

```
  Props     prop-{show}-{name}.md          prop-sbw-revolver.md
    hero    prop-revolver-hero.png
    ortho   prop-revolver-ortho-front.png  -back / -side-l / -side-r / -top
    detail  prop-revolver-detail-01.png    state suffix: prop-revolver-hero-aged.png
  Sets      set-{show}-{name}.md           set-sbw-livingroom.md
    plate   set-livingroom-plate.png
    cov     set-livingroom-cov-01.png      (incl. the reverse angle)
    tod     set-livingroom-tod-dawn.png    -tod-night / -tod-rain (one variable)
```

- [ ] **Step 5: Verify.** `grep -n "hero\|ortho\|plate\|tod\|top\|bottom" context/guide-asset-reference.md` shows the new facets/views; code fences balanced; no em-dash/emoji regressions.

- [ ] **Step 6: Commit.**

```bash
git add context/guide-asset-reference.md
git commit -m "feat(context): extend asset taxonomy §9 with prop/location facets + top/bottom views"
```

---

### Task 2: `reference-craft-artdept.md` (creative craft) + record sources

**Files:**
- Create: `context/reference-craft-artdept.md`
- Modify: `knowledge-base/Miscellaneous-Sources.md` (append three entries)

**Interfaces:**
- Produces: `context/reference-craft-artdept.md` (bundled by Tasks 5, 6, 8; read by agents in Task 7).

- [ ] **Step 1: Study the sibling** `context/reference-craft-character.md` for the exact knowledge-catalog format (H1 + intro + department sections each with prose principles + an `### Anchors` table with columns like Name | Signature | Known for | When to reference + a closing "How this feeds the pipeline"). Match it.

- [ ] **Step 2: Write `context/reference-craft-artdept.md`.** Structure:
  - H1 `# Art-Department Craft — Props, Locations & Sets` + 2-3 sentence intro (creative companion to the technical `guide-prop-turntable.md` / `guide-location-pack.md`; each role is dual art+tool; extensible with a Production Designer section in a later phase).
  - `## Props — the object as character` — 4-6 real prose principles: (1) hero vs dressing vs action props; (2) the prop that tells story / period / status; (3) *multiples* — stunt/destruction/continuity duplicates that must match; (4) state variants (pristine/aged/bloodied) as narrative; (5) fabrication and sourcing realities; (6) the propmaster's continuity discipline. Then `### Anchors` table with real entries: **Eric Hart** (prop-building authority), **Independent Studio Services (ISS)** and the prop-house tradition, and 2-3 celebrated hero-prop crafts (e.g. the *Pulp Fiction* briefcase, the *Lord of the Rings* One Ring by Jens Hansen, *Indiana Jones* whip/idol) attributed accurately.
  - `## Locations & Sets — environment as storytelling` — principles: (1) the scouting packet / recce beyond the frame; (2) environment carries disproportionate story; (3) sun-path and light logistics; (4) reverse-angle coherence and set extension; (5) location dressing vs built set vs set decoration. Then `### Anchors` table with real production designers/art directors: **Ken Adam**, **Dante Ferretti**, **Stuart Craig**, **Rick Carter**, **Jack Fisk**, **Nathan Crowley** (attribute their signature films accurately), plus **Michael Rizzo** as the art-department-handbook authority.
  - `## How this feeds the pipeline` — 3-5 lines connecting the art to what `prop-turntable` / `location-pack` lock (hero anchor + ortho ring; master plate + coverage + variants).
  - House style per Global Constraints. Use accurate craft facts; do not fabricate attributions.

- [ ] **Step 3: Append sources to `knowledge-base/Miscellaneous-Sources.md`** in the existing `## Author, _Title_` + note + URL-bullet format:

```markdown
## Eric Hart, _The Prop Building Guidebook: For Theatre, Film, and TV_

the props master's craft: fabrication, materials, multiples, state variants, continuity.

- https://www.propbuildingguidebook.com/
- https://www.routledge.com/The-Prop-Building-Guidebook-For-Theatre-Film-and-TV/Hart/p/book/9781032154619

## Michael Rizzo, _The Art Direction Handbook for Film & Television_

art-department setup, location scouting, executing the design, building scenery.

- https://www.routledge.com/The-Art-Direction-Handbook-for-Film--Television/Rizzo/p/book/9780415842792

## Jane Barnwell, _Production Design: Architects of the Screen_ (with Vincent LoBrutto, _The Filmmaker's Guide to Production Design_)

the production designer's role; environment as storytelling; landmark screen designs.

- https://cup.columbia.edu/book/production-design/9780231850131/
- https://www.amazon.com/Filmmakers-Guide-Production-Design/dp/1581152248
```

- [ ] **Step 4: Verify.** `grep -c "^## " context/reference-craft-artdept.md` >= 4 (intro H1 is `#`, sections are `##`); both `### Anchors` tables have header + separator rows; `grep -n "Prop Building Guidebook" knowledge-base/Miscellaneous-Sources.md` finds the new entry.

- [ ] **Step 5: Commit.**

```bash
git add context/reference-craft-artdept.md knowledge-base/Miscellaneous-Sources.md
git commit -m "feat(context): add reference-craft-artdept (creative craft) + sources"
```

---

### Task 3: `guide-prop-turntable.md` (technical craft)

**Files:**
- Create: `context/guide-prop-turntable.md`

**Interfaces:**
- Produces: `context/guide-prop-turntable.md` (bundled by Tasks 5, 8; read by `propmaster` in Task 7).

- [ ] **Step 1: Study** `context/guide-turnaround-sheets.md` (the closest sibling — object/multi-view craft) and `context/guide-asset-reference.md` §1/§9 for format and the taxonomy filenames.

- [ ] **Step 2: Write the guide.** Decision-unit format. Intro: building a geometry-true prop turntable from a hero anchor via `image-edit`; this is the *technical* companion to `reference-craft-artdept.md` (Props). Sections:
  1. **The hero view (anchor)** — one clean, frame-filling, evenly-lit shot of the prop on a neutral background; why it is the load-bearing anchor; filename `prop-{name}-hero.png`.
  2. **The orthographic ring** — `ortho` views front/back/side-l/side-r/top (add bottom when the underside shows); alignment/scale held constant; filenames `prop-{name}-ortho-front.png` etc.; derive each from the hero via `image-edit` (rotate the object, hold identity) — cross-ref `guide-asset-reference.md` §1 and `guide-image-editing.md`.
  3. **Detail / macro** — `detail` views for hero-prop close-ups (engraving, wear, mechanisms); `prop-{name}-detail-01.png`.
  4. **State variants & multiples** — pristine/aged/bloodied as a state suffix (`prop-{name}-hero-aged.png`); *multiples must match* (stunt/destruction/continuity duplicates); progress states by editing the prior state, not regenerating.
  5. **Optional 360** — `360` facet for an 8-12 step turntable when needed; note diminishing returns.
  6. **Framing-the-asset rules** — fill frame, neutral background, even flat light, consistent scale/lens across views.
  - One-line **3D-assist forward-pointer**: for props that must survive many angles or destruction, a 3D geometry-lock + depth-pass approach is a known technique, deferred to a later phase.
  - Close with `## Quick application` + companion-guides line (`guide-asset-reference.md`, `reference-craft-artdept.md`, `guide-image-editing.md`).

- [ ] **Step 3: Verify.** `grep -n "prop-.*-ortho\|prop-.*-hero" context/guide-prop-turntable.md` finds taxonomy filenames; decision-unit format present; the 3D-assist pointer is a single line (no full guide); no `[PLACEHOLDER]`.

- [ ] **Step 4: Commit.**

```bash
git add context/guide-prop-turntable.md
git commit -m "feat(context): add guide-prop-turntable (object multi-view craft)"
```

---

### Task 4: `guide-location-pack.md` (technical craft)

**Files:**
- Create: `context/guide-location-pack.md`

**Interfaces:**
- Produces: `context/guide-location-pack.md` (bundled by Tasks 6, 8; read by `location-scout` in Task 7).

- [ ] **Step 1: Study** `context/guide-turnaround-sheets.md` and `context/guide-asset-reference.md` §1/§9 for format and taxonomy.

- [ ] **Step 2: Write the guide.** Decision-unit format. Intro: building a location/set pack from a locked master plate via `image-edit`; technical companion to `reference-craft-artdept.md` (Locations & Sets). Sections:
  1. **The master establishing plate (anchor)** — one locked wide plate that fixes geometry, light logic, and key features; filename `set-{name}-plate.png`; the load-bearing anchor everything else is derived from.
  2. **Coverage angles** — `cov` views including the crucial **reverse angle**; keep them consistent with the plate's geometry and light; filenames `set-{name}-cov-01.png` …; derive via `image-edit` from the plate — cross-ref `guide-asset-reference.md` §1 and `guide-image-editing.md`.
  3. **Time-of-day / weather variants** — `tod` variants derived from the *locked master geometry*, changing **one variable at a time** (dawn/day/dusk/night/rain); filenames `set-{name}-tod-dawn.png` etc.; hold geometry, vary only light/atmosphere.
  4. **The continuity table** — record per-variant light direction, key colour, and atmosphere so shots cut together; what to restate in each shot prompt.
  5. **Reverse-angle & set-extension coherence** — the hard cases; keep the plate's landmarks consistent across the reverse.
  - One-line **3D-assist forward-pointer**: blocking the space in 3D for reverse-angle/set-extension coherence is a known technique, deferred to a later phase.
  - Close with `## Quick application` + companion-guides line.

- [ ] **Step 3: Verify.** `grep -n "set-.*-plate\|set-.*-tod" context/guide-location-pack.md` finds taxonomy filenames; decision-unit format present; 3D-assist pointer is one line; no `[PLACEHOLDER]`.

- [ ] **Step 4: Commit.**

```bash
git add context/guide-location-pack.md
git commit -m "feat(context): add guide-location-pack (environment master-plate + coverage + variants craft)"
```

---

### Task 5: `prop-turntable` skill + output template

**Files:**
- Create: `skills/prop-turntable/SKILL.md`
- Create: `skills/prop-turntable/references/prop-template.md`

**Interfaces:**
- Consumes (bundled into `references/` by Task 8): `reference-craft-artdept.md`, `guide-prop-turntable.md`, `guide-asset-reference.md`, `guide-image-editing.md`, `model-currency-2026-06.md`, editing/image model docs.
- Produces: `skills/prop-turntable/SKILL.md` (repointed + validated in Task 8); `prop-template.md` (registered as an assemble HELPER in Task 8).

- [ ] **Step 1: Study** `skills/character-sheet/SKILL.md` (the closest sibling) for frontmatter shape (`name` + multiline `description: >-` with trigger phrases), the load-craft/workflow/output structure, and the `](references/…)` / `](references/models/…)` link convention. Also read `roadmap/skills/prop-turntable/SKILL.md` (the stub being promoted).

- [ ] **Step 2: Write `skills/prop-turntable/SKILL.md`.** Body:
  - Purpose — build a persistent prop reference; identity lives in the asset, prompts carry only change.
  - When to use — a prop recurring across shots, or any turntable/model-sheet/hero-prop request.
  - Core principle — anchor (hero view) then fan out (ortho ring, details) via `image-edit`.
  - Step: Load craft — read `](references/reference-craft-artdept.md)`, `](references/guide-prop-turntable.md)`, `](references/guide-asset-reference.md)`, `](references/guide-image-editing.md)`; inherit `project-context-{show}.md` / `art-bible` if present.
  - Step: Hero anchor → Step: orthographic ring (front/back/side-l/side-r/top) → Step: details → Step: state variants/multiples (edit prior state) → optional 360.
  - Step: Model + references — pick i2i model; verify counts vs `](references/model-currency-2026-06.md)`; read the matching `](references/models/model-*.md)`.
  - Step: Output — write `prop-{show}-{name}.md` per `](references/prop-template.md)` + images under `assets/prop/{name}/` **to the user's working folder**; image filenames carry no `{show}`.
  - Critical rules — anchor before fan-out; hold form/scale/lens across views; pin material/finish/hex; multiples must match; edit-don't-regenerate for states; binaries to user folder; verify counts vs currency.

- [ ] **Step 3: Write `skills/prop-turntable/references/prop-template.md`.** Output skeleton: H1 `# {SHOW} - {Name} - Prop Sheet`; `## Hero` (hero image path `assets/prop/{name}/prop-{name}-hero.png` + description/material/finish); `## Orthographic ring` (the five/six view paths); `## Details` (detail paths + what each shows); `## State variants` (per state: name + suffix path, e.g. `-hero-aged.png`); `## Multiples` (duplicates that must match, if any); `## Reference notes` (counts/strength/model). Real taxonomy paths as examples. No leftover placeholders in prose (template fill-in tokens like `{Name}` are fine).

- [ ] **Step 4: Verify.** `grep -n "](references/" skills/prop-turntable/SKILL.md` lists the links; frontmatter has `name` + `description`, no tabs; template has the sections + taxonomy-correct paths (no `{show}` in image names).

- [ ] **Step 5: Commit.**

```bash
git add skills/prop-turntable/SKILL.md skills/prop-turntable/references/prop-template.md
git commit -m "feat(skills): add prop-turntable skill + prop output template"
```

---

### Task 6: `location-pack` skill + output template

**Files:**
- Create: `skills/location-pack/SKILL.md`
- Create: `skills/location-pack/references/set-template.md`

**Interfaces:**
- Consumes (bundled by Task 8): `reference-craft-artdept.md`, `guide-location-pack.md`, `guide-asset-reference.md`, `guide-image-editing.md`, `model-currency-2026-06.md`, editing/image model docs.
- Produces: `skills/location-pack/SKILL.md`; `set-template.md` (assemble HELPER in Task 8).

- [ ] **Step 1: Study** `skills/character-sheet/SKILL.md` and the just-written `skills/prop-turntable/SKILL.md` for structure/link convention; read `roadmap/skills/location-pack/SKILL.md` (stub).

- [ ] **Step 2: Write `skills/location-pack/SKILL.md`.** Body mirrors the prop skill's shape but for environments:
  - Purpose/when/core-principle (anchor = master plate, fan out = coverage + variants via `image-edit`).
  - Load craft — read `](references/reference-craft-artdept.md)`, `](references/guide-location-pack.md)`, `](references/guide-asset-reference.md)`, `](references/guide-image-editing.md)`; inherit project/art-bible if present.
  - Step: master plate anchor → Step: coverage angles incl. reverse (`cov`) → Step: time/weather variants (`tod`, one variable at a time) → Step: continuity table.
  - Step: Model + references — verify vs `](references/model-currency-2026-06.md)`; read `](references/models/model-*.md)`.
  - Step: Output — write `set-{show}-{name}.md` per `](references/set-template.md)` + images under `assets/set/{name}/` **to the user's working folder**; note the crew is `location-scout` but the asset type is `set`.
  - Critical rules — lock the master plate; derive coverage/variants from it; change one variable per `tod`; keep reverse-angle landmarks consistent; binaries to user folder; verify counts vs currency.

- [ ] **Step 3: Write `skills/location-pack/references/set-template.md`.** Skeleton: H1 `# {SHOW} - {Name} - Location/Set Pack`; `## Master plate` (`assets/set/{name}/set-{name}-plate.png` + geometry/light-logic notes); `## Coverage` (cov paths incl. reverse angle); `## Time-of-day / weather variants` (per variant: `-tod-*` path + light direction/colour/atmosphere); `## Continuity table` (per-variant key direction/colour/atmosphere to restate in shots); `## Reference notes`. Real taxonomy paths; no `{show}` in image names.

- [ ] **Step 4: Verify.** `grep -n "](references/" skills/location-pack/SKILL.md` lists links; frontmatter valid; template has the sections + `set-{name}-plate.png` / `-tod-*` paths.

- [ ] **Step 5: Commit.**

```bash
git add skills/location-pack/SKILL.md skills/location-pack/references/set-template.md
git commit -m "feat(skills): add location-pack skill + set output template"
```

---

### Task 7: `propmaster` + `location-scout` agents

**Files:**
- Create: `plugin/agents/propmaster.md`
- Create: `plugin/agents/location-scout.md`

**Interfaces:**
- Consumes: `${CLAUDE_PLUGIN_ROOT}/context/reference-craft-artdept.md`, `guide-prop-turntable.md`, `guide-location-pack.md` (in `plugin/context/` after Task 8's assemble run).
- Produces: two agent files that pass assemble.py's strict-YAML validation.

- [ ] **Step 1: Study** `plugin/agents/cinematographer.md` / `plugin/agents/casting-director.md` (persona → When it fires → Method reading `${CLAUDE_PLUGIN_ROOT}/context/…` → Output). Match shape and voice.

- [ ] **Step 2: Write `plugin/agents/propmaster.md`.** Frontmatter verbatim:

```markdown
---
name: propmaster
description: >-
  The Propmaster. Build a persistent prop reference — a hero anchor and an
  orthographic ring — so an object holds across every shot. Use when the user says
  "build a prop turntable", "lock this prop", "make a hero prop reference", "keep
  this object consistent", or "turntable this". Owns hero/dressing/action props,
  multiples, and state variants; applies the prop-turntable craft. Reads the creative
  craft and the technical guide; hands the locked prop to shot-prompt / image-edit.
model: inherit
color: pink
tools: ["Read", "Grep", "Glob"]
---
```
  Body: persona (a propmaster who thinks in hero vs dressing vs action props, multiples, state variants — per `reference-craft-artdept.md` Props); when it fires; method (read `${CLAUDE_PLUGIN_ROOT}/context/reference-craft-artdept.md` + `guide-prop-turntable.md` + `guide-asset-reference.md`; build hero anchor → ortho ring → details → states via image-edit); output (`prop-{show}-{name}.md` + `assets/prop/{name}/prop-{name}-hero.png`, `-ortho-*`, `-detail-*`). Image names carry no `{show}`.

- [ ] **Step 3: Write `plugin/agents/location-scout.md`.** Same frontmatter shape, `name: location-scout`, `color: cyan`, trigger phrases ("scout this location", "build a location pack", "lock this environment", "master plate + coverage", "time-of-day variants"). Body: persona (a location scout/manager — scouting packet, environment as story, reverse-angle coherence — per `reference-craft-artdept.md` Locations & Sets); method (read Locations craft + `guide-location-pack.md` + `guide-asset-reference.md`; build master plate → coverage incl. reverse → tod variants via image-edit); output (`set-{show}-{name}.md` + `assets/set/{name}/set-{name}-plate.png`, `-cov-*`, `-tod-*`). Note the crew name is `location-scout` but the asset type/file is `set`.

- [ ] **Step 4: Verify frontmatter.**

```bash
for a in propmaster location-scout; do echo "== $a =="; sed -n '1,12p' plugin/agents/$a.md; done
```
Expected: each shows the five keys, correct colors (pink/cyan), no `<` lines in frontmatter.

- [ ] **Step 5: Commit.**

```bash
git add plugin/agents/propmaster.md plugin/agents/location-scout.md
git commit -m "feat(agents): add propmaster and location-scout crew"
```

---

### Task 8: Build wiring + integration validation (the gate)

**Files:**
- Modify: `skills/build.py` (add `prop-turntable` and `location-pack` to `MANIFEST`)
- Modify: `plugin/assemble.py` (add both skills to `SKILLS`; add `prop-template.md` + `set-template.md` to `HELPERS`)

**Interfaces:**
- Consumes: all files from Tasks 1-7.
- Produces: populated `references/` for both skills; regenerated `plugin/context/*`, `plugin/skills/*`; a passing `VALIDATE: OK`.

- [ ] **Step 1: Add MANIFEST entries to `skills/build.py`** (after the `character-sheet` entry):

```python
    "prop-turntable": [
        ("reference-craft-artdept.md", "references/reference-craft-artdept.md"),
        ("guide-prop-turntable.md", "references/guide-prop-turntable.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-image-editing.md", "references/guide-image-editing.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-editing-flux-kontext.md", "references/models/model-editing-flux-kontext.md"),
        ("model-image-gemini-flash.md", "references/models/model-image-gemini-flash.md"),
        ("model-image-seedream-4.md", "references/models/model-image-seedream-4.md"),
        ("model-image-flux-pro.md", "references/models/model-image-flux-pro.md"),
    ],
    "location-pack": [
        ("reference-craft-artdept.md", "references/reference-craft-artdept.md"),
        ("guide-location-pack.md", "references/guide-location-pack.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-image-editing.md", "references/guide-image-editing.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-editing-flux-kontext.md", "references/models/model-editing-flux-kontext.md"),
        ("model-image-gemini-flash.md", "references/models/model-image-gemini-flash.md"),
        ("model-image-seedream-4.md", "references/models/model-image-seedream-4.md"),
        ("model-image-flux-pro.md", "references/models/model-image-flux-pro.md"),
    ],
```

- [ ] **Step 2: Register skills + helpers in `plugin/assemble.py`.** Set the `SKILLS` list to:

```python
SKILLS = ["project-context", "sequence-design", "shot-prompt", "model-docs", "footage-transform", "image-edit", "character-sheet", "prop-turntable", "location-pack"]
```
And append to `HELPERS`:

```python
    SKILLS_SRC / "prop-turntable/references/prop-template.md",
    SKILLS_SRC / "location-pack/references/set-template.md",
```

- [ ] **Step 3: Run the skill build.**

```bash
python skills/build.py
```
Expected: `sync prop-turntable: …` and `sync location-pack: …` lines, then `zip … prop-turntable.skill` and `zip … location-pack.skill`, no traceback. (It also re-syncs `image-edit` and `character-sheet` bundles of `guide-asset-reference.md` because Task 1 changed §9 — expected.)

- [ ] **Step 4: Run assemble + validate (the gate).**

```bash
python plugin/assemble.py
```
Expected: `skill: prop-turntable`, `skill: location-pack`, and final line `VALIDATE: OK`. If it prints `FAIL …`, fix the named missing reference/agent and re-run before committing. Paste the final line into your report.

- [ ] **Step 5: Commit build-script edits AND every regenerated output** (Phase 1 lesson — include the re-synced `image-edit`/`character-sheet` bundles so the tree is clean):

```bash
git add skills/build.py plugin/assemble.py skills/prop-turntable/references skills/location-pack/references skills/image-edit/references skills/character-sheet/references plugin/context plugin/skills
git status --porcelain   # confirm nothing else pending (except .superpowers scratch)
git commit -m "build: wire prop-turntable + location-pack into build.py + assemble.py"
```

- [ ] **Step 6: Confirm tree clean** (excluding `.superpowers/`): `git status --porcelain | grep -v .superpowers` prints nothing. If a regenerated bundle remains, `git add` it and amend the commit.

---

### Task 9: Docs, ROADMAP cleanup, version bump, stub removal + final validate

**Files:**
- Modify: `README.md`, `plugin/README.md`, `CHANGELOG.md`, `ROADMAP.md`, `roadmap/README.md`
- Modify: `plugin/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- Delete: `roadmap/agents/propmaster.md`, `roadmap/agents/location-scout.md`, `roadmap/skills/prop-turntable/`, `roadmap/skills/location-pack/`

- [ ] **Step 1: Bump versions to `0.7.0`** in `plugin/.claude-plugin/plugin.json` (`"version"`), `.claude-plugin/marketplace.json` (BOTH `metadata.version` and the plugin-entry `version`), and README banners (`README.md` `**Version**: 0.7.0`; `plugin/README.md` version text). Verify: `grep -rn '0.6.0' plugin/.claude-plugin/plugin.json .claude-plugin/marketplace.json README.md` returns nothing.

- [ ] **Step 2: Update `README.md`** — add `prop-turntable` and `location-pack` rows to the Skills table (Level: Asset), `propmaster` and `location-scout` rows to the Agents table, mention `reference-craft-artdept`/`guide-prop-turntable`/`guide-location-pack` in the craft-guides paragraph, note the `assets/prop/{name}/` and `assets/set/{name}/` conventions. Update the repository-layout skill/agent counts to `skills/ (9) agents/ (10)`. Model list unchanged.

- [ ] **Step 3: Update `plugin/README.md`** — mirror the 2 skill rows + 2 agent rows; skill count language → nine skills.

- [ ] **Step 4: Add the `CHANGELOG.md` v0.7.0 entry** at the top:

```markdown
## v0.7.0 - 2026-07-01

### New: Props & Locations (art department, Phase 2)

- Added the `prop-turntable` skill — build a persistent prop reference (hero anchor, orthographic ring, detail views, state variants/multiples) written to your working folder; uses `image-edit` as the derive engine.
- Added the `location-pack` skill — build a location/set reference (master establishing plate, coverage incl. the reverse angle, time-of-day/weather variants from locked geometry) with a continuity table.
- Added two art-department agents: `propmaster` (prop turntables) and `location-scout` (location packs).
- Added creative craft `context/reference-craft-artdept.md` (props + locations/sets artistry with real-master anchors) and technical guides `guide-prop-turntable.md` + `guide-location-pack.md`. 3D-assist (Blender) is noted as a deferred technique.
- Extended the asset naming taxonomy in `guide-asset-reference.md` §9 with prop facets (`hero`/`ortho`/`detail`/`360`), location facets (`plate`/`cov`/`tod`), and `top`/`bottom` views. Environment asset type is `set`.
- Wired into `skills/build.py` + `plugin/assemble.py`; docs updated to nine skills / ten agents; sources added to `knowledge-base/Miscellaneous-Sources.md`.
```

- [ ] **Step 5: Update `ROADMAP.md`** — mark `### Phase 2 - Props & Locations ✅ *shipped in v0.7.0*`, check off its bullets, and finish the deferred cleanup: rename any remaining `location-{show}-{name}.md` → `set-{show}-{name}.md` (esp. §3.6 Location Scout "Builds" and §4 skill table), and update pre-taxonomy `assets/…` longhand in §3.2/§3.4/§3.5 to the §9 forms (`assets/char/{name}/`, `assets/prop/{name}/`, `assets/set/{name}/`).

- [ ] **Step 6: Remove promoted stubs.**

```bash
git rm -r roadmap/agents/propmaster.md roadmap/agents/location-scout.md roadmap/skills/prop-turntable roadmap/skills/location-pack
```
Then edit `roadmap/README.md` to drop `propmaster`, `location-scout`, `prop-turntable`, `location-pack` from the listing (leave `production-designer` + `art-direction` for Phase 3).

- [ ] **Step 7: Final validate.**

```bash
python plugin/assemble.py
```
Expected: `VALIDATE: OK`.

- [ ] **Step 8: Commit.**

```bash
git add -A
git commit -m "docs: ship v0.7.0 props & locations (README/CHANGELOG/ROADMAP, version, stubs, taxonomy cleanup)"
```

---

## Post-plan notes

- **Release (Task 10, after final whole-branch review + merge):** merge `feat/props-locations` → `main`; `git tag -a v0.7.0`; `python plugin/assemble.py --package`; `gh release create v0.7.0 generative-cinema.plugin` (keep v0.6.0 + v0.5.1 releases intact). GitHub release proceeds per the user's standing go-ahead for this phase. The `.plugin` is gitignored — do not commit it.
- After all tasks: `git log --oneline feat/props-locations` should show the spec + 9 task commits.
