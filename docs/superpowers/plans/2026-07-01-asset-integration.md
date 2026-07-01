# Asset Integration & QC (Phase 4) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship v0.9.0 (final roadmap phase) - wire the persistent assets into the shot pipeline: a `refs:` attachment notation, sequence-design/first-ad attach, shot-prompt/cinematographer consume, script-supervisor asset-continuity audit, model-currency caveats, and a new pipeline doc.

**Architecture:** `context/` is the single source of truth; `skills/build.py` bundles context files into each skill's `references/`; `plugin/assemble.py` regenerates `plugin/context/` + `plugin/skills/` (repointing `](references/...)` to `${CLAUDE_PLUGIN_ROOT}/context/`) and validates. No unit tests - the gate is `python plugin/assemble.py` printing `VALIDATE: OK` and `python skills/build.py` clean. No new skills or agents - only edits to existing skills/agents + one new doc. Mirrors the Phase 1-3 pipelines.

**Tech Stack:** Markdown (library + skills + agents + docs), Python 3 stdlib build scripts. Spec: `docs/superpowers/specs/2026-07-01-asset-integration-design.md`.

## Global Constraints

- **Target version:** `0.9.0` - verbatim in `plugin/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` (both `metadata.version` and the plugin-entry `version`), and README banners.
- **The `refs:` notation:** a per-shot field `refs: <id>[, <id>...]` where each id is an asset spec-file stem - `char-{name}`, `prop-{name}`, `set-{name}` - with NO `{show}` and NO extension. A shot with no assets omits `refs:`. This exact form is used consistently across guide, sequence-design, first-ad, shot-prompt, cinematographer, script-supervisor, and `docs/05-asset-pipeline.md`.
- **House style:** match existing files - `guide-*.md` use em-dashes + decision-unit format; `docs/0X-*.md` match the existing docs style; `plugin/agents/*.md` match existing agents. `model-currency`/`docs` prose: straight quotes, no emojis, technical terms in `code`. No `[PLACEHOLDER]` in shipped files.
- **No new skills or agents.** Agent edits are BODY-ONLY (do not change frontmatter). No `SKILLS`/`HELPERS` changes in `assemble.py`.
- **Project name is `generative-wrangler`** (do not reintroduce `generative-cinema` in any new/edited functional file).
- **Commits:** OMIT the `Co-Authored-By` trailer. Branch: `feat/asset-integration` (already created).
- **Build hygiene (Phase 1-3 lesson):** editing `context/guide-asset-reference.md` or `context/model-currency-2026-06.md` re-syncs EVERY skill that bundles them; editing a skill's `SKILL.md` regenerates its `plugin/skills/` copy. After `build.py`/`assemble.py` run, commit ALL regenerated outputs so the tree is clean.

---

### Task 1: The `refs:` attachment notation (guide-asset-reference) + source

**Files:**
- Modify: `context/guide-asset-reference.md` (add a new section after the current last numbered section, before `## Quick application`)
- Modify: `knowledge-base/Miscellaneous-Sources.md` (append one entry)

**Interfaces:**
- Produces: the canonical `refs:` notation that Tasks 2-7 and the new doc reference.

- [ ] **Step 1: Read** `context/guide-asset-reference.md` to find the current last numbered section (it will be `## 9. Naming & storage` or higher after prior phases) and the `## Quick application` block. Add the new section with the next number, before `## Quick application`.

- [ ] **Step 2: Add the "Attaching references to shots" section** in the decision-unit format:

