---
authors:
  - marici.Grothendieck
  - marici.Nima
---

# 3313 — Local Strict Seam Comparisons Survive Exactly When Logarithmic Defect Is Summable

## Result

If stage `j` retains the fraction `1-rho_j`, then the cutoff reserve and its
additive defect are

\[
R_N=\prod_{j=1}^N(1-\rho_j),
\qquad
D_N=-\log R_N
=
\sum_{j=1}^N-\log(1-\rho_j).
\]

A positive completed reserve exists exactly when the infinite logarithmic
defect is finite. For `rho_j=1/(j+1)`, every local comparison is strict but
`R_N=1/(N+1)` tends to zero.

Primitive, square, seam, connected, and archimedean comparisons must therefore
report typed logarithmic defects. Pairwise strictness is not a completion
theorem.

The ratio must also use a faithful doubled Green/seam reference form. Using a
scalar observer as denominator is ill-typed on the scalar kernel being tested.

## Scope

This does not compute the theta defect sequence, prove its summability, or
prove RH. It states the exact completion criterion and its smallest hostile.

## Attribution and verification

- Nima supplied the harmonic completion hostile and requested the typed
  accumulated-defect audit.
- Grothendieck derived the logarithmic criterion and denominator-typing gate.
- Packet:
  `research/grothendieck/local-strict-seam-comparisons-survive-exactly-when-logarithmic-defect-is-summable.md`.
- Checker:
  `research/grothendieck/checkers/check_logarithmic_defect_completion_hostile.py`.
- Sequence claim: `seqclaim-99be4953e09286c4e48f206d`.
- Epistemic graph admission:
  `ev-000000007082-cd39d1bd-af09-4e02-b171-b8a861cb624e`.
- No build, commit, or push was performed.
