# The primitive seam incidence misses the standard limiting-absorption weight by the endpoint one-half

> **Withdrawn for the completed centered carrier.** The successor packet
> `correction-the-centered-joint-cut-column-has-a-bounded-common-mode-not-an-unbounded-outgoing-wall-column.md`
> shows that this calculation used one fixed uncentered polynomial weight.
> The retained constructor translates the graph weight with each seam label
> and decomposes the joint column as \(p^{-1/2}\Phi+r_p\). The endpoint
> incompatibility below is only a warning for the uncentered realization.

## Question

Can the seam-weighted Hilbert--Schmidt incidence be composed with the standard
limiting-absorption boundary value of the translation generator?

## Weighted history spaces

For the bilateral translation generator, the ordinary limiting-absorption
principle uses weighted spaces

\[
L^2_\sigma\longrightarrow L^2_{-\sigma},
\qquad
\sigma>\frac12.
\]

The theta forcing is rapidly decaying and belongs to every such positive
weighted space. The arithmetic incidence requires a separate test because its
primitive cut atoms move to logarithmic locations.

## Primitive column growth

The primitive column is

\[
b_p=p^{-1/2}u_{\log p}.
\]

The cut atom has scale-independent ordinary norm, but its seam component is a
translate concentrated at distance comparable to \(\log p\). Consequently,
for a polynomial history weight,

\[
\|u_{\log p}\|_{L^2_\sigma}^2
\asymp
(1+\log p)^{2\sigma}
\]

up to constants independent of sufficiently large \(p\). The tail component
decays and does not remove this translated seam contribution.

After identifying the source metric

\[
\|x\|_U^2=
\sum_p(\log p)|x_p|^2
\]

with ordinary \(\ell^2\), the weighted Hilbert--Schmidt budget is therefore
comparable to

\[
\sum_p
\frac{(\log p)^{2\sigma}}{p\log p}
=
\sum_p
\frac{(\log p)^{2\sigma-1}}p.
\]

## Exact threshold

Prime-density comparison gives

\[
\sum_p
\frac{(\log p)^{2\sigma-1}}p
\quad\text{the same convergence threshold as}\quad
\int^\infty
\frac{(\log t)^{2\sigma-2}}t\,dt.
\]

With \(u=\log t\), this is

\[
\int^\infty u^{2\sigma-2}\,du,
\]

which converges exactly when

\[
\sigma<\frac12.
\]

Thus

\[
B_\Sigma:U\to L^2_\sigma
\]

is Hilbert--Schmidt only below the endpoint \(\sigma=1/2\), while the standard
translation limiting-absorption theorem requires \(\sigma>1/2\).

There is no admissible exponent common to the two estimates.

## Scope

This does not refute existence of a more structured boundary value for

\[
B_\Sigma^\dagger(A-x\mp i0)^{-1}B_\Sigma.
\]

Oscillation, reciprocal pairing, subtraction, or a Besov-type endpoint space
may still yield a relative limit. It does prove that ordinary polynomially
weighted \(L^2\) limiting absorption cannot be imported as a black box for the
primitive all-prime incidence.

Square and connected grades have stronger arithmetic decay and do not create
this endpoint obstruction. The failure is primitive.

## Required repair classes

A valid seam theorem must use at least one source-derived mechanism absent from
the standard estimate:

1. endpoint Besov or trace spaces adapted to translation;
2. reciprocal cancellation before taking the boundary limit;
3. an additional logarithmic source weight justified by the arithmetic
   carrier;
4. a renormalized relative resolvent in which the primitive divergent channel
   is explicitly subtracted;
5. a direct oscillatory prime estimate stronger than the absolute
   Hilbert--Schmidt budget.

## Disposition

The current seam-weighted incidence is bounded into ordinary history space but
misses the standard limiting-absorption domain by the exact endpoint
\(\sigma=1/2\). The seam-state gate is therefore blocked more sharply than a
missing generic theorem: the default weighted-space route is unavailable for
the primitive sector. No RH conclusion is authorized.
