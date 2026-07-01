# Asset Pipeline: From Look to Locked Shot

This doc traces the full path a project takes from "what does this look like" to a
QC-checked, model-ready prompt that carries a locked character, prop, or location
without drifting. `docs/02-workflow-basics.md` covers per-model generation workflows
and `docs/04-six-layer-framework.md` covers prompt structure; this doc covers the
handoff between the skills that sit above both - how identity gets built once, then
carried through every downstream shot instead of being re-described (and re-drifted)
each time.

---

## The flow

```
project-context  ->  art-bible  ->  assets                 ->  sequence-design  ->  shot-prompt  ->  script-supervisor
   (the look)          (the world)   (character-sheet /          (attach refs:)      (consume refs:)   (QC continuity)
                                      prop-turntable /
                                      location-pack)
```

Six stages, six skills/agents, each consuming the output of the one before it. Nothing
here is optional in principle - a stage can be skipped, but the next stage then falls
back to prose description instead of a locked reference, and consistency degrades.
The rest of this doc walks the stages in order, then works one shot through all of
them end to end.

## Stage 1: `project-context` - the look

Run first, before any asset or shot exists. A guided interview produces
`project-context-{show-code}.md`: the Standard Prompt Prefix, color palette (hex),
lighting style, lens signature, atmosphere, and a forbidden-terms list. Every later
stage inherits from this file - it is the project's visual DNA.

## Stage 2: `art-bible` - the world

Run after `project-context`, before individual assets. Synthesizes
`art-bible-{show}.md`: the global palette (named + hex), a CMF (camera/material/finish)
lexicon, era and genre rules, a locked global style-reference image, and an index of
every asset in the show. Character, prop, and location assets construct their prompts
*from* the bible's fields rather than loosely matching them - see
`context/guide-asset-reference.md` §8 ("Inherit top-down").

## Stage 3: assets - `character-sheet` / `prop-turntable` / `location-pack`

Each asset skill builds one persistent reference: a spec file plus a folder of locked
images.

- `character-sheet` -> `char-{show}-{name}.md` + `assets/char/{name}/`
- `prop-turntable` -> `prop-{show}-{name}.md` + `assets/prop/{name}/`
- `location-pack` -> `set-{show}-{name}.md` + `assets/set/{name}/`

Every spec follows the same shape: an **anchor** image built first (front portrait /
hero view / master plate, neutral background, evenly lit), a fan-out of views/states
derived from it, and an **identity block** - 40-80 words, hex-pinned, written to be
pasted **verbatim** into every downstream prompt (see `guide-asset-reference.md` §§1-2).
Note the naming split: the **spec file** keeps `{show}` (`char-sbw-eli.md`); **image
files** under `assets/` do not (`char-eli-id-front.png`) - the show is implied by the
project folder. Full taxonomy: `guide-asset-reference.md` §9.

## Stage 4: attach - `refs:` in `sequence-design`

`sequence-design` plans a scene at the shot-list level (coverage, staging, screen
direction, intensity arc) and, per `guide-asset-reference.md` §10, appends a `refs:`
line to every shot that needs a locked asset in frame:

```
S2-03  Coverage CU - 85mm - serves the turn - refs: char-eli, prop-revolver, set-livingroom
```

Each id is an asset spec-file stem - `char-{name}` / `prop-{name}` / `set-{name}` -
with **no** `{show}` and **no** extension. This line is the contract: it tells
`shot-prompt` which anchor images and identity blocks to pull in for that shot. A shot
that needs an asset but has no `refs:` will re-derive identity from text and drift.

## Stage 5: consume - `shot-prompt`

