# Turnaround Sheets (Model-Sheet View-Set & Alignment Craft)

This is the **model-sheet technical** guide — how to build a geometry-true turnaround
from the hero anchor via `image-edit`, hold alignment lines across all six views, and
extend into companion sheets. The **hero anchor** (front-facing, neutral expression,
evenly lit portrait) is generated per `guide-character-consistency.md` §1; the
**anchor-then-fan-out discipline** — the spine of all asset building — lives in
`guide-asset-reference.md` §1; the **derive engine** (denoise dial, i2i mechanisms,
state progressions) is in `guide-image-editing.md`. Do not duplicate those here —
cross-reference them.

Each entry uses the library's decision-unit format:
**Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The view set

- **Use when:** building a turnaround sheet for any character who needs multi-angle
  reference coverage — supporting recurring characters and above.
- **Because:** a turnaround gives downstream work (LoRA training, costume verification,
  staging reference, blocking) a geometry-true picture of the character from every angle
  that will appear on screen. Without it, each off-axis shot is an independent guess at
  what the character looks like from that direction; with it, every off-axis shot derives
  from a locked prior.
- **Prompt translation:** the standard six views, mapped to their `turn` facet filenames
  from the asset taxonomy (see `guide-asset-reference.md` §9):

  | View | Filename | What it shows |
  |---|---|---|
  | Front (= the anchor) | `char-eli-turn-front.png` | Full face, front garment panels, front silhouette |
  | Left profile | `char-eli-turn-side-l.png` | Nose-tip projection, ear placement, left garment edge, front-to-back silhouette |
  | Right profile | `char-eli-turn-side-r.png` | Same as side-l from the right |
  | Back | `char-eli-turn-back.png` | Occiput, back of hair, rear garment panels, shoe heels |
  | Three-quarter left | `char-eli-turn-3q-l.png` | Face at ~45°; bridges front identity to left profile |
  | Three-quarter right | `char-eli-turn-3q-r.png` | Same from the right |

  The front view is the **anchor** — it is not re-generated for the turnaround. Use the
  hero identity reference already stored as `char-eli-id-front.png` (or generate one per
  `guide-character-consistency.md` §1), then copy or symlink it to
  `char-eli-turn-front.png` to make the turnaround set complete. All other five views are
  derived from the anchor.
- **Watch-outs:** do not skip the back view — rear garment silhouette and hair back-mass
  are the most common continuity gaps in downstream shots. Do not add top-down or
  worm's-eye views unless the production specifically requires them; they fall outside the
  standard six and disrupt the alignment grid.
- **Anchors:** traditional character model-sheet convention (six orthographic views: front,
  side-l, side-r, back, 3q-l, 3q-r); `guide-asset-reference.md` §9 (asset taxonomy and
  naming convention).

---

## 2. Alignment lines

- **Use when:** generating or reviewing any view in the turnaround set.
- **Because:** a turnaround sheet is usable as a multi-angle reference only when the
  character occupies the same vertical position and scale in every view. If the character
  is taller in the front view than in the side view, proportions cannot be taken across
  views and the sheet fails as a measurement reference. If lighting is directional, shadow
  geometry shifts the perceived silhouette from view to view. The alignment discipline is
  what turns six separate images into one coherent sheet.
- **Prompt translation:** hold five horizontal guide lines constant across all views —
  stated explicitly in every turnaround-view prompt:
  - **Eye line** — top reference; anchors face position across views
  - **Shoulder line** — width reference; marks torso top
  - **Waist line** — torso bottom; lapel, belt, and waistband placement
  - **Knee line** — trouser or skirt break; leg proportion
  - **Foot line** — ground contact; the baseline for all measurements

  Three compositional requirements to state in every view prompt:
  1. **Neutral A-pose** — arms hanging slightly away from the body, feet at roughly
     shoulder width, no action, no tilt, no gesture. The A-pose keeps the silhouette
     readable and garment fall consistent across views.
  2. **Even, flat diffuse lighting** — no directional key light, no hard shadow. Diffuse
     light shows silhouette and surface uniformly without baking a particular lighting
     state that downstream shots must then match.
  3. **Plain neutral background** — low-contrast mid-grey or white, no environment, no
     props. The background must not compete with the character's edge definition.
