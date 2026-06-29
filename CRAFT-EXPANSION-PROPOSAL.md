# Craft Expansion Proposal — From Taxonomy to Decision Support

**Goal:** evolve the library from a *menu of cinematic options* into a *creative
support system* that augments an artist's judgment — encoding not just **what**
shots/lenses/moves exist, but **when**, **why**, and **how to translate intent
into a prompt**.

Researched June 2026. Sources at the end.

---

## 1. The core gap

The current `context/` library is strong on **taxonomy** and weak on
**decision rules**:

- `reference-film-grammar.md` exhaustively lists shot sizes, moves, angles,
  editing types, composition principles, dialogue staging, transitions.
- `reference-visual-*.md` catalog directors/DPs/photographers as style anchors.
- `guide-prompting-framework.md` defines the six layers as *fields to fill*.

What's missing is the connective reasoning a skilled DP carries in their head:

- **Shot selection logic** — *why* this size here, how scale escalates emotion.
- **Lens language** — *why* a 24mm threatens and an 85mm flatters; DOF as intent.
- **Sequence strategy** — how to *build a scene* (coverage, staging, intensity arc).
- **Spatial continuity** — the 180°/30°/eyeline rules (currently absent as actionable rules).
- **Visual structure** — contrast/affinity and visual intensity mapped to story.
- **Color as story** — schemes and associative color, not just a palette list.
- **Creative approach** — motivated camera, subjectivity, subtext, motif, intentional rule-breaking.
- **AI-generation reality** — how craft survives current model limits (continuity, drift).

A taxonomy answers "what could I do?" A decision-support system answers "what
*should* I do, and why?" — that's the leap that augments rather than just informs.

---

## 2. Design principle for every new doc

Each new reference should be written as **actionable heuristics**, not prose
essays, in a consistent unit:

```
Decision: <the choice the artist faces>
Use when: <intent / emotional or narrative trigger>   (IF)
Because: <the craft rationale — the "why" that builds judgment>   (WHY)
Prompt translation: <how to express it in a shot-prompt / six-layer terms>
Watch-outs: <failure modes, incl. AI-generation caveats>
Anchors: <director/DP/film exemplars from the reference library>
```

This format is what makes the content *teach* while it *assists*, and it plugs
directly into the `shot-prompt` and `project-context` skills.

---

## 3. Proposed new reference docs

Naming follows the existing `reference-*` / `guide-*` convention so files slot in
and the build manifest can bundle them per skill.

### P0 — highest leverage

**A. `guide-shot-selection.md` — Shot selection logic**
Psychological distance of each shot size (intimacy vs. observation); when to
push in vs. cut; emotional escalation through scale; coverage intent (what each
of establishing/master/CU/insert/reaction *does* for the audience); the
"prime/peak moment" principle. Grounds Mercado's *Why it works / How it works*
per shot and Mascelli's continuity of attention.
→ consumed by **shot-prompt** (drives Layer 2 choices and the sequence workflow).

**B. `guide-lens-language.md` — Lens & optical intent**
Focal-length psychology (wide = inclusion, distortion, unease, power; normal =
neutral/relatable; telephoto = compression, isolation, voyeurism, tension);
depth-of-field as narrative choice (shallow isolates, deep informs); lensing by
emotion and genre; anamorphic/fisheye intent. Replaces the thin "optical
distortions" bullet list with reasoning.
→ consumed by **shot-prompt** (Layer 5) and **project-context** (lens spec section).

**C. `guide-continuity-rules.md` — Spatial & continuity logic**
The 180° rule and axis of action; 30° rule; eyeline match; consistent screen
direction; entrances/exits; matching on action. **Currently absent as usable
rules** and *doubly important for AI*, where multi-shot coherence is fragile —
encoding screen direction and eyelines into prompts is how you keep a generated
sequence legible.
→ consumed by **shot-prompt** (sequence/coverage) and a future sequence skill.

**D. `guide-sequence-construction.md` — Scene & sequence strategy**
How to build a scene as a unit: coverage strategy (master + coverage vs.
fragmented vs. oner); Katz's A/I/L staging patterns; establishing→detail
progression; building an intensity arc across shots; "shoot for the edit";
intercutting and rhythm. Turns the existing shot-level workflow into scene-level
thinking.
→ consumed by **shot-prompt**; motivates a dedicated **sequence-design** skill (see §5).

### P1 — strong creative differentiators