`shot-prompt` renders each shot line into a final, model-optimized prompt. When a shot
line carries `refs:`, it resolves every id before finalizing that shot (per
`guide-asset-reference.md` §10 and the skill's own Step 5):

1. Locate the spec each id names (`char-{show}-{name}.md`, etc.) and read its identity block.
2. Restate that identity block **verbatim** as the prompt's identity segment - never paraphrased, never re-derived from the shot description.
3. Attach the asset's anchor image as a model reference (`char-{name}-id-front.png`, `prop-{name}-hero.png`, `set-{name}-plate.png`).
4. Split the prompt in two: identity = the attached reference plus its verbatim block; change = the shot's action, camera, lighting, and scene specifics only (`guide-asset-reference.md` §2).

A shot with no `refs:` proceeds as before, building identity from the project-context
file and the shot's prose alone.

## Stage 6: QC - `script-supervisor`

Before (or after) generation, `script-supervisor` audits the sequence for continuity:
the 180-degree line, eyelines, the 30-degree rule, motion vectors, and look
consistency against the show bible. It also audits the asset contract specifically -
per its own brief, checking every `refs:` id against its spec file and flagging:

- a shot that needs a locked asset but has no `refs:` line,
- a `refs:` id with no matching spec (a broken reference),
- state drift (wardrobe/HMU/prop-condition changes across a cut with no motivating beat),
- geometry mismatch (a coverage angle that contradicts the master plate's geometry or light-key).

`script-supervisor` is read-only - it surfaces issues for `shot-prompt` to correct, it
does not rewrite prompts itself.

---

## Worked example: one shot, end to end

Show code `sbw`. A character (`eli`), a prop (`revolver`), and a location
(`livingroom`) are already built.

**Assets on disk:**

```
project-context-sbw.md
art-bible-sbw.md
char-sbw-eli.md            assets/char/eli/char-eli-id-front.png
prop-sbw-revolver.md       assets/prop/revolver/prop-revolver-hero.png
set-sbw-livingroom.md      assets/set/livingroom/set-livingroom-plate.png
```

**`char-sbw-eli.md` identity block:**

> Mid-30s man, lean build, sharp jaw, close-cropped dark brown hair, pale olive skin
> (`#D4B896`), faint scar above left brow. Default: slate-grey wool peacoat (`#4A4E57`),
> charcoal trousers, white shirt open at collar.

**`prop-sbw-revolver.md` descriptor block:**

> Snub-nose revolver, blued-steel finish (`#2B2B2E`), worn walnut grip (`#6B4A32`),
> brass front sight, faint holster wear along the barrel. Approximately 20 cm overall.

**`set-sbw-livingroom.md` identity block:**

> 1970s New Jersey living-room interior, worn oak floor (`#7B5C3A`), cream plaster walls
> (`#E8DFC8`), large picture window on the north wall framing falling snow, warm tabletop
> practicals lower right. Long axis window-to-hearth; soft window key wraps camera-left,
> negative fill camera-right.

### Before - the shot line (`sequence-design` output)

```
S2-03  Coverage CU - 85mm - serves the turn - refs: char-eli, prop-revolver, set-livingroom
```

Nothing about Eli's face, the revolver's finish, or the room's light logic is written
here - the `refs:` line points at it instead.

### After - the rendered prompt (`shot-prompt` output)

`shot-prompt` resolves all three ids, restates each identity block verbatim, attaches
each anchor image as a model reference, and writes only the shot-specific change:

```
References attached: assets/char/eli/char-eli-id-front.png,
assets/prop/revolver/prop-revolver-hero.png,
assets/set/livingroom/set-livingroom-plate.png

Mid-30s man, lean build, sharp jaw, close-cropped dark brown hair, pale olive skin
(#D4B896), faint scar above left brow. Default: slate-grey wool peacoat (#4A4E57),
charcoal trousers, white shirt open at collar. Holding a snub-nose revolver, blued-steel
finish (#2B2B2E), worn walnut grip (#6B4A32), brass front sight, faint holster wear
along the barrel. 1970s New Jersey living-room interior, worn oak floor (#7B5C3A), cream
plaster walls (#E8DFC8), large picture window on the north wall framing falling snow,
warm tabletop practicals lower right - close-up on Eli's hands checking the revolver's
cylinder, window light wrapping from camera-left, negative fill camera-right, shallow
depth of field. Shot on 85mm lens, eye-level, static frame, rule-of-thirds with lead
room right.
```

The identity, prop, and location sentences are the three blocks restated verbatim
from their spec files (unchanged shot to shot); only the final clause - framing, action,
lens, and light direction for *this* shot - is new. That is the two-block split from
`guide-asset-reference.md` §2 applied across three assets at once.

---

## Reference counts and strength

How many reference images an asset can carry into one generation, and at what
strength, is model-specific and moves fast. The general rule of thumb -
**~4-6 references, strength ~0.7 (workable 0.6-0.8)** - lives in
`guide-asset-reference.md` §4. Current per-model ceilings (how many objects or
characters a given model can hold in one call) live in
`context/model-currency-2026-06.md`, in the "Reference-count & strength caveats"
table - check it before quoting a number, since it is re-verified quarterly and this
doc is not.

## Taxonomy quick reference

| Asset | Spec file (keeps `{show}`) | Anchor image (no `{show}`) |
|---|---|---|
| Character | `char-{show}-{name}.md` | `assets/char/{name}/char-{name}-id-front.png` |
| Prop | `prop-{show}-{name}.md` | `assets/prop/{name}/prop-{name}-hero.png` |
| Location | `set-{show}-{name}.md` | `assets/set/{name}/set-{name}-plate.png` |

`refs:` ids always match the second column's stem with no `{show}` and no extension -
`char-eli`, not `char-sbw-eli.md`.

## Common pitfalls

**Pitfall 1**: A shot needs a locked asset but the shot line has no `refs:`.
- **Solution**: `sequence-design` Step 7 scans the working folder for `char-`/`prop-`/`set-` specs and attaches `refs:` to every shot that needs one; `script-supervisor` catches any it missed.

**Pitfall 2**: `refs:` names an id with no matching spec file.
- **Solution**: build the asset first (`character-sheet` / `prop-turntable` / `location-pack`) - a broken reference re-derives identity from text and drifts.

**Pitfall 3**: The identity block gets paraphrased instead of pasted verbatim.
- **Solution**: `shot-prompt` Step 5 requires the exact block from the spec file - paraphrasing reintroduces the drift the asset was built to prevent.

**Pitfall 4**: Wardrobe, HMU, or prop condition changes across a cut with no story beat.
- **Solution**: `script-supervisor` flags state drift; revert to the established variant or add the motivating action.

**Pitfall 5**: Stacking more references than a model holds well.
- **Solution**: stay near the ~4-6 sweet spot and check the current per-model ceiling in `model-currency-2026-06.md` before adding more.
