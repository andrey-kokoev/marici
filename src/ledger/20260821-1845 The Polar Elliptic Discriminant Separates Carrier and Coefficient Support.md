# 1845 — The Polar Elliptic Discriminant Separates Carrier and Coefficient Support

## Invariant Hessians

At an interior point of focal segment \(i\), let \(e_i\) be its unit tangent,
\(R_i\) its length, and \(s_i\in(0,R_i)\) the intersection parameter.  The
distance-sum Hessian is

\[
H_i
=
h_i(I-e_ie_i^T),
\qquad
h_i=\frac{R_i}{s_i(R_i-s_i)}>0.
\]

If \(\theta\) is the angle between the two segment directions, direct
determinant reduction gives

\[
\boxed{
\det(xH_1+(1-x)H_2)
=
x(1-x)h_1h_2\sin^2\theta
\bigl(xh_1+(1-x)h_2\bigr).
}
\]

## Explicit elliptic family

Up to a nonzero square and unit, Entry 1844's curve is

\[
w^2
=
x(1-x)
\bigl(xh_1+(1-x)h_2\bigr)
\bigl(x\delta_1+(1-x)\delta_2\bigr).
\]

Its four branch points are

\[
0,\quad
1,\quad
-\frac{h_2}{h_1-h_2},\quad
-\frac{\delta_2}{\delta_1-\delta_2}.
\]

## Discriminant support

Branch collisions factor into four typed classes:

1. \(\sin\theta=0\): parallel or coincident focal directions, a deeper Gram
   degeneration;
2. focal endpoints encoded by degeneration of \(h_i\): existing soft support;
3. \(\delta_1\delta_2=0\): the two existing labelled wall normals;
4. the residual collision
   \[
   \boxed{h_1\delta_2-h_2\delta_1=0.}
   \]

The fourth divisor is internal coefficient support: it equates the two
normal deformations after weighting by the source-derived transverse
Hessians.  It is not a new incidence condition on the carrier.

## Architectural result

Every geometric degeneration of the elliptic family lies on already frozen
Gram, soft, or wall support.  The only residual divisor is generated inside
the elliptic coefficient object itself.

Thus the polar boundary gives another exact H2 pattern:

\[
\boxed{
\text{shared existing carrier}
+
\text{sector-specific elliptic discriminant}.
}
\]

## Next falsifier

Compute the Legendre cross-ratio of these four branch points and its
nearby-cycle limits on each support factor.  Test whether the residual
coefficient collision has Tate/Kummer degeneration without adding carrier
incidence.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_polar_elliptic_discriminant.py`
- `research/benincasa/results/five-site-region-pair-polar-elliptic-discriminant.json`
- Entries 1843--1844
- allocator claim: `seqclaim-0e937fe00c77aeca96ef073a`