```markdown
## 10. Attaching references to shots

- **Use when:** a shot uses one or more locked assets (character, prop, set) and
  must carry their identity.
- **Because:** the coverage layer knows which assets a beat needs; the shot layer
  needs that list to attach the right anchor images and restate the right identity
  blocks. A written contract keeps attach and consume in sync.
- **Prompt translation - the notation:** end the shot line with
  `refs: <id>[, <id>...]`, where each id is an asset spec-file stem:
  `char-{name}` - `prop-{name}` - `set-{name}` (NO `{show}`, NO extension; the show
  is implied by the loaded project). Example:

  ```
  S2-03  Coverage CU - 85mm - serves the turn - refs: char-eli, prop-revolver, set-livingroom
  ```

  Each id resolves to its spec (`char-{show}-{name}.md`) and anchor image
  (`assets/char/{name}/char-{name}-id-front.png`, `assets/prop/{name}/prop-{name}-hero.png`,
  `assets/set/{name}/set-{name}-plate.png`) via the taxonomy (§9).
- **Watch-outs:** a shot that needs an asset but omits `refs:` will re-derive
  identity from text and drift; an id with no matching spec is a broken reference -
  the `script-supervisor` audits both.
- **Anchors:** the continuity script (every shot names what it must match).
```

- [ ] **Step 3: Add a bullet to `## Quick application`** (final item):

```markdown
8. **Attach** the shot's assets with `refs:` (§10) so the shot layer carries identity
   from the anchor image and restates the identity block verbatim.
```

- [ ] **Step 4: Append the source to `knowledge-base/Miscellaneous-Sources.md`:**

```markdown
## Pat P. Miller, _Script Supervising and Film Continuity_

the industry-standard continuity craft: matching, screen direction, breakdowns; grounds the asset-continuity audit.

- https://www.routledge.com/Script-Supervising-and-Film-Continuity/Miller/p/book/9780240802947
```

- [ ] **Step 5: Verify.** `grep -n "refs:" context/guide-asset-reference.md` shows the notation; `grep -n "Script Supervising" knowledge-base/Miscellaneous-Sources.md` finds the source; code fences balanced; no `[PLACEHOLDER]`.

- [ ] **Step 6: Commit.**

```bash
git add context/guide-asset-reference.md knowledge-base/Miscellaneous-Sources.md
git commit -m "feat(context): add refs: attachment notation (guide-asset-reference) + continuity source"
```

---

### Task 2: Attach - `sequence-design` skill

**Files:**
- Modify: `skills/sequence-design/SKILL.md`

**Interfaces:**
- Consumes: the `refs:` notation from Task 1.
- Produces: a shot-list format that includes `refs:` per shot (read by `shot-prompt` in Task 4).

- [ ] **Step 1: Read** `skills/sequence-design/SKILL.md` fully (note its steps and its shot-list output-format block).

- [ ] **Step 2: Add an "Attach asset references" step** (after the shot-list step): instruct the skill to scan the working folder for `char-`/`prop-`/`set-` spec files and append `refs: <ids>` to each shot line naming the assets that beat needs (a shot with no assets omits `refs:`). Reference the craft with a `](references/guide-asset-reference.md)` link (Task 8 bundles it).

- [ ] **Step 3: Update the output-format example** in the SKILL to show `refs:` on shot lines, e.g. `S<n>-03  Coverage CU - <lens> - serves <beat> - intensity <x> - refs: char-eli, set-livingroom`.

- [ ] **Step 4: Verify.** `grep -n "refs:" skills/sequence-design/SKILL.md` shows the notation in the step + example; `grep -n "](references/guide-asset-reference.md)" skills/sequence-design/SKILL.md` shows the new link; no frontmatter change; no `[PLACEHOLDER]`.

- [ ] **Step 5: Commit.**

```bash
git add skills/sequence-design/SKILL.md
git commit -m "feat(skills): sequence-design attaches asset refs: to shot lines"
```

---

### Task 3: Attach - `first-ad` agent

**Files:**
- Modify: `plugin/agents/first-ad.md` (BODY only - no frontmatter change)

- [ ] **Step 1: Read** `plugin/agents/first-ad.md`. In its Method + Output, add the attach step: scan for `char-`/`prop-`/`set-` specs and append `refs:` to each shot line per the notation in `${CLAUDE_PLUGIN_ROOT}/context/guide-asset-reference.md` §10. Keep the frontmatter untouched.

