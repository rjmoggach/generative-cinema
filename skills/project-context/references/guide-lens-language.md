# Lens Language — Focal Length & Optics as Intent

The lens is a psychological instrument, not just a framing tool. Two shots of the
same size feel completely different on a 24mm vs. an 85mm. This guide encodes the
*why* so lens choice becomes deliberate. Drives Layer 5 in `shot-prompt` and the
camera/lens section of a `project-context`.

Format: **Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The two things a lens controls

1. **Perspective / spatial feel** — set by focal length (and camera distance),
   independent of how much fits in frame. Wide lenses *expand* space and
   exaggerate depth; long lenses *compress* it and flatten depth.
2. **Selective focus / depth of field** — longer focal length and wider aperture
   = shallower DOF (isolates subject); shorter focal length / smaller aperture =
   deeper DOF (everything legible).

Choose the lens for the *feeling of space* and *what's in focus*, then frame.

---

## 2. Focal-length psychology

| Lens | Spatial effect | Feeling it creates | Reach for it to… |
|---|---|---|---|
| Ultra-wide (≤18mm) | Extreme depth, edge distortion | Unease, vertigo, grandeur | Disorient; make a space vast or warped |
| Wide (24–35mm) | Expanded space, immersive | Energy, inclusion, instability | Put viewer *inside* the action/environment |
| Normal (40–58mm) | Human-eye perspective | Neutral, honest, relatable | Disappear; let performance speak |
| Short tele (85–135mm) | Compression, isolation | Intimacy, longing, scrutiny | Flatter a face; isolate from background |
| Long tele (200mm+) | Heavy compression, flattening | Voyeurism, fate, tension | Spy on a subject; stack distance; trap them |

### Wide for inclusion and unease

- **Use when:** the environment is a character, or you want instability/power.
- **Because:** wide lenses stretch space and exaggerate movement toward/away from
  camera; faces near the lens distort, which reads as intensity, threat, or
  comic energy. A hallway gets longer and more ominous.
- **Prompt translation:** "24mm wide-angle, deep depth of field, immersive,
  slight edge distortion"; pair with a low angle for dominance.
- **Watch-outs:** wide + close = facial distortion; intentional for unease,
  unflattering otherwise. AI models may over-warp on ultra-wide.

### Telephoto for isolation and intensity

- **Use when:** a character is alone in a crowd, observed, or emotionally walled off.
- **Because:** compression flattens the subject against a soft background and
  slows the feeling of motion, concentrating attention on expression. It also
  literally separates them from their surroundings.
- **Prompt translation:** "135mm telephoto, shallow depth of field, compressed
  background, subject isolated in soft bokeh".
- **Watch-outs:** compression kills depth cues — don't use when geography matters.

### Normal for honesty

- **Use when:** you want the technique invisible and the performance central.
- **Because:** ~50mm approximates human vision; nothing about the space editorial-
  izes the moment, so the audience engages with the character directly.
- **Prompt translation:** "50mm, natural perspective, medium depth of field".

---

## 3. Depth of field as a narrative choice

- **Shallow DOF** isolates: the world melts away, attention is forced onto one
  plane. Reads as subjective, intimate, lyrical. *Use when* one thing matters.
- **Deep DOF** informs: foreground and background are both legible, letting the
  audience read relationships across space (classic for staging in depth). *Use
  when* the composition tells the story (a figure small against what looms behind).
- **Rack focus** moves the *attention* between planes within a shot — a focus pull
  is an edit inside a single frame; use it to redirect the eye on a beat.
- **Prompt translation:** state aperture and intent — "f/1.8 shallow, background
  dissolved to bokeh" vs. "f/8 deep focus, foreground and background both sharp".
- **Anchors:** Mercado (DOF and focal-length relationship), deep-staging directors
  (Welles, Cuarón); see `reference-visual-*.md`.

---

## 4. Lensing by emotion and genre (starting points)

- **Romance / nostalgia:** short tele (85mm), shallow DOF, soft, compressed.
- **Horror / dread:** wide on tight spaces, low angle, deep focus to hide threats
  in the frame; occasional ultra-wide for distortion.
- **Action / immersion:** wide (24–35mm), deep focus, camera close to motion.
- **Thriller / surveillance:** long tele, compression, subject "watched" from afar.
- **Epic / awe:** wide for landscape grandeur; anamorphic for scope and flares.
- **Comedy:** wide-ish, deeper focus, faces readable; distortion for absurdity.

### Format flavor

- **Anamorphic** — wide scope (≈2.39:1), oval bokeh, horizontal flares, slight
  edge stretch; reads as "cinematic/epic". *Prompt:* "anamorphic, horizontal lens
  flares, oval bokeh".
- **Spherical** — clean, neutral, naturalistic. *Prompt:* "spherical lens".
- **Fisheye** — extreme spherical distortion; novelty, subjectivity, chaos.
- **Macro** — extreme close detail with razor-thin focus; insert/texture work.

---

## 5. Quick selection table

| Intent | Lens | DOF | Note |
|---|---|---|---|
| Make a place overwhelming | 18–24mm | Deep | low angle amplifies |
| Disappear into performance | 50mm | Medium | the "honest" choice |
| Isolate an emotion | 85–135mm | Shallow | compression + bokeh |
| Watch from outside | 200mm+ | Shallow | voyeurism, fate |
| Read a relationship in depth | 28–35mm | Deep | stage front-to-back |
| Epic scope | anamorphic wide | varies | flares, 2.39:1 |

Pair with `guide-shot-selection.md` (which size, why) and respect the
`project-context` lens spec so a show's optical signature stays consistent.