**E. `guide-visual-structure.md` — Visual intensity (Bruce Block)**
Block's seven visual components (space, line, shape, tone, color, movement,
rhythm) and the master principle of **contrast vs. affinity** (contrast = higher
visual intensity, affinity = lower). Map visual intensity to story structure so
the *look* rises and falls with the *narrative*. This is the single biggest
conceptual upgrade — it gives the system a theory of *why a sequence feels right*.
→ consumed by **project-context** (defines a show's intensity strategy) and **shot-prompt**.

**F. `guide-color-story.md` — Color as narrative**
Color schemes and their feel (analogous = harmony; complementary = tension;
triadic = balanced vibrancy; monochromatic = lulling/unified); associative color
(a hue tied to a character/theme), transitional color, and the idea of a "color
script" across a project. Extends the palette section from *what colors* to
*what the colors mean*.
→ consumed by **project-context** (palette/grading) and **shot-prompt** (Layer 4).

**G. `guide-creative-approaches.md` — Authorial intent & technique**
Motivated camera (every move earns its narrative reason); objective vs.
subjective framing and the POV shot; visual subtext (how blocking/lensing carry
unspoken meaning); visual motif/repetition; and **intentional rule-breaking**
(when to break the 180°, go canted, use a jump cut — and the effect it buys).
This is where the system stops being a rulebook and starts supporting *voice*.
→ consumed by **project-context** (creative brief) and **shot-prompt**.

### P2 — bridges craft to the tools

**H. `guide-ai-generation-strategy.md` — Craft under current model limits**
How the above survives real 2026 model behavior: aim for **perceptual
continuity, not pixel-perfect identity**; prefer **reference images + locked
style + first/last frame** over text-only "character bibles"; sequence shots to
play to each model's strengths (per the currency file); the 5-10-1 cost-efficient
iteration loop; prompting screen-direction/eyelines to fight drift. This is the
unique connective tissue between film theory and generative practice — few
libraries have it.
→ consumed by **shot-prompt** and **model-docs**; pairs with `model-currency-*.md`.

---

## 4. Integration with the skills

| New doc | project-context | shot-prompt | model-docs | (new) sequence-design |
|---|:--:|:--:|:--:|:--:|
| A Shot selection | | ● | | ● |
| B Lens language | ● | ● | | ● |
| C Continuity rules | | ● | | ● |
| D Sequence construction | | ● | | ●● |
| E Visual structure | ●● | ● | | ● |
| F Color as story | ●● | ● | | |
| G Creative approaches | ●● | ● | | ● |
| H AI generation strategy | | ●● | ● | ●● |

`●● = primary owner`. After adding any doc, extend the `MANIFEST` in
`skills/build.py` so the relevant skill bundles it, then rebuild.

---

## 5. Optional: a 4th skill — `sequence-design`

The current `shot-prompt` skill operates at the **shot** level. Docs C/D/E imply a
**scene/sequence** level: plan coverage, set screen direction and the intensity
arc, then hand a shot list to `shot-prompt`. The original repo already hinted at
this (`prompts/system-prompt-sequence-context-assistant.md`,
`template-sequence-context.md`). A `sequence-design` skill would sit between
`project-context` and `shot-prompt`:

```
project-context → sequence-design → shot-prompt → prompts
   (the look)     (the scene plan)   (each shot)
```

Recommend building it after P0 docs exist (it depends on C and D).

---

## 6. Suggested roadmap

1. **P0 (A–D).** Biggest immediate lift to `shot-prompt`; C and D also unlock the sequence skill.
2. **P1 (E–G).** Deepens `project-context` into a real creative brief; E is the marquee addition.
3. **P2 (H) + `sequence-design` skill.** Connect craft to tool reality and scene-level planning.

Each doc is ~150–250 lines in the heuristic format above. I can draft them with
the `model-docs`-style research rigor (cited, current) and wire them into the
build manifest as we go.

---

## 7. Sources

- Bruce Block, *The Visual Story* — seven visual components; contrast & affinity. https://www.routledge.com/The-Visual-Story-Creating-the-Visual-Structure-of-Film-TV-and-Digital-Media/Block/p/book/9781138014152
- Gustavo Mercado, *The Filmmaker's Eye* — per-shot Why/How it works; focal length & DOF. https://www.routledge.com/The-Filmmakers-Eye-Learning-and-Breaking-the-Rules-of-Cinematic-Composition/Mercado/p/book/9781138780316
- Steven D. Katz, *Film Directing: Shot by Shot* — coverage, staging, A/I/L patterns. https://mwp.com/product/film-directing-shot-shot-25th-anniversary-edition-visualizing-concept-screen/
- Focal length psychology. https://www.indepthcine.com/videos/focal-length · https://www.premiumbeat.com/blog/various-focal-lengths-for-images/
- Continuity rules (180°/30°/eyeline/screen direction). https://www.studiobinder.com/blog/what-is-continuity-editing-in-film/ · https://learnaboutfilm.com/film-language/sequence/180-degree-rule/
- Motivated camera / subjective POV / subtext. https://www.premiumbeat.com/blog/cinematography-tip-motivated-camera-movement/ · https://www.indepthcine.com/videos/objective-vs-subjective
- Color theory in film. https://www.studiobinder.com/blog/how-to-use-color-in-film-50-examples-of-movie-color-palettes/ · https://boords.com/blog/color-theory-in-film
- AI character/continuity reality (2026). https://magichour.ai/blog/how-to-keep-characters-consistent-in-ai-video · https://blog.mage.space/article/best-ai-video-generators-consistent-characters-2026/9459a229-806d-4a73-8abf-a19db645a248

Also already in `knowledge-base/`: Arijon *Grammar of the Film Language*,
Mascelli *Five C's of Cinematography*, Frost *Cinematography for Directors*,
Landau *Lighting for Cinematography*, Spottiswoode *A Grammar of the Film*,
Metz *Film Language* — primary sources these heuristics can cite directly.
