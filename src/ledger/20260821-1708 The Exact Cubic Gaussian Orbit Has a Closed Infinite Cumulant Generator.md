# 1708 — The Exact Cubic Gaussian Orbit Has a Closed Infinite Cumulant Generator

## Completion falsifier

Entries 1692--1693 identify the first two non-Gaussian grades individually.
Derive the complete source-defined moment tower rather than extending finite
truncations by positivity alone.

## Exact generating germ

For an initially diagonal centered Gaussian with

\[
\langle Q^2\rangle=a,
\qquad
\langle P^2\rangle=b,
\]

the cubic unitary gives

\[
\Pi=P-t(Q^2-a).
\]

Gaussian integration yields the Weyl-ordered moment-generating germ

\[
M(x,y)
=e^{by^2/2+tay}
(1+2aty)^{-1/2}
\exp\!\left(\frac{ax^2}{2(1+2aty)}\right).
\]

Thus

\[
\boxed{
K(x,y)=\log M
=\frac b2y^2+tay-\frac12\log(1+2aty)
+\frac{ax^2}{2(1+2aty)}.
}
\]

The complete connected tower follows:

\[
\kappa_{QQ\Pi^r}=a(-2at)^r r!,
\]

and for `r>=3`,

\[
\kappa_{\Pi^r}
=(-1)^r2^{r-1}(r-1)!a^rt^r.
\]

All cumulants with more than two `Q` slots vanish.  The formulas reproduce

\[
\kappa_{QQ\Pi}=-2ta^2,
\qquad
\kappa_{QQ\Pi\Pi}=8t^2a^3,
\qquad
\kappa_{\Pi^4}=48t^4a^4.
\]

## Narrow result

\[
\boxed{
\text{the source cubic Gaussian sector has a closed infinite, density-representable cumulant coefficient object.}
}
\]

No flat-extension choice is required on this orbit.  The singular expression

\[
1+2aty=0
\]

belongs to the auxiliary dual variable of the generating germ; it is not a
new physical carrier divisor.

## Architectural consequence

The coefficient object is infinite but finitely presented by one logarithmic
and one rational generating term.  This is a sharper surviving form of H2:
the carrier remains the labelled Cut structure, while nonlinear dynamics is
encoded by a sector-specific completed cumulant algebra.

## Durable artifacts

- `research/benincasa/checkers/cubic_gaussian_cumulant_generator.rs`
- `research/benincasa/results/cubic-gaussian-cumulant-generator.json`
- `research/benincasa/cubic-gaussian-cumulant-generator.md`

## Next falsifier

Derive the Cut coproduct of the generating germ itself.  For independent and
then correlated Gaussian blocks, test whether cardinality-weighted substitution
and the mixed cubic cocycle reproduce the complete generator without
coefficient-by-coefficient fitting.