- **Watch-outs:** a directional key on a turnaround view is not merely an aesthetic
  choice — it introduces shadow geometry that is inconsistent between views (shadow
  falls forward on the front view; falls sideways on the profile). This is the most
  common reason a turnaround set fails as a reference. Hold diffuse light for all six
  views; dramatic light belongs in the scene block of individual shots, not on the
  reference sheet.
- **Anchors:** orthographic technical illustration convention; animation production
  model-sheet standards (consistent ground-plane and horizon across all views).

---

## 3. Derive from the anchor, never independently

- **Use when:** generating any of the five non-anchor turnaround views.
- **Because:** generating each view independently produces siblings — characters who
  resemble each other but are not the same person. Nose-tip projection, ear placement,
  shoulder width, and garment silhouette all drift if each view starts from zero. Deriving
  every view from the anchor via `image-edit` gives the model a fixed thing to reconstruct
  from; it changes the angle, not the identity. This is the anchor-then-fan-out principle
  applied to the turnaround context — see `guide-asset-reference.md` §1 for the full
  treatment.
- **Prompt translation:**
  - Use **full-frame i2i with the denoise dial** (mechanism C from `guide-image-editing.md`
    §3-C) for every derived turnaround view.
  - Set denoise at **low-to-moderate: ~0.3–0.5**. This range permits the model to rotate
    the subject without severing its connection to the anchor identity. See
    `guide-image-editing.md` §4 for the full denoise-strength dial reference.
  - Hold the **descriptor block verbatim** in every edit prompt — identity block constant,
    rotation instruction in the scene block only. See `guide-character-consistency.md` §2
    for the descriptor block method.
  - Rotation instruction in the scene block only: `"left profile, same A-pose, even
    diffuse lighting, plain neutral background"`. Do not alter the identity block.
  - **Back view — special case:** no face is visible; identity comes entirely from the
    descriptor block and the body/garment/hair. State explicitly: `"rear view, same
    character, face not visible; show back of hair, rear garment panels, shoe heels; same
    A-pose, even diffuse light, neutral background."` Hold every garment descriptor
    verbatim.
  - **Three-quarter views and LoRA training:** the 3q-l and 3q-r views bridge the front
    identity to the profiles. They are the highest-value views for LoRA training image
    sets because they show the face at an angle that neither the front anchor nor the pure
    profiles can cover individually.
- **Watch-outs:**
  - Do not raise denoise above ~0.5 for turnaround views — identity risk climbs sharply
    above that threshold. If the rotation didn't fully take at ~0.4, sharpen the rotation
    instruction before raising denoise.
  - Always derive from the **front anchor** — not from a previously derived side or back
    view. Chaining edits (front → side → back) compounds drift at each step.
  - Side views expose nose-tip projection and ear placement. If either drifts, the view is
    unusable as a multi-angle reference; re-derive at lower denoise.
- **Anchors:** `guide-asset-reference.md` §1 (anchor-then-fan-out); `guide-image-editing.md`
  §3-C and §4 (mechanism C and denoise dial).

---

## 4. Companion sheets

Three companion sheets extend the turnaround. Each must inherit the turnaround's even
diffuse lighting and consistent scale — they live alongside the turnaround in the
reference set and must read as visually coherent with it.

- **Expression sheet**
  - **Use when:** the character has dialogue, reaction shots, or any emotional arc.
  - **Because:** expressions are states of the face, not the identity — but generating
    them independently from scratch re-rolls the facial fingerprint. Deriving expressions
    from the front anchor via single-attribute edit preserves structure while permitting
    the expression change.
  - **Prompt translation:** 4–6 expressions (neutral / slight smile / full smile / frown /
    surprise / anger); mechanism A from `guide-image-editing.md` §3-A (single-attribute
    conversational edit) at very low denoise (~0.2–0.3); change only the expression
    descriptor; hold face structure and descriptor block verbatim. Filename pattern:
    `char-eli-id-expr-smile.png`, `char-eli-id-expr-frown.png`.
  - **Watch-outs:** strong expressions distort face structure at higher denoise — stay at
    ~0.2–0.3 and name the expression precisely (`"open smile, teeth visible, eyes
    crinkled"`) rather than relying on the model to interpret a vague affect like `"happy"`.

