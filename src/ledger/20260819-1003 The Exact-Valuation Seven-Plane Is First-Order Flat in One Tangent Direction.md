# The Exact-Valuation Seven-Plane Is First-Order Flat in One Tangent Direction

## From ambient flatness to the intrinsic object

Entry 994 proves that the full length-three Rees cokernel has no first-order
tangential obstruction along

\[
(X_1,X_2,X_3)=(2+\tau,3,5+\tau+\Lambda).
\]

That ambient statement does not by itself prove flatness of

\[
E_2(C)=
\frac{\ker\Lambda\cap\operatorname{im}\Lambda}
     {\ker\Lambda\cap\operatorname{im}\Lambda^2}.
\]

The missing data are the mixed ranks at normal lengths one and two.

## Complete truncation census

Over

\[
B=\mathbf F_{32003}[\tau]/(\tau^2),
\]

exact syzygy-derivative reduction gives

\[
\begin{array}{c|c|c|c}
k&\operatorname{rank}R_{k,\tau}
&2\operatorname{rank}R_k&\text{excess}\\
\hline
1&12610&12610&0\\
2&25230&25230&0\\
3&37864&37864&0.
\end{array}
\]

Thus all three truncated cokernels are free over \(B\).  With 11520
ambient columns per normal grade, their dimensions over the ground field are

\[
\dim C_{1,\tau}=2(11520)-12610=10430,
\]

\[
\dim C_{2,\tau}=4(11520)-25230=20850,
\]

\[
\dim C_{3,\tau}=6(11520)-37864=31256.
\]

## Exact-valuation dimension

Because \(C_{3,\tau}/\Lambda^jC_{3,\tau}\simeq C_{j,\tau}\),

\[
\dim\operatorname{im}\Lambda
=31256-10430
=20826,
\]

and

\[
\dim\operatorname{im}\Lambda^2
=31256-20850
=10406.
\]

Since \(\Lambda^3=0\),

\[
\dim E_{2,\tau}
=
\dim\operatorname{im}\Lambda
-2\dim\operatorname{im}\Lambda^2
=14.
\]

The special fiber has dimension seven.  Moreover, freeness of the three
truncated cokernels makes the corresponding image and kernel sequences free
over the local principal ring \(B\).  The inclusion defining the denominator
is therefore saturated, and the exact-valuation quotient is free of rank
seven:

\[
\boxed{
E_{2,\tau}\simeq B^7.
}
\]

## Meaning

The rank-seven object is no longer merely pointwise stable or unobstructed
inside its ambient length-three cokernel.  It survives the source-derived
first tangential deformation as an intrinsic dual-number-flat subquotient.

This still does not choose a basis or produce a connection matrix.  A free
first-order deformation admits trivializations, but the canonical
Gauss--Manin transport must be derived from the source relations and checked
against occurrence symmetry.

Only the \(X_1\) tangential direction is proved here.  The independent
\(X_2\) mixed calculation remains in progress.

## Next gate

1. replicate all three truncation ranks in the \(X_2\) direction;
2. derive the connection class on the free rank-seven deformation without
   choosing elimination witnesses;
3. test occurrence covariance and compare with the generic rank-seven
   algebraic kernel.

## Durable artifacts

- `research/nima/export_triangle_wall_dual_rows.py`;
- `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- `research/nima/triangle-wall-dual-relation-rank.json`.

## Sequence

- allocator claim: `seqclaim-f72b9ab610cc6f716b4e8b99`.
