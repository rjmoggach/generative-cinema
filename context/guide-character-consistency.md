# Character Consistency (Technical Face, Wardrobe & HMU Craft)

This is the **character-specific technical** guide — how to build a hero identity reference,
write a locking descriptor block, manage drift, and build wardrobe and HMU state libraries.
The **general spine** (anchor-then-fan-out, two-block prompting, effective reference counts,
the asset taxonomy) is in `guide-asset-reference.md`; the **creative craft** (casting
instincts, costume design principles, makeup-and-hair discipline) is in
`reference-craft-character.md`; the **derive engine** (inpaint, denoise dial, state
progression) is in `guide-image-editing.md`. Do not duplicate those here — cross-reference
them.

Each entry uses the library's decision-unit format:
**Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The hero identity reference

- **Use when:** starting any character asset — before writing a descriptor, before generating
  any scene. This is the first file in the character folder, full stop.
- **Because:** the anchor portrait is the single most load-bearing asset in the character
  pipeline. Every downstream view, state, and shot derives from it. A strong anchor
  constrains the model toward a fixed face; a weak one propagates its weaknesses into every
  derivative and cannot be corrected cheaply after the fact.
- **Prompt translation:** generate one **front-facing, neutral-expression, evenly lit,
  high-res portrait on a plain neutral background** — no angle, no strong emotion, no
  dramatic light, no busy setting. The model reconstructs the face from this image; it must
  show every feature in full fidelity. Filename: `char-{name}-id-front.png` (see
  `guide-asset-reference.md` §9 for the full asset taxonomy and naming convention).
- **Watch-outs:**
  - **Angled anchors** (3/4, profile) hide half the face and degrade cheek, ear, and jaw
    consistency on every derivative.
  - **Expressive anchors** (strong smile, squint, grimace) bake an expression into the
    identity — neutral or contrasting expressions will drift toward it.
  - **Low-res anchors** starve the model of micro-detail (skin texture, iris colour,
    freckle placement); the model interpolates and drifts.
  - **Cluttered backgrounds** leave edge definition ambiguous, making silhouette
    inconsistent across shots.
  - Get the anchor right before fanning out — correcting it means re-deriving every
    downstream asset.
- **Anchors:** VFX hero-scan methodology (the locked, neutral, full-fidelity capture that
  feeds every downstream department); `guide-asset-reference.md` §1 (anchor, then fan out).

---

## 2. The descriptor block (50-80 words, verbatim)

- **Use when:** writing a character spec for any figure who appears in more than one shot.
- **Because:** a verbatim identity block, reused across every prompt without paraphrase, is
  the cheapest and most reliable drift lock available. If the block changes — even slightly —
  the model is free to re-interpret identity. The block must be **self-contained**: a reader
  with no visual reference should be able to reconstruct the face, body, and locked look from
  the text alone.
- **Prompt translation — what to include:** face (structure, skin tone with Fitzpatrick
  qualifier, eye colour and shape, distinctive marks), hair (length, texture, colour — hex
  mandatory), body (build, height register), locked wardrobe (garment names, silhouette, hex
  per piece), accessories, HMU baseline (foundation level, any standing SFX), distinctive
  marks (tattoos, scars, freckles — pinned by position, side, size, hex). Copy this block
  **verbatim** into every prompt that features the character; never paraphrase.
