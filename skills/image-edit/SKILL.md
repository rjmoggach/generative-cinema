---
name: image-edit
description: >-
  Write, improve, or rewrite image-to-image (i2i) edit prompts that TRANSFORM a still
  the user already has, rather than building one from scratch. Use whenever a real
  photo or generated still is the starting point and they want a prompt to: change one
  element while preserving the subject, swap the background/crowd/environment around a
  preserved subject, recolor or change wardrobe/material, add or progress a
  wound/scar/blood, age a face, relight or regrade, remove or clean up an object, or
  compose a locked character into a new scene. Trigger phrases include "change this
  image to X", "swap the crowd/background/wardrobe", "give me a prompt to edit this
  photo", "make these fans Moroccan instead of Dutch", "recolor this costume", "rewrite
  this so it's Y instead of Z", "age this character", "add a scar", "remove the sign",
  "relight this", "put this character in <place>". This is the i2i sibling of
  footage-transform (which is video-to-video); for a brand-new scene with no source
  still to preserve, use shot-prompt instead.
---

# Image-Edit Assistant (image-to-image)

Translate "here's my still, change this one thing" into a precise, copy-paste
image-to-image / inpaint prompt for a chosen model. You keep what makes the source
recognizable and change only what's asked. This is the i2i sibling of
`footage-transform`: it reuses the same craft and project-locking, scoped to single
images. It is also the **engine** the asset skills (`character-sheet`, `prop-turntable`,
`location-pack`) call to derive views and states from a locked anchor.

## When to use

The user has a **source still** (a real photo or a generated image) and wants to edit
it, not generate a new scene. If there is no still to preserve, use `shot-prompt`. If
the source is a video clip, use `footage-transform`.

## Step 1 — Load context

1. **Project / world lock (if any).** If the user names a show code, read
   `project-context-<show-code>.md` (and `art-bible-<show-code>.md` if present) and
   hold the Standard Prompt Prefix, hex codes, CMF lexicon, style reference, lighting,
   lens specs, atmosphere, and forbidden terms; construct prompts from those fields.
   A one-off with no project file is fine — say it won't be consistency-locked.
2. **Load the craft guides:**
   [`references/guide-image-editing.md`](references/guide-image-editing.md) — the
   durable i2i principles (preserve-then-change, edit mechanisms, the denoise dial,
   lighting integration, common edit types). For any edit that places or carries a
   locked subject, also read
   [`references/guide-asset-reference.md`](references/guide-asset-reference.md)
   (identity-block vs scene-block, multi-reference composition, reference counts).
   Read the sections relevant to the request before writing.

## Step 2 — Inspect the source first

Before writing anything, **look at the still** if you can open it: subject, framing,
wardrobe, palette, time of day, and especially the **light-key direction** (name it —
screen-left or screen-right). Build the edit from what the image actually shows, not
the user's one-line summary. If no source still is described, ask what they're starting
from before writing.

## Step 3 — Pick the target model and its i2i syntax

Confirm the target model (ask once if unstated). Load that model's doc for the
source/reference syntax, reference-image limits, and the denoise/strength or
inpaint/mask controls:

- FLUX.1 Kontext: [`references/models/model-editing-flux-kontext.md`](references/models/model-editing-flux-kontext.md)
  (instruction-style editing, character/region preservation).
- Nano Banana (Gemini Image): [`references/models/model-image-gemini-flash.md`](references/models/model-image-gemini-flash.md)
  (conversational / partial-denoise edits, multi-image reference).
- Seedream: [`references/models/model-image-seedream-4.md`](references/models/model-image-seedream-4.md)
  (multi-reference identity preservation).
- FLUX.2: [`references/models/model-image-flux-pro.md`](references/models/model-image-flux-pro.md).

Check [`references/model-currency-2026-06.md`](references/model-currency-2026-06.md)
for the current version and the model's reference-count/strength limits before quoting
one — these change monthly.

## Step 4 — Choose the edit mechanism (the key fork)

Decide before writing; each changes the whole prompt (guide §3):

- **A. Conversational / partial-denoise** — one attribute, rest pixel-stable (lowest
  identity risk).
- **B. Masked inpaint** — a bounded region (remove/fix/add at a spot).
- **C. Full-frame i2i on a denoise dial** — global change (restyle/relight/reworld);
  set strength deliberately (guide §4: ~0.2–0.35 light, ~0.4–0.6 moderate, ~0.7+ heavy).
- **D. Multi-reference composition** — compose locked assets (subject + location +
  costume); assign each reference an explicit role (guide-asset-reference §5).

## Step 5 — Build the prompt: preserve, then change one thing

State **both halves explicitly** (guide §1):

- **Identity block** — what to preserve *exactly* (subject/face, wardrobe, framing,
  light-key direction), reused verbatim. Restate the project prefix when a show is loaded.
- **Edit instruction** — the single thing to change, stated concretely: hex colors,
  garment/material names, wound position+side+size, target style/grade.
- **Reference roles** (mechanism D) — "Image 1 = this exact person, keep face and
  features; Image 2 = background; Image 3 = costume/prop."
- **Integration** — for added/swapped elements, match light direction, optics, haze,
  depth of field, grain, and remove hard cut-out edges (guide §5; full craft in
  `guide-footage-transformation.md` §4–5).
- **Lock-down clause** — restate the fragile guardrail: "face and identity unchanged;
  everything else identical to the source."

## Step 6 — Output format

- Wrap **every** prompt in a triple-backtick code block (easy copy-paste).
- A short label above each is fine (`Recolor — navy jacket`).
- Put model parameters (denoise/strength, reference count, mask note) **outside** the
  code block.
- Inside the block, write the prompt as plain prose in the model's order
  (identity/preserve → change → integration → lock-down; references declared first if
  the model expects them up top).
- English first; add a translation only if asked, after the English.

## Step 7 — Iterate

Change **only the named thing** ("warmer grade," "scar a touch lower," "navy not
black," "keep the original crop") and keep the rest of the prompt stable — re-rolling
the whole prompt loses what already worked. **Edit the chosen result** (pass it back as
the base) rather than starting over; for any progression (wound stages, aging), edit
from the previous stage at low denoise.

## Critical rules

1. Always state both halves: lock what's preserved, name the one thing that changes.
2. Repeat the fragile guardrail ("face and identity unchanged") at the end.
3. Pin exact values — hex, garment/material, wound position+side+size; vague language drifts.
4. Hold the source's light-key direction unless the edit *is* a relight.
5. Prefer partial-denoise / inpaint over full regeneration for one-attribute changes;
   start low on the denoise dial and raise only if the change didn't take.
6. Verify per-model reference-count/strength limits against `model-currency` before quoting.
