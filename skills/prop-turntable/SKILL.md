---
name: prop-turntable
description: >-
  Build or refresh a persistent prop reference — spec file plus a folder of locked
  multi-view images — that keeps an object consistent across every shot. Trigger phrases:
  "build a prop turntable", "lock this prop", "make a hero prop reference", "make a
  model sheet / object reference", "keep this object consistent across shots",
  "turntable this". Produces a hero anchor plus an orthographic ring
  (front/back/side-l/side-r/top), detail macros, state variants, and an optional 360.
  The output is the reference that shot-prompt and image-edit carry to hold the object's
  form, material, and finish consistent across scenes and states.
---

# Prop-Turntable Assistant

Build a persistent, multi-angle prop reference. Identity lives in the asset; downstream
prompts carry only change. When `shot-prompt` or `image-edit` needs to carry a prop
into a new scene, state, or angle, it attaches the outputs of this skill and pastes the
descriptor block verbatim. This skill calls `image-edit` as its derive engine — every
orthographic view, detail macro, and state is an i2i operation driven from the locked
hero anchor.

## When to use

Whenever a prop will recur across more than one shot, or when the user requests a
turntable, model sheet, object reference, or hero prop — even for a single scene if
form consistency matters. If the spec file already exists (`prop-{show}-{name}.md`),
refine it in place: update only the changed view or state and re-export the affected
images. Do not rebuild from scratch unless the object design has fundamentally changed.

## Core principle: anchor, then fan out

Generate one clean **hero view** first — frame-filling, even-lit, neutral background,
high-res, oriented to show the object's dominant face — then derive every orthographic
view, detail, and state *from it* via reference conditioning and `image-edit`. Never
generate views independently; siblings built without a shared anchor diverge immediately
in form, scale, and material reading. A weak anchor — off-angle, specular-blown,
low-res, or background-cluttered — poisons the entire ring. Get the hero right before
fanning out. Orient the object so its natural reading axis is vertical or horizontal
depending on form; hold that orientation and apparent scale constant across every
derived view.

## Step 1 — Load craft

Read these before writing any prompt:

- [`references/reference-craft-artdept.md`](references/reference-craft-artdept.md) —
  the creative foundation: prop class, design language, material palette, production
  intent (hero/dressing/action).
- [`references/guide-prop-turntable.md`](references/guide-prop-turntable.md) —
  view-angle discipline, ortho-ring alignment, 360 spacing, contact-sheet assembly, and
  a pointer to 3D-assist (a deferred technique).
- [`references/guide-asset-reference.md`](references/guide-asset-reference.md) —
  anchor-then-fan-out, reference counts and strength, multi-reference composition, and
  the asset naming taxonomy (§9).
- [`references/guide-image-editing.md`](references/guide-image-editing.md) —
  the i2i mechanics used to derive views, detail crops, and state progressions from the
  anchor.

If the user names a show code, read `project-context-{show}.md` (and
`art-bible-{show}.md` if present) and inherit the Standard Prompt Prefix, palette hex
codes, CMF lexicon, style reference, lighting logic, and forbidden terms; construct
prompts from those fields. Hold these consistently across all views and states.

## Step 2 — Hero anchor

Generate the **hero view**: the object centered, frame-filling, even-lit from a
three-quarter front angle that reveals its dominant silhouette. Neutral background —
grey card or seamless white — no shadow drama. The goal is maximum material and form
information with minimum distraction.

Once the anchor is approved:

1. **Write the descriptor block** — 40–70 words, hex-pinned: object class, overall
   form, primary material and finish with hex, secondary material if relevant, key
   identifying marks (engraving, logo, wear, patina), scale cue (length/weight class),
   and any critical proportional note. This block is pasted verbatim into every
   downstream prompt — vague language here becomes drift everywhere downstream.
2. Confirm the **prop class**: hero (screen-used, close-up-legible), dressing
   (background O/S), or action (stunt/breakaway). Hero props demand the highest
   material lock; dressing props tolerate a looser reference set.

## Step 3 — Orthographic ring

Using the hero anchor as the locked reference, derive the **orthographic ring** via
`image-edit` — one view at a time, each pinned to the same apparent object scale:

- Front: `prop-{name}-ortho-front.png`
- Back: `prop-{name}-ortho-back.png`
- Side left: `prop-{name}-ortho-side-l.png`
- Side right: `prop-{name}-ortho-side-r.png`
- Top: `prop-{name}-ortho-top.png`
- Bottom: `prop-{name}-ortho-bottom.png` *(only if relevant to scene use)*

Hold camera distance, lens length, and background constant across the ring. Align views
on the object's dominant axis — the same virtual horizon through the widest cross-
section — so cuts between views read as a coherent turntable, not separate shoots.
Derive each view from the hero; never cross-derive views from sibling orthos, as that
compounds drift.

## Step 4 — Details

Derive **detail / macro views** for signature features: engraving, maker's mark, clasp
mechanism, material seam, wear pattern, or any element small enough to drop from a
wide-angle shot. Each detail macro is an i2i crop-and-enlarge from the ortho view that
best exposes that feature.