- **Example block (~60 words):**

  > Late-30s woman; angular jaw, high cheekbones, warm olive skin (Fitzpatrick III);
  > amber-brown irises, heavy upper lids; small crescent scar below left eyebrow. Dark brown
  > hair (#2b1a0e), shoulder-length, loose waves. Lean athletic build, 170 cm. Worn olive
  > field jacket (#4a5240), straight-leg cargo trousers (#2e2d28), scuffed tan boots. No
  > foundation; faint freckle scatter across nose bridge.

- **Watch-outs:** hex codes are mandatory for any colour that must hold (hair, garments, eye
  colour); garment names without silhouette allow the model to reinterpret cut; distinctive
  marks without position, side, and size drift in placement; "olive skin" without a Fitzpatrick
  qualifier allows a wide range. The block is immutable once locked — any edit is a
  continuity break.
- **Anchors:** `guide-asset-reference.md` §2 (two-block prompting: identity vs change);
  continuity-script discipline (the same physical description every shooting day).

---

## 3. Drift failure modes and fixes

All five patterns below share a root cause: the model lacks a specific, pinned constraint
and re-rolls the unconstrained element. The fix in every case is to add or tighten a
constraint — not to regenerate and hope.

| Failure | Cause | Fix |
|---|---|---|
| Face morphs across shots | Anchor is angled, expressive, or low-res; identity block is absent or vague | Re-generate the anchor (front, neutral, high-res); add the verbatim descriptor block; feed 4-6 references at ~0.7 reference strength |
| Wardrobe colour shifts | Hex codes absent; garment described by name only | Pin every colour in the descriptor block; append hex to every garment name in the prompt |
| Age / weight drift | Body-language or action cues in the scene block bleed into identity | Add explicit age and build anchors to the identity block; hold them constant across all shots; raise reference strength to ~0.7+ |
| Micro-detail loss (freckles, logos, insignia, small tattoos) | Models drop fine detail first under generation pressure; no dedicated reference | Add a close-up detail reference image; composite the detail in post if generation cannot hold it; see `guide-asset-reference.md` §6 |
| Light-key flip changes perceived identity | Switching the dominant key direction alters shadow placement and perceived bone structure | Hold one dominant key direction per scene; state it explicitly in the scene block; do not rely on the model to infer it — see `guide-asset-reference.md` §6 and `guide-image-editing.md` §5 |

---

## 4. Wardrobe-state library

- **Use when:** a character wears a garment across multiple shots where the garment's
  condition changes — not its identity.
- **Because:** wardrobe states (clean, wet, damaged, day-1, day-2) are distinct, independently
  lockable assets, not regenerated variants. Each state needs its own reference image so the
  model reconstructs from a known prior, not from an open interpretation of the descriptor.
- **Prompt translation:**
  - Lock every garment with **name + silhouette + hex** in the descriptor block: `worn olive
    field jacket (#4a5240), relaxed boxy silhouette, patch pockets` — not `olive jacket`.
    Silhouette is the constraint that prevents the model from reinterpreting cut.
  - Define states explicitly and give each a filename following the asset taxonomy:
    `char-{name}-fit-day1.png`, `char-{name}-fit-day1-wet.png`,
    `char-{name}-fit-day2-damaged.png` (see `guide-asset-reference.md` §9).
  - **Progress states by editing the prior state**, never by regenerating from scratch.
    Day-1-wet is an i2i edit of day-1-clean at low-moderate denoise (~0.3–0.45) — this
    preserves fabric texture, garment shape, and the specific crease fingerprint of the
    original image. See `guide-image-editing.md` §4 (denoise dial) and §6 (state
    progressions).
  - Never jump more than one state in a single edit — progress incrementally: clean →
    lightly dirty → heavily soiled → torn. Each step locks the previous result as its source.
- **Watch-outs:** generating a "damaged" garment from scratch produces a different garment
  that happens to look damaged; editing from the clean state produces *this specific garment*
  in a damaged condition. The distinction matters for continuity.
- **Anchors:** `guide-image-editing.md` §6 (edit for progressions); `guide-asset-reference.md`
  §7; wardrobe-continuity distressing chart.

---

## 5. HMU-state library

- **Use when:** a character's makeup, hair, or practical SFX condition changes across the
  story — wound progression, aging arc, wet or exhausted states.
- **Because:** HMU states are as lockable as wardrobe states. A wound re-rolled from scratch
  is a different wound. The position, side, size, and colour of every SFX element must be
  pinned and held across every shot in which it appears; any absent field is an invitation for
  the model to place or colour the element differently.
- **Prompt translation:**
  - Define a baseline and all variant states; give each a filename: `char-{name}-hmu-clean.png`,
    `char-{name}-hmu-wound-01.png`, `char-{name}-hmu-aged.png`.
  - Pin every SFX element with full specificity: `2 cm laceration, inner left eyebrow to upper
    lid, fresh blood (#b03a2e), slight surrounding swelling.` Position (which feature), side
    (left / right), size (cm), and hex are all required.
  - **Progress wounds by editing the previous state:** fresh → scabbed → scarred is three
    successive i2i edits (mechanism B, masked inpaint), not three independent generations. Run
    each edit at low denoise (~0.2–0.3) to isolate the SFX region while holding the face.
    See `guide-image-editing.md` §3-B and §6.
  - Treat an aged state as a **new anchor** — lock it separately and store it as its own
    reference if it recurs. See `guide-image-editing.md` §6 (age-a-face pattern).
  - The creative principles behind HMU design — aging anatomy, wound storytelling, prosthetic
    continuity — are in `reference-craft-character.md` (Makeup & Hair section); this guide
    covers only the technical locking method.
- **Watch-outs:** `healing` as a descriptor is vague — name the stage (`scabbed`,
  `hypertrophic`, `flat scar`); `bruise` without a hex range allows the model to interpret
  severity. Hair-state changes (cut, dye, wet) follow the same edit-from-prior-state rule as
  wounds.
- **Anchors:** `guide-image-editing.md` §6; `reference-craft-character.md`; practical
  makeup-and-hair continuity bible (position photograph + written note per element).

---

## 6. Reference vs LoRA — the gate for faces

The plugin advises on this decision; it does not train LoRAs. The gate must be set before
generating any scene work for the character.

- **Use when:** deciding the lock strategy for any character who will appear on screen.
- **Because:** reference images alone deliver perceptual consistency (~65–75%); a trained LoRA
  combined with a fixed descriptor block reaches near-identity (~85–92%). The gap matters for
  leads who carry the show; it is irrelevant for one-offs. The cost — curated training images,
  training compute, trigger-word management — only amortises over many shots. See
  `guide-asset-reference.md` §3 for the general reference-vs-LoRA decision.
- **Prompt translation — the character-specific gate:**
  - **Background / one-off (≤ ~1 scene):** reference only. 4-6 anchor images at ~0.7 reference
    strength + verbatim descriptor. No LoRA.
  - **Supporting recurring character (few scenes):** reference only, but with denser angle
    coverage — 6 images spanning front, 3/4-L, 3/4-R, and side — plus verbatim descriptor.
  - **Recurring hero (many shots or multi-episode):** reference + trained LoRA + fixed
    descriptor block. **Record the LoRA trigger word in the character spec file** (e.g.,
    `trigger_word: eliana_sbw_v1`) — this is required so any agent or user generating for
    that character activates identity correctly without guessing. Changing the trigger word
    after locking breaks all prior prompts that used it.
- **Watch-outs:** do not train a LoRA for a character who appears in one scene — the cost is
  unjustified and the trigger word adds management overhead with no continuity benefit. Do not
  rely on a bare reference for a lead who carries the show — drift will compound across many
  shots and will not be recoverable without the LoRA.
- **Anchors:** `guide-asset-reference.md` §3 (reference for speed, LoRA for scale);
  cost-aware production planning.

---

## Quick application

1. Generate the **hero identity reference** first: front-facing, neutral expression, even
   light, high-res, neutral background — stored as `char-{name}-id-front.png`.
2. Write the **verbatim descriptor block** (50-80 words, hex-pinned for every colour that
   must hold) and store it in the character spec file.
3. Set the **reference-vs-LoRA gate**: one-off → reference only; recurring hero → reference +
   LoRA + record the trigger word in the spec file.
4. Build the **wardrobe-state library**: lock each garment by name + silhouette + hex; define
   states (clean / wet / damaged / day-1 / day-2); progress each state by editing the prior,
   never regenerating.
5. Build the **HMU-state library**: pin every SFX element by position + side + size + hex;
   progress wounds (fresh → scabbed → scarred) through successive masked inpaints at low
   denoise.
6. **Hold the light-key** direction across all shots featuring this character; a flipped key
   changes perceived identity.
7. When drift appears, **do not regenerate** — identify which constraint is absent and add it.

**Companion guides:** `guide-asset-reference.md` (anchor, fan-out, two-block prompting, LoRA
gate, asset taxonomy) · `reference-craft-character.md` (casting, costume, and
makeup-and-hair creative craft) · `guide-turnaround-sheets.md` (multi-angle coverage and
turnaround methodology) · `guide-image-editing.md` (derive engine: inpaint, denoise dial,
state progressions).
