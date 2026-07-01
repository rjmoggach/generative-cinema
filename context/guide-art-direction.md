# Art Direction — World Bible Mechanics

Decision rules for **building and maintaining `art-bible-{show}.md`**, the technical world spec
that translates the Production Design creative vision into a locked, queryable reference that
every character, prop, and set asset inherits from. The creative foundation — how production
designers, propmasters, and set decorators build the physical world — is in
`reference-craft-artdept.md`. The mechanics of generating and composing individual assets are in
`guide-asset-reference.md`. This guide sits between them: it defines the structure of the bible
so that assets stay coherent as a world, not merely as a collection.

The bible inherits its lens, grade, and palette baseline from `project-context-{show}.md`, which
holds production-wide workflow defaults. What the bible adds is world content: the CMF lexicon,
era/genre rules, and the asset index that maps every locked asset by taxonomy path. Construct
asset prompts *from* the bible's fields, not loosely inspired by them.

Each entry uses the library's decision-unit format:
**Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The art bible as a queryable world spec

- **Decision:** keep `art-bible-{show}.md` separate from `project-context-{show}.md`.
- **Use when:** beginning any show or episode; orienting a new agent to the world.
- **Because:** `project-context` holds production-wide workflow defaults — lens, grade, palette
  baseline, output specs, model preferences. The art bible holds *world content*: what the world
  is made of, who inhabits it, what they carry, where they live, and what visual rules every asset
  must obey. Folding world content into project-context turns a concise workflow document into an
  unnavigable sprawl and makes the world's rules invisible to asset skills and the production
  designer. `project-context` tells the pipeline *how to work*; the art bible tells it *what world
  to build*.
- **Prompt translation:** when constructing any asset or shot prompt, pull fields from the bible
  directly — CMF lexicon entry, era/genre rules, palette hex — and paste them verbatim. The bible
  is not a mood board to be paraphrased; it is the source of truth to be quoted.
- **Watch-outs:** don't let world-specific decisions (a character's wardrobe palette, a set's
  entropy level) drift into project-context. Don't let the bible grow prose that can't be
  queried — keep it in defined, labeled fields. If a field does not exist in the bible, it is not
  a world rule.
- **Anchors:** `project-context-{show}.md` (lens, grade, baseline palette);
  `reference-craft-artdept.md` ("The production designer as world author").

---

## 2. Global palette

- **Decision:** name every world color with a label *and* a hex value in the art bible; declare
  the dominant/accent structure explicitly.
- **Use when:** defining any surface, costume, or environment in the world.
- **Because:** named colors without hex drift across agents and sessions. Hex values without names
  cannot be used in prose briefs or spoken direction. The dominant/accent structure tells every
  department where each color lives — in walls and skies, or in hero costumes and practicals — so
  that individual assets stay legible against their environments. The color scheme (complementary,
  analogous, monochromatic) is set in `project-context` and inherited; the bible translates that
  scheme into specific named swatches with hex pins.
- **Prompt translation:** every surface description in an asset prompt takes the form
  `{name}, {hex}, {finish}` — for example, `dusty sienna, #B87050, matte`. Never use the name
  alone; the model does not know your name. Include the hex in the identity block so any agent can
  reconstruct the palette without reading the full bible.
- **Watch-outs:** AI grades drift; restate the palette in every asset's identity block, not just
  in the bible. Mark which colors are dominant (occupy the most frame area) and which are accent
  (used sparingly); mistaking an accent for a dominant overwrites the world's emotional baseline.
  See `guide-color-story.md` for scheme, temperature contrast, and associative color.
- **Anchors:** `guide-color-story.md` (§2 schemes, §3 associative color, §4 temperature
  contrast); `project-context-{show}.md` (inherited color scheme and grade).

The bible's palette block follows this structure:

```
### Palette
| Role     | Name           | Hex     | Finish notes              |
|----------|----------------|---------|---------------------------|
| Dominant | {color-name}   | #{hex}  | matte / satin / gloss     |
| Dominant | {color-name}   | #{hex}  | {finish}                  |
| Accent   | {color-name}   | #{hex}  | {finish}                  |
| Accent   | {color-name}   | #{hex}  | {finish}                  |
| Skin ref | {color-name}   | #{hex}  | subsurface, not a surface |
```

---

## 3. The CMF lexicon

- **Decision:** define a shared material/finish/texture vocabulary in the art bible and reuse it
  verbatim across every asset.
