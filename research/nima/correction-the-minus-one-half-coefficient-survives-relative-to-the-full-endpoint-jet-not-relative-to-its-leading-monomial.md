# Correction: the minus-one-half coefficient survives relative to the full endpoint jet, not relative to its leading monomial

## Question

Does the jet-dependent curvature correction rule out a fixed relative
ordinary-overlap multiplier at first subleading order?

## Claim boundary

No. The full combined jet has a jet- and parameter-dependent coefficient when
expanded relative to its leading monomial. But the ordinary jet remains
\(-1/(2\Lambda)\) times the full endpoint jet at the first relative order.
Thus a fixed shell multiplier can reproduce the two-term asymptotic if it acts
on the complete endpoint section, including curvature and parameter
dependence. It cannot reproduce the exact bulk density without an additional
source identity.

## Two valid normalizations

Let

\[
 E_j=\partial_z^jI^{({\rm end})},
 \qquad
 O_j=\partial_z^jI^{(0)},
 \qquad
 L=\Lambda(a).
\]

The curvature-aware expansions give

\[
 E_j
 =(-1)^j\frac{j!\Phi(a)^2}{L^{j+1}}
 \left[
 1-\frac{(j+1)(z+j+2)}{L}+O(L^{-2})
 \right],
\]

and

\[
 O_j
 =(-1)^{j+1}\frac{j!\Phi(a)^2}{2L^{j+2}}
 \left[1+O(L^{-1})\right].
\]

Therefore

\[
 \frac{O_j}{E_j}
 =-\frac1{2L}+O(L^{-2})
\]

for every fixed \(j\).

## Leading-monomial expansion

If one instead factors only

\[
 (-1)^j\frac{j!\Phi(a)^2}{L^{j+1}},
\]

then

\[
 E_j+O_j
 =(-1)^j\frac{j!\Phi(a)^2}{L^{j+1}}
 \left[
 1-\dfrac{(j+1)(z+j+2)+1/2}{L}
 +O(L^{-2})
 \right].
\]

The jet dependence comes from the endpoint section itself. The extra ordinary
correction is still the universal \(1/2\) in this bracket.

## Consequence for response models

A response of the asymptotic form

\[
 R_j
 =-\left(1-\frac1{2L}+O(L^{-2})\right)E_j
\]

matches the combined endpoint-plus-ordinary shell through first relative
order for every fixed jet, provided the multiplier acts on one entire endpoint
section before differentiation.

Thus the statement that no fixed scalar correction can match the jet hierarchy
was too strong.

## What remains impossible to infer

This asymptotic proportionality does not identify the exact ordinary shell
with a boundary trace. The exact ordinary term is

\[
 I^{(0)}(z)
 =-\int_0^\infty e^{-zt}\rho_{a,b}(t)\,dt,
\]

where \(\rho_{a,b}\) is the completed-theta bulk autocorrelation density. Exact
equality with a scalar endpoint multiplier would force a density-level source
identity, not merely agreement of two asymptotic coefficients.

## Corrections to prior packets

- `the-reciprocal-linking-shell-must-match-a-two-term-asymptotic-not-only-the-leading-endpoint-flux.md` correctly identified the relative ordinary/end ratio at first order, but its displayed total response omitted curvature because it factored the leading monomial.
- `correction-the-first-subleading-late-shell-coefficient-includes-theta-curvature-and-the-evans-parameter.md` correctly repaired the leading-monomial expansion but retracted the \(-1/2\) ratio too broadly.
- `every-fixed-evans-jet-has-a-distinct-curvature-corrected-late-shell-coefficient.md` correctly computed the jet-dependent total bracket, but its claim excluding a fixed multiplier is withdrawn.

## Correct hostile

The first-order asymptotic test has two layers:

1. verify that the proposed response transports the full curvature-aware
   endpoint section;
2. verify the additional relative multiplier \(1-1/(2L)\).

Passing both is necessary but not sufficient. Exact candidate-one closure still
requires equality of the complete source densities and all finite shells.

## Disposition

The universal minus-one-half coefficient survives in endpoint-relative
normalization. The jet-dependent coefficient belongs to leading-monomial
normalization. Their distinction removes the apparent contradiction and leaves
the exact bulk-to-boundary source identity open. No RH conclusion is
authorized.
