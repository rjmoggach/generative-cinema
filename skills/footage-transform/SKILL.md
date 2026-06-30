---
name: footage-transform
description: >-
  Write, improve, or rewrite video-to-video (v2v) prompts that TRANSFORM footage
  the user already has, rather than building a scene from scratch. Use whenever a
  real clip is the starting point and they want a prompt to: add a VFX element (set
  a head or hair on fire, transform a hand, make a limb invisible), swap the
  environment around a preserved subject (clouds, lava, a neon city), drop a giant
  photoreal creature onto a landmark, relight or regrade so subject and added
  elements look like one shot, sync a crash zoom or push-in to a spoken line or
  timecode, or generate a matching transformed start frame to animate from. Also use
  when they paste such a prompt and ask to change its lighting, timing, creature, or
  runtime, or just say "make a Seedance prompt for this video" with a clip attached.
  This is the video-to-video specialization; for a brand-new scene from references
  with no source clip to preserve, use the `shot-prompt` skill instead.
---

# Footage Transformation Assistant

Translate "here's my clip, change this one thing" into a precise, copy-paste
video-to-video prompt for a chosen model. You keep the real subject and the real
camera move, and change only what's asked. This is the v2v sibling of `shot-prompt`:
it reuses the same craft and project-locking, and adds the transformation layer.

## When to use

The user has a **source clip** and wants to edit it, not generate a new scene. If
there is no clip to preserve, use `shot-prompt` instead.

## Step 1 — Load context

1. **Project lock (if any).** If the user names a show code, read
   `project-context-<show-code>.md` and hold its Standard Prompt Prefix, hex codes,
   lighting, lens specs, atmosphere, and forbidden terms. A one-off with no project
   file is fine — say it won't be consistency-locked.
2. **Load the craft guide:**
   [`references/guide-footage-transformation.md`](references/guide-footage-transformation.md)
   — the durable v2v principles (preserve-then-change, lighting integration, timed
   moves, duration budget, first-frame workflow). Read the sections relevant to the
   request before writing.

## Step 2 — Inspect the source first

Before writing anything, **probe the clip** if you can open it: duration / fps /
aspect, and extract a few frames. Build the source declaration and the output runtime
from what the footage actually shows — subject, wardrobe, framing, camera move, time
of day, key direction — not from the user's one-line summary. Default the output
duration to the probed runtime. If no clip is described, ask what footage they're
starting from before writing.

## Step 3 — Pick the target model and its v2v syntax

Confirm the target model (ask once if unstated; Seedance is the common default). Load
that model's doc for the source-declaration syntax, input limits, and audio flags:

- Seedance 2.x: [`references/models/model-video-seedance-pro.md`](references/models/model-video-seedance-pro.md)
  (`@source` / `@creature` declarations, NON-IP guardrail, SFX line, input limits).
- Other v2v models (Runway, Kling, Wan, Veo): use their model doc for the equivalent
  source/reference syntax; the craft from the guide is the same.

Check [`references/model-currency-2026-06.md`](references/model-currency-2026-06.md)
for the current version before quoting one.

## Step 4 — Decide the two forks with the user

Two choices change the whole prompt; settle them before writing:

1. **Transformation mode** — add an element to the plate, or replace the environment
   around a preserved subject (guide §3).
2. **Lighting** — preserve the subject's light and grade only the new elements
   (lowest identity risk), or relight the whole frame under one look (higher face
   risk; lock identity explicitly) (guide §4).

## Step 5 — Build the prompt: preserve, then change one thing

State **both halves explicitly** (guide §1):

- **Source declaration** naming what to preserve *exactly* and the single thing to
  change (plus a texture-only second input if a real fur/material keeps faking).
- **Specs line** with aspect, source-matched duration, look/grade, NON-IP guardrail
  when a design is added, and the right audio mode.
- **Scene action** as one continuous shot (lead with shot/lens + "same framing as
  source," then preserved performance, then the transformation with physics + plate
  interaction, then any timed move with **both** a semantic and numeric anchor).
- **Lock-down clause** restating the fragile guardrail (usually "face and identity
  unchanged; everything else identical to the source").
- **Behavioral SFX line** (ordered, specific — not "fire" but "a soft whoomph as it
  catches, then a low steady flame roar and crackle, occasional ember pop").

If a payoff needs lip-sync or a prepended intro, run the **duration budget**
(`intro + remaining = total`, guide §7) and flag what falls off *before* delivering —
never promise lip-sync on a fixed total without the subtraction.

## Step 6 — Output format

- Wrap **every** prompt in a triple-backtick code block (easy copy-paste).
- A short label above each is fine (`Hook_2 · Variant 1 — Through the clouds`).
- Put model parameters and the duration-budget note **outside** the code block.
- Inside the block, write the prompt as plain prose in the model's order
  (`@source` → `@creature` → specs → continuous action + lock-down → SFX).
- English first; add a translation only if asked, after the English.

## Step 7 — Iterate

Change **only the named thing** ("softer light," "from the right," "make it huge," "a
beat before the zoom," "keep the original runtime") and keep the rest of the prompt
stable — re-rolling the whole prompt loses what already worked. On any change to
runtime or intro length, **recompute** the duration budget and tell the user the new
marks. When refining a generated still, edit the chosen result rather than starting
over.

## Critical rules

1. Always state both halves: lock what's preserved, name the one thing that changes.
2. Repeat the fragile guardrail ("face and identity unchanged") at the end of the action.
3. Match the source runtime by default; recompute timing on every runtime change.
4. NON-IP guardrail whenever a creature/design is added; no negative prompts on Seedance.
5. Never promise lip-sync + a prepended intro on a fixed total without the budget subtraction.
6. Be specific and behavioral — texture and physics words over "cinematic" or "stunning".
