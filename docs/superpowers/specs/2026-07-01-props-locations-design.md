# Props & Locations (Phase 2) — Design

**Date:** 2026-07-01 · **Status:** Approved · **Target release:** v0.7.0
**Owner:** Rob (Creative Producer) · **Roadmap:** [`ROADMAP.md`](../../../ROADMAP.md) Phase 2

---

## 1. Goal

Extend the art-department asset layer from characters (Phase 1, v0.6.0) to **props**
and **locations/sets**: give the plugin a way to build and store persistent,
re-attachable reference assets for objects and environments, so downstream shots
carry a prop's or place's identity from images while the prompt states only what
changes. Ship the `propmaster` and `location-scout` crew and the skills that
orchestrate them, following the exact dual creative+technical pattern proven in
Phase 1.

## 2. Scope (full Phase 2, one shippable spec)

**In:** 2 skills, 2 agents, 1 creative-craft file, 2 technical guides, taxonomy
extension, 2 output templates, build wiring, ROADMAP `location-→set-` cleanup, docs,
version bump to 0.7.0, research sources, release.
**Out:** 3D-assist / Blender MCP (deferred entirely, see §3.2); Production Designer /
`art-bible` (Phase 3); asset-reference wiring into sequence/shot/QC (Phase 4).

## 3. Decisions locked in brainstorming

1. **Full Phase 2 in one spec** → v0.7.0.
2. **3D-assist deferred entirely.** No `guide-3d-assist.md` this phase. Each technical
   guide carries a one-line forward-pointer that 3D-assist (geometry-lock, depth-pass
   conditioning) is a known technique for reverse-angle/destruction coherence, deferred
   to a later phase — acknowledging the gap without shipping unproven craft.
3. **Environment asset type stays `set`** (VFX-standard, already reserved in the §9
   taxonomy). Crew/skill names stay `location-scout` / `location-pack` (the role finds
   locations; the built asset is the "set"/environment). So skill name (`location`) ≠
   asset type (`set`) — intentional and documented.
4. **Asset binaries live in the user's working folder only** (plugin stays text-only,
   same as Phase 1).
5. **Every role is dual** — creative craft (the art) and technical execution.
6. **One combined creative file** (`reference-craft-artdept.md`), extensible so Phase 3
   adds a Production Designer section.

## 4. Two kinds of craft file (creative vs technical)

### 4.1 NEW `context/reference-craft-artdept.md` — the creative craft

Sibling of `reference-craft-character.md`. Two sections, each = real prose craft
principles + an anchor table of masters:

- **Props** — hero vs dressing vs action props; sourcing and fabrication; *multiples*
  (stunt/destruction/continuity duplicates that must match); prop-as-character and
  state variants (pristine/aged/bloodied) as story; the propmaster's continuity
  discipline. Anchors: notable property masters / prop houses / prop makers
  (e.g. Eric Hart; ISS/Independent Studio Services and prop-house tradition; a few
  celebrated hero-prop builds).
- **Locations & Sets** — the scouting packet (recce beyond the frame), environment as
  storytelling, sun-path/light logistics, reverse-angle coherence, set decoration vs
  location dressing. Anchors: production designers / art directors / location pros
  (e.g. Ken Adam, Rick Carter, Dante Ferretti, Stuart Craig, Jack Fisk; Michael Rizzo
  as art-department authority).

### 4.2 NEW technical guides (decision-unit format: Decision / Use when / Because / Prompt translation / Watch-outs / Anchors)

- `context/guide-prop-turntable.md` — object multi-view conventions: hero view →
  orthographic ring (front/back/side-l/side-r/top) → detail/macro → optional 360;
  anchor-then-fan-out; framing-the-asset rules (fill frame, neutral bg, even light);
  state variants and *multiples must match*; derive views via `image-edit`. Carries the
  3D-assist forward-pointer.
- `context/guide-location-pack.md` — master establishing plate → multi-angle coverage
  (including the reverse angle) → time-of-day / weather variants derived from the
  *locked master geometry* (change one variable at a time) → a continuity table; derive
  via `image-edit`. Carries the 3D-assist forward-pointer.

Both cross-reference `guide-asset-reference.md` (spine), `guide-image-editing.md`
(engine), and `reference-craft-artdept.md` (creative) rather than duplicating them.

### 4.3 Extend `context/guide-asset-reference.md` §9 — new facets/views

Add to the taxonomy (same way Phase 1 added `expr`/`pose`/`palette`):

- **Prop facets:** `hero` (hero view), `ortho` (orthographic ring member), `detail`
  (macro/detail), `360` (turntable step).
- **Location/set facets:** `plate` (master establishing plate), `cov` (coverage angle),
  `tod` (time-of-day / weather variant).
- **New views** (for objects/environments): `top`, `bottom`.

## 5. Asset naming (uses the reserved taxonomy)

```
Props      prop-{show}-{name}.md      assets/prop/{name}/
  hero     prop-{name}-hero.png
  ortho    prop-{name}-ortho-front.png  -back / -side-l / -side-r / -top
  detail   prop-{name}-detail-01.png
  state    prop-{name}-hero-aged.png    (state suffix; e.g. pristine/aged/bloodied)

Locations  set-{show}-{name}.md       assets/set/{name}/
  plate    set-{name}-plate.png
  cov      set-{name}-cov-01.png        (incl. the reverse angle)
  tod      set-{name}-tod-dawn.png      -tod-night / -tod-rain (one variable at a time)
```

