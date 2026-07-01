# generative-cinema — ROADMAP

**Status:** Draft 1 · **Created:** 2026-06-30 · **Owner:** Rob (Creative Producer)

This roadmap plans the next major expansion of the plugin: an **art department** —
the below-the-line creative crew that builds the *persistent visual reference
assets* (character sheets, prop turntables, location packs, a world bible) that
generative image/video models need to hold a character, object, and place
consistent across shots.

It is grounded in the plugin's existing principle, already stated in
[`context/guide-ai-generation-strategy.md`](context/guide-ai-generation-strategy.md):

> *Reference images beat text "character bibles." Generate one strong "hero"
> reference still first, then drive subsequent shots from it… the reference pins
> *who*, the prefix pins *the look*.*

Today the plugin can write that principle but has **nowhere to build and store the
references it depends on**. This roadmap fills that gap.

---

## 1. Where we are

The plugin is a Project → Sequence → Shot system with a crew you talk to:

| Layer | Skill | Agent (crew) | Output |
|---|---|---|---|
| Library | `model-docs` | `researcher` | `context/model-*.md` |
| **Project** | `project-context` | `director` | `project-context-{show}.md` (the look) |
| **Sequence** | `sequence-design` | `first-ad` | coverage shot list |
| **Shot** | `shot-prompt` | `cinematographer` | model-optimized prompt |
| Shot (v2v) | `footage-transform` | `cinematographer` | video-to-video prompt |
| QC | — | `script-supervisor` | continuity audit |

The crew is **above-the-line + camera** (director, DP, 1st AD, script supervisor,
researcher). There is no art department, and **no asset layer** between Project and
Shot. The system can describe *who/what/where* in prose but can't build, store, or
re-attach a locked visual reference for them.

### Two gaps to close

1. **No asset/reference layer.** Characters, props, and locations have no persistent,
   named, re-attachable reference asset. Every shot re-derives identity from text.
2. **No image-to-image (i2i) skill.** `footage-transform` is gated to *video*. There
   is no skill for "change this still to X / swap the background around a preserved
   subject" — yet i2i editing is the **engine** the whole asset workflow runs on
   (derive a turnaround view from a hero still, drop a locked character into a new
   plate, progress a wound, recolor a costume). This is a prerequisite, not a nicety.

---

## 2. The plan in one picture

Introduce an **Asset layer** owned by a new **art department**, sitting between
Project and Sequence:

```
Library      model docs + craft guides
   │
Project      project-context-{show}.md         ← the LOOK (DP/Director)
   │
ART BIBLE    art-bible-{show}.md               ← the WORLD (Production Designer)   ◀ NEW
   │           unifies palette · material/CMF · era · indexes every asset below
   │
ASSETS       char-{show}-{name}.md              ← casting · costume · HMU           ◀ NEW
             prop-{show}-{name}.md              ← propmaster                        ◀ NEW
             set-{show}-{name}.md               ← location scout/manager            ◀ NEW
   │           each = a markdown spec + a folder of locked reference images
   │
Sequence     coverage shot list (1st AD)
   │           ↑ now attaches the right asset refs to each shot
Shot         shot-prompt / image-edit / footage-transform
             ↑ identity = reference image · change = prompt
QC           script-supervisor → now also audits asset continuity
```

**Core operating principle (applies to every new role): identity lives in the
reference, change lives in the prompt.** Each art-department role exists to produce a
clean, locked **anchor** — and then a small set of derived views/states — so that
downstream shots carry identity from the image while the prompt only states what
changes.

---

## 3. The new crew (6 agents) and what they build

Each role is **dual**: a creative identity (real-world craft judgment) *and* a
technical execution method (how to build the asset with 2026 tools). The roadmap
treats both as first-class — an agent that only knows the tool produces sterile
assets; one that only knows the craft can't realize them.

### 3.1 Production Designer — *art-department lead*

