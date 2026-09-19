# Apache-2.0 change notice — `impeccable-detector-rules.csv`

The notice lives beside the CSV rather than inside it: a comment line at the head of the file
would break `csv.DictReader` and every other naive parser, and a rule table that cannot be
parsed is worse than one whose notice sits next to it.

**Derived from** [pbakaus/impeccable](https://github.com/pbakaus/impeccable) v4.1.0
(engine `ENGINE_VERSION` 0.1.5).
**Licence:** Apache License 2.0, Copyright 2025 Paul Bakaus —
`licenses/impeccable-APACHE-2.0.txt`.
**Upstream NOTICE**, reproduced per Apache-2.0 § 4(d): `licenses/impeccable-NOTICE.md` and the
skill's root `NOTICE`.

## This file has been modified from the original

There is no upstream CSV. `impeccable-detector-rules.csv` is a **transformation of impeccable's
source code into a table**:

| Column | Where it came from |
|---|---|
| `Rule ID`, `Category`, `Scope`, `Severity`, `Name`, `Engines`, `Description` | the rule registry, `crates/foundation/src/registry.rs` (itself a port of `cli/engine/registry/antipatterns.mjs`) |
| `Trigger / Threshold` | **written for this skill** by reading each check's implementation. Not upstream prose. |

50 rules, one header row. No rule was invented, renamed, dropped or re-severitied. How to read
the table, and what each column means, is in `reference/impeccable-detector-rules.md`; the
extraction record is `MANIFEST.md` § 14 and every deviation from upstream is § 17.
