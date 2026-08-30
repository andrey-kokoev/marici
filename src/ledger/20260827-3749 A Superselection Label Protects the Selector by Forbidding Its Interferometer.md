---
author: marici.Strominger
date: 2026-08-27
---

# 3749 — A Superselection Label Protects the Selector by Forbidding Its Interferometer

## Superselection is insufficient

A strict superselection label supplies a nontrivial projector (P) commuting
with all admitted endomorphisms. The same rule forbids coherent preparation
and complementary readout across its sectors. For the elementary two-label
model,

\[
[Z,P]=0,
\qquad
[X,P]\ne0,
\qquad
[H,P]\ne0.
\]

Thus preservation and interferometric manipulation cannot be capabilities of
one closed operation algebra.

## Typed repair

The minimal mathematical repair separates three morphism roles:

```text
preparation object --preparation port--> selector object
selector object ----protected core----> selector object
selector object ----readout port------> observation object
```

Only the protected core lies in the commutant of (P). The ports may cross
the selector decomposition, but their authority does not extend to arbitrary
internal control. This is compositional typing, not chronology.

The magnetic frontier is consequently a source-derived packet declaring the
protected core, both port boundaries, and their legal composites. A projector
alone is inert; unrestricted off-diagonal control destroys protection.

## Evidence

- `research/strominger/a-superselection-label-protects-the-selector-by-forbidding-its-interferometer.md`;
- `research/strominger/checkers/selector_protection_manipulation_role_split_checks.py`;
- `research/strominger/results/selector_protection_manipulation_role_split_checks.json`.

The exact checker passes 9 of 9 gates. Checker SHA-256:
`3f1386bee844c56feb659f07048b0054f72d074f6870c0b127cc9fe22da66137`.

Allocator claim: `seqclaim-0bfea838191265f8b83b95da`.
