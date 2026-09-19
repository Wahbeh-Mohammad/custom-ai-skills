# Impeccable's three-artifact split — PRODUCT.md, DESIGN.md, surface brief

> **Apache-2.0 change notice.** Derived from [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
> v4.1.0 at commit `cb56ed6c19a07329a9fa0cd4e657bee040156593` — **Apache-2.0,
> Copyright 2025 Paul Bakaus** (`licenses/impeccable-APACHE-2.0.txt`;
> upstream NOTICE at `licenses/impeccable-NOTICE.md`).
>
> **This file has been modified from the original.** Schema tables and the belongs /
> does-not-belong lists are verbatim; the surrounding process prose is summarised, and
> impeccable's CLI invocation steps are dropped.
>
> Upstream paths named below are impeccable's own and resolve in its tree, not in this skill.
> Full per-file record: `MANIFEST.md` §§ 13–16; every deviation: § 17.

Sources: `skill/SKILL.src.md`, `skill/reference/init.md`, `skill/reference/document.md`,
`skill/reference/new-work.md`, `docs/CLI-CONTRACT.md`.

The one-line statement of the split, verbatim from `new-work.md`:

> PRODUCT.md owns product truth. DESIGN.md owns durable visual decisions. A surface brief keeps
> strategy that belongs to one route or artifact.

Three files, three lifetimes. Product truth outlives every redesign. The visual world outlives
every page. Surface strategy dies with the page it describes. Everything below is the mechanics
that keep the three from bleeding into each other.

---

## 1. PRODUCT.md

**Written by:** `/impeccable init` only. Never by `document`, never by `new-work`.
**Lives at:** `PROJECT_ROOT/PRODUCT.md` (or the path `impeccable context` resolves, on a child
app inheriting root context).
**Schema stamp:** `<!-- impeccable:product-schema 1 -->`, copied verbatim, including when
updating an older file. `PRODUCT_SCHEMA_VERSION = 1`.

### Template (verbatim from `init.md` Step 4)

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
| `## Platform` | The bare value `web`, `ios`, `android`, or `adaptive`. Mobile web is `web`; a native wrapper around a website is not native. Absent in a legacy file means `web` unless evidence says otherwise. |
| `## Stack` | Greenfield only. Records the answer, including the literal word `delegated` when the user left the choice to the agent — "so later work knows the choice was offered". |
| All | Write only confirmed facts and explicitly marked open decisions. Omit irrelevant sections rather than filling them with generic prose. |
| All | Preserve useful legacy headings. |
| Schema stamp | Records which version of the product record the file follows, "so later versions can tell a deliberately short record from one written before a section existed, and never propose an interview the user has already sat through". |

**Version bookkeeping** (`lib/artifact-schema.mjs`, per `docs/CLI-CONTRACT.md`):

- `PRODUCT_SCHEMA_VERSION = 1`
- `PRODUCT_V4_SECTIONS = ['Positioning', 'Operating Context', 'Evidence on Hand', 'Product Principles']`
- `PRODUCT_DEPRECATED_SECTIONS = { Register: "v4 replaced the brand/product register axis with the four visitor modes (Persuade, Operate, Read, Experience), which are chosen per surface and persisted in that surface's brief. Nothing reads ## Register any more." }`
- Stamp regex: `/^[ \t]*<!--[ \t]*impeccable:product-schema[ \t]+(\d+)[ \t]*-->[ \t]*$/im`
- `stampProductSchema`: an existing stamp is replaced in place; otherwise inserted after the first `/^#\s+\S/` line; with no heading, `stamp + '\n\n' + body`.
- Deprecated sections are reported at boot; deleted only when the user agrees.

### The init interview

`init` explores first so the user never repeats a known fact, then asks. Constraints on the asking:

- Structured question tool when available; otherwise ask and wait.
- **At most three focused questions per round.**
- **One real answer or approval round is required before writing a new PRODUCT.md.**
- Confirm inferences. Ask only about material gaps the repository and the original request do not
  already answer with strong evidence.
- Whether anyone can answer is a mechanical test, not a judgment call. Probe once with a real
  first round before concluding nobody is there. Only after that probe errors or times out may
  facts be inferred from the brief — and then every inferred fact is labelled in PRODUCT.md and
  the substitution is disclosed in the first reply, not the last.

**The three opening questions, verbatim:**

1. Who is the primary user, in what situation, and what job are they doing?
2. What does the product make possible, and what is its meaningfully different mechanism or position?
3. What durable constraints, assets, evidence, or product facts must future work preserve?

**Conditional questions:**

| Trigger | Question | Recorded as |
|---|---|---|
| Platform ambiguous | Confirm platform separately | `## Platform` |
| No framework or scaffold and the request implies building | Ask once: plain static HTML/CSS, a specific framework, or your recommendation — plus any deploy target that constrains the answer | `## Stack` |
| A material audience, brand commitment, evidence, or accessibility gap | One extra round | the matching section |
| Image generation available and no `buildPath` recorded | Step 5, its own question, never a clause inside another: **comp-first** (an image sets the bar before any code; bolder composition, slower, and the build must match the image) or **code-first** (build directly; the ambition is written into the direction contract and audited at the finish; leaner, faster) | `.impeccable/config.json` → `"buildPath": "comp"` or `"code"` — *not* PRODUCT.md |

Undecided facts are recorded as undecided, never invented.

**Never asked during init:** aesthetic direction, emotional feel, visual references, colors,
typography, style. A volunteered binding visual constraint is recorded without expansion.

### What belongs / what does not (verbatim)

**Belongs:**

- users, jobs, workflows, purpose, success, positioning, and operating context;
- capabilities, constraints, terminology, evidence, platform, and accessibility;
- confirmed voice, assets, and brand commitments.

**Does not belong:**

- visual worlds, palettes, typography, components, or page concepts;
- visitor mode, narrative, CTA/proof sequence, or other surface strategy;
- invented testimonials, customers, benchmarks, pricing, licensing, or deployment claims;
- a requirement to decide every optional field.

### Completion gate

Before loading new-work or resuming shape/build, verify PRODUCT.md exists at the resolved path
and contains the confirmed product record. If the file is absent, init is incomplete. Interview
notes, a planning packet, or later design prose do not substitute for the file.

---

## 2. DESIGN.md

**Written by:** `/impeccable document` (scan mode from code, seed mode from a chosen world) and
replaced wholesale by a redesign in `new-work`. Never by `init`.
**Format:** the [official DESIGN.md format spec](https://raw.githubusercontent.com/google-labs-code/design.md/main/docs/spec.md) —
optional YAML frontmatter of machine-readable tokens, then up to eight markdown sections in a
fixed order.

> **Tokens are normative; prose provides context for how to apply them.**

### Frontmatter token schema (verbatim)

```yaml
---
name: <project title>
description: <one-line tagline>
colors:
  primary: "#b8422e"
  neutral-bg: "#faf7f2"
  # ...one entry per extracted color; key = descriptive slug
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

**Rules that matter** (verbatim):

- **Token refs** use `{path.to.token}` (e.g. `{colors.primary}`, `{rounded.md}`). Components may
  reference primitives; primitives may not reference each other.
- **Colors accept any valid CSS color string.** Hex is the recommended default for portability,
  but preserve an incumbent `rgb()`, `hsl()`, `oklch()`, wide-gamut, or mixed-color value when it
  is the project's normative source. Never split the source of truth without explicit reason.
- **Component sub-tokens** are limited to 8 props: `backgroundColor`, `textColor`, `typography`,
  `rounded`, `padding`, `size`, `height`, `width`. Shadows, motion, focus rings, backdrop-filter:
  none of those fit. Carry them in the sidecar.
- **Scale keys are open-ended.** Use whatever names the project already uses (`oxblood-deep`,
  `surface-container-low`). Don't rename to Material defaults.
- **Variants are naming convention, not schema.** `button-primary` / `button-primary-hover` /
  `button-primary-active` as sibling keys.

Top-level groups are limited to what Stitch's Zod schema accepts: `colors`, `typography`,
`rounded`, `spacing`, `components`. No `motion:`, `breakpoints:`, `shadows:` at the top level —
those belong in the sidecar's `extensions`.

### Markdown body — eight canonical sections, fixed order

1. `## Overview`
2. `## Colors`
3. `## Typography`
4. `## Layout`
5. `## Elevation & Depth`
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

Omit irrelevant sections rather than inventing rules; those present stay in this order. Responsive
layout goes in Layout, depth in Elevation & Depth, radius and form language in Shapes,
per-component behavior in Components. Motion goes with the world or component it affects — it gets
no section of its own.

Section content conventions:

| Section | Carries |
|---|---|
| Overview | `**Creative North Star: "[metaphor]"**`, 2–3 paragraphs of personality/density/philosophy, closing `**Key Characteristics:**` bullets |
| Colors | Grouped **Primary / Secondary / Tertiary / Neutral** (Material-derived roles), each as `**[Descriptive Name]** (#HEX): [where and why]` |
| Typography | Display / Body / Label-Mono families, a **Character** line, then a **Hierarchy** list of Display / Headline / Title / Body / Label with weight, size, line-height, purpose |
| Layout | Grid or spatial model, container behavior, density, responsive changes, spacing rhythm |
| Elevation & Depth | Shadows vs tonal layering vs hybrid, plus a **Shadow Vocabulary** list of exact `box-shadow` values when applicable |
| Shapes | Corner/radius strategy, borders, clipping, recurring silhouette |
| Components | Per component: character line, shape, color assignment, states, distinctive behavior |
| Do's and Don'ts | Concrete visual guardrails grounded in the incumbent implementation or the user's chosen world |

**Named Rules** are the skill's signature device, available in any section:
`**The [Name] Rule.** [short doctrine]`, 1–3 per section. Example given verbatim:
*"The One Voice Rule. The primary accent is used on ≤10% of any given screen. Its rarity is the point."*

### The sidecar — `.impeccable/design.json`

`DESIGN_SIDECAR_SCHEMA_VERSION = 2`. It carries **what the frontmatter schema cannot hold** and
does not duplicate it: tonal ramps, shadow/elevation tokens, motion tokens, breakpoints, full
component HTML/CSS snippets, and narrative.

```json
{
  "schemaVersion": 2,
  "generatedAt": "ISO-8601 string",
  "title": "Design System: [Project Title]",
  "extensions": {
    "colorMeta": {
      "primary":    { "role": "primary", "displayName": "Editorial Magenta", "canonical": "oklch(60% 0.25 350)", "tonalRamp": ["...", "...", "..."] },
      "cool-paper": { "role": "neutral", "displayName": "Cool Paper",       "canonical": "oklch(96% 0.005 230)", "tonalRamp": ["...", "...", "..."] }
    },
    "typographyMeta": {
      "display": { "displayName": "Display", "purpose": "Hero headlines only." }
    },
    "shadows": [
      { "name": "ambient-low", "value": "0 4px 24px rgba(0,0,0,0.12)", "purpose": "Diffuse hover glow under accent elements." }
    ],
    "motion": [
      { "name": "ease-standard", "value": "cubic-bezier(0.4, 0, 0.2, 1)", "purpose": "Default easing for state transitions." }
    ],
    "breakpoints": [
      { "name": "sm", "value": "640px" }
    ]
  },
  "components": [
    {
      "name": "Primary Button",
      "kind": "button | input | nav | chip | card | custom",
      "refersTo": "button-primary",
      "description": "One-line what and when.",
      "html": "<button class=\"ds-btn-primary\">SAVE CHANGES</button>",
      "css": ".ds-btn-primary { ... } .ds-btn-primary:hover { ... }"
    }
  ],
  "narrative": {
    "northStar": "The Editorial Sanctuary",
    "overview": "2-3 paragraphs of the philosophy, pulled from DESIGN.md Overview section.",
    "keyCharacteristics": ["...", "..."],
    "rules": [{ "name": "The One Voice Rule", "body": "...", "section": "colors|typography|elevation" }],
    "dos":   ["Do use ..."],
    "donts": ["Don't use ..."]
  }
}
```

Sidecar component snippets must be self-contained drop-ins for a shadow DOM: Tailwind utilities
expanded to literal CSS; CSS custom properties referenced via `var(--x)` when they exist on
`:root`, otherwise resolved to literals; icons inlined as SVG; `:hover` / `:focus-visible` /
`:active` included; universal resets stripped; every class prefixed `ds-`. Target 5–10 components.
Tonal ramps are 8 steps, dark to light, same hue and chroma, lightness ~15% → ~95%.

`narrative` is mapped from the DESIGN.md that was just written, **not reworded**:
`northStar` ← the Creative North Star line; `overview` ← the philosophy paragraphs;
`keyCharacteristics` ← the Key Characteristics bullets; `rules` ← every `**The [Name] Rule.**`
across all sections, tagged with `section`; `dos` / `donts` ← the Do's and Don'ts bullets verbatim.

**schemaVersion 1 → 2:** v1 carried token primitive arrays (`tokens.colors[]`, …). Those values
moved into the frontmatter; the sidecar now carries only metadata that cannot live there (tonal
ramps, canonical OKLCH when the hex is an approximation, display names, role hints), keyed by
frontmatter token name (`colorMeta.<token-name>`, `typographyMeta.<token-name>`).

### Seed mode

For a pre-implementation project, `document --seed` routes through new-work's world workshop and
writes a directional DESIGN.md that leads with a literal commitment marker:

```markdown
<!-- SEED: established with the user before implementation; re-run /impeccable document once there's code to capture the actual tokens and components. -->
```

A seed writes frontmatter with `name` and `description` only — no colors, typography, rounded,
spacing, or components — omits `## Components` entirely, and skips the sidecar. Unresolved values
are marked `[to be resolved during implementation]` rather than invented.

### Parser contract (`lib/design-parser.mjs`, used by `doctor`)

`parseDesignMd(md)` → `{ schemaVersion: 2, title, frontmatter, overview, colors, typography,
layout, elevation, shapes, components, dosDonts }`. Each section is `null` when its canonical H2
is absent. Canonical H2 names in match precedence: `Overview, Colors, Typography, Layout,
Elevation, Shapes, Components, Do's and Don'ts`. H2 regex
`/^##\s+(?:\d+\.\s*)?([^:\n]+?)(?::\s*(.+))?$/`; exact match first (case-insensitive, curly
apostrophes normalized), then word-boundary containment. This is why the skill insists:

> Don't rename sections even slightly. "Colors" not "Color Palette & Roles". "Typography" not
> "Typography Rules". Tooling parsing depends on exact headers.

---

## 3. The surface brief — the pressure valve that keeps the other two clean

**Lives at:** `<projectRoot>/.impeccable/surfaces/<slug>.md`, one brief per slug.

Slug derivation (`lib/surface-briefs.mjs`): a URL is stripped of hash and search and one trailing
slash; `route:<r>` must start with `/` and contain no `..`, is cut at `?`/`#`, has `//` collapsed
and the trailing `/` stripped (root stays `/`); a bare `/` is `route:/`; a path that is neither
inside the project nor on disk becomes a route; anything else is a project-relative posix path.
`route:/pricing` → `route-pricing`, `route:/` → `route`.

File shape, verbatim:

```
---
version: 1
slug: "<slug>"
primary_target: "<normalized>"
related_targets: ["<n1>",...]   (deduped, primary removed, JSON array)
---

<body.trim()>
```

### The direction contract

Before code, the chosen direction is recorded under `## Direction contract` **in the surface
brief** — six short blocks, roughly 150 words:

| Block | Content |
|---|---|
| `THESIS` | the one idea this surface owns and the category-default arrangement it refuses |
| `OWN-WORLD` | the palette and component language, specific enough to be recognizable with all content removed |
| `STORY` | what the visitor understands, believes, and does |
| `FIRST VIEWPORT` | the exact composition, what is where and at what scale, and where the primary action sits |
| `FORM` | the chosen form, its position on your ordered list, and the seed key the script printed |
| `FINISH` | verbatim: "unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance" |

"If a block reads like a mood, the direction is not decided yet."

**The contract never reaches the browser.** It is banned from implementation source and any
browser-delivered artifact: HTML or framework comments, hidden DOM, `<template>` elements,
`data-*` attributes, rendered JSX/TSX output, serialized props or state, RSC payloads, client
bundles, metadata or JSON-LD, accessibility-only text, and files served beside the artifact. "A
compiler or optimizer removing development metadata is not a safety boundary." Reviewers and
documenters read it from the brief.

---

## 4. How the separation is actually enforced

Not by convention — by six mechanisms:

1. **Separate writers.** `init` writes PRODUCT.md and is forbidden from offering DESIGN.md
   ("Never silently overwrite an existing file or offer DESIGN.md during init"; "**Only DESIGN.md
   exists:** leave it untouched and create PRODUCT.md"). `document` writes DESIGN.md and its
   sidecar. `new-work` writes the surface brief. No command writes two layers on a whim.

2. **Explicit belongs/does-not-belong lists** on PRODUCT.md (above) and a matching prohibition on
   DESIGN.md: *"Don't duplicate content from PRODUCT.md. DESIGN.md is strictly visual."* Product
   truth may constrain DESIGN.md only as a **durable brand commitment** — a binding logo, identity
   asset, accessibility need: *"Carry a line from PRODUCT.md only when it is a durable brand
   commitment that actually constrains the visual system."*

3. **The visitor mode is per-surface, never global.** Persuade / Operate / Read / Experience is
   chosen from the requested surface, not the product, and persisted only in that surface's brief.
   A tool's landing page is still Persuade; a fashion house's documentation is still Read. The
   deprecated `## Register` section in PRODUCT.md is exactly the mistake this replaced — a
   product-wide register where a per-surface mode belonged.

4. **Composition never gets promoted.** In seed mode: *"Keep the selected first-surface expression
   in its surface brief; do not promote its composition into the global world."* In Do's and
   Don'ts: *"Do not turn a task-specific concept or surface strategy into a system-wide
   prohibition."* In new-work: extending an existing surface produces *"no DESIGN.md change unless
   the user approves a durable system change."*

5. **Redesign semantics are asymmetric.** Redesign preserves product truth, content, function,
   native affordances, and constraints, and **replaces** DESIGN.md — treating the old look as
   evidence and anti-reference. Refinement preserves the incumbent identity and everything outside
   scope. *"Never split the difference into polish on the discarded look."* And: *"Visual
   authority is evidence, not a filename"* — a missing DESIGN.md alone does not make a project
   greenfield.

6. **One source of truth per value.** Inside DESIGN.md the frontmatter is normative and prose may
   not restate a different value; the sidecar extends the frontmatter rather than duplicating it;
   `buildPath` lives only in `.impeccable/config.json` and is explicitly barred from `## Stack` or
   any other PRODUCT.md section, "where a second copy would outlive the setting and steer rounds
   nobody could trace back to it".

**Drift is reported, not repaired.** From SKILL.md: *"Never repair drift as a side effect of a
design task. A `CONTEXT_STALE` finding is reported, not acted on, unless the user asks. The one
exception is a finding marked `auto`, which the next write to that file performs anyway."*
`/impeccable doctor` is the command that reconciles the artifacts on request.
