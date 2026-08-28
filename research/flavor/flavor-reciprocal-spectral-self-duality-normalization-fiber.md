# Reciprocal Spectral Self-Duality Has a Normalization Fiber

## Question

Can inversion symmetry remove WP839's spectral-action coefficient freedom and
select the portal magnitude without a fitted coefficient?

## Coefficient-free reciprocal action

On the current-aligned spectral ray (D_m=mH_q), introduce a comparison scale
(L>0) and the dimensionless coordinate

\[
z=\frac{m^2}{L^2}.
\]

The reciprocal action

\[
\mathcal R(z)=z+z^{-1}
\]

is invariant under (z\mapsto z^{-1}), obeys
(\mathcal R(z)\geq2), and has the unique positive minimum (z=1). Unlike
WP839's polynomial family, reciprocity forces the relative coefficients of
the two monomials to agree.

This is a genuine dimensionless selector: conditional on the comparison
scale, it fixes (m=L). It is also covariant under the common rescaling

\[
(m,L)\mapsto(\lambda m,\lambda L).
\]

Therefore it does not select the absolute scale (L).

## Dimensionless portal hostile

The same issue persists even if reciprocity is applied directly to the
dimensionless fixed-point coordinate. For a normalization (eta>0), set

\[
z=\eta x,
\qquad
\mathcal R_\eta(x)=\eta x+\frac1{\eta x}.
\]

The unique minimum is (x_*=1/\eta). Both (eta=2) and (eta=3) have the
identical abstract inversion law (z\mapsto z^{-1}), but they select

\[
x_*^{(2)}=\frac12,qquad
x_*^{(3)}=\frac13.
\]

With primitive charge contrast one, the corresponding portals are
(1/\sqrt2) and (1/\sqrt3). Reciprocity fixes a self-dual point only after
the map from the physical coupling to the reciprocal coordinate has been
normalized.

## Source typing

The inversion (m\mapsto L^2/m) already contains (L). Likewise,
(x\mapsto1/(\eta^2x)) contains (eta). Calling either transformation a
symmetry does not derive its reference unit. A source-authorized reciprocity
principle must therefore supply:

1. the physical variable on which inversion acts;
2. the invariant pairing that fixes its normalization;
3. the comparison scale or dimensionless unit;
4. the map from the self-dual coordinate into the beta system.

Without these data, self-duality is a family of conjugate presentation laws,
not a unique physical selector.

## Consequence for the active objective

Reciprocity is progressive because it can remove the relative coefficient
freedom of a two-sided action. It does not yet make the portal unavoidable.
The exact surviving fiber is the normalization (eta), or equivalently the
comparison scale (L). The next admissible positive route must derive this
normalization from the same primitive source—most plausibly through a
quantized pairing or a calibrated common clock—and then show that the induced
self-dual point is a controlled fixed point with a global basin and surviving
threshold readout.

## Verdict

Conditional relative-scale selector; absolute-scale and coupling-
normalization rigidifier only. The smallest exact falsifier is the pair
(eta=2,3), which shares the same reciprocal germ but predicts distinct
portal magnitudes.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp840_reciprocal_spectral_self_duality_normalization_fiber.py
```