- Detail images: `prop-{name}-detail-01.png`, `-detail-02.png`, etc.
- Caption each in the spec file: what feature, which ortho it was derived from, and why
  it matters for production (e.g., "barrel inscription — legible in close-up insert").

Models routinely drop micro-detail under even moderate strength values — if a detail is
identity-critical (a logo, a serial number, an insignia), composite it in rather than
relying on i2i alone.

## Step 5 — State variants and multiples

**State variants** — aged, damaged, wet, soiled, burnt, pristine — are derived by
editing forward from the closest prior state at low denoise (~0.15–0.25), not by
regenerating from the hero. The suffix pattern follows the taxonomy: state suffix appended
to the base view name.

- Aged hero: `prop-{name}-hero-aged.png`
- Damaged hero: `prop-{name}-hero-damaged.png`
- Wet hero: `prop-{name}-hero-wet.png`

For each state: note the base image it was derived from and the denoise value used; this
lets a future session re-derive from the same branch rather than guessing. Never
regenerate from the hero anchor when a progression state is needed — it breaks the
progression fingerprint.

**Multiples** — instances of the same prop in the same frame (a pair of handcuffs, a
set of glasses, a rack of rifles) — must be derived from the same hero anchor, held at
the same reference strength, so they read as the same object rather than variants.
Record each multiple path in the spec file under `## Multiples`.

**Optional 360:** if requested or if the prop appears in a wide range of camera angles,
generate 8–12 evenly-spaced views at 30° or 45° intervals from the ortho ring as the
locked reference set. Name as `prop-{name}-360-000.png`, `-030.png`, `-045.png`, etc.
(degree of rotation, zero-padded). Do not attempt 360 work before the ortho ring is
locked — it will diverge.

## Step 6 — Model + references

Identify the target model for all i2i work in this session (ask once if unstated;
prefer the model already in use for the project). Load the model doc for
source/reference syntax, per-model reference-image limits, and denoise/strength controls:

- FLUX.1 Kontext: [`references/models/model-editing-flux-kontext.md`](references/models/model-editing-flux-kontext.md)
- Gemini Flash (Nano Banana): [`references/models/model-image-gemini-flash.md`](references/models/model-image-gemini-flash.md)
- Seedream 4: [`references/models/model-image-seedream-4.md`](references/models/model-image-seedream-4.md)
- FLUX.1 Pro: [`references/models/model-image-flux-pro.md`](references/models/model-image-flux-pro.md)

Before quoting reference counts or strength values, check
[`references/model-currency-2026-06.md`](references/model-currency-2026-06.md) for the
current version and per-model limits — these change monthly. The general sweet spot is
**4–6 reference images at strength ~0.7** (guide-asset-reference §4), but verify the
hard limits per model before advising any specific count. Props with complex geometry,
reflective or transparent surfaces, or destruction requirements are strong candidates for
3D-assist (Blender MCP + orthographic renders) before the image skin pass — 3D-assist is a deferred technique; see `guide-prop-turntable.md` for the current pointer.

## Step 7 — Output

Write all outputs to the **user's working folder** — never to the plugin repo.

**Spec file:** `prop-{show}-{name}.md`, filled from
[`references/prop-template.md`](references/prop-template.md). State the descriptor
block prominently at the top of the Hero section so `shot-prompt` and `image-edit` can
locate and paste it verbatim without scanning the whole document.

**Image folder:** `assets/prop/{name}/` — use the asset taxonomy filenames exactly
(guide-asset-reference §9):

- Hero: `prop-{name}-hero.png`
- Ortho ring: `prop-{name}-ortho-front.png`, `-ortho-back.png`, `-ortho-side-l.png`,
  `-ortho-side-r.png`, `-ortho-top.png`
- Details: `prop-{name}-detail-01.png`, `-detail-02.png`, etc.
- State variants: state suffix appended — `prop-{name}-hero-aged.png`, `-hero-damaged.png`
- 360 (optional): `prop-{name}-360-000.png`, `-360-030.png`, etc.

All filenames are lowercase ASCII kebab-case. Image filenames carry **no `{show}`
prefix** — the show code lives only in the spec filename. A version suffix (`-v02`,
etc.) is optional but recommended once the asset enters shot production. Confirm the
output paths aloud before saving — the user's working folder, not the repo.

## Critical rules

1. **Anchor before fan-out.** No orthographic view, detail, or state generates until
   the hero anchor is approved.
2. **Hold form, scale, and lens across views.** Camera distance and apparent object
   scale must be visually identical across the ring — drift here reads as different
   objects, not different angles.
3. **Pin material, finish, and hex.** "Worn brass" is vague; "brushed brass `#B5A642`,
   mild tarnish at seams" is a lock. Vague language drifts immediately.
4. **Edit, don't regenerate, for state progressions.** Aged, damaged, soiled — always
   edit from the prior state at low denoise; regenerating from the hero breaks the
   progression fingerprint.
5. **Multiples must match.** Every instance of a prop in the same frame is derived from
   the same hero anchor at the same reference strength.
6. **Binaries to the user's folder only.** Images and spec files go to the user's
   working folder; nothing writes to the plugin repo.
7. **Verify counts vs currency.** Reference count and strength limits are
   version-sensitive — check `model-currency-2026-06` before advising any specific
   value.
