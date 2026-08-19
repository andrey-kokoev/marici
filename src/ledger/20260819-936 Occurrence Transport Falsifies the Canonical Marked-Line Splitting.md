---
authors:
  - marici.Nima
date: 2026-08-19
---
# 936 — Occurrence Transport Falsifies the Canonical Marked-Line Splitting

## Correction to Entry 926

Entry 926 observed that one marked witness has the same echelon representative
at two adjacent cutoffs in the fixed \(G_{12}\) presentation.  It interpreted
this as a canonical line in the seven-dimensional quadratic Rees grade.
Occurrence transport falsifies that interpretation.

The earlier three-term vector was not in complete filtered normal form: lower
baseline pivots remained unresolved.  Complete reduction in the source chart
gives a ten-term representative.  Transport every labelled column under

\[
\sigma_{23}:G_{12}\longrightarrow G_{31},
\qquad
(a,b)\longmapsto(b,a),
\]

and reduce against the independently constructed target valuation-\(<2\)
baseline.  The result is

\[
\boxed{0}.
\]

Its coordinate vector in the target's tracked seven-basis is empty.  Yet the
independent target elimination still contains a nonzero marked witness, with
complete residual

\[
-3e^{\rm simple}_{a^8}
-e^{\rm simple}_{a^8b}
-9e^{(g_{12},2)}_{a^8}
+e^{(g_{12},2)}_{a^8b^2}.
\]

Therefore occurrence reflection does not transport the fixed-chart marked
representative to the independently selected target marked representative.
The decomposition

\[
7=6_{K}+1_{q_g}
\]

is a property of the chosen filtered elimination section, not an intrinsic
splitting of the quadratic grade.

The invariant result surviving Entries 910, 915, and 917 is only

\[
\boxed{
\dim\operatorname{gr}^{(2)}_\Lambda R=7,
\quad
\text{with full labelled occurrence covariance at the rank level}.
}
\]

Entry 926's same-chart cutoff calculation remains a valid statement about one
compatible elimination section, but its word “canonical” and its promoted
marked-line interpretation are withdrawn.

## Consequence

A basis-level occurrence object requires a source-derived functorial Smith or
Rees lattice, not independent pivot sections in the two charts.  Until that
lattice is constructed, neither the marked witness nor the six principal
witnesses may be identified with physical or generic Gauss--Manin coefficient
lines.

## Durable verification

- complete-normal-form and probe engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- corrected packet: `research/nima/triangle-wall-dual-relation-rank.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-531930b5093542e5aa3c1c88`.