| | |
|---|---|
| **Creative context** | Owns the coherent visual world. In prep a PD produces the **look book**, **mood boards**, **concept art**, and the color/material/texture direction that unifies every other art-dept role. They are the parent the others inherit from. |
| **Technical context** | Maintains `art-bible-{show}.md`: a *queryable* world spec — global palette (named + hex), material/CMF lexicon, era/genre, default lens & grade inherited from `project-context`, a global **style-reference image**, and an **index of every character/prop/location asset** with its anchor image. Prompts for sub-assets are *constructed from* this, not loosely inspired by it. |
| **Builds** | `art-bible-{show}.md` + concept-art plates + palette/CMF board. |
| **Agent** | `production-designer` — the art-dept counterpart to `director`. The Director sets story intent; the PD sets the world. Delegates to the five sub-roles and keeps them coherent. |

### 3.2 Casting Director — *the face / identity*

| | |
|---|---|
| **Creative context** | Writes the **character breakdown** (age, look, presence) and locks one identity to one character for the whole show. |
| **Technical context** | Produces the **hero identity reference**: a front-facing, evenly-lit, neutral-expression, high-res portrait — the single most load-bearing asset in the pipeline — plus a multi-angle identity bundle. Records the **locked descriptor block** (50–80 words, reused verbatim) and the **reference-vs-LoRA** decision (see §5). |
| **Builds** | The identity section of `char-{show}-{name}.md` + `assets/char/{name}/identity-*.png`. |
| **Agent** | `casting-director`. |

### 3.3 Costume Designer (Wardrobe) — *turnaround + wardrobe continuity*

| | |
|---|---|
| **Creative context** | Builds the **costume plot / wardrobe bible**: each costume change by script day, silhouette, color, distressing/state, with continuity notes. |
| **Technical context** | Produces the **character turnaround / model sheet** (front · side · back · ¾×2, aligned on eye/shoulder/waist/knee/foot lines) — both a deliverable *and* the multi-angle reference bundle that boosts downstream identity. Locks wardrobe by exact garment name + silhouette + **hex color**, restated verbatim; tracks **costume states** (clean / wet / damaged). |
| **Builds** | Turnaround + wardrobe-state section of `char-{show}-{name}.md`. |
| **Agent** | `costume-designer`. Also owns the general **character-design / model-sheet** craft. |

### 3.4 Makeup & Hair (HMU) — *look states + continuity*

| | |
|---|---|
| **Creative context** | Continuity discipline (a look must reproduce identically regardless of shoot order), **aging**, **SFX/prosthetics**, hair continuity, wound/scar/blood progression. |
| **Technical context** | Maintains a small library of **HMU "state" references** per character (clean / aged / wounded / wet), each independently lockable — the AI equivalent of *molds and paint formulas on file*. Pins each injury by **position + side + size + hex**, restated every shot; progresses injuries by **editing from the previous state**, not regenerating. |
| **Builds** | HMU-state section of `char-{show}-{name}.md` + `assets/char/{name}/hmu-*.png`. |
| **Agent** | `makeup-hair`. |

> **Why casting + costume + HMU share one asset file.** A "character" is one
> reference in practice. `char-{show}-{name}.md` is a single living file with
> three sections (identity / wardrobe / HMU). The three agents are *facets* that
> collaborate on facets of one asset — mirroring how a real production builds a
> character.

### 3.5 Propmaster — *prop turntables*

| | |
|---|---|
| **Creative context** | Hero vs. dressing vs. action props; sourcing; **multiples** (stunt/destruction/continuity duplicates that must match); per-prop state variants (pristine/aged/bloodied). |
| **Technical context** | Builds a **prop turntable / multi-view object sheet**: front · back · L/R side · top · ¾ hero · detail/macro · optional 8–12-step 360. Anchor-then-fan-out from one clean frame-filling hero view. For props that must survive many angles/destruction, use **3D-assist** (Blender MCP) to lock geometry and render orthographic/depth views (see §6). |
| **Builds** | `prop-{show}-{name}.md` + `/assets/prop-{name}/*.png`. |
| **Agent** | `propmaster`. |