- **Use when:** describing any surface in any asset — character costume, prop material, set wall,
  vehicle panel.
- **Because:** "weathered metal" means something different to every model and every agent.
  "Oxidized steel, brushed horizontal finish, surface rust at rivet heads" does not. The CMF
  lexicon is the material equivalent of the character identity block: a shared vocabulary written
  once and pasted exactly into every asset that uses those materials. Without it, assets that
  should look like they belong to the same world produce different finishes on the same
  material — the world fragments.
- **Prompt translation:** for each material class the world uses, write one CMF entry in the
  bible — a short name, a material call, a finish call, and a texture note. When writing an asset
  prompt, copy the entry verbatim into the material slot; do not rephrase. Example entries:

  ```
  aged-brass:     cast brass, verdigris patina, slight surface relief at seams
  raw-concrete:   poured concrete, unsealed, fine aggregate visible, hairline cracks at joints
  worn-linen:     natural linen, preshrunk, pulled threads at collar and cuffs
  ```

- **Watch-outs:** do not invent new CMF terms per asset — if a new material appears, add it to
  the bible's lexicon first, then use it. Expanding the lexicon is a world-level decision. Resist
  adjectives like "beautiful" or "elegant" — they are not CMF. Every term must describe a
  physical property the model can render: material, finish, texture. The skin-ref entry in the
  palette (§2) is not a CMF entry; it describes subsurface light response, not a surface finish.
- **Anchors:** `reference-craft-artdept.md` ("Color, material, and finish as world language");
  `guide-asset-reference.md` §2 (identity block pinned to material names).

---

## 4. Era, genre, and world rules

- **Decision:** enumerate the world's hard constraints — period, genre, technology level, entropy
  level — as a list of checkable rules in the art bible.
- **Use when:** designing or generating any asset; reviewing a generated image for world
  coherence.
- **Because:** individual assets that look good in isolation can collectively destroy the world's
  logic if they carry contradictory period signals or genre registers. A single anachronistic
  texture or wrong-technology-level prop breaks the audience's trust in the world faster than any
  technical flaw. The rules block answers the question: what can and cannot exist in this world?
  Every asset must pass it before it is locked.
- **Prompt translation:** prepend the era/genre block to every first-generation asset prompt:
  "World: {era}, {genre register}, {technology level}, {entropy level}." Keep it to one or two
  lines — enough to orient the model without displacing the identity block. Example:
  "World: 1930s rural American South, social realist, pre-electrification, high entropy —
  worn surfaces, no chrome, no plastics."
- **Watch-outs:** genre conventions are defaults, not rules — if the world departs from genre
  convention, the bible must say so explicitly, or every agent will default to genre. Entropy
  level (pristine / lived-in / decayed / ruined) is the most overlooked rule: state it globally
  and override per-asset only with explicit justification. Technology level sets the ceiling on
  what materials, finishes, and forms can appear — a prop that exists in the world but not in its
  era is an error, not a choice, unless the bible names it.
- **Anchors:** `reference-craft-artdept.md` ("Era and genre legibility");
  `reference-film-movements.md` (period visual register).

---

## 5. The global style reference

- **Decision:** generate and lock one global style-reference image before creating any other
  asset; derive it via `image-edit` from mood-board inputs.
- **Use when:** beginning a show; onboarding a new agent to the world's visual register.
- **Because:** a single locked image fixes the world's visual register — light quality, surface
  feel, color temperature, tonal contrast — in a form that is unambiguous to the model and to any
  agent. No amount of prose description substitutes for a reference image as an alignment device.
  The global style-ref is not an asset (it depicts no specific character, prop, or set); it is
  the visual grammar of the world itself.
- **Prompt translation:** use `image-edit` with mood-board references as inputs, guided by the
  palette, CMF, and era/genre rules already locked in the bible. Generate until one image captures
  the world's feel, then lock it. Store at `assets/style/style-{show}-global.png`. Attach it as
  a background reference to every first asset generation; use it to calibrate the visual register
  before fanning out to characters, props, and sets.
- **Watch-outs:** the style-ref is not the palette (it cannot stand in for hex values), not the
  CMF lexicon (it cannot stand in for material call-outs), and not the era/genre rules (it cannot
  stand in for a list of world constraints). It anchors *mood and overall visual language* only —
  do not use it as a composition reference. The default lens and grade it implies must be stated
  explicitly in `project-context-{show}.md` and cross-referenced from the bible; don't let them
  live only in the image.
