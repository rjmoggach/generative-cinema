# Shot Selection Logic

Decision rules for *which shot, when, and why*. The film-grammar reference lists
shot sizes; this guide gives the reasoning that turns the menu into judgment. Use
it to drive Layer 2 (composition/framing) and the sequence workflow in the
`shot-prompt` skill.

Each entry uses the library's decision-unit format:
**Decision / Use when / Because / Prompt translation / Watch-outs / Anchors.**

---

## 1. The master variable: psychological distance

Shot size is not about how much fits in frame — it is about **how close the
audience feels to the subject**. As the camera moves nearer, identification and
intimacy rise; as it pulls back, the audience becomes an observer and the subject
becomes part of a larger context. Choose size by the *relationship* you want the
viewer to have with the moment, then let "how much fits" follow.

| Shot | Felt relationship | Primary job |
|---|---|---|
| ELS / LS | Observer; subject dwarfed by world | Place, scale, isolation, context |
| FS / MFS | Witness; whole body, body language | Action, blocking, physical performance |
| MS / MCU | Conversational peer | Dialogue, gesture, everyday intimacy |
| CU | Confidant; private | Emotion, decision, reaction |
| BCU / ECU | Inside the moment; pressure | Micro-emotion, detail, tension |

---

## 2. Core decisions

### Picking the baseline size for a beat

- **Use when:** establishing how the audience should relate to this story beat.
- **Because:** size sets identification before any other choice. A confession
  played in LS reads as detached; the same line in CU implicates the viewer.
- **Prompt translation:** lead the prompt with the size and the intent, e.g.
  "Close Up, intimate and confessional" not just "Close Up".
- **Watch-outs:** don't default to MS for everything ("TV coverage" flatness).
  Pick size for *meaning*, then add coverage around it.
- **Anchors:** Mascelli (continuity of attention), Mercado (*why each shot works*).

### Escalating emotion through scale

- **Use when:** a scene needs to intensify (rising stakes, dawning realization).
- **Because:** progressively tighter framing across a scene raises pressure — the
  "approaching pattern". Each tighter cut tells the viewer *this matters more*.
- **Prompt translation:** build a shot list LS → MS → CU → BCU on the key
  performer; hold the tightest size on the turning point.
- **Watch-outs:** if you start tight you have nowhere to go; reserve the BCU.
- **Anchors:** Arijon (approaching/receding patterns).

### Push-in vs. cut-in

- **Use when:** you want to tighten on a subject.
- **Because:** a **cut** to a closer size is a punctuation — clean, energetic,
  the editor's emphasis. A **push-in (dolly/move)** is continuous — it feels like
  the audience *leaning in*, growing pressure within an unbroken moment.
- **Prompt translation:** cut = generate a separate tighter shot; push-in =
  describe "slow dolly push-in" within one shot (Layer 3).
- **Watch-outs:** in AI video, slow push-ins read cleaner than fast ones and
  hold subject identity better; sudden scale changes can cause drift.
- **Anchors:** Katz (moving camera), motivated-camera principle.

### Cutting wide for relief or context

- **Use when:** after sustained tightness, or to re-establish geography.
- **Because:** the audience needs to breathe and to know where things are; a wide
  release resets tension and re-anchors space (especially after intercut CUs).
- **Prompt translation:** insert an establishing/re-establishing LS that matches
  the scene's lighting and layout.
- **Watch-outs:** dropping wides entirely makes a scene claustrophobic and
  spatially confusing — sometimes intended, usually not.

---

## 3. Coverage intent — what each shot *does* for the scene

A scene is built from shots with distinct jobs. Generate with intent, not habit:

- **Establishing shot** — answers *where/when*. Sets geography, light, mood,
  scale. First in a sequence; revisit to re-orient.
- **Master shot** — the spatial spine. Whole action in one wide-ish frame so all
  later angles have a ground truth to match.
- **Two-shot / group shot** — the *relationship*. Shows who is with whom and the
  power geometry between them (see dialogue staging in the grammar reference).
- **Medium / coverage** — the *performance* of the beat at conversational distance.
- **Close-up** — the *emotion or decision*. The scene's punctuation marks.
- **Insert** — a story-critical detail (the note, the gun, the ring).
- **Cutaway / reaction** — what someone else feels about it; also buys editorial
  flexibility and lets time compress invisibly.

### The peak-moment principle

- **Use when:** deciding how much to show.
- **Because:** film selects *crucial moments only* — the audience completes the
  rest. Showing the single decisive frame (the look, the touch, the turn) is
  stronger than covering the whole continuous action.
- **Prompt translation:** identify the one or two peak beats of a scene and lavish
  shot detail there; treat connective action as brief or implied.
- **Anchors:** Arijon/Spottiswoode (peak moments, fragmentation & reconstruction).

---

## 4. Framing within the size (quick rules)

- **Headroom** scales with size: generous in LS, minimal in CU, none in BCU.
- **Lead/look room** in the direction of gaze or motion implies intent and space.
- **Cut the figure between joints**, never at wrists/elbows/knees/ankles.
- **Eye line on the upper third** for stable portraits; lower the subject in frame
  to imply weight or threat above.

---

## 5. Default progressions to reach for

- **Reveal:** ELS (world) → LS (subject in it) → MS (who they are) → CU (why we care).
- **Tension build:** MS → MCU → CU → BCU on the decisive beat, hold, then release wide.
- **Two-hander:** establishing two-shot → matched OTS singles → CU singles on the turn.
- **Discovery/insert:** CU of face → POV/insert of what they see → CU reaction.

Combine with `guide-lens-language.md` (the *how it's rendered*) and
`guide-sequence-construction.md` (the *order and coverage*).