### 3.6 Location Scout & Manager — *location packs*

| | |
|---|---|
| **Creative context** | The **scouting packet**: recce photography well beyond the on-screen frame, sun-path/lighting notes, logistics. Environment carries a disproportionate amount of the storytelling. |
| **Technical context** | Builds a **location pack / environment reference set**: a locked **master establishing plate**, multi-angle coverage (incl. reverse angle), and **time-of-day / weather variants derived from the same locked geometry** (change one variable at a time). For reverse-angle coherence and **set extension**, use 3D-assist (block the space, render plates + depth). |
| **Builds** | `location-{show}-{name}.md` + `/assets/location-{name}/*.png`. |
| **Agent** | `location-scout`. |

---

## 4. The new workflow (5 skills)

| Skill | Layer | Does | Calls |
|---|---|---|---|
| **`image-edit`** ◀ *foundation* | Shot (i2i) | "Change this still to X / swap the background / recolor the costume / add a wound" — the i2i sibling of `footage-transform`. Six-layer discipline, scoped to single-image edits and partial-denoise. | model docs |
| **`art-direction`** | Art bible | PD interview → `art-bible-{show}.md` (palette, CMF, era, global style ref, asset index). Extends `project-context`. | `project-context` output |
| **`character-sheet`** | Asset | Build/refresh `char-{show}-{name}.md`: hero identity → turnaround → expressions → wardrobe states → HMU states. | `image-edit`, art-bible |
| **`prop-turntable`** | Asset | Build/refresh `prop-{show}-{name}.md`: hero view → orthographic ring → details → optional 360 (3D-assist optional). | `image-edit`, Blender |
| **`location-pack`** | Asset | Build/refresh `location-{show}-{name}.md`: master plate → coverage → time/weather variants (3D-assist optional). | `image-edit`, Blender |

All asset skills share one engine — **`image-edit`** — to derive views and states
from a locked anchor, and all inherit the world from `art-bible`. This is why
`image-edit` is **Phase 0**: nothing else works cleanly without it.

### Shared craft guides to add to `context/`

These are the durable, model-agnostic craft (same heuristic format as the existing
guides) the skills and agents read:

- `guide-asset-reference.md` — the spine: anchor-then-fan-out, multi-reference
  composition (locked character + location + costume), effective reference counts,
  identity-block-vs-scene-block.
- `guide-image-editing.md` — i2i/inpaint/partial-denoise craft (shared by `image-edit`
  *and* `footage-transform`).
- `guide-character-consistency.md` — hero ref, descriptor block, reference-vs-LoRA gate,
  HMU/wardrobe state libraries, drift failure modes.
- `guide-turnaround-sheets.md` — model-sheet views & alignment conventions (front-anchor,
  eye/shoulder/waist/knee/foot lines, expression/pose/palette companion sheets).
- `guide-prop-turntable.md` — object multi-view conventions, framing-the-asset rules.
- `guide-location-pack.md` — master-plate + coverage + variant conventions, continuity table.
- `guide-art-direction.md` — world bible, palette/CMF, top-down inheritance.
- `guide-3d-assist.md` — Blender-MCP geometry-lock + depth-pass conditioning + OrthoRender.

---

## 5. Best practices the build must encode

Distilled from current (mid-2026) practitioner research. These are the rules the
agents/skills should enforce, not just mention.

1. **Anchor, then fan out.** Generate one clean, frame-filling, evenly-lit anchor on
   a neutral background *first*; derive every other view/state/variant *from it* via
   reference conditioning. Never generate each view independently.
2. **Two-block prompts everywhere.** A constant **identity block** (50–80 words: face,
   hair, body, locked wardrobe, accessories, HMU state, marks) reused *verbatim*, plus
   a variable **scene block** (location, camera, light, action). Vague language is the
   #1 drift source — pin hex colors, garment names, silhouette, wound position+side+size.
