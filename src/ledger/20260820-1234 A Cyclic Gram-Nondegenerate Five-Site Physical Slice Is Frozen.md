# Entry 1234 — A Cyclic Gram-Nondegenerate Five-Site Physical Slice Is Frozen

> **Superseded and retyped by Entry 1256.** The displayed vectors obey
> \(\sum_iP_i=(0,0,5)\neq0\), so this is a Gram-nondegenerate algebraic slice,
> not a physical momentum-conserving slice. All downstream calculations remain
> algebraically valid only in that narrower scope.

## Purpose

Entry 1233 requires a one-parameter physical family frozen before period evaluation. A planar regular pentagon would make the physical three-dimensional routing Gram degenerate. Use instead a regular cone orbit.

## Spatial resultants

For $k=0,\ldots,4$, set

\[
P_k
=
\left(
\cos\frac{2\pi k}{5},
\sin\frac{2\pi k}{5},
1
\right).
\]

Then

\[
P_i^2=2,
\]

and the cyclic dot products are

\[
P_i\cdot P_{i\pm1}
=
\frac{3+\sqrt5}{4},
\]

\[
P_i\cdot P_{i\pm2}
=
\frac{3-\sqrt5}{4}.
\]

The five-vector Gram matrix has rank three, exactly as required in physical $d=3$.

## Routing Gram

Choose the source routing basis

\[
q_1=P_1,
\qquad
q_2=P_1+P_2,
\qquad
q_3=P_1+P_2+P_3.
\]

Exact Symbolica evaluation gives

\[
\boxed{
\det H
=
\frac58(5-\sqrt5)>0.
}
\]

Thus the family is Gram-nondegenerate and lies on the physical Euclidean contour.

## One parameter

Set all five site energies equal:

\[
X_1=\cdots=X_5=t.
\]

The real physical domain is

\[
t\ge\sqrt2.
\]

It is realizable by adding opposite external-momentum pairs at each site, which increase the sum of external magnitudes without changing the resultant $P_k$.

The analytic parameter is $t$, with

\[
E_T=5t.
\]

At generic $t$, all site momenta are nonsoft and the routing Gram determinant is fixed and nonzero. The family has exact $C_5$ symmetry.

## Frozen period

Restrict Entry 1233's scalar period to this family:

\[
\Pi_{C_5}^{\rm cyc}(t)
=
\Pi_{C_5}(X_i=t,P_k).
\]

This slice and normalization are frozen before numerical evaluation, recurrence search, or creative telescoping.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_physical_slice.rs`
- `research/benincasa/results/five-site-cyclic-physical-slice.json`

## Next falsifier

Derive the specialized rational integrand on the physical $u_1,u_2,u_3$ variables and enumerate its exact singular polynomials in $t$. These source-derived singularities must bound any scalar annihilator denominator before numerical period sampling. Do not infer an operator order from fitted values.
