# Cubic Hermite residual packet

## Grothendieck source

This formalizes the exact finite polynomial layer of
`research/grothendieck/theta-cubic-poisson-hermite-energy.md`.

## Formal objects

- `cubicQuadraticReserve` is the already-positive quadratic channel `k`.
- `cubicPointedChannel` is the signed cubic channel `e`, including `z2`.
- `cubicHermiteResidual=36*k^3-e^2` is the unresolved Schur direction.
- `single_scale_residual_identity` proves the exact one-atom formulas and
  residual `224*w^6*y^24`.
- `single_positive_scale_residual_positive` proves its positivity over the
  reals for positive weight and scale.
- `twoOrbitLeadingPacket` is `(1027,1081,1243,1729)`.
- the exact integer theorems prove positive quadratic reserve, negative
  pointed channel, and negative final residual.
- the three polarized theorems reproduce the full symbolic polynomials in
  the second-orbit weight.

## Assumptions and coefficient types

The polynomial identities hold over arbitrary commutative rings. Positivity
of one scale is stated over the real numbers. The hostile and symbolic
polarization use exact integers.

## Analytic and source gates

The file does not infer that the integer packet is itself a theta moment
sequence. Lifting it to Grothendieck's analytic two-orbit source requires the
Poisson-closed scale-pair construction, exact moment expansion, a positive
leading mass, and a certified bound on the `O(T^46)` remainder proving
eventual dominance of the negative `T^48` coefficient.

The standard theta source is a primitive single-scale object, whereas the
hostile uses two independently weighted reciprocal-scale orbits. Therefore
this falsifies additive Poisson-energy universality, not the standard-theta
exceptional inequality. Primitive indecomposability, a nonadditive energy,
the final Schur sign for the standard source, and RH remain gated.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
