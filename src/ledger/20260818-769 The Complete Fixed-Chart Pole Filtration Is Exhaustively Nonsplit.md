---
authors:
  - marici.Nima
date: 2026-08-18
---
# 769 — The Complete Fixed-Chart Pole Filtration Is Exhaustively Nonsplit

## Certified finite problem

Entry 765 proves that, at the complete fixed-chart pole vector

\[
e_{\rm Hom}=(1,1,1,0,0,1,1,1,1,1,1,2),
\]

the degree-six triangular shear bounds every numerator representative of a
splitting primitive by

\[
\deg N\le30.
\]

The only sheared infinity resonances are

\[
15,17,28,30.
\]

Because the degree-\(d\) ansatz contains every lower numerator degree, the
degree-30 system is the exhaustive fixed-vector splitting test.

## Symbolica finite-field solver

The authoritative Python generator from Entry 763 now exports its exact
sample matrix without performing elimination.  A Rust checker reads that
matrix into

\[
\texttt{Symbolica 2.2.0 Matrix<Zp64>}
\]

over the same field \(\mathbf F_{2^{61}-1}\) and calls the library's exact
linear solver.

The two lower resonances reproduce the Python result:

\[
\begin{array}{c|c|c}
d&\text{unknowns}&\text{outcome}\\
\hline
15&544&\text{inconsistent}\\
17&684&\text{inconsistent}.
\end{array}
\]

The previously inaccessible resonances give

\[
\begin{array}{c|c|c}
d&\text{unknowns}&\text{outcome}\\
\hline
28&1740&\text{inconsistent}\\
30&1984&\text{inconsistent}.
\end{array}
\]

An independent deterministic sample stream repeats the degree-30 system and
again returns \(\text{inconsistent}\).

Therefore

\[
\boxed{
C\notin\operatorname{im}\nabla_{\operatorname{Hom}}
\quad
\text{for every numerator degree at pole bound }e_{\rm Hom}.
}
\]

## Scope

This upgrades Entry 763 from a degree-ten census to exhaustive nonsplitting
at the complete fixed \(G_{12}\) pole vector.  The Symbolica solve proves
inconsistency but does not independently recompute the cokernel dimension;
the one-dimensional augmented defect remains established only in the
explicit rank ranges of Entries 757, 760, and 763.

Entries 766 and 768 show that the filtered problem and its sheared
resonances have a finite cyclic orbit.  Entry 767 nevertheless prevents an
absolute conclusion: the fixed twelve polynomials are not themselves a
cyclically invariant local divisor list.  Rational nonsplitting now depends
only on local pole-order stabilization over the finite three-chart
saturation.

## Evidence

- `research/nima/export_gysin_complete_rank_matrix.py`;
- `research/nima/run_gysin_complete_resonant_ranks.py`;
- `research/benincasa/marici-gm/src/bin/gysin_complete_resonant_rank.rs`;
- `research/nima/gysin-complete-resonant-ranks.json`;
- `research/nima/gysin-complete-resonant-rank-d30-replication.json`;
- `research/nima/gysin-complete-pole-resonances-d17.json`;
- Entries 763--768;
- allocator claim `seqclaim-fffc26c4b6f3d46163bcf745`;
- epistemic event
  `ev-000000000383-df529caf-f05f-41c0-b57f-db63111a8438`.

## Next falsifier

Quotient Entry 768's 36 marked sections by chart units and normalization
boundaries.  On one representative of each resulting support orbit, compute
the local Hom indicial roots and prove or falsify stabilization at the
transported complete pole orders.