- [ ] **Step 2: Verify.** `grep -n "refs:" plugin/agents/first-ad.md` shows it; `sed -n '1,12p' plugin/agents/first-ad.md` confirms frontmatter unchanged (still the five keys).

- [ ] **Step 3: Commit.**

```bash
git add plugin/agents/first-ad.md
git commit -m "feat(agents): first-ad attaches asset refs to the shot list"
```

---

### Task 4: Consume - `shot-prompt` skill

**Files:**
- Modify: `skills/shot-prompt/SKILL.md`

**Interfaces:**
- Consumes: the `refs:` shot lines from Task 2.

- [ ] **Step 1: Read** `skills/shot-prompt/SKILL.md` fully.

- [ ] **Step 2: Add a "Consume attached references" step** (in the load/build flow): for each id in a shot's `refs:`, read the asset spec (`char-{show}-{name}.md` etc.), restate its **identity/descriptor block verbatim**, attach its **anchor image path** as the model reference, apply *identity = reference, change = prompt*, and inherit the `art-bible-{show}.md` palette/CMF. Add `](references/guide-asset-reference.md)` and `](references/guide-image-editing.md)` links for the craft (Task 8 bundles them).

- [ ] **Step 3: Add a Critical rule** that a shot with `refs:` must carry the anchor image + verbatim identity block, not re-derive identity from text.

- [ ] **Step 4: Verify.** `grep -n "refs:\|identity block\|](references/guide-asset-reference.md)\|](references/guide-image-editing.md)" skills/shot-prompt/SKILL.md` shows the additions; no frontmatter change; no `[PLACEHOLDER]`.

- [ ] **Step 5: Commit.**

```bash
git add skills/shot-prompt/SKILL.md
git commit -m "feat(skills): shot-prompt consumes attached asset refs (identity = reference)"
```

---

### Task 5: Consume - `cinematographer` agent

**Files:**
- Modify: `plugin/agents/cinematographer.md` (BODY only)

- [ ] **Step 1: Read** `plugin/agents/cinematographer.md`. In its Method, add the consume step: for each id in a shot's `refs:`, load the asset spec, restate the identity block verbatim, attach the anchor image, apply identity = reference / change = prompt (cross-ref `${CLAUDE_PLUGIN_ROOT}/context/guide-asset-reference.md` §10). Frontmatter untouched.

- [ ] **Step 2: Verify.** `grep -n "refs:\|identity" plugin/agents/cinematographer.md` shows it; frontmatter unchanged.

- [ ] **Step 3: Commit.**

```bash
git add plugin/agents/cinematographer.md
git commit -m "feat(agents): cinematographer consumes attached asset refs"
```

---

### Task 6: Audit - `script-supervisor` agent

**Files:**
- Modify: `plugin/agents/script-supervisor.md` (BODY only)

- [ ] **Step 1: Read** `plugin/agents/script-supervisor.md` (note its "What to audit" + severity-grouped output).

- [ ] **Step 2: Add an "Asset continuity" audit item** to its checks: (a) missing/wrong reference - a shot needing an asset but with no `refs:`, or an id with no matching spec; (b) state drift - costume/HMU/prop state changing across a cut without motivation (wrong `-fit-`/`-hmu-`/`-hero-<state>` variant); (c) geometry mismatch - a location reverse/coverage breaking the master plate's geometry/light. Fold into the existing severity-grouped report. Cross-ref `${CLAUDE_PLUGIN_ROOT}/context/guide-asset-reference.md` §10. Frontmatter untouched.

- [ ] **Step 3: Verify.** `grep -n "asset\|refs:\|state drift\|geometry" plugin/agents/script-supervisor.md` shows the additions; frontmatter unchanged (five keys).

- [ ] **Step 4: Commit.**

```bash
git add plugin/agents/script-supervisor.md
git commit -m "feat(agents): script-supervisor audits asset continuity (missing ref, state drift, geometry)"
```

---

### Task 7: Currency caveats + the pipeline doc

**Files:**
- Modify: `context/model-currency-2026-06.md`
- Create: `docs/05-asset-pipeline.md`