Lowercase kebab; `-vNN` optional; image files carry no `{show}` (only the `.md` spec
does) — consistent with the Phase 1 fix.

## 6. New skills

- `skills/prop-turntable/SKILL.md` (promote roadmap stub) → build/refresh
  `prop-{show}-{name}.md` + `assets/prop/{name}/`. Anchor (hero) → orthographic ring →
  detail → optional 360, all via `image-edit`. Output to the user's working folder.
- `skills/location-pack/SKILL.md` (promote roadmap stub) → build/refresh
  `set-{show}-{name}.md` + `assets/set/{name}/`. Master plate → coverage → time/weather
  variants via `image-edit`. Output to the user's working folder.
- `references/` for each (bundled by `build.py`): `reference-craft-artdept`, the skill's
  own technical guide, `guide-asset-reference`, `guide-image-editing`,
  `model-currency-2026-06`, and the relevant image/editing model docs.
- `references/prop-template.md` and `references/set-template.md` — hand-authored output
  skeletons (wired as `assemble.py` HELPERS, like `character-template.md`).

## 7. New agents `plugin/agents/`

Thin personas, strict-YAML frontmatter (`name`/`description`/`model`/`color`/`tools`),
`model: inherit`, `tools: ["Read", "Grep", "Glob"]`. Read both the creative reference
and the technical guide:

- `propmaster` (`color: pink`) — hero prop anchor + orthographic ring + details +
  state variants; reads `reference-craft-artdept.md` (Props) + `guide-prop-turntable.md`.
- `location-scout` (`color: cyan`) — master plate + coverage + time/weather variants;
  reads `reference-craft-artdept.md` (Locations & Sets) + `guide-location-pack.md`.

## 8. Build wiring

- `skills/build.py` — add `prop-turntable` and `location-pack` MANIFEST entries.
- `plugin/assemble.py` — add both skills to `SKILLS`; add `prop-template.md` and
  `set-template.md` to `HELPERS`.
- `python plugin/assemble.py` must end `VALIDATE: OK`; `python skills/build.py` clean.

## 9. Docs, ROADMAP cleanup + release

- **ROADMAP cleanup (deferred from Phase 1):** finish the `location-{show}-{name}.md` →
  `set-{show}-{name}.md` rename in ROADMAP §3.6 and §4, and update the pre-taxonomy
  `assets/…` longhand strings (§3.2/§3.4/§3.5) to the §9 forms.
- `README.md` + `plugin/README.md`: add 2 skill rows + 2 agent rows + the new
  guides/reference; skill count → nine; agent count → ten; bump banner to 0.7.0.
- `CHANGELOG.md` v0.7.0 entry; `ROADMAP.md` mark Phase 2 shipped.
- `plugin/.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` → 0.7.0.
- Remove promoted stubs: `roadmap/agents/propmaster.md`, `roadmap/agents/location-scout.md`,
  `roadmap/skills/prop-turntable/`, `roadmap/skills/location-pack/`; update
  `roadmap/README.md` (leave `production-designer` + `art-direction` for Phase 3).
- Record research sources in `knowledge-base/Miscellaneous-Sources.md` (§11).
- **Release (Task 9):** merge to `main`, git tag `v0.7.0`, `python plugin/assemble.py
  --package`, `gh release create v0.7.0 generative-cinema.plugin` (keep v0.6.0 + v0.5.1
  releases intact). GitHub release is outward-facing — proceed per the user's standing
  go-ahead for this phase.

## 10. Verification

- `python plugin/assemble.py` → `VALIDATE: OK` (no dead references, valid agent YAML).
- `python skills/build.py` → syncs + zips clean.
- Every `](references/…)` in both new SKILL.md files resolves to a bundled file.
- Both agent frontmatters parse as strict YAML with the required keys.
- Naming coherence: image filenames carry no `{show}`; facets/views used consistently
  across guides, templates, skills, and agents (the Phase 1 final-review lesson).
- No `[PLACEHOLDER]` in shipped files.

## 11. Research — creative-context sources (added to `knowledge-base/Miscellaneous-Sources.md`)

- **Props** — Eric Hart, *The Prop Building Guidebook: For Theatre, Film, and TV*
  (Routledge) — the standard prop-construction reference by a working props master.
  <https://www.propbuildingguidebook.com/> ·
  <https://www.routledge.com/The-Prop-Building-Guidebook-For-Theatre-Film-and-TV/Hart/p/book/9781032154619>
- **Art department / set decoration** — Michael Rizzo, *The Art Direction Handbook for
  Film & Television* — art-department setup, location scouting, executing the design,
  building scenery; by a working production designer.
  <https://www.routledge.com/The-Art-Direction-Handbook-for-Film--Television/Rizzo/p/book/9780415842792>
- **Production design** — Jane Barnwell, *Production Design: Architects of the Screen*
  (and Vincent LoBrutto, *The Filmmaker's Guide to Production Design*) — the PD's role,
  landmark designs, environment as storytelling.
  <https://cup.columbia.edu/book/production-design/9780231850131/> ·
  <https://www.amazon.com/Filmmakers-Guide-Production-Design/dp/1581152248>

## 12. Approach considered & rejected

- **Separate creative files per department** (`reference-craft-props.md` +
  `reference-craft-locations.md`) — rejected in favor of one combined
  `reference-craft-artdept.md`, matching the single `reference-craft-character.md`
  precedent and keeping the art-department craft together for Phase 3 extension.
- **Including 3D-assist now** — rejected (deferred): unproven at scale and outside the
  text-craft plugin's lane; better as a separate hands-on spike.
