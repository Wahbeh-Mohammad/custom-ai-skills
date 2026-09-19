# Third-party notices

`design-runbooks` is assembled from four upstream projects. This file names each one, what it
licenses, and which files in this skill derive from it. Full licence texts are in `licenses/`.
File-by-file provenance, fidelity claims and every deviation from upstream are in `MANIFEST.md`.

The skill as a whole is distributed under the **Apache License 2.0** (see `LICENSE` and
`NOTICE`). Apache-2.0 is the only licence compatible with all four inbound terms: it accepts the
three MIT-licensed components and satisfies impeccable's Apache-2.0 obligations. Each upstream
component remains under its own licence; combining them here does not relicense them.

---

## Summary

| Upstream | Version | Pinned commit | Licence | Copyright | Lands in |
|---|---|---|---|---|---|
| [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 2.13.0 | [`15de38fb7`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/15de38fb70bc80ae9276fa7703b48ae861a672e6) | MIT | (c) 2024 Next Level Builder | `data/**`, `scripts/**`, `reference/retrieval-split.md` |
| [hallmark](https://github.com/nutlope/hallmark) | 1.1.0 | [`13ac0ec7e`](https://github.com/nutlope/hallmark/tree/13ac0ec7e148655948100b6396439e481361d690) | MIT | (c) 2026 Hallmark contributors | `reference/hallmark-*.md`, two marked blocks in `reference/svg-assets.md` |
| [Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines) | unversioned | [`e3d624baa`](https://github.com/vercel-labs/web-interface-guidelines/tree/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1) | MIT | (c) 2025 Vercel Labs | `guidelines-and-review.md` |
| [impeccable](https://github.com/pbakaus/impeccable) | 4.1.0 (engine 0.1.5) | [`cb56ed6c1`](https://github.com/pbakaus/impeccable/tree/cb56ed6c19a07329a9fa0cd4e657bee040156593) | **Apache-2.0** | 2025 Paul Bakaus | `reference/impeccable-*.md`, `data/impeccable-detector-rules.csv`, parts of `reference/contract.md` and `reference/runbook-create.md` |

Not derived from any upstream — original to this skill, Apache-2.0, (c) 2026 Mohammad Wahbeh:
`SKILL.md`, `MANIFEST.md`, `reference/merged-rules.md`, `reference/runbook-revamp.md`,
`reference/runbook-audit.md`, `reference/runbook-revise.md`, `history/**`, `scripts/svg_lint.py`,
`scripts/test_svg_lint.py` (despite the `scripts/**` row above). See `MANIFEST.md` § 18.
`reference/svg-assets.md` is original prose that embeds two verbatim hallmark blocks, each
marked by an *Extraction note*. `reference/contract.md` and `reference/runbook-create.md` are original prose that embeds
verbatim impeccable schemas and questions — both carry an Apache-2.0 change notice.

This list was established mechanically, not by recollection: every line of 60 characters or
more in every file of this skill was matched against every text file in all four upstream
trees. The files above returned zero matches.

---

## 1. ui-ux-pro-max — MIT

- **Upstream:** <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill>, v2.13.0, commit
  `15de38fb70bc80ae9276fa7703b48ae861a672e6` (24 extracted files re-diffed at that commit, all identical)
- **Licence:** MIT — `licenses/ui-ux-pro-max-MIT.txt`
- **Copyright:** (c) 2024 Next Level Builder
- **Derives:** every file under `data/` (except `impeccable-detector-rules.csv`) and `scripts/`;
  `reference/retrieval-split.md` distils the scripts' behaviour.
- **Fidelity:** byte-identical at extraction, verified with `diff -rq`. Four files were
  subsequently modified by conflict resolution — `data/typography.csv`, `data/ui-reasoning.csv`,
  `scripts/core.py`, `scripts/design_system.py`. Every changed line is named in `MANIFEST.md`
  § 17 (C1–C5). No row was deleted from any CSV; `data/colors.csv` is unmodified.

## 2. hallmark — MIT

- **Upstream:** <https://github.com/nutlope/hallmark>, v1.1.0, commit
  `13ac0ec7e148655948100b6396439e481361d690` (27 extracted files re-diffed at that commit, all identical)
- **Licence:** MIT — `licenses/hallmark-MIT.txt`
- **Copyright:** (c) 2026 Hallmark contributors
- **Derives:** `reference/hallmark-macrostructures.md`, `reference/hallmark-custom-theme.md`,
  `reference/hallmark-slop-gates.md`, and two marked blocks in the otherwise-original
  `reference/svg-assets.md` (from `references/assets.md`)
- **Fidelity:** rule text, tables, palettes and stamps verbatim in source order. Selection at
  block granularity — whole blocks kept or dropped, never edited. Additions are confined to `>`
  blockquotes headed *Extraction note*. See `MANIFEST.md` §§ 9–11b.

## 3. Web Interface Guidelines (Vercel Labs) — MIT

- **Upstream:** <https://github.com/vercel-labs/web-interface-guidelines>, `command.md` at commit
  `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1` (re-diffed at that commit, identical)
- **Licence:** MIT — `licenses/vercel-web-interface-guidelines-MIT.txt`
- **Copyright:** (c) 2025 Vercel Labs
- **Derives:** `guidelines-and-review.md`
- **Fidelity:** every rule verbatim, in source order, under its source heading. Two mechanical
  changes only: section headings demoted `###` → `##`, and the upstream `## Output Format`
  section plus the `$ARGUMENTS` preamble dropped (this skill's Runbook 3 owns its own reporting
  format). No rule was reworded, reordered or removed. See `MANIFEST.md` § 12.

## 4. impeccable — Apache-2.0

- **Upstream:** <https://github.com/pbakaus/impeccable>, v4.1.0 (engine 0.1.5), commit
  `cb56ed6c19a07329a9fa0cd4e657bee040156593` (10 extracted files re-diffed at that commit, all
  identical). **Not current HEAD** — upstream added a `generate` verb on 2026-09-15, so its
  verb table now holds 24 rather than the 23 recorded here. See `MANIFEST.md` § Pinned
  provenance.
- **Licence:** Apache License 2.0 — `licenses/impeccable-APACHE-2.0.txt`
- **Upstream NOTICE:** `licenses/impeccable-NOTICE.md`, reproduced in this skill's `NOTICE` per
  Apache-2.0 § 4(d)
- **Copyright:** 2025 Paul Bakaus
- **Derives:** `reference/impeccable-anti-patterns.md`, `reference/impeccable-artifacts.md`,
  `reference/impeccable-commands.md`, `reference/impeccable-detector-rules.md`,
  `data/impeccable-detector-rules.csv`, and two otherwise-original files that embed verbatim
  upstream fragments — `reference/contract.md` (the PRODUCT.md / DESIGN.md schemas, their
  bracketed field prompts and the `<!-- impeccable:product-schema 1 -->` stamp) and
  `reference/runbook-create.md` (the three opening questions from `init.md`)
- **Modifications** (Apache-2.0 § 4(b)): every one of those files is a modified derivative and
  carries a change notice at its head. Ban-list and schema text is verbatim; process prose is
  summarised; `data/impeccable-detector-rules.csv` is a tabular extraction of the rule registry
  in `crates/foundation/src/registry.rs` plus the trigger conditions read out of the check
  implementations. See `MANIFEST.md` §§ 13–16.

---

## Obligations this file discharges

| Obligation | Where |
|---|---|
| MIT: copyright + permission notice with substantial portions (×3) | `licenses/*-MIT.txt`, table above |
| Apache-2.0 § 4(a): copy of the Licence | `licenses/impeccable-APACHE-2.0.txt` |
| Apache-2.0 § 4(b): modified files carry prominent change notices | head of each `reference/impeccable-*.md`, plus `reference/contract.md` and `reference/runbook-create.md`; for the CSV, the sibling `data/impeccable-detector-rules.NOTICE.md` (a comment line inside a CSV breaks naive parsers); `MANIFEST.md` § 17 |
| Apache-2.0 § 4(c): retain attribution notices from the source | § 4 above, `NOTICE` |
| Apache-2.0 § 4(d): reproduce the upstream NOTICE | `NOTICE`, `licenses/impeccable-NOTICE.md` |

## Fonts

`data/typography.csv` names Google Fonts families and emits their CDN URLs. **No font binary is
distributed with this skill** and no font licence is bundled — upstream's
`data/google-font-licenses.json` was not extracted (`MANIFEST.md` § 8). A project that ships a
font is responsible for that font's own licence, usually the SIL Open Font License.