- [ ] **Step 1: Add a "Reference-count & strength caveats (per model)" subsection to `context/model-currency-2026-06.md`** (after the Image Generation table or in a clearly-headed subsection). Content (version-anchored, plain hyphens, no emojis):

```markdown
## Reference-count & strength caveats (per model)

The asset layer's reference-count guidance is version-sensitive - verify here before quoting.

| Model | Effective reference capacity | Notes |
|---|---|---|
| Nano Banana Pro (Gemini 3 Pro Image) | ~14 objects / ~5 characters | strongest multi-subject holder |
| FLUX.2 | up to ~10 references | strong multi-image reference |
| Seedream 5 | up to ~10 references | multi-reference identity |
| Luma Uni-1 | up to 9 references (explicit roles) | STYLE/CHARACTER/COMPOSITION role system |

General: ~4-6 references is the consistency sweet spot; reference strength ~0.7 (workable 0.6-0.8). These numbers move with model versions - the `researcher` / `model-docs` loop keeps them current.
```

- [ ] **Step 2: Create `docs/05-asset-pipeline.md`** matching the existing `docs/0X-*.md` style (read `docs/02-workflow-basics.md` and `docs/04-six-layer-framework.md` for tone). Cover the end-to-end flow: `project-context` (look) -> `art-bible` (world) -> assets (`character-sheet` / `prop-turntable` / `location-pack`) -> attach (`refs:` in `sequence-design`) -> consume (`shot-prompt`) -> QC (`script-supervisor`). Include a worked shot line with `refs:` and a short before/after showing how `shot-prompt` renders it (identity block restated + anchor image attached). Use the canonical `refs:` notation and taxonomy paths. No emojis; technical terms in `code`.

- [ ] **Step 3: Verify.** `grep -n "refs:" docs/05-asset-pipeline.md` shows the worked example; `grep -n "Reference-count" context/model-currency-2026-06.md` shows the subsection; no `[PLACEHOLDER]`.

- [ ] **Step 4: Commit.**

```bash
git add context/model-currency-2026-06.md docs/05-asset-pipeline.md
git commit -m "docs: add per-model reference-count caveats + docs/05-asset-pipeline.md"
```

---

### Task 8: Build re-wire + integration validation (the gate)

**Files:**
- Modify: `skills/build.py` (add `guide-asset-reference.md` to `sequence-design`; add `guide-asset-reference.md` + `guide-image-editing.md` to `shot-prompt`)

**Interfaces:**
- Consumes: the edited SKILL.md links from Tasks 2, 4 and the context edits from Tasks 1, 7.
- Produces: bundled references for the new links; a passing `VALIDATE: OK`.

- [ ] **Step 1: Add to the `sequence-design` MANIFEST entry in `skills/build.py`** (append this pair inside the existing `"sequence-design": [ ... ]` list):

```python
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
```

- [ ] **Step 2: Add to the `shot-prompt` MANIFEST entry in `skills/build.py`** (append these two pairs inside the existing `"shot-prompt": [ ... ]` list):

```python
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-image-editing.md", "references/guide-image-editing.md"),
```

- [ ] **Step 3: Run the skill build.**

```bash
python skills/build.py
```
Expected: `sync sequence-design: guide-asset-reference.md ...` and `sync shot-prompt: guide-asset-reference.md ...` + `guide-image-editing.md ...`. It also re-syncs every skill that bundles `guide-asset-reference.md` / `model-currency-2026-06.md` because Tasks 1 + 7 changed them - expected. No traceback.

- [ ] **Step 4: Run assemble + validate (the gate).**

```bash
python plugin/assemble.py
```
Expected: final line `VALIDATE: OK`. If `FAIL ...`, fix the named missing reference and re-run. Paste the final line into your report.

- [ ] **Step 5: Commit build-script edit AND every regenerated output** (Phase 1-3 lesson - include re-synced bundles for all skills that bundle guide-asset-reference/model-currency AND the regenerated `plugin/skills/*/SKILL.md` for sequence-design + shot-prompt):

