---
id: 504
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Naive Even Cartier Action Does Not Descend

Entry 502 proposes a Smith or minimal-presentation calculation over

\[
A_+=\mathbb Q[x]/(x^2),\qquad x=a^2.
\]

Before that calculation, (x) must act on the complete exact cokernel.
This is not automatic: Entry 449 already found multiplication commutators
for the frozen exact image.

Using the complete frozen four-sector exact matrix, multiply every admissible
exact-image column by (a^2), retaining only columns whose full support lies
inside the cutoff.  At

\[
D=12,16,20,24,28
\]

the enlarged image has one additional rank in every case:

\[
\boxed{
\operatorname{rank}(operatorname{im}d+a^2operatorname{im}d)
-\operatorname{rank}(operatorname{im}d)=1.
}
\]

Therefore

\[
\boxed{
a^2\operatorname{im}d\not\subseteq\operatorname{im}d.
}
\]

## Consequence

The cyclic local-cohomology object (A_+\eta) of Entry 502 is valid in the
conormal coefficient model, but the complete orbit cokernel is not yet an
(A_+)-module.  A Smith form over (A_+) is therefore undefined on the
naive presentation.

The stable rank-one multiplication commutator is numerically compatible with
the plus defect, but this is not an identification.  The next comparison must
construct a chain homotopy correcting multiplication by (a^2), or prove
that no such correction exists.  Only the corrected action can test whether
the incidence generator (eta) supplies the invariant defect.

No new carrier datum is indicated.  The obstruction is failure of a
coefficient operation to descend through the exact differential.

## Next falsifier

Compute

\[
[d,a^2]
\]

sector by sector and seek a source-derived homotopy through the retained
gradient/Kodaira--Spencer complex.  If it is nullhomotopic, repeat Entry
502's module presentation with that corrected action.  If it is not, the
even-incidence explanation of the plus defect fails in its present form.

## Evidence

- `research/benincasa/marici-gm/src/bin/soft_axis_plus_defect_module.rs`;
- Entries 449, 473, 500, 501, and 502.