3. **Reference for speed, LoRA for scale.** Decision gate:
   - ≤ ~1 scene / quick turnaround → **reference image only** (~65–75% consistency).
   - Recurring hero across many shots/episodes → **reference + trained LoRA + fixed
     descriptor block** (~85–92%).
   - Background / one-off → reference only.
4. **Effective reference counts (verify against `model-currency`).** ~**4–6** reference
   images is the consistency sweet spot; below 3 the model lacks angle/light info; above
   ~8 is diminishing returns. Reference strength ~0.7 (0.6–0.8). Nano Banana Pro holds
   ~14 objects / ~5 characters; FLUX.2 and Seedream take up to ~10 refs. *These numbers
   are version-sensitive — the `researcher`/`model-docs` loop must keep them current.*
5. **Edit, don't regenerate, for continuity progressions.** Use partial-denoising /
   targeted edits (the `image-edit` skill) to change one attribute (shirt color, add a
   wound, age a face) while preserving the facial fingerprint.
6. **Hold one dominant light-key direction per scene** — the cheapest, most-overlooked
   identity lever; flipping the key flips identity.
7. **Don't depend on micro-detail** (freckles, logos, insignia) for identity — models
   drop these first; keep simple or composite them in.
8. **3D-assist where 2D drifts** (see §6).
9. **Inherit top-down.** Art bible (global style/palette/grade) → constrains → asset
   sheets → feed → shots. The bible is a hard dependency, not a loose mood board.

---

## 6. 3D-assist (Blender MCP)

A Blender MCP is available in this environment. For any prop or location that must
survive many camera angles, destruction, or **set extension**, 2D-only references
drift on un-referenced faces (back/top/underside, reverse angles, seams). The robust
fix:

1. Model or AI-generate the object/environment once in 3D and **lock it**.
2. Render **orthographic / multi-angle views** (e.g. via an OrthoRender-style pass) to
   build a geometry-true turnaround sheet.
3. Render a **depth pass** from any needed shot angle and use it as ControlNet-style
   conditioning so the image model "skins" locked geometry — guaranteeing geometric
   consistency the image model alone can't hold.

This is a sound composite of documented capabilities; treat it as **recommended, not
proven-at-scale**, and pilot it on one hero prop before standardizing (see Phase 2).

---

## 7. Phased delivery

Sequenced by dependency and ROI. Each phase is shippable on its own.

### Phase 0 — Foundation: close the i2i gap ✅ *shipped in v0.5.1*
- ✅ Added the **`image-edit`** skill (i2i sibling of `footage-transform`): single-image
  edits, swaps, recolors, inpaint, partial-denoise, multi-reference composition. Reuses
  the same discipline and project-lock; missing trigger phrasings folded into its
  description.
- ✅ Added `guide-image-editing.md` and `guide-asset-reference.md` to `context/`.
- ✅ Wired into `skills/build.py` + `plugin/assemble.py`; README/CHANGELOG updated; six skills.
- `footage-transform` stays v2v-clean; the i2i triggers now live in `image-edit`.
- **Why first:** every asset skill needs an i2i engine to derive views/states.

### Phase 1 - Character pipeline ✅ *shipped in v0.6.0*
- ✅ Agents: `casting-director`, `costume-designer`, `makeup-hair`.
- ✅ Skill: `character-sheet` → `char-{show}-{name}.md` + image set.
- ✅ Guides: `guide-character-consistency.md`, `guide-turnaround-sheets.md`.
- ✅ Asset naming convention: `assets/char/{name}/` (typed taxonomy in `guide-asset-reference.md` §9).

### Phase 2 — Props & Locations
- Agents: `propmaster`, `location-scout`.
- Skills: `prop-turntable`, `location-pack`.
- Guides: `guide-prop-turntable.md`, `guide-location-pack.md`, `guide-3d-assist.md`.
- Pilot the Blender depth-pass workflow on one hero prop; document the result.

