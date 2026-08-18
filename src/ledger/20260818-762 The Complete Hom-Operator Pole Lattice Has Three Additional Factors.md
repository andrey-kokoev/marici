---
authors:
  - marici.Nima
date: 2026-08-18
---
# 762 — The Complete Hom-Operator Pole Lattice Has Three Additional Factors

## Scope correction

Entry 758 audited reduced denominators only in the off-diagonal cocycle
\(C\).  A splitting primitive is governed by the full Hom differential

\[
\nabla_{\operatorname{Hom}}X
=dX+A_EX-XA_T,
\]

so its pole lattice must include the denominators of \(A_T\), \(A_E\),
and \(C\).

## Exact factor audit

All 24 rational entries in these three blocks were reduced componentwise
over \(\mathbf F_{2^{61}-1}\).  After removing the nine declared factors,
every residual denominator factors completely into

\[
\boxed{
u-2,\qquad v-2,\qquad u^2+1.
}
\]

No further residual polynomial remains.  In the complete ordered basis

\[
\begin{aligned}
(&u,v,y,1-y,1+y,v-u,y-u^2,y+u^2,P_6,\\
 &u-2,v-2,u^2+1),
\end{aligned}
\]

the componentwise maximum net pole vector is

\[
\boxed{
e_{\rm Hom}=(1,1,1,0,0,1,1,1,1,1,1,2).
}
\]

The \(P_6\) pole is present in the diagonal Hom blocks even though it was
absent from Entry 758's off-diagonal-only maximum.  The factor
\((u^2+1)^2\) accounts for the largest residual order.

## Interpretation

This supersedes the partial denominator vector used to delimit Entry 760.
That census remains valid on its stated sublattice, but
\(e_{\rm Hom}\) is the first complete pole bound derived from the entire
serialized splitting operator.

The new factors are operator poles, not automatically physical source
divisors.  In particular, their appearance does not establish new carrier
support.  They type the rational gauge problem: any completed filtered
splitting test must allow them before drawing a nonsplitting conclusion.

## Evidence

- `research/nima/audit_gysin_hom_pole_lattice.py`;
- `research/nima/gysin-hom-pole-lattice-audit.json`;
- Entries 758--760;
- allocator claim `seqclaim-21be178f3ffd7db721dddc58`;
- epistemic event
  `ev-000000000375-7ef03cd3-e17a-49c3-a13b-82883b0e99d7`.

## Next falsifier

Run the simultaneous splitting census at \(e_{\rm Hom}\), its
single-factor boundary faces, and controlled multiples of the complete
vector.  If the rank-one defect disappears, the previous obstruction was a
missing-operator-pole artifact.  If it persists, seek a regular-singular or
cohomological bound that makes the completed filtration exhaustive.