```bash
git add skills/build.py skills plugin/context plugin/skills
git status --porcelain | grep -v '\.superpowers'   # confirm nothing else pending
git commit -m "build: bundle guide-asset-reference into sequence-design + shot-prompt; re-sync"
```

- [ ] **Step 6: Confirm tree clean** (excluding `.superpowers/`): `git status --porcelain | grep -v '\.superpowers'` prints nothing. If a regenerated file remains, `git add` it and amend.

---

### Task 9: Docs, version bump, ROADMAP complete + final validate

**Files:**
- Modify: `README.md`, `plugin/README.md`, `CHANGELOG.md`, `ROADMAP.md`
- Modify: `plugin/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`

- [ ] **Step 1: Bump versions to `0.9.0`** in `plugin/.claude-plugin/plugin.json` (`"version"`), `.claude-plugin/marketplace.json` (BOTH `metadata.version` AND the plugin-entry `version` - both currently 0.8.0), and README banners (`README.md` `**Version**: 0.9.0`; `plugin/README.md` version text). Verify `grep -rn '0.8.0' plugin/.claude-plugin/plugin.json .claude-plugin/marketplace.json README.md` returns nothing.

- [ ] **Step 2: Update `README.md`** - refresh the crew/skill flow to show the integrated pipeline: sequence-design/first-ad **attach** asset `refs:`, shot-prompt/cinematographer **consume** them (identity = reference), script-supervisor **audits** asset continuity. Mention `docs/05-asset-pipeline.md` in the docs area. Skill/agent counts unchanged (ten skills / eleven agents). Model list unchanged.

- [ ] **Step 3: Update `plugin/README.md`** - mirror the integrated-flow mention.

- [ ] **Step 4: Add the `CHANGELOG.md` v0.9.0 entry** at the top:

```markdown
## v0.9.0 - 2026-07-01

### New: Asset integration & QC (art department, Phase 4 - roadmap complete)

- Added the `refs:` attachment notation (`context/guide-asset-reference.md` §10): each shot line names its assets by spec-stem (`char-{name}`, `prop-{name}`, `set-{name}`).
- `sequence-design` + `first-ad` now attach `refs:` to each shot line; `shot-prompt` + `cinematographer` consume them - loading each asset's anchor image and restating its identity block verbatim (identity = reference, change = prompt), inheriting the art-bible palette/CMF.
- `script-supervisor` now audits asset continuity: missing/wrong reference, costume/HMU/prop state drift, and location geometry mismatch, alongside its screen-direction/eyeline checks.
- Added per-model reference-count/strength caveats to `model-currency-2026-06.md` and a new end-to-end guide `docs/05-asset-pipeline.md`.
- Also in this release: the `model-image-luma-uni-1.md` doc (Luma Uni-1 unified image model). Sources: Pat P. Miller, Script Supervising and Film Continuity.
```

- [ ] **Step 5: Update `ROADMAP.md`** - mark `### Phase 4 - Integration & QC ✅ *shipped in v0.9.0*`, check off its bullets, and add a line at the top noting the **art-department roadmap (Phases 0-4) is complete**.

- [ ] **Step 6: Final validate.**

```bash
python plugin/assemble.py
```
Expected: `VALIDATE: OK`.

- [ ] **Step 7: Commit.**

```bash
git add -A
git commit -m "docs: ship v0.9.0 asset integration & QC (README/CHANGELOG/ROADMAP, version) - roadmap complete"
```

---

## Post-plan notes

- **Release (after final whole-branch review + merge):** merge `feat/asset-integration` -> `main`; `git tag -a v0.9.0`; `python plugin/assemble.py --package`; `gh release create v0.9.0 generative-wrangler.plugin` (keep prior releases). The `.plugin` is gitignored. `.superpowers/` is now gitignored - `git add -A` is safe.
- After all tasks: `git log --oneline feat/asset-integration` should show the spec + 9 task commits. This completes the art-department roadmap (Phases 0-4).
