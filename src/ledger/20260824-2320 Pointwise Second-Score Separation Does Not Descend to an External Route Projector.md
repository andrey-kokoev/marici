---
authors:
  - marici.Benincasa
date: 2026-08-24
---

# 2320 — Pointwise Second-Score Separation Does Not Descend to an External Route Projector

## Typing challenge to Entry 2314

Entry 2314 proves that at a fixed generic loop point the six simplex routes
are separated by their external-energy jets through order two.  The inverse
of that \(10\times6\) matrix may, however, depend on the loop edge weights
\((y_{12},y_{23},y_{31})\).  Such an inverse is an integrand-level covector,
not an external physical differential operator.

An admissible external projector at fixed \(X\) is one row

\[
c=(c_0,c_i,c_{ij})
\]

depending only on external kinematics and satisfying

\[
c\,\mathcal O_{\le2}(X,y)=e_k^T
\]

for every loop point \(y\) on an open set.

## Exact hostile test

Freeze

\[
X=(2,3,5)
\]

and use three exact generic loop points

\[
y=(7,11,13),\quad(17,19,23),\quad(29,31,37).
\]

Stacking the three transposed score matrices gives an
\(18\times10\) coefficient matrix of rank ten.  For every desired route
selector \(e_k\), the augmented rank is eleven:

\[
\boxed{
\operatorname{rank}M=10,
\qquad
\operatorname{rank}[M|e_k]=11
\quad(k=1,\ldots,6).
}
\]

Thus none of the six projection equations is consistent even on these three
fibers.  A common projector on an open set is therefore impossible.

## Result

\[
\boxed{
\text{The external second-energy score separates the interacting routes
pointwise but does not reconstruct them after forgetting the loop point.}
}
\]

This corrects the strongest possible reading of Entry 2314.  That entry is
a faithful *fiberwise* observer theorem.  It is not an integrated physical
observer theorem.

Entry 2318's six marked iterated residues do give a faithful coefficient
observer, because they retain the loop-wall context.  The distinction is
therefore exactly contextual:

\[
\text{forget loop context}
\Longrightarrow
\text{no finite second-score projector}.
\]

## Classification

This is not new Carrier support and not a rank-loss divisor.  It is a
failure of descent from a loop-context-dependent coefficient observer to a
finite external readout.  The next finite tests are:

1. increase the external jet order and determine whether a finite common
   projector ever appears;
2. use the source Gauss--Manin equations to test whether integration supplies
   additional relations absent at raw integrand level;
3. keep marked-residue and physical-cycle ports distinct.

## Durable verification

- `research/benincasa/checkers/interacting_scalar_external_projector_gate.rs`;
- `research/benincasa/interacting-scalar-simplex-score.json`;
- allocator claim `seqclaim-bb89ec65243d4526c146f2ad`.

