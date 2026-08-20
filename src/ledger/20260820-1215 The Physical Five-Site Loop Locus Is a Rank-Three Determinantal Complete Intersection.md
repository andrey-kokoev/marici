---
title: "The Physical Five-Site Loop Locus Is a Rank-Three Determinantal Complete Intersection"
date: 2026-08-20
entry: 1215
status: active-supported-symbolic
sector: cosmology
---

# 1215 — The Physical Five-Site Loop Locus Is a Rank-Three Determinantal Complete Intersection

Sequence claim: `seqclaim-9c39a0e6d94ffd7b793fd143`.

## Source problem

Entry 1214 shows that the physical \(d=3\) five-cycle cannot use five
independent loop-edge variables. This entry derives the missing constrained
locus directly from Gram rank, retaining all five labelled occurrences.

## Labelled Gram-pivot chart

Choose a labelled nonsingular \(3\times3\) external Gram pivot \(H\). On
this chart write the fourth external vector as

\[
q_4=\sum_{i=1}^3c_iq_i.
\]

Let \(u=(\ell\cdot q_1,\ell\cdot q_2,\ell\cdot q_3)^T\), let \(v_4=\ell\cdot
q_4\), and let \(Y_1^2=\ell^2\). Rank three forces

\[
\boxed{L=v_4-c^Tu=0}
\]

and

\[
\boxed{
Q=\det(H)Y_1^2-u^T\operatorname{adj}(H)u=0.
}
\]

The first equation states that the mixed loop column obeys the same labelled
linear dependence as the external vectors. The second states that its norm is
the norm reconstructed from the pivot.

## Exact determinantal verification

Build the full \(5\times5\) Gram matrix of \((\ell,q_1,q_2,q_3,q_4)\).
Symbolica verifies that all 25 labelled \(4\times4\) row--column minors vanish
after imposing \((L,Q)\).

Moreover,

\[
\det\frac{\partial(L,Q)}{\partial(v_4,Y_1^2)}
=
\det(H),
\]

which is a unit on the chosen pivot chart. Hence the physical locus is a
regular codimension-two complete intersection:

\[
\boxed{
5\ \text{labelled edge variables}
-2\ \text{rank constraints}
=3\ \text{physical loop variables}.
}
\]

## Pivot covariance

Changing the nonsingular labelled \(3\times3\) pivot changes the local pair
\((L,Q)\) by an invertible generator transformation on overlaps. The global
object is the intrinsic rank-\(\le3\) determinantal locus, not any selected
pivot presentation.

## Classification

\[
\boxed{
\text{physical dimensional reduction}
=
\text{restriction to existing external-Gram determinantal support}.
}
\]

No new cosmological carrier stratum is required. The source's reduction from
five edge variables to three is already encoded by the labelled Gram carrier.

## Remaining measure calculation

This entry derives the physical support but not its induced current. The next
step is the coarea/Poincare-residue reduction of the five-variable
Cayley--Menger measure along \((L,Q)\), including its Jacobian, orientation,
and boundary current. Only that three-dimensional current can test physical
activation of the endpoint conductor or any Kummer coefficient.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_d3_rank_constrained_cm.rs`
- `research/benincasa/results/five-site-d3-rank-constrained-cm.json`
