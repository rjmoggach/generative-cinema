# roadmap/ — staged stubs for the art-department expansion

These were **skeleton drafts** for the new crew and workflow described in
[`../ROADMAP.md`](../ROADMAP.md), staged here so they could be fleshed out and
promoted without shipping half-finished.

## What's here

All Phase 1–3 stubs have shipped and been promoted to their live locations —
`roadmap/agents/` and `roadmap/skills/` are now **empty** (no stub files remain).

> `image-edit` (Phase 0) shipped in **v0.5.1**; `character-sheet`, `casting-director`,
> `costume-designer`, and `makeup-hair` (Phase 1) shipped in **v0.6.0**; `prop-turntable`,
> `location-pack`, `propmaster`, and `location-scout` (Phase 2) shipped in **v0.7.0**;
> `art-direction` and `production-designer` (Phase 3) shipped in **v0.8.0** — all
> promoted to their live locations.

The remaining roadmap work — **Phase 4: Integration & QC** (teaching
`sequence-design`/`first-ad`/`shot-prompt` to attach and consume asset references,
extending `script-supervisor` to audit asset continuity) — is **not staged as new
stubs here**. It lands as edits to the existing skills and agents already shipped
(`sequence-design`, `first-ad`, `shot-prompt`, `script-supervisor`), not as new
crew or skills. See [`../ROADMAP.md`](../ROADMAP.md) §7 (Phase 4) for scope.

## How to promote a stub into the live plugin

**An agent:**
1. Finish `roadmap/agents/{name}.md` (keep the strict-YAML frontmatter:
   `name`, `description`, `model`, `color`, `tools`).
2. Move it to `plugin/agents/{name}.md`.
3. Add it to the crew table in `plugin/README.md` and the root `README.md`.

**A skill:**
1. Finish `roadmap/skills/{name}/SKILL.md` and create its `references/` (bundled
   craft guides — add the new `context/guide-*.md` first).
2. Move the folder to `skills/{name}/`.
3. Add `{name}` to the `SKILLS` list in **both** `plugin/assemble.py` and
   `skills/build.py`, and add its `MANIFEST` entry in `skills/build.py`.
4. `python plugin/assemble.py` (validates), then `--package` for release.

Build order followed the phases in `../ROADMAP.md`: `image-edit` first (Phase 0),
then the character pipeline, then props/locations, then the world bible.

> Stubs marked `DRAFT — STUB` in the body. Remove that line when the file is real.