- **Anchors:** `guide-asset-reference.md` §1 (anchor-then-fan-out); `project-context-{show}.md`
  (lens, grade, and palette baseline the style-ref inherits).

---

## 6. The asset index

- **Decision:** maintain a flat asset index table in the art bible, mapping every locked asset to
  its spec file and anchor image path.
- **Use when:** beginning any generation session; constructing multi-reference shots; auditing
  world completeness.
- **Because:** without a map, an agent must search the filesystem to find out what is locked and
  where it lives — error-prone, slow, and invisible to other agents. With the index, any agent
  reads one table and knows every locked asset in the world, its taxonomy path, and which image to
  attach as the anchor reference. The bible is the map of the world; the index is the map of the
  map.
- **Prompt translation:** populate the index as assets are locked, not after the fact. Spec-file
  names carry `{show}`; image-file names do not (see `guide-asset-reference.md` §9). The table
  format:

  | Type   | Name     | Spec file                | Anchor image path                             |
  |--------|----------|--------------------------|-----------------------------------------------|
  | `char` | `{name}` | `char-{show}-{name}.md`  | `assets/char/{name}/char-{name}-id-front.png` |
  | `prop` | `{name}` | `prop-{show}-{name}.md`  | `assets/prop/{name}/prop-{name}-hero.png`     |
  | `set`  | `{name}` | `set-{show}-{name}.md`   | `assets/set/{name}/set-{name}-plate.png`      |

- **Watch-outs:** the index is live — update it when an asset is locked, when its anchor image is
  replaced, and when an asset is retired. An out-of-date index is more dangerous than no index:
  it sends agents to paths that no longer exist. Do not list assets that are not yet locked (not
  anchored, not spec-filed); a partial asset in the index implies it is safe to reference, which
  it is not.
- **Anchors:** `guide-asset-reference.md` §9 (taxonomy: `{type}-{show}-{name}.md`,
  `assets/{type}/{name}/`, image files carry no `{show}`).

---

## 7. Top-down inheritance

- **Decision:** always construct asset prompts and shot prompts from the bible's fields; never
  design an asset in isolation.
- **Use when:** generating any asset (character sheet, prop turntable, location pack) or shot.
- **Because:** assets generated independently produce siblings — they may each look plausible, but
  they do not look like they come from the same world. Top-down inheritance is the mechanism that
  makes the world cohere: the bible defines the rules, asset sheets apply them, the feed executes
  from asset references, and shots assemble from locked references. Each level inherits from the
  one above; each level adds only what its level controls. See `guide-asset-reference.md` §8.
- **Prompt translation — the inheritance chain in practice:**
  1. Pull `CMF entry`, `era/genre block`, and `palette hex` from the bible.
  2. Merge with the asset's own identity block (face, silhouette, locked wardrobe, marks).
  3. Attach the global style-ref + the asset's anchor image as references.
  4. Assemble into the shot prompt with the scene block (location, camera, light, action).

  Do not skip levels. Do not paraphrase bible fields into the identity block — copy them.
- **Watch-outs:** if an asset must break a world rule (a character whose wardrobe intentionally
  clashes with the world palette; a prop that is anachronistically pristine), document the
  exception in the bible first, then apply it in the asset sheet. Undocumented exceptions
  propagate silently and cannot be audited. Propagate changes upward: if a world rule changes,
  update the bible before updating any asset sheet.
- **Anchors:** `guide-asset-reference.md` §8 ("Inherit top-down");
  `reference-craft-artdept.md` ("Top-down inheritance").

---

## Quick application

1. Create `art-bible-{show}.md` with palette (named + hex), CMF lexicon, era/genre rules, and an
   empty asset index table.
2. Generate the global style-ref via `image-edit`; lock it at
   `assets/style/style-{show}-global.png`.
3. Confirm lens, grade, and baseline palette in `project-context-{show}.md`; cross-reference
   from the bible.
4. Build the asset index as assets are locked — spec file + anchor image path, never before the
   anchor exists.
5. Construct every asset prompt from the bible's fields (CMF entry + era/genre block + palette
   hex), merged with the asset identity block; attach the style-ref as a background reference.
6. Propagate changes upward: bible first, then asset sheets, then feed.

Companion guides: `project-context-{show}.md` (lens, grade, baseline palette),
`guide-asset-reference.md` §8 (top-down inheritance), `guide-color-story.md` (palette
mechanics), `reference-craft-artdept.md` (Production Design creative foundation).
