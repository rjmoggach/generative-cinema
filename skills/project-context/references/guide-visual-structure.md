# Visual Structure — Intensity, Contrast & Affinity

The single most useful idea for making a *sequence* (not just a shot) feel right.
Based on Bruce Block's *The Visual Story*: every image is built from visual
components, and the **contrast or affinity** of those components controls **visual
intensity** — which should rise and fall *with the story*. Use this in
`project-context` to set a show's intensity strategy, and in `shot-prompt` to
plan a scene's arc.

Format: **Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The master principle: contrast vs. affinity

- **Contrast** (components differ strongly) = **higher visual intensity** =
  more energy, tension, drama.
- **Affinity** (components are similar) = **lower visual intensity** = calm,
  harmony, stillness.

Every visual choice can be dialed toward contrast or affinity. The skill is to
make **visual intensity track dramatic intensity**: open calm (affinity), build
to the climax (contrast), resolve (affinity). When the look fights the story —
a tense scene shot with total affinity — it feels flat or "off" without the
viewer knowing why.

> **Tip:** This is the *why* behind the intensity arc in
> `guide-sequence-construction.md`. That guide says "escalate intensity"; this one
> says *which knobs* to turn.

---

## 2. The seven visual components (the knobs)

Each can be pushed toward contrast (intensify) or affinity (settle):

| Component | Affinity (calm) | Contrast (intense) | Prompt levers |
|---|---|---|---|
| **Space** | Flat, frontal, shallow | Deep, diagonal, layered | lens, staging depth, perspective |
| **Line** | Few, aligned, horizontal | Many, opposed, diagonal | set/architecture, body lines, horizon |
| **Shape** | Repeated, similar | Mixed circle/square/triangle | composition, props, silhouettes |
| **Tone** | Narrow gray range, low contrast | Wide range, deep blacks/bright highs | lighting ratio, key/fill |
| **Color** | Analogous / monochrome | Complementary / wide hue range | palette, grade (see `guide-color-story.md`) |
| **Movement** | Slow, smooth, static | Fast, erratic, multi-directional | camera move + subject motion (Layer 3) |
| **Rhythm** | Even, predictable cuts | Uneven, accelerating cuts | shot duration, edit pace |

To **raise** a scene's intensity, push several components toward contrast at once;
to **release**, return them to affinity. Coordinated movement of multiple
components is what reads as a real shift.

---

## 3. Core decisions

### Set the project's intensity range

- **Use when:** defining a show in `project-context`.
- **Because:** a film has a baseline and a ceiling. A meditative drama might live
  in affinity and peak at "medium"; an action film lives hot. Establishing the
  range keeps every scene proportionate to the whole.
- **Prompt translation:** record a baseline (e.g., "mostly flat space, analogous
  palette, slow movement") and what the peaks look like; encode the baseline into
  the standard prompt prefix.
- **Watch-outs:** if every scene is maxed, the climax has nowhere to go.

### Build a scene's intensity arc

- **Use when:** planning any multi-shot scene.
- **Because:** the audience feels the *change* in intensity more than its absolute
  level. Design the curve: where it starts, where it peaks (the turn), where it lands.
- **Prompt translation:** assign each shot a target intensity and set the
  components accordingly — open wide/flat/slow/analogous, escalate into the turn
  with deeper space, diagonal lines, wider tonal range, faster movement, more
  saturated/complementary color, then resolve.
- **Anchors:** Block (*The Visual Story*); pairs with the intensity-arc step in
  `guide-sequence-construction.md`.

### Use contrast to direct the eye within a frame

- **Use when:** you want the viewer to look *here*.
- **Because:** the area of greatest local contrast (a bright face in shadow, the
  one red object, the one moving thing) wins attention. Composition is contrast
  management.
- **Prompt translation:** describe the subject as the point of maximum contrast
  (tonal, color, or movement) against an affinity-heavy surround.

### The principle of "visual continuum" across a cut

- **Use when:** sequencing shots so they relate.
- **Because:** if successive shots share affinity (similar tone/color/movement)
  they feel continuous; a deliberate contrast between shots creates a visual
  accent — the equivalent of a stress beat.
- **Prompt translation:** hold components steady across coverage for smoothness;
  introduce a sharp component change on the shot you want to *land*.

---

## 4. Quick application

1. Name the scene's **dramatic** arc (calm → turn → resolve).
2. Choose which **components** carry the intensity (often tone + movement + color).
3. Map each shot's **target intensity** and set those components to match.
4. Keep other components in **affinity** so the chosen ones read clearly.
5. Reserve maximum contrast for the **peak beat** only.

Companion guides: `guide-color-story.md` (the color knob in depth),
`guide-sequence-construction.md` (where the arc lives), `guide-shot-selection.md`
and `guide-lens-language.md` (size/space/movement levers).
