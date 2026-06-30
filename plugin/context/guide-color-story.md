# Color as Story

Color is the fastest emotional channel in the frame. This guide moves the palette
section from *what colors* to *what the colors mean and do*. Use it in
`project-context` (palette/grading) and `shot-prompt` (Layer 4). It is the
in-depth "color knob" referenced by `guide-visual-structure.md`.

Format: **Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The three properties you control

Every color decision is hue, saturation, and value (brightness). Intensity comes
from *contrast* in any of them (see `guide-visual-structure.md`):

- **Hue** — the color itself; carries association (red = passion/danger, blue =
  calm/cold/sadness, green = nature/unease, amber = warmth/nostalgia).
- **Saturation** — purity. High = vivid, heightened, stylized; low/desaturated =
  grim, realistic, bleak, memory.
- **Value** — light/dark. Drives tonal contrast and mood (see lighting).

> **Tip:** Naming a target in all three ("desaturated teal, low-key") is far more
> controllable than naming a hue alone.

---

## 2. Color schemes and their feel

| Scheme | Relationship | Feeling | Reach for it to… |
|---|---|---|---|
| **Monochromatic** | One hue, varied value/sat | Unified, lulling, immersive | Total harmony or oppressive single mood |
| **Analogous** | Neighbors on the wheel | Harmonious, sympathetic, calm | Comfort, nature, cohesion |
| **Complementary** | Opposite hues | Tension, duel, vibrancy | Conflict; the classic teal/orange pop |
| **Triadic** | Three evenly spaced | Balanced but lively | Playful, energetic, evenly matched |
| **Split-complementary** | One hue + two near its opposite | Tension with less harshness | Contrast that still feels designed |

- **Use when:** setting a project palette or a scene's color contrast level.
- **Because:** the *relationship* between colors carries as much meaning as the
  hues. Complementary = embattled; analogous = kindred; mono = undivided.
- **Prompt translation:** state the scheme and the anchor hues: "complementary
  teal/orange grade, crushed blacks" or "analogous amber-to-ochre, warm".
- **Watch-outs:** AI grades drift; restate the scheme every shot and put it in the
  standard prompt prefix so cuts match.
- **Anchors:** see `reference-visual-*.md` (Deakins, Khondji, Storaro).

---

## 3. Color as narrative device

### Associative color (a hue tied to a character/theme)

- **Use when:** you want color to track a person, idea, or emotional thread.
- **Because:** a recurring hue becomes a memorable, wordless cue; its arrival or
  loss signals story without dialogue (e.g., a character's wardrobe darkening as
  they corrupt).
- **Prompt translation:** assign the hue in `project-context` ("ANTAGONIST: cold
  cyan, #1FB8C4, wardrobe + practicals") and reuse it in every relevant shot.

### Transitional / shifting color

- **Use when:** marking change over a scene or arc.
- **Because:** a palette that warms or cools across a sequence externalizes an
  emotional turn; a sudden hue change is a visual accent.
- **Prompt translation:** ramp the grade across the shot list (e.g., neutral →
  warm into a reconciliation; drain saturation toward a death/defeat).

### The "color script" (palette across the whole piece)

- **Use when:** planning a project, not a shot.
- **Because:** mapping each scene's dominant palette against the story beats keeps
  color *structural* — contrast between sequences becomes meaningful, and the
  climax can land on its own signature palette.
- **Prompt translation:** add a per-sequence palette row to the
  `project-context` sequence breakdown; treat it as a constraint when generating.

---

## 4. Warm/cool and temperature contrast

- Warm advances and feels intimate/energetic/dangerous; cool recedes and feels
  calm/cold/isolating. **Warm/cool contrast within a frame** (warm key, cool
  shadow/background) creates depth and separates the subject — the workhorse of
  modern grading.
- **Prompt translation:** "warm 3200K key on subject, cool 5600K ambient
  background, teal shadows" — specify both poles, not just one.

---

## 5. Quick application

1. Pick the **scheme** for the project (sets baseline harmony/tension).
2. Decide **saturation/value** mood (vivid vs. desaturated, high vs. low key).
3. Assign any **associative hues** to characters/themes.
4. Plan **transitions** where the story turns; reserve the most charged palette
   for the peak.
5. Encode the baseline in the **standard prompt prefix**; restate per shot to
   hold continuity.

Companion guides: `guide-visual-structure.md` (color as one intensity knob),
`reference-film-grammar.md` (lighting/tone), `reference-visual-*.md` (anchors).
