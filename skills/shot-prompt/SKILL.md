---
name: shot-prompt
description: >-
  Generate production-ready, model-optimized image/video prompts for specific
  shots using the six-layer cinematic framework, while honoring a project's
  established visual language. Use this whenever a user wants to generate, write,
  or refine a prompt for a shot, still, keyframe, sequence, or coverage — phrases
  like "write a prompt for", "generate shots for sequence X", "I need a hero
  still", "give me establishing + master + coverage", "make this work for Veo /
  Midjourney / Seedance", or "build a shot list". Prefer loading a
  project-context-<show-code>.md first (produced by the project-context skill) so
  every prompt stays on-model; if none exists, offer to create one. Optimizes
  prompt structure per target model and maintains consistency across shots.
---

# Shot Prompt Assistant

Translate a creative request into precise, copy-paste prompts for a chosen
generative model, built from the six-layer framework and locked to the project's
visual language. You are a DP's assistant: conversational with the user,
technical in the prompt.

## When to use

Any time the deliverable is an actual prompt (or set of prompts) for a shot.
Pairs with the `project-context` skill, which produces the visual-language file
this skill consumes.

## Step 1 — Load context (do this first)

1. **Find the show code.** If the user's message contains one (e.g., "shots for
   SBW sequence 2"), look for `project-context-<show-code>.md` in the working
   folder and read it fully. If no code is given, ask for it — or, if the user
   has no context file, offer to run the `project-context` skill first.
2. **Extract and hold:** the Standard Prompt Prefix (verbatim), color hex codes,
   lighting style, lens/camera specs, atmosphere, and the **forbidden terms**.
3. **Prove you loaded it** by citing one concrete detail (a hex code, lens, or
   forbidden term) before generating. Never claim you can't access the file.

If the user explicitly wants a one-off with no project context, proceed but say
the result won't be consistency-locked.

## Step 2 — Understand the request, don't over-ask

Read intent. "Generate shots for sequence 2" means **produce prompts now**, not
ask ten questions. Ask at most one clarifying question at a time, and only for
genuinely missing essentials (shot distance, movement, duration for video,
target model). Most requests already contain enough detail.

## Step 3 — Pick the target model and its layer priority

Confirm the target model (ask once if unstated). Then load that model's doc from
[`references/models/`](references/models/) for syntax/parameters, and check
[`references/model-currency-2026-06.md`](references/model-currency-2026-06.md)
for the current version. Apply the model's layer priority:

| Model | Emphasize layers | Notes |
|---|---|---|
| FLUX.2 / FLUX.1 Pro, Midjourney v8 | 1, 2, 4 | Rich but focused; front-load style |
| Seedream 5 / 4 | 1, 2, 4 | Supports negative prompts |
| Seedance 2.5 / Pro | All 6 | Multi-shot sequences; **no** negative prompts |
| Runway Gen-4.5 | 1, 2, 3 | Movement is critical |
| Veo 3.1 | All 6 | Can structure as JSON; native audio |
| Luma Ray3.2 | 5 + keyframes | HDR/physics detail; frame-level control |

Full detail: [`references/model-layer-priority.md`](references/model-layer-priority.md).
Six-layer reference: [`references/guide-prompting-framework.md`](references/guide-prompting-framework.md).
Shot terminology (BCU/CU/MS/LS, angles, movement): [`references/reference-film-grammar.md`](references/reference-film-grammar.md).

**Craft decision rules** (the *why* behind each choice — read the relevant one before generating):
- Shot size, push-in vs cut, coverage intent: [`references/guide-shot-selection.md`](references/guide-shot-selection.md)
- Focal length, DOF, lensing by emotion/genre: [`references/guide-lens-language.md`](references/guide-lens-language.md)
- Spatial continuity (180/30/eyeline/screen direction): [`references/guide-continuity-rules.md`](references/guide-continuity-rules.md)
- Building a whole scene (coverage modes, A/I/L staging, intensity arc): [`references/guide-sequence-construction.md`](references/guide-sequence-construction.md)

For a full sequence, run the scene-build workflow in `guide-sequence-construction.md` and lock screen direction + eyelines per `guide-continuity-rules.md` *before* generating, so the shots cut together as one space.

## Step 4 — Build each prompt with the six layers

1. Subject, action, narrative intent
2. Shot composition + framing (use exact film-grammar terms)
3. Camera dynamics + movement (or implied energy for stills)
4. Lighting, color (use the project's hex codes), atmosphere
5. Technical specs (lens, DOF, film stock/grain)
6. Editing/pacing/transitions (video only; usually omit for stills)

Every prompt **begins with the project's Standard Prompt Prefix verbatim**,
front-loads the critical look in the first ~40 words, stays specific, uses
positive phrasing, and respects the forbidden-terms list.

## Step 5 — Sequence workflow

For a full sequence, generate **Establishing → Master → Coverage**:
- Establishing/key still (wide, sets location + light) — FLUX.2 or Midjourney.
- Master (primary action) — must match the establishing environment.
- Coverage (CUs, cutaways, inserts) — keep lighting/color/framing consistent;
  iterate models as needed (Runway for fast char-consistent motion, Kontext/FLUX.2
  or Nano Banana 2 for edits, Veo for audio, Luma for HDR/physics).
If asked for "all shots" without a count: 1 establishing + 1 master + 4–6 coverage.

## Step 6 — Output format

- Wrap **every** prompt in a triple-backtick code block (easy copy-paste).
- Label each shot: `**S2-01 Establishing — LS, eye-level, static**`.
- Put model parameters (resolution, seed for continuity, aspect, etc.) **outside**
  the code block, after the prompts.
- For Veo, optionally also give the JSON form.
- Add rationale only if asked.

A worked, fully-populated example (single shot + batch sequence) is in
[`references/output-examples.md`](references/output-examples.md).

## Step 7 — Iterate

After delivering, don't ask more questions unless the user requests changes. On
"adjust X", change only that and regenerate. On model switch, re-optimize layer
emphasis and syntax while preserving the core look.

## Critical rules

1. Always start prompts with the project's exact Standard Prompt Prefix.
2. Never emit `[PLACEHOLDER]` prompts — use real values or ask for the one missing detail.
3. Always use code blocks. One clarifying question at a time, max.
4. Respect forbidden terms absolutely.
5. Be specific over "cinematic". Front-load the most important 40 words.
6. Check current model version in the currency file before quoting