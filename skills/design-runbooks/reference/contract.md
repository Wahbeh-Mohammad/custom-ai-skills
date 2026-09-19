# The shared contract — PRODUCT.md and DESIGN.md

Two files. Every runbook reads both and writes at most one. Nothing else in this skill is
allowed to hold durable product truth or durable visual direction — including `history/`,
which holds the user's taste across projects and is neither (§ 3).

Schemas are from `impeccable-artifacts.md` (itself extracted from upstream impeccable and the
official DESIGN.md format spec). This file is the pinned, skill-local version — the runbooks
read *this*, not the extraction note.

> **Apache-2.0 change notice.** Contains material derived from
> [pbakaus/impeccable](https://github.com/pbakaus/impeccable) v4.1.0 at commit
> `cb56ed6c19a07329a9fa0cd4e657bee040156593` — **Apache-2.0, Copyright 2025 Paul Bakaus** (`licenses/impeccable-APACHE-2.0.txt`; upstream NOTICE at
> `licenses/impeccable-NOTICE.md`).
>
> **This file has been modified from the original.** The prose, the five mechanisms and the
> `history/` carve-out are original to this skill. The PRODUCT.md and DESIGN.md schemas — their
> field names, the bracketed field prompts, and the `<!-- impeccable:product-schema 1 -->` stamp
> — are **verbatim** from impeccable's `skill/reference/init.md`, `document.md` and
> `new-work.md`, pinned here so the runbooks read a fixed version rather than the extraction.
>
> Full record: `MANIFEST.md` §§ 13–16; every deviation: § 17.

| | PRODUCT.md | DESIGN.md |
|---|---|---|
| Owns | durable product truth | durable visual decisions |
| Lifetime | outlives every redesign | outlives every page, replaced by a redesign |
| Written by | Runbook 2 (CREATE) intake; afterwards only the two asset appends in § 1 | Runbook 2 step 3, Runbook 1 step 2, or Runbook 4 amending one token group |
| Read by | all four runbooks | all four runbooks |
| Changes | rarely | per redesign, and per kept revision |

> PRODUCT.md owns product truth. DESIGN.md owns durable visual decisions.
> — `impeccable-artifacts.md`, verbatim from upstream `new-work.md`

---

## 1. PRODUCT.md

**Lives at:** `PROJECT_ROOT/PRODUCT.md`
**Schema stamp:** `<!-- impeccable:product-schema 1 -->`, copied verbatim, including when
updating an older file. Replaced in place if present; otherwise inserted after the first
`# ` heading line.

### Template

```markdown
# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
[Greenfield only: the user's answer to the stack question, e.g. "static HTML/CSS", "Astro", or "delegated: <what you chose and why>". Omit the section when an existing codebase already answers it.]

## Users
[Primary users, their situation, and job. Add other audiences only when confirmed.]

## Product Purpose
[What the product does, why it exists, and what success means.]

## Positioning
[The product mechanism or claim a neighboring product could not truthfully copy.]

## Operating Context
[Workflows, environments, tools, documents, materials, and rituals that are factual parts of using or evaluating the product.]

## Capabilities and Constraints
[Confirmed functionality, technical constraints, terminology, and explicitly undecided product facts.]

## Brand Commitments
[Existing name, voice, assets, personality, identity constraints, and references the user explicitly made binding. Omit when none exist.]

## Evidence on Hand
[Real content, data, demonstrations, testimonials, case studies, press, or assets, with paths where applicable. State absences that future work must not fabricate.]

## Product Principles
[Three to five durable strategic principles derived from confirmed answers; no visual recipes.]

## Accessibility & Inclusion
[Known user needs or required standard. Omit when no product-specific requirement was established.]
```

### Field rules

| Field | Rule |
|---|---|
| `## Platform` | The bare value `web`. This skill is web-only — see SKILL.md § Out of scope. |
| `## Stack` | Greenfield only. Records the answer including the literal word `delegated` when the user left the choice to the agent, so later work knows the choice was offered. |
| `## Brand Commitments` · `## Evidence on Hand` | The only two sections written after intake, and only by Runbooks 1 and 2, each an **append after the user's answer**: an adopted mark to Brand Commitments (`svg-assets.md` § 3), owed assets to Evidence on Hand (`svg-assets.md` §§ 0, 2). Nothing else in the file changes, and neither runbook creates a missing PRODUCT.md to make room. |
| All | Write only confirmed facts and explicitly marked open decisions. Omit irrelevant sections rather than filling them with generic prose. |
| All | Preserve useful legacy headings. |

`PRODUCT_V4_SECTIONS = ['Positioning', 'Operating Context', 'Evidence on Hand', 'Product Principles']`
— a file missing these is pre-v4, not deliberately short.

`## Register` is **deprecated**. v4 replaced the product-wide register axis with the four
visitor modes, which are per-surface (§ 3). Report a legacy `## Register` at boot; delete it
only when the user agrees.

### Belongs / does not belong

**Belongs:** users, jobs, workflows, purpose, success, positioning, operating context;
capabilities, constraints, terminology, evidence, platform, accessibility; confirmed voice,
assets, brand commitments.

**Does not belong:** visual worlds, palettes, typography, components, page concepts; visitor
mode, narrative, CTA/proof sequence, or any surface strategy; invented testimonials,
customers, benchmarks, pricing, licensing, or deployment claims; a requirement to decide
every optional field.

### Completion gate

Before any build, verify PRODUCT.md exists at the resolved path and holds the confirmed
record. Absent file = intake incomplete. Interview notes, a plan, or later design prose do
not substitute for the file.

---

## 2. DESIGN.md

**Lives at:** `PROJECT_ROOT/DESIGN.md`
**Format:** optional YAML frontmatter of machine-readable tokens, then up to eight markdown
sections in a fixed order.

> Tokens are normative; prose provides context for how to apply them.

### Frontmatter token schema

```yaml
---
name: <project title>
description: <one-line tagline>
colors:
  primary: "oklch(58% 0.19 25)"
  neutral-bg: "oklch(97% 0.006 25)"
  # ...one entry per role; key = descriptive slug
typography:
  display:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(2.5rem, 7vw, 4.5rem)"
    fontWeight: 300
    lineHeight: 1
    letterSpacing: "normal"
  body:
    # ...
rounded:
  sm: "4px"
  md: "8px"
spacing:
  sm: "8px"
  md: "16px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral-bg}"
    rounded: "{rounded.sm}"
    padding: "16px 48px"
  button-primary-hover:
    backgroundColor: "{colors.primary-deep}"
---
```

**Five rules:**

1. **Token refs** use `{path.to.token}`. Components may reference primitives; primitives may
   not reference each other.
2. **Colors accept any valid CSS color string.** Preserve an incumbent `rgb()`/`hsl()`/
   `oklch()`/wide-gamut value when it is the project's normative source. Never split the
   source of truth without explicit reason. Palettes emitted by this skill are OKLCH — see
   § Neutral tinting below.
3. **Component sub-tokens are limited to 8 props:** `backgroundColor`, `textColor`,
   `typography`, `rounded`, `padding`, `size`, `height`, `width`. Shadows, motion, focus
   rings and backdrop-filter do not fit — they go in the prose sections named below.
4. **Scale keys are open-ended.** Use the names the project already uses. Don't rename to
   Material defaults.
5. **Variants are naming convention, not schema:** `button-primary` / `button-primary-hover`
   / `button-primary-active` as sibling keys.

Top-level groups are limited to `colors`, `typography`, `rounded`, `spacing`, `components`.
No `motion:`, `breakpoints:` or `shadows:` at the top level.

### Markdown body — eight sections, fixed order

1. `## Overview`
2. `## Colors`
3. `## Typography`
4. `## Layout`
5. `## Elevation & Depth`
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

Omit irrelevant sections rather than inventing rules; those present stay in this order.
**Do not rename a section, even slightly.** "Colors", not "Color Palette & Roles".
"Typography", not "Typography Rules". Section matching is exact-first, then word-boundary
containment — a near-synonym silently drops the section.

| Section | Carries |
|---|---|
| Overview | `**Creative North Star: "[metaphor]"**`, 2–3 paragraphs of personality/density/philosophy, closing `**Key Characteristics:**` bullets |
| Colors | Grouped **Primary / Secondary / Tertiary / Neutral**, each as `**[Descriptive Name]** (value): [where and why]`. The 16 semantic roles from `colors.csv` map here |
| Typography | Display / Body / Label-Mono families, a **Character** line, then a **Hierarchy** list of Display / Headline / Title / Body / Label with weight, size, line-height, purpose |
| Layout | Grid or spatial model, container behavior, density, responsive changes, spacing rhythm — **and the macrostructure family commitment** (§ Macrostructure below). Breakpoints live here |
| Elevation & Depth | Shadows vs tonal layering vs hybrid, plus a **Shadow Vocabulary** list of exact `box-shadow` values |
| Shapes | Corner/radius strategy, borders, clipping, recurring silhouette |
| Components | Per component: character line, shape, color assignment, states, distinctive behavior. When the run drew one, a **Mark** entry (what it draws, grid, fills as token refs, sizes, placement, kit files) and a **Placeholder** entry (fill token, label face, treatment) — `svg-assets.md` §§ 2–3 |
| Do's and Don'ts | Concrete visual guardrails grounded in the incumbent implementation or the chosen direction |

**Motion gets no section of its own** — it goes with the world or component it affects.

**Named Rules** are available in any section: `**The [Name] Rule.** [short doctrine]`, 1–3
per section. Example, verbatim from upstream: *"The One Voice Rule. The primary accent is
used on ≤10% of any given screen. Its rarity is the point."*

### Macrostructure commitment

DESIGN.md records **one macrostructure family for the whole site**, in `## Layout`, by its
name from the 21 in `hallmark-macrostructures.md`. The machine-readable carrier is the CSS
stamp at the top of the stylesheet:

```css
/* <Project> · macrostructure: <name> · nav: N# · footer: Ft# · slop: pass (42–45) */
```

The diversification rule reads `<name>` from this stamp. Variety is **across projects, never
across pages of one site** — see SKILL.md § Always true.

### Neutral tinting (resolution C3)

`colors.csv` encodes surfaces as **slot markers, not final values**. Neutrals are tinted at
token-emission time, never read straight into DESIGN.md:

- tint from the palette's primary hue, chroma clamped just above the gate-22 floor (0.005),
  lightness preserved, emitted as OKLCH;
- gate 7's modern-minimal `#fff`-paper exception is honoured by reading the selected genre;
- pure-black backgrounds additionally lift to `L ≈ 0.12–0.15` for OLED halation;
- AA contrast re-verified on the **post-transform** values, not the source hex.

Gates 7 and 22 stay global and unscoped. `colors.csv` is not modified.

### No sidecar

Upstream impeccable carries a `.impeccable/design.json` sidecar for what the frontmatter
schema cannot hold. This skill does not. Everything the sidecar carried has a home in the
prose sections above: shadows → `## Elevation & Depth` Shadow Vocabulary; motion → with its
world or component; breakpoints → `## Layout`. One file, one source of truth.

### Belongs / does not belong

**Belongs:** tokens, palette with semantic roles, type scale, spacing, component conventions,
macrostructure family, visual guardrails, the mark's construction and the placeholder
convention.

**Does not belong:** anything in PRODUCT.md. *DESIGN.md is strictly visual.* Carry a line
from PRODUCT.md only when it is a durable brand commitment that actually constrains the
visual system — a binding logo, identity asset, or accessibility need.

---

## 3. The run artifact, and what is deliberately *not* an artifact

Upstream impeccable has a third file, the surface brief, holding per-surface strategy. This
skill has two **durable** artifacts, so two things the brief carried need an explicit home:

**Visitor mode** — Persuade / Operate / Read / Experience. Chosen **per surface, never per
product**. A tool's landing page is still Persuade; a fashion house's documentation is still
Read. It is barred from PRODUCT.md (this is exactly the mistake the deprecated `## Register`
made) and from DESIGN.md (it is strategy, not visual system).

Its home is the **run artifact**: `REVAMP.md`'s surface table carries a visitor mode per row
(`runbook-revamp.md` § 1). Runbook 2 states it per surface at direction time. Runbook 3 reads
it if a plan exists and does not invent one if not.

`REVAMP.md` is a **third lifetime**, deliberately shorter than either artifact above. A fourth
sits at the other end of the scale and outside the project entirely:

| | Lives | Lifetime | Carries |
|---|---|---|---|
| `history/` | in the skill | outlives every project | the user's taste across projects |
| PRODUCT.md | in the project | outlives every redesign | product truth |
| DESIGN.md | in the project | outlives every page | the visual system |
| REVAMP.md | in the project | dies with the run | scope, batch order, per-surface status and visitor mode |
| `mark-concepts.html` | in the project | dies with the run | the mark concepts, labelled A/B/C — nothing else (`svg-assets.md` § 3) |

`REVAMP.md` is written **before any source file is edited**, updated as the run proceeds, and
disposable at the end. Nothing durable lives there: a fact worth keeping belongs in PRODUCT.md,
a visual decision worth keeping belongs in DESIGN.md. Never delete it on the user's behalf.
`mark-concepts.html` has the same lifetime and the same rule. It sits at a project root that may
be served, so it carries labels only — why each concept exists is said in chat, never in the file.

**`history/` is skill-local and barred from DESIGN.md.** A learned taste rule is a preference
this user has shown across unrelated projects; a DESIGN.md is one project's visual system. The
rule may explain why a token was chosen — it is never a token, never a section, and never
copied into the file. The traffic runs one way: a confirmed rule steers a decision at boot,
the decision lands in DESIGN.md, and DESIGN.md does not record that a rule was involved. Two
projects that share a taste rule still have two independent design systems.

Nothing in `history/` belongs in PRODUCT.md either. Taste is not product truth, and a
preference the user showed on someone else's project is not a fact about this one.

**Direction rationale** — why this palette, this pairing, this macrostructure. Stated to the
user in the runbook, and **never shipped to the browser**: banned from HTML or framework
comments, hidden DOM, `<template>`, `data-*` attributes, rendered JSX/TSX output, serialized
props or state, RSC payloads, client bundles, metadata, JSON-LD, accessibility-only text, and
files served beside the artifact. A compiler stripping development metadata is not a safety
boundary. The CSS stamp is the one exception and carries names only, never rationale.

---

## 4. How the separation holds

Not by convention — by five mechanisms:

1. **Separate writers.** Runbook 2 intake writes PRODUCT.md and never offers DESIGN.md.
   Runbooks 1 and 2 write DESIGN.md and never touch PRODUCT.md, except the two confirmed asset
   appends in § 1 — an adopted mark, owed assets — which are product truth the run discovered,
   not visual decisions. Runbook 1 additionally writes
   REVAMP.md, which is the only artifact it may write before editing source. Runbook 3 writes
   nothing at all. Runbook 4 amends DESIGN.md for a kept revision and writes `history/`; it
   never touches PRODUCT.md and never writes a new project artifact. Only DESIGN.md exists →
   leave it untouched and create PRODUCT.md.
2. **Explicit belongs / does-not-belong lists** on both sides, above.
3. **Composition is never promoted.** A concept that works on one surface stays on that
   surface. Never turn a task-specific concept or surface strategy into a system-wide rule.
   Extending an existing surface produces no DESIGN.md change unless the user approves a
   durable system change.
4. **Redesign and refinement are asymmetric.** Redesign preserves product truth, content,
   function and constraints, and **replaces** DESIGN.md — treating the old look as evidence
   and anti-reference. Refinement preserves the incumbent identity and everything outside
   scope. Never split the difference into polish on the discarded look. And: *visual
   authority is evidence, not a filename* — a missing DESIGN.md alone does not make a project
   greenfield.
5. **One source of truth per value.** Frontmatter is normative; prose may name a token and
   describe its role but may not restate a different value.

**Drift is reported, not repaired.** A stale or contradictory artifact is a finding in the
report. Never repair drift as a side effect of a design task.