### Phase 3 — Production Designer / world bible
- Agent: `production-designer`. Skill: `art-direction` → `art-bible-{show}.md`.
- Guide: `guide-art-direction.md`.
- Retrofit Phase 1–2 assets to inherit from the bible; add palette/CMF.
- Update the `director` → `production-designer` handoff in the README crew flow.

### Phase 4 — Integration & QC
- Teach `sequence-design` / `first-ad` to **attach the right asset references** to each
  shot line, and `shot-prompt` / `cinematographer` to consume them (identity =
  reference, change = prompt).
- Extend `script-supervisor` to audit **asset continuity** (wrong/missing reference,
  costume/HMU/prop state drift, location geometry mismatch).
- Update `model-currency` notes with per-model reference-count/strength caveats.
- Docs: new `docs/05-asset-pipeline.md`; refresh README crew/skill tables.

---

## 8. Implementation notes (wiring)

How the repo is built (so each addition lands correctly):

- **Source of truth** is the repo root: `context/` (library) and `skills/{name}/SKILL.md`
  (+ bundled `references/`). `plugin/agents/*.md` and `plugin/README.md` are authored by
  hand. `python plugin/assemble.py` regenerates `plugin/context/` + `plugin/skills/` and
  repoints links to `${CLAUDE_PLUGIN_ROOT}/context/...`.
- **New skill** → create `skills/{name}/SKILL.md`; add `{name}` to the `SKILLS` list in
  **both** `plugin/assemble.py` and `skills/build.py` (with its `MANIFEST` of bundled
  references); add any new `context/guide-*.md`; rebuild.
- **New agent** → create `plugin/agents/{name}.md` with strict-YAML frontmatter and the
  required keys (`name`, `description`, `model`, `color`, `tools`). `assemble.py`
  validates this; non-YAML frontmatter or missing keys fail the build.
- **New craft guide** → drop `context/guide-*.md`; it's copied verbatim into the plugin.
  Wire it into the relevant skill's `MANIFEST` so it's bundled.
- **i2i trigger phrases** (from the flagged coverage gap) — make sure the `image-edit`
  skill description includes verbatim user-style lines so the router locks on, e.g.:
  *"change this image to X", "swap the crowd/background/wardrobe around a preserved
  subject", "give me a prompt to edit this photo", "make these fans Moroccan instead of
  Dutch", "recolor this costume", "rewrite this so it's Y instead of Z."*
- **Rebuild & release:** `python plugin/assemble.py --package`; attach the `.plugin` to a
  GitHub Release; bump `plugin/.claude-plugin/plugin.json` version; log in `CHANGELOG.md`.

### Stub files included with this roadmap
Skeleton drafts are staged in [`roadmap/`](roadmap/) (agents + skill `SKILL.md`s) so you
can start fleshing them out immediately. They are **not yet wired into the build** — move
them into `plugin/agents/` and `skills/` and update the `SKILLS`/`MANIFEST` lists when each
is ready. See [`roadmap/README.md`](roadmap/README.md).

---

## 9. Open questions

1. **Art bible vs. project-context:** keep `art-bible-{show}.md` as a separate
   PD-owned file (recommended — clean separation of *look* vs. *world*), or fold an
   art-direction section into `project-context`? Decide before Phase 3.
2. **LoRA training:** the consistency ceiling for recurring heroes needs LoRA, which is
   out of the current text-prompt scope. Do we (a) just *advise* it and record the
   trigger word in the character sheet, or (b) add a `lora-train` skill/runbook later?
3. **Asset storage:** ✅ Resolved — `assets/{type}/{name}/` convention (type-first hierarchy,
   see `guide-asset-reference.md` §9); image binaries live in the user's working folder only, never the plugin repo.
4. **3D-assist scope:** how far to lean on Blender — every hero prop/location, or only
   the hardest cases? Pilot result (Phase 2) should answer this.

---

*Companion reading already in the repo:*
[`context/guide-ai-generation-strategy.md`](context/guide-ai-generation-strategy.md) ·
[`context/guide-continuity-rules.md`](context/guide-continuity-rules.md) ·
[`README.md`](README.md).
