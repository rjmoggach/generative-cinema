---
name: model-docs
description: >-
  Research and write (or refresh) a structured model-{type}-{name}.md context doc
  for a generative image/video/editing model, following the library's unified
  documentation pattern so it slots cleanly beside the existing model docs. Use
  whenever a user wants to "add a model", "document a new model", "update the
  FLUX/Veo/Kling/Sora doc", "the model docs are out of date", or asks to research a
  generative model's prompting structure, parameters, costs, or capabilities for
  the context library. Always web-research current facts first, then write to the
  template; also update the currency snapshot so the version table stays accurate.
---

# Model Docs Generator

Produce a concise, consistent, **researched** reference doc for one generative
model, suitable for use as cached context by the other skills and by Custom GPTs.

## When to use

Adding a new model, or refreshing an existing `model-*.md` whose facts have aged.
Known coverage gaps (Kling 3.0, Sora 2 / 2 Pro, Wan 2.6) are listed in the gaps
table of
[`references/model-currency-2026-06.md`](${CLAUDE_PLUGIN_ROOT}/context/model-currency-2026-06.md)
— good first candidates.

## Step 1 — Scope

- Identify the exact model **and version** (e.g., "Kling 3.0", "Seedance 2.5").
- Determine primary function: text-to-image, image-to-video, editing, etc. If a
  model spans functions, write a **separate doc per function**.
- File name: lowercase kebab-case `model-<type>-<name>.md` where type ∈
  {image, video, editing} (e.g., `model-video-kling-3.md`).

## Step 2 — Research current facts (required, do this before writing)

Web-search official sources first (developer site, API docs, release notes), then
reputable secondary sources (Replicate/Fal/community) for practical details.
Collect: current version + release date, resolution, duration (video), speed,
cost, prompting structure/syntax, full parameter list, unique capabilities,
common failure modes + fixes, API endpoint + a minimal integration example.

> Do not write version/spec facts from memory — this space changes monthly.

## Step 3 — Write to the unified template

Follow [`references/model-doc-template.md`](${CLAUDE_PLUGIN_ROOT}/context/model-doc-template.md)
exactly (Quick Reference table → Overview → When to Use → Prompting Structure →
Parameters → Techniques → Common Workflows → Troubleshooting → Integration). Use
the bundled exemplar for style:
[`references/example-model-doc.md`](${CLAUDE_PLUGIN_ROOT}/context/example-model-doc.md).

Formatting rules: standard Markdown only (no emojis, no em/en dashes — plain
hyphens, straight quotes). Put all syntax/params/technical terms in `code`. Use
tables for parameters and troubleshooting. Use `> **Note:**` / `> **Tip:**` /
`> **Warning:**` callouts. Keep it tight — this is cached context, not prose.

## Step 4 — Sync currency + finalize

1. Add or update this model's row in the currency snapshot (current version,
   release date, what changed). If it closes a coverage gap, remove it from the
   gaps table. The canonical copy lives at `context/model-currency-2026-06.md`
   in the library repo; the bundled `references/` copy is a snapshot.
2. Run the quality checklist:
   - [ ] Quick Reference table complete and accurate
   - [ ] All template sections present
   - [ ] Every parameter in a table
   - [ ] Troubleshooting actionable
   - [ ] `kebab-case.md` filename, correct `model-<type>-` prefix
   - [ ] Concise, no emojis/em-dashes, technical terms in `code`
3. Save into the library's `context/`. Mention it in `CHANGELOG.md`.

## Critical rules

1. Research before writing; cite sources to the user.
2. One doc per function; consistent `model-<type>-<name>.md` naming.
3. Alway