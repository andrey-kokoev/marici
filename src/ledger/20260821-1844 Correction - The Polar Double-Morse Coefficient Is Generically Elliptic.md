# 1844 — Correction: The Polar Double-Morse Coefficient Is Generically Elliptic

## Scope of the correction

Entry 1840 correctly derives the square-root scaling

\[
I(\delta,\delta)\sim\delta^{-1/2}
\]

and its Kummer monodromy.  Calling the **full** coefficient object rank one
was too strong.  The square-root character describes the common normal
scaling, not the complete two-normal period variation.

## Feynman-parameter reduction

Let \(H_1,H_2\) be the two rank-two transverse Hessians.  The local integral
is

\[
I(\delta_1,\delta_2)
=
\int_{\mathbb R^3}
\frac{d^3x}
{(x^TH_1x+\delta_1)(x^TH_2x+\delta_2)}.
\]

Using

\[
\frac1{pq}=\int_0^1\frac{ds}{(sp+(1-s)q)^2}
\]

and the three-dimensional Gaussian identity gives

\[
I
=
\pi^2\int_0^1
\frac{ds}
{\sqrt{\det(sH_1+(1-s)H_2)}
\sqrt{s\delta_1+(1-s)\delta_2}}.
\]

## Elliptic curve

Each Hessian has rank two, and their kernel lines are distinct.  Therefore

\[
\det(sH_1+(1-s)H_2)
=
s(1-s)L(s),
\]

with \(L(s)\) generically linear and nonzero on \((0,1)\).  The period curve
is

\[
\boxed{
w^2
=
s(1-s)L(s)
\bigl(s\delta_1+(1-s)\delta_2\bigr).
}
\]

For generic data this is a four-branch-point genus-one curve.  The complete
coefficient system is therefore a rank-two elliptic Gauss--Manin variation
with an overall square-root Kummer scaling character.

On the diagonal \(\delta_1=\delta_2=\delta\),

\[
I
=
\delta^{-1/2}
\times
\text{an elliptic period of }s(1-s)L(s).
\]

## Architectural result

The elliptic structure is compiled canonically from the two physical
Hessians.  Its carrier remains Entry 1839's existing Gram/segment-intersection
stratum.  Thus

\[
\boxed{
\text{existing carrier}
+
\text{Hessian-compiled elliptic coefficient object}.
}
\]

No new carrier datum is required, but the coefficient complexity is genuinely
rank two rather than rank one.

## Next falsifier

Compute \(L(s)\) invariantly from the two focal-segment directions and
distances.  Derive the elliptic discriminant and test whether every branch
collision lies on existing Gram, soft, or focal-length supports.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_polar_feynman_elliptic.py`
- `research/benincasa/results/five-site-region-pair-polar-feynman-elliptic.json`
- Entries 1839--1843
- allocator claim: `seqclaim-d4fa0cdb71ec43a250220042`