- **Pose sheet**
  - **Use when:** the character is action-heavy, or the production needs to verify
    silhouette and garment fall in motion poses.
  - **Because:** poses alter garment drape, limb occlusion, and silhouette in ways the
    A-pose turnaround cannot show. A pose sheet provides locked reference for these states.
  - **Prompt translation:** 4–6 standing or action poses derived from the front anchor
    at moderate denoise (~0.4–0.5) — higher than expression edits because the body
    position changes more extensively. Hold the descriptor block verbatim; add only the
    pose description in the scene block. Filename pattern: `char-eli-pose-walk.png`,
    `char-eli-pose-reach.png`.
  - **Watch-outs:** pose sheets are harder to lock than expression sheets — moderate
    denoise brings more identity risk. If the face drifts, add a close-up face reference
    alongside the anchor as a secondary reference at the same step.

- **Palette / callout sheet**
  - **Use when:** beginning any character's reference set — build it for every hero
    character.
  - **Because:** the palette/callout sheet is the living hex-reference document for every
    future prompt and revision. It makes the verbatim descriptor block visually
    auditable — someone can verify hex codes against the actual rendered swatches.
  - **Prompt translation:** this is a **design document**, not a generation artifact.
    Compose the front turnaround view with annotated swatches and hex codes for every
    locked colour: skin tone (with Fitzpatrick qualifier), hair, every garment piece,
    accessories, and any standing SFX (wound colour, prosthetic colour). Filename:
    `char-eli-palette.png`.
  - **Watch-outs:** the palette sheet must stay in sync with the descriptor block. If a
    hex code changes in the descriptor, update the palette sheet immediately — a stale
    palette creates false confidence in wrong values, which is worse than no palette.

---

## 5. Reference counts

- **Use when:** assembling the finished turnaround set to use as references in downstream
  shot prompts or LoRA training image sets.
- **Because:** the turnaround's value as a reference set lies in multi-angle coverage of
  the same locked identity. The consistency sweet spot — the range where adding views
  still improves identity hold without muddying it — is the same effective-reference-count
  window that applies to all asset types.
- **Prompt translation:** ~**4–6 turnaround views** at reference strength ~**0.7** is the
  working target (workable range: 0.6–0.8). A complete six-view turnaround sits at the
  top of that window. If model limits require trimming, drop the back view before the
  three-quarter views — the 3q views carry higher identity reconstruction value. See
  `guide-asset-reference.md` §4 for the full effective-reference-count and strength
  guidance.
- **Watch-outs:** per-model limits (maximum reference images per prompt, multi-character
  reference limits) are **version-sensitive**. Verify current limits against
  `model-currency-2026-06.md` before hard-coding a count. The 4–6 / ~0.7 numbers are the
  target; the model doc is the ceiling.
- **Anchors:** `guide-asset-reference.md` §4 (effective reference counts; strength
  ~0.6–0.8); `model-currency-2026-06.md` (per-model current limits).

---

## Quick application

1. Generate or locate the **hero identity reference** (`char-eli-id-front.png`) per
   `guide-character-consistency.md` §1; this is `char-eli-turn-front.png` — the anchor
   of the turnaround.
2. Set **alignment requirements** for all derived views: neutral A-pose, even flat diffuse
   light, plain neutral background, consistent scale.
3. Derive the **five remaining views** via `image-edit` (mechanism C, denoise ~0.3–0.5),
   holding the descriptor block verbatim in every prompt — never generate views
   independently:
   `char-eli-turn-side-l.png` / `char-eli-turn-side-r.png` / `char-eli-turn-back.png` /
   `char-eli-turn-3q-l.png` / `char-eli-turn-3q-r.png`.
4. Check alignment across the six views: eye, shoulder, waist, knee, and foot lines
   should be visually consistent. Any view that is perceptibly taller or shorter must be
   re-derived.
5. Build **companion sheets** as warranted: expression sheet (dialogue-heavy characters);
   pose sheet (action characters); palette/callout sheet (every hero character — build
   this one first).
6. Assemble the finished set as downstream references at ~**0.7 strength**, ~**4–6
   views**; verify the per-model ceiling against `model-currency-2026-06.md`.

**Companion guides:** `guide-character-consistency.md` (hero identity reference §1;
descriptor block §2; drift locks §3) · `guide-asset-reference.md` (anchor-then-fan-out
§1; effective reference counts §4; asset taxonomy §9) · `guide-image-editing.md` (i2i
mechanisms §3; denoise dial §4).
