# roadmap/ — staged stubs for the art-department expansion

These are **skeleton drafts** for the new crew and workflow described in
[`../ROADMAP.md`](../ROADMAP.md). They are deliberately **not wired into the build**
yet, so they can't ship half-finished. Flesh them out, then promote them.

## What's here

```
agents/   production-designer · propmaster · location-scout   (3 agent stubs)
skills/   art-direction · prop-turntable · location-pack      (3 skill stubs)
```

> `image-edit` (Phase 0) shipped in **v0.5.1**; `character-sheet`, `casting-director`,
> `costume-designer`, and `makeup-hair` (Phase 1) shipped in **v0.6.0** — all promoted
> to their live locations.

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

Build order follows the phases in `../ROADMAP.md`: `image-edit` first (Phase 0),
then the character pipeline, then props/locations, then the world bible.

> Stubs marked `DRAFT — STUB` in the body. Remove that line when the file is real.
