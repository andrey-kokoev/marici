# 1315 — Affine Five-Site IBP Closure Begins Only After Forgetting the Infinity Boundary

> **RETRACTED.** The apparent degree-four closure used only three of the 32
> Kummer sheets and counted sheet rows rather than independent base points.
> The full-deck, independent-base-point rerun is inconsistent through degree
> five. See the next correction entry. This file is retained as a defect and
> provenance record; none of its positive closure claims remain admissible.

## Question

Can the frozen asymmetric five-cycle form admit a first-order scalar telescoper through a bounded polynomial integration-by-parts identity

\[
\partial_z\Omega+a(z)\Omega
=
\sum_{i=1}^3\partial_{u_i}(V_i\Omega),
\qquad \deg V_i\le d?
\]

This is only an affine discovery test. A physical period identity additionally requires the primitive to define a valid relative class at every boundary of the compactified integration chain.

## Frozen computation

The checker evaluates the complete 180-term canonical form with all five Kummer square roots retained. It works over two finite fields,

\[
\mathbf F_{1009},\qquad \mathbf F_{1013},
\]

at two projective fibers,

\[
z=7,\qquad z=11,
\]

and three deck sheets at independently generated generic points in \((u_1,u_2,u_3)\).

An earlier sampler accidentally placed all points on one affine line. That defect was found from the anomalously low rank pattern, repaired by independently evolving the three coordinates, and the complete census was rerun.

## Result

For unrestricted polynomial vector fields:

\[
d=0,1,2,3
\quad\Longrightarrow\quad
\text{inconsistent}
\]

at every tested prime and fiber.

At

\[
d=4
\]

the affine system becomes consistent. However the same system remains consistent after setting the scalar coefficient to zero:

\[
\partial_z\Omega
=
\sum_i\partial_{u_i}(V_i\Omega).
\]

Thus the affine identity does not determine a scalar Picard--Fuchs coefficient.

Imposing the coordinate-relative condition

\[
u_i\mid V_i
\]

shifts the first closure by one degree:

\[
d\le4: \text{inconsistent},
\qquad
d=5: \text{consistent}.
\]

Again the scalar-free system is already consistent.

## Interpretation

The scalar-free affine closure cannot be promoted to a period identity. The numerical period is nonconstant and satisfies the independently established scaling law

\[
\Pi(z)\sim C_5z^{-7}.
\]

Therefore the affine primitive necessarily carries nontrivial boundary data on the projective compactification, even though its pointwise divergence identity closes in the open chart.

The surviving narrow statement is

\[
\boxed{
\text{bounded affine IBP closes at degree four, but the closure forgets the infinity-relative structure.}
}
\]

Equivalently, increasing affine polynomial degree is now the wrong search direction. The next source-typed calculation must resolve the infinity strata and require the primitive to extend as a relative/logarithmic class there.

## Consequence for the Carrier program

This is a finite example of the distinction

\[
\text{absolute affine exactness}
\not\Rightarrow
\text{relative period exactness}.
\]

The obstruction is not evidence for a new carrier cell. It is evidence that the existing compactified carrier and its boundary incidence data must be retained by the telescoper reduction.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_first_order_ibp_pilot.rs`
- `research/benincasa/results/five-site-asymmetric-first-order-ibp-pilot.json`

## Next falsifier

Homogenize the degree-four primitive, restrict it to every labelled infinity stratum of the frozen projective alphabet, and compute its residue/costalk packet. Either:

1. all boundary classes cancel after the existing incidence differential, yielding a valid first-order relative telescoper; or
2. a nonzero supported boundary class survives, falsifying first-order closure in the relative complex.

No larger affine degree census is admissible before this boundary test.

Allocator claim: `seqclaim-63e2ebebf0ecc4a9c9e6cf23`.
