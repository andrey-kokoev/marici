# Incidence-divisor rotation packet

## Grothendieck sources

This formalizes finite cores from:

- `research/grothendieck/theta-cross-zeros-are-incidence-divisor-crossings-not-operator-failures.md`;
- `research/grothendieck/theta-zero-bearing-incidence-is-additive-poisson-sewing-not-tate-transition.md`.

## Formal objects

- `quarterRotation` is the exact ninety-degree two-port hostile.
- its determinant is one and its transpose times itself is the identity.
- `incidenceSource` and `endpointCoordinate` define the selected scalar chart.
- `quarterRotation_incidence_crossing` proves zero selected readout while the
  complementary coordinate is one and the transfer remains invertible.
- `InIncidenceCell` is the nonvanishing open scalar chart.
- `fourChannelIncidence` types additive Poisson aggregation.
- `incidenceDescentDefect` vanishes exactly when the transported and source
  incidences agree.
- `nonzero_four_channels_can_cancel` is the smallest additive cancellation
  hostile.

## Assumptions and coefficient types

The rotation uses real two-dimensional matrices. Four-channel sewing and its
descent defect use an arbitrary additive commutative group; the concrete
cancellation witness uses integers.

## Category boundary

The rotation is orthogonal, orientation-preserving, invertible, and fully
observable across two ports. Its scalar zero is loss of transversality in one
chosen coordinate, not failure of the full transfer. Likewise, additive
cancellation of four nonzero channels is not failure of any multiplicative
Tate transition.

Open-cell confinement would require a source-derived sign-regular minor,
Gauss factorization, acute semigroup, oriented-matroid chamber, or boundary
current. The standard four-channel Tate--Poisson continuation additionally
requires the adelic source, self-dual Haar normalization, convergence
chambers, Poisson summation, and polar boundary terms. None is manufactured
by these finite hostiles. Spectral incidence and RH remain gated.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
