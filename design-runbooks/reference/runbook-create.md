# Runbook 2 — CREATE

No existing UI, or a genuinely new surface. This is the only runbook that may create a
DESIGN.md.

**If DESIGN.md already exists, skip step 2 and step 3.** A new surface inside an established
site inherits the system. Building it is steps 1, 4, 5 against the incumbent DESIGN.md, and it
produces **no DESIGN.md change unless the user approves a durable system change**. A section,
component, feature or state inside an established surface inherits that surface — never turn a
local addition into a new identity exercise. Step 3b runs only when neither the user nor
DESIGN.md supplies a mark; step 4b derives only the kit pieces the site does not already have.

---

## Step 1 — Intake → PRODUCT.md

**Explore before you ask.** Read the repository, the brief, and anything the user attached, so
you never make the user repeat a fact you could have found. Then ask only about **material
gaps** the repository and the original request do not already answer with strong evidence.
Confirm inferences rather than assuming them.

**Do not interrogate the user through fields the brief already answers.**

### The three opening questions

> **Apache-2.0 change notice.** Contains material derived from
> [pbakaus/impeccable](https://github.com/pbakaus/impeccable) v4.1.0 at commit
> `cb56ed6c19a07329a9fa0cd4e657bee040156593` — **Apache-2.0, Copyright 2025 Paul Bakaus** (`licenses/impeccable-APACHE-2.0.txt`; upstream NOTICE at
> `licenses/impeccable-NOTICE.md`).
>
> The three questions below are **verbatim** from impeccable's `skill/reference/init.md`. The
> rest of this runbook is original to this skill.
>
> Full record: `MANIFEST.md` §§ 13–16; every deviation: § 17.

Verbatim:

1. Who is the primary user, in what situation, and what job are they doing?
2. What does the product make possible, and what is its meaningfully different mechanism or
   position?
3. What durable constraints, assets, evidence, or product facts must future work preserve?

### Conditional questions

| Trigger | Ask | Lands in |
|---|---|---|
| No framework or scaffold, and the request implies building | Once: plain static HTML/CSS, a specific framework, or your recommendation — plus any deploy target that constrains the answer | `## Stack` |
| A material audience, brand commitment, evidence, or accessibility gap | One extra round | the matching section |

`## Platform` is `web`. This skill does not build native — see SKILL.md § Out of scope.

### Constraints on the asking

- **At most three focused questions per round.**
- **One real answer or approval round is required before writing a new PRODUCT.md.**
- Whether anyone is there to answer is a **mechanical test, not a judgment call**. Probe once
  with a real first round before concluding nobody is there. Only after that probe errors or
  times out may facts be inferred from the brief — and then **every inferred fact is labelled
  in PRODUCT.md and the substitution is disclosed in the first reply, not the last**.
- Undecided facts are **recorded as undecided, never invented**.

### The asset check

Mechanical, and **no new question** — question 3 already asks about assets. Read the repository
and the answers for a logo, photography and product screenshots. Whatever is absent is written to
PRODUCT.md § Evidence on Hand **as an absence**, so no later step fabricates it
(`svg-assets.md` § 0).

### Never asked here

Aesthetic direction, emotional feel, visual references, colours, typography, style. None of it
belongs to intake — it belongs to step 2. A volunteered binding visual constraint is recorded
in `## Brand Commitments` without expansion.

### Write it

Per `contract.md` § 1 — full template, schema stamp `<!-- impeccable:product-schema 1 -->`,
belongs/does-not-belong list. Omit sections that do not apply rather than filling them with
generic prose.

**Completion gate:** PRODUCT.md exists at the resolved path and holds the confirmed record.
Interview notes are not the file.

---

## Step 2 — Direction

### 2a · Decide the visitor mode

Per surface, from the surface — not from the product. Persuade / Operate / Read / Experience.
A tool's landing page is still Persuade; a fashion house's documentation is still Read. State
it; it is not written to either artifact (`contract.md` § 3).

### 2b · Retrieve candidates

```bash
python3 scripts/search.py "<the brief in the user's own words>" --design-system
```

This resolves the product type and returns a candidate style, palette, type pairing and
landing pattern in one pass. Narrow with `--domain` where the aggregate is wrong for the
brief. Bias, don't replace, with the dials — `--variance`, `--motion`, `--density`.

**If retrieval abstains, it is telling you something.** *"No matches. This is not a match with
an empty value — the query did not hit the database."* Take the suggested terms, or accept
that the catalogue has no row for this brief.

### 2c · Pick the macrostructure

From the 21 in `hallmark-macrostructures.md`. **Pick one before writing any code.**

- **Diversification is mandatory.** Check the codebase for an existing
  `/* … macrostructure: <name> … */` CSS stamp. Found one → your pick must differ.
- **Vague brief** (no theme, no tone) → pick from the **first ten**. They cover ~80% of briefs
  and are the strongest non-Specimen shapes.
- **Specimen is not a default.** Reach for 10 only when the brief is explicitly editorial,
  foundry-adjacent, or the user named it. Specimen fall-through is banned (gate 21).
- **Stat-Led (04) has a selection gate.** Available only when the brief supplies a specific
  verifiable metric that is the product's own claim. Membership in the SaaS default sequence
  does not satisfy this. No such metric → pick another shape. Once selected, gate 46 still
  binds: the stat is never the hero's sole headline. (`merged-rules.md` § C1.)
- **Image-led shapes have a selection gate too.** 05 Workbench, 08 Photographic, 16 Feature
  Stack and 18 Portfolio Grid are made of imagery. Available only when the asset check found the
  imagery or the user confirms it is coming; otherwise pick another shape
  (`svg-assets.md` § 1).
- **Pick nav and footer alongside it** — N-archetype and Ft-archetype from the routing tables
  in `hallmark-macrostructures.md` § Archetype name key. They are part of the page shape, not
  optional chrome. Gates 42 and 43 fail the AI defaults.

### 2d · Present 2–3 distinct directions

Not one. Each direction names: macrostructure, palette with its semantic roles, type pairing,
style, landing pattern, and the one-line reason it fits *this* brief.

**Distinct means categorically distant** — Bento Grid + Long Document + Manifesto, not three
colour-swaps of the same shape.

**Justify the pick against the brief, not against the catalogue.** A retrieved row is a
candidate, not a decision. "The mapping returned it" is not a justification. If a candidate
carries a style that the ban list defaults against — glassmorphism, liquid-glass, hard offset
shadows — it is available only with **a stated purpose the effect serves**, and that purpose
is recorded in DESIGN.md. Absent one, drop it (`merged-rules.md` § C5).

**Type pairings:** the seven gate-1-flagged rows are filtered out of candidate sets before
they reach you. If one surfaces anyway, it arrives with its note — the user named the font, or
an incumbent DESIGN.md specifies it (`merged-rules.md` § C4).

### 2e · The custom branch — rare

`hallmark-custom-theme.md` fires **only** on one of its five enumerated trigger signals:
explicit ask · named brand colour · a multi-attribute aesthetic no catalogue theme is within
one axis-step of · an attached brand-mood reference · a singular structural vision.

**One adjective is not a signal** — "warm", "technical", "playful" are tones the catalogue
already carries.

If a signal fires: ask the one confirmation question, **wait**, and **default to catalogue on
silence**. If no signal fires, do not mention the fork at all.

Tuned custom keeps every structure and every gate; only the palette/pairing combination is
per-brief. Bespoke — signal 5 only — drops the structures too, floored by the gates. Bespoke
on a vanilla brief is over-reach.

---

## Step 3 — Write DESIGN.md

Per `contract.md` § 2. Before writing:

- **Tint the neutrals.** `colors.csv` values are slot markers. Apply the § Neutral tinting
  transform — tint from the primary hue, clamp chroma just above 0.005, preserve lightness,
  emit OKLCH; lift pure-black backgrounds to `L ≈ 0.12–0.15`; honour gate 7's modern-minimal
  `#fff` exception by reading the selected genre. **Re-verify AA contrast on the
  post-transform values.**
- **Record the macrostructure family** in `## Layout`.
- **Do not rename a section.** Exact headers, fixed order.
- **Frontmatter is normative.** Prose names a token and describes its role; it never restates
  a different value.
- **Nothing from PRODUCT.md** unless it is a durable brand commitment that actually constrains
  the visual system.

---

## Step 3b — The mark

**Skipped when the user supplied a logo, or an incumbent DESIGN.md records one.** Its kit is
derived at step 4b, never redrawn.

Otherwise, per `svg-assets.md` § 3: two or three concepts, each drawn from a different named fact
in PRODUCT.md, shown in `mark-concepts.html` at the project root, then **one question, and
wait**. It comes after DESIGN.md because the mark draws from the palette, and before the build
because the nav carries it.

- **A pick** → DESIGN.md § Components › Mark, and one line in PRODUCT.md § Brand Commitments
  (`contract.md` § 1 — one of the two PRODUCT.md writes allowed after intake).
- **None, or silence** → no mark. The wordmark stays live text; step 4b builds the og-card only.

---

## Step 4 — Build against it

Never re-derive direction mid-run. DESIGN.md is now the source of truth; if building reveals
it is wrong, change DESIGN.md deliberately and say so — don't drift.

**Structural reference:**

- the chosen macrostructure's **fingerprint** in `hallmark-macrostructures.md` — heading
  placement, body composition, divider language, button voice, image treatment, reveal
  pattern. Read only the one you picked.
- `landing.csv:Section Order` for the chosen pattern, plus its `Primary CTA Placement`,
  `Color Strategy` and `Conversion Optimization`.
- `styles.csv:Implementation Checklist` for the chosen style.
- the **SaaS page sequence** in `hallmark-macrostructures.md` when the macrostructure is Bento
  Grid / Stat-Led / Workbench / Marquee Hero *and* the brief is B2B SaaS marketing. It is a
  recipe of what should be present, not a template to stamp out. It does not apply to
  editorial, manifesto, letter, long-document or quote-led work — a bakery does not need a
  pricing tier comparison.

**Open the stylesheet with the stamp:**

```css
/* <Project> · macrostructure: <name> · nav: N# · footer: Ft# · slop: pass (42–45) */
```

**While building:**

- one icon library throughout — Phosphor if you want glyph lookup from this skill
  (`scripts/search.py "<query>" --domain icons`), Lucide or Heroicons if you prefer. Mixing
  two, or an emoji standing in for an icon, fails gate 30.
- charts come from `charts.csv` **by data shape, not by chart name**. `When NOT to Use` is a
  hard negative; `Data Volume Threshold` is the render-strategy switch. Use
  `Accessibility Risk`, not the dead `Accessibility Grade`.
- stack rules: `scripts/search.py "<query>" --stack <name>`. Retrieval picks one coherent
  framework generation per answer — don't mix generations.
- motion: one authored moment, not one identical entrance on every section. `motion.csv`
  presets carry a `prefers-reduced-motion` note and a compositor justification.
- **the quality floor's numbers**: body measure 65–75ch, display max 6rem, tracking floor
  -0.04em, contrast 4.5:1 / 3:1.
- **browser surfaces ship with the design** — text selection, caret, scrollbars, focus rings,
  underline offset, tabular numerals. The cheapest signal a page was built rather than
  assembled, and the one most reliably skipped.
- **picture surfaces** — every image slot resolves by the slot rule (`svg-assets.md` § 1):
  geometry when the product defines the shape exactly, a labelled placeholder when only the user
  can supply the subject, nothing when the slot was a template's habit. Placeholders follow § 2,
  and their shot briefs go to the final report, never into the page.

**Run the six-axis pre-emit critique before you emit** (`hallmark-slop-gates.md`): Philosophy ·
Hierarchy · Execution · Specificity · Restraint · Variety, scored 1–5. Anything **< 3 forces a
revision pass** before the gate sweep. Record the six scores in the stamp comment. Two passes
is normal; three means the brief is wrong, not the design.

---

## Step 4b — Derive the kit

After the build, because the og-card depicts the built hero. Per `svg-assets.md` § 4:

- **Core** — `mark.svg`, `favicon.svg` and `apple-touch-icon.png` when there is a mark;
  `og-card.svg` and its PNG always.
- **Extended** — the maskable app icon, its PNGs and `manifest.webmanifest` when the product is
  installable; `lockup.svg` when there is a mark and type can be outlined.
- **Wire it** — the `<head>` links and meta, and the inline nav mark beside the live wordmark.

A missing rasterizer or outliner skips the pieces that need it, and the final report names them
(§ 5). Never trace a logo, never hand-draw glyphs.

---

## Step 5 — VERIFY

Run Runbook 3 (`runbook-audit.md`) against what you built.

**Re-read the rules from disk.** Auditing from memory of what you just wrote is self-grading
and it passes everything.

That includes the assets: `python3 scripts/svg_lint.py <project-root>` (`svg-assets.md` § 6).
Then open the PNGs — the linter reads source, and cannot see a mark that blurs at 16px.

**Any BLOCKING finding means fix and re-verify.** Do not report "done" with open BLOCKING
items. ADVISORY findings are reported, not auto-fixed.

**The final report lists what is owed** — every placeholder with its shot brief (subject, crop,
ratio, target size, path), every kit piece skipped for a missing tool, and `mark-concepts.html`
as a run artifact that is safe to delete.

---

## Step 6 — REVISE

**VERIFY is not the end of the run.** Hand to Runbook 4 (`runbook-revise.md`) once it reports
clean, carrying the direction and the surfaces you already settled — do not re-derive them and
do not re-confirm them.

The user sees the design for the first time here. A build that emits, verifies and reports
"done" has taken the one round of judgment that matters and thrown it away.

Runbook 4 asks what they want different, offers real alternatives for the dimension they name,
keeps the winner, and writes the history entry at exit. It ends when they say done.
