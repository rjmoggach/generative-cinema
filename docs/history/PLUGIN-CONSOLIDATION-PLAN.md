# Plugin Consolidation Plan

Fold the four skills + the `context/` library into **one installable plugin**,
consolidate the tightly-coupled skills, and add **subagents** for research and
continuity tracking. Grounded in the Cowork/Claude Code plugin spec.

---

## 1. Why a plugin (and why now)

The four skills are no longer independent — they share one knowledge base and run
as a pipeline. A plugin is the right container:

- **One install, one unit.** A single `.plugin` file ships all skills, agents,
  and the whole `context/` library together.
- **Kills the duplication.** Today `skills/build.py` copies the library into each
  skill's `references/` so each `.skill` is self-contained. Inside *one* plugin
  there is exactly one `context/` at the plugin root that every skill and agent
  reads via `${CLAUDE_PLUGIN_ROOT}`. **`build.py` and the bundled copies go away.**
- **Adds agents + hooks.** Plugins can carry subagents (isolated context windows)
  and an optional session hook to auto-load the active show bible.

---

## 2. Proposed structure (repo *is* the plugin)

Add a manifest at the repo root and let the repository itself be the plugin, so
`context/` stays the single source of truth with no copying.

```
generative-cinema/                      (= plugin root, ${CLAUDE_PLUGIN_ROOT})
├── .claude-plugin/
│   └── plugin.json                       # manifest (name, version, author)
├── context/                              # THE library — one copy, unchanged
│   ├── guide-*.md  reference-*.md  model-*.md  model-currency-*.md
├── skills/
│   ├── cinematography/SKILL.md           # unified creative pipeline (router)
│   └── model-docs/SKILL.md               # library maintenance
├── agents/
│   ├── continuity-supervisor.md          # verify a sequence's spatial coherence
│   ├── model-researcher.md               # isolated web research for model docs
│   └── context-keeper.md                 # query/lookup over a show bible
├── hooks/hooks.json                      # (optional) auto-load active show bible
├── knowledge-base/  docs/  prompts/      # unchanged
└── README.md  CHANGELOG.md
```

Skills/agents reference the library as `${CLAUDE_PLUGIN_ROOT}/context/<file>` —
no `references/` copies, no sync step.

---

## 3. Skill consolidation — recommendation: 2 skills

The three creative skills (project-context, sequence-design, shot-prompt) are one
workflow used in sequence and share the same references. Merge them into a single
`cinematography` skill whose SKILL.md **routes by intent** to bundled workflow
docs. Keep `model-docs` separate — it's a different job (librarian), triggered by
different language, rarely used alongside creative work.

```
skills/cinematography/
├── SKILL.md                 # detects stage, routes, lists craft refs
└── workflows/
    ├── project-context.md   # the visual-DNA interview (was project-context)
    ├── sequence-design.md   # scene/coverage planning (was sequence-design)
    └── shot-prompt.md       # six-layer prompt generation (was shot-prompt)
```

`SKILL.md` opens with a router: "Defining a look? -> workflows/project-context.md.
Planning a scene? -> workflows/sequence-design.md. Writing prompts? ->
workflows/shot-prompt.md," then points at the shared craft guides and model docs
in `${CLAUDE_PLUGIN_ROOT}/context/`.

### Options (pick one)

| Option | Skills | Pros | Cons |
|---|---|---|---|
| A. **2 skills** (recommended) | `cinematography` + `model-docs` | Matches the real coupling; precise triggers stay clean; one creative entry point | Slight router logic in one SKILL.md |
| B. 1 skill | everything in `cinematography` | Maximum consolidation | One broad description must trigger for librarian + creative intents; muddier |
| C. keep 4 | as today, just in the plugin | No rewrite; finest triggering | Keeps the coupling/duplication the user wants gone |

Recommendation: **A**. It's the consolidation you're after without overloading a
single description.

---

## 4. Subagents — for research + continuity tracking

Honest framing first: **subagents don't persist memory between calls** — each run
starts fresh. Durable "context" lives in **files** (the show bible, saved shot
lists). Agents add value through *isolated context windows* and *focused tool
sets*: research and verification that would otherwise bloat the main thread.

| Agent | Job | Why a subagent | Tools | Color |
|---|---|---|---|---|
| `continuity-supervisor` | Audit a shot list / sequence against the show bible + `guide-continuity-rules.md`: screen direction, eyelines, the 180° line, palette/light/lens consistency. Report issues. | Holds the running continuity state of a whole sequence in its own window; pure verification step | Read, Grep, Glob | yellow |
| `model-researcher` | Do the web research to write/refresh a model doc; return a structured summary. | Keeps heavy web-fetch noise out of the main conversation | WebSearch, WebFetch, Read | cyan |
| `context-keeper` | Given a show code, load `project-context-{show}.md` and answer "what's our palette / lens / forbidden terms?" Summarize or check completeness. | Lets the main thread query the show bible without re-reading the whole file each time | Read, Grep | blue |

`continuity-supervisor` is the strongest "tracking various contexts" play — it's
the verification step the `shot-prompt`/`sequence-design` workflows already gesture
at ("review as a cut"). `model-researcher` slots into `model-docs`.

---

## 5. State & context tracking

- **Per-project state = files** in the user's working folder:
  `project-context-{show}.md` (the bible) and, proposed, saved sequence shot lists
  `sequence-{show}-S{n}.md`. These persist across sessions and are what the agents
  read/write.
- **Static knowledge = `context/`** in the plugin (craft guides, model docs).
- **Optional `SessionStart` hook**: if exactly one `project-context-*.md` exists in
  the folder, `cat` it so the active look is loaded automatically. Cowork uses
  hooks rarely; include only if you want auto-loading. Otherwise the
  `cinematography` skill loads it on first use (as it does today).

---

## 6. Optional future phase — actually generate

A plugin can carry an `.mcp.json`. Wrapping the model APIs (FLUX, Veo, Kling, …)
as an MCP server would let the plugin *run* generations, not just write prompts —
turning the pipeline end-to-end. Needs API keys/endpoints and is out of scope for
the consolidation itself; flag for later.

---

## 7. Migration steps

1. Add `.claude-plugin/plugin.json` (name `generative-cinematography`, v0.3.0).
2. Create `skills/cinematography/` with a routing `SKILL.md` + `workflows/` built
   from the three existing creative SKILL.md bodies (lightly edited to reference
   `${CLAUDE_PLUGIN_ROOT}/context/`).
3. Keep `skills/model-docs/SKILL.md`; repoint its references to the shared library.
4. Write the three `agents/*.md`.
5. Delete the per-skill `references/` copies and **retire `skills/build.py`**;
   replace with a tiny `package.py` (or a one-line zip) that produces the `.plugin`.
6. Update `.gitignore` (`*.plugin`, `dist/`), README, CHANGELOG.
7. Validate structure (plugin.json valid, each skill has SKILL.md, agents parse),
   package to `.plugin`, present for install.

### What changes vs. today
- 4 skills -> 2 skills + 3 agents, in 1 plugin.
- No more bundled `references/` duplication or `build.py` sync.
- One `.plugin` install instead of four `.skill` files.

---

## 8. Open decision (drives the build)

**Skill granularity** — Option A (2 skills) vs B (1) vs C (4). Recommendation: A.
Confirm this and I'll build the plugin: manifest, consolidated `cinematography`
skill, `model-docs`, the three agents, packaging, and the README/CHANGELOG updates.
