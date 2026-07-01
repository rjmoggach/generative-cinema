# Character Pipeline (Phase 1) — Design

**Date:** 2026-06-30 · **Status:** Approved · **Target release:** v0.6.0
**Owner:** Rob (Creative Producer) · **Roadmap:** [`ROADMAP.md`](../../../ROADMAP.md) Phase 1

---

## 1. Goal

Close the roadmap's **asset-layer gap** for characters: give the plugin a way to
*build and store* a persistent, re-attachable **character reference** (face,
wardrobe, makeup/hair) so downstream shots carry identity from an image while the
prompt states only what changes. Ship the first below-the-line **art department**
crew (casting, costume, makeup/hair) and the skill that orchestrates them.

Grounding principle (already in `guide-ai-generation-strategy.md`): *reference
images beat text "character bibles"; the reference pins **who**, the prefix pins
**the look**.* Every new role exists to produce a clean, locked **anchor** and a
small set of derived views/states.

## 2. Scope (full Phase 1, one shippable spec)

**In:** 1 skill, 3 agents, 3 new library files, 1 new section in an existing
guide, build wiring, docs, version bump to 0.6.0.
**Out (later phases):** props/locations/PD (Phase 2–3), LoRA training, 3D-assist,
sequence/QC integration of assets (Phase 4).

## 3. Decisions locked in brainstorming

1. **Full Phase 1 in one spec** → v0.6.0.
2. **Asset binaries live in the user's working folder only** — the skill writes the
   markdown spec + `assets/…` images into the user's project dir; the plugin repo
   stays text-only (mirrors how `project-context-*.md` already works). Nothing
   binary is committed to the plugin.
3. **LoRA = advise-only + record the trigger word** — the reference-vs-LoRA gate
   advises *when* a hero warrants a LoRA and records its trigger word in the
   character file; the plugin does not train (matches the text-prompt scope).
4. **Every role is dual** — creative craft (the *art*) **and** technical execution
   (the 2026 tool method). Both are first-class; an agent that only knows the tool
   makes sterile assets.

## 4. Two kinds of craft file (creative vs technical)

Mirrors the library's existing split between knowledge catalogs (`reference-*`) and
decision-rules (`guide-*`).

### 4.1 NEW `context/reference-craft-character.md` — the creative craft

The "how to cast great characters / what wardrobe *means* cinematically" depth that
technical skills usually omit. Three sections, each = principles + an anchor table
of masters (sibling of `reference-visual-*`):

- **Casting** — typage & presence; the face that tells a story before a line;
  ensemble chemistry; casting against type; what a casting director actually reads
  for. Anchors: great casting directors (e.g. Marion Dougherty, Juliet Taylor,
  Jenkins/Hirshenson).
- **Costume** — wardrobe as character: silhouette, colour-as-character, status/period
  legibility, the *costume arc*, distressing/aging as narrative, the difference
  between fashion and costume. Anchors: Edith Head, Colleen Atwood, Sandy Powell,
  Ruth Carter, Milena Canonero.
- **Makeup & Hair** — the "invisible" naturalistic look; aging; wounds/SFX as
  storytelling; hair as silhouette/era; continuity as discipline. Anchors: Rick
  Baker, Ve Neill, and peers.

Establishes a **`reference-craft-*` pattern** Phase 2 extends ("the art of being a
propmaster", set decoration, the PD's world-building).

### 4.2 NEW technical guides (heuristic format: Decision / Use when / Because / Prompt translation / Watch-outs / Anchors)

- `context/guide-character-consistency.md` — the *character-specific* technical craft
  `guide-asset-reference.md` (the general spine) does not cover: the hero identity
  portrait spec; how to write the **50–80-word descriptor block** reused verbatim;
  face/identity **drift failure modes + fixes**; the **wardrobe-state** and
  **HMU-state** libraries; the reference-vs-LoRA gate *for faces* incl. recording the
  trigger word. Cross-references `guide-asset-reference` rather than duplicating it.
- `context/guide-turnaround-sheets.md` — model-sheet conventions: the view set
  (front-anchor · side · back · ¾×2), alignment lines (eye/shoulder/waist/knee/foot),
  neutral pose/light/background, deriving each view from the anchor via `image-edit`,
  and companion sheets (expressions / poses / palette).

### 4.3 Extend `context/guide-asset-reference.md` — naming & storage

Add one **"Naming & storage"** section defining the canonical asset taxonomy (below),
so every current and future asset skill inherits it.

## 5. Asset naming taxonomy (industry-standard, extensible)

Typed, coded, versioned, self-describing to a human or a fresh agent browsing
`assets/`. Supersedes the roadmap's longhand (`character-{show}-{name}.md`,
`/assets/character-{name}/`); ROADMAP naming refs updated to match.

**Type codes (reserved now; `char` built in Phase 1):**
`char` · `prop` · `set` · `veh` · `cam` · `light` · `style` · `fx`

```
Spec file     {type}-{show}-{name}.md            char-sbw-eli.md
Asset folder  assets/{type}/{name}/              assets/char/eli/   (type-first:
                                                 assets/char/ lists every character)
Image files   {type}-{name}-{facet}-{view}[-vNN].png
  identity    char-eli-id-front.png   char-eli-id-3q-l.png
  turnaround  char-eli-turn-front.png  -side-l / -side-r / -back / -3q-l / -3q-r
  wardrobe    char-eli-fit-day1.png    char-eli-fit-day2-wet.png
  hmu         char-eli-hmu-clean.png   char-eli-hmu-wound-01.png
```

Facet codes: `id` · `turn` · `fit` · `hmu`. Views: `front/back/side-l/side-r/3q-l/3q-r`.
Everything lowercase kebab; `-vNN` version suffix optional.

## 6. New skill `skills/character-sheet/`

- `SKILL.md` — fleshes out the roadmap stub into the three-facet workflow:
  1. **Identity (casting):** hero portrait + multi-angle bundle → descriptor block +
     reference-vs-LoRA gate.
  2. **Turnaround + wardrobe (costume):** front-anchor turnaround aligned on the body
     lines; lock garments by name + silhouette + hex; wardrobe states.
  3. **HMU states (makeup-hair):** small state library (clean/aged/wounded/wet), each
     independently lockable; pin injuries by position+side+size+hex; progress by
     editing the previous state.
  Uses **`image-edit` as the derive engine** (anchor-then-fan-out; never generate
  views independently). Reference counts ~4–6, strength ~0.7, verify vs currency.
  **Output → user's working folder** per §5.
- `references/` (bundled via `build.py` MANIFEST): `reference-craft-character`,
  `guide-character-consistency`, `guide-turnaround-sheets`, `guide-asset-reference`,
  `guide-image-editing`, `model-currency-2026-06`, and the editing/image model docs
  (`model-editing-flux-kontext`, `model-image-gemini-flash`, `model-image-seedream-4`,
  `model-image-flux-pro`).
- `references/character-template.md` — hand-authored output template (the character
  file skeleton: identity/wardrobe/HMU sections + descriptor block + `assets/char/…`
  paths + LoRA-trigger field). Wired as an `assemble.py` HELPER (mirrors
  `project-context`'s `output-template.md`).

## 7. Three new agents `plugin/agents/`

Thin personas, strict-YAML frontmatter (`name/description/model/color/tools`),
`model: inherit`, `tools: [Read, Grep, Glob]`. Each reads **both** the creative
reference and the technical guide, so it speaks with real department voice:

- `casting-director` — identity/hero ref; reads `reference-craft-character` (Casting)
  + `guide-character-consistency`.
- `costume-designer` — turnaround + wardrobe; also owns model-sheet craft; reads
  `reference-craft-character` (Costume) + `guide-turnaround-sheets`.
- `makeup-hair` — HMU state library; reads `reference-craft-character` (Makeup & Hair)
  + `guide-character-consistency`.

They are facets of **one** asset file (`char-{show}-{name}.md`, three sections),
mirroring how a real production builds a character.

## 8. Build wiring

- `skills/build.py` — add the `character-sheet` MANIFEST entry (the §6 bundle).
- `plugin/assemble.py` — add `character-sheet` to `SKILLS`; add `character-template.md`
  to `HELPERS`.
- Run `python plugin/assemble.py` → must print `VALIDATE: OK` (no dead references,
  valid agent YAML). Run `python skills/build.py` → syncs + zips cleanly.

## 9. Docs + release

- `README.md` + `plugin/README.md`: add the skill row, 3 agent rows, guides/reference
  mention; bump banner to 0.6.0.
- `CHANGELOG.md`: v0.6.0 entry. `ROADMAP.md`: mark Phase 1 ✅; update naming refs to §5.
- `plugin/.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json`: version 0.6.0.
- Remove the promoted stubs from `roadmap/` (the `character-sheet` skill + the 3
  agents), per the roadmap's own "promote a stub" instructions.
- Record research sources in `knowledge-base/Miscellaneous-Sources.md` (§11).
- `.plugin` rebuild + GitHub Release is a maintainer step (via the `version-bump`
  skill) — flagged, not performed here.

## 10. Verification

- `python plugin/assemble.py` prints `VALIDATE: OK`.
- `python skills/build.py` syncs + zips with no errors.
- Every `](references/…)` in the new `SKILL.md` resolves to a bundled file.
- All three agent frontmatters parse as strict YAML with the required keys.
- Spot-read the new files for the heuristic format and no `[PLACEHOLDER]`s.

## 11. Research — creative-context sources (added to `knowledge-base/Miscellaneous-Sources.md`)

Real, authoritative craft sources grounding `reference-craft-character.md`:

- **Casting** — Janet Hirshenson & Jane Jenkins, *A Star Is Found: Our Adventures
  Casting Some of Hollywood's Biggest Movies* — first-hand account of what casting
  directors read for (presence, chemistry, star-making).
  <https://www.goodreads.com/book/show/398485.A_Star_Is_Found>
- **Costume** — Deborah Nadoolman Landis, *FilmCraft: Costume Design* — sixteen
  leading designers on envisioning character through clothes; and *Dressed: A Century
  of Hollywood Costume Design*.
  <https://books.google.com/books/about/FilmCraft_Costume_Design.html?id=3yCkCgAAQBAJ>
  · <https://www.deborahlandis.com/publications>
- **Makeup & Hair** — Penny Delamar, *The Complete Make-Up Artist: Working in Film,
  Television, and Theatre*; and Richard Corson, *Stage Makeup* (the standard craft
  reference).
  <https://www.amazon.com/Complete-Make-Up-Artist-Working-Television/dp/0810119692>

These join the existing anchors (Block, Mercado, Katz, …) in the sources file.

## 12. Approach considered & rejected

- **Single `character-designer` agent** instead of three — less surface, but breaks
  the film-crew metaphor the whole product runs on, and the roadmap explicitly wants
  casting/costume/HMU as distinct real-world roles. Rejected.
