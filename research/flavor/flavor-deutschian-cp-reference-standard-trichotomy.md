# Deutschian CP Reference-Standard Trichotomy

Work package: WP918

## Question

What would make the normalization of the Jarlskog coordinate unavoidable
rather than an elaborate restatement of measured quark masses?

## The kinematic part is uniquely fixed

Let (D=\det[H_u,H_d]). Under the common scaling
(H_u,H_d\mapsto sH_u,sH_d), (D^2) scales as (s^{12}), while the product
of the two cubic spectral discriminants, (\Delta_u\Delta_d), scales as
(s^6). Hence

\[
\frac{D^2}{(\Delta_u\Delta_d)^p}
\]

is invariant only for (p=2). Scale invariance therefore explains the power
of the denominator. It does not explain the spectral gaps whose product gives
its numerical value.

This separates two questions that WP917 left adjacent:

1. why the physical CP coordinate uses the squared discriminant product;
2. what source mechanism fixes the dimensionless spectral shape entering that
   product.

The first is kinematic. The second is dynamical.

## Three candidate constructors

### Common clock

WP591 ties the CP scale and flavor scale to one dilaton clock. It removes a
common rescaling fiber but migrates the ambiguity into dimensionless Wilson
ratios. The same limitation applies here: a clock fixes scale, not spectral
shape.

The exact hostile pair is

\[
(0,1,2),\qquad (0,1/2,2).
\]

Both spectra have the same clock value (2), but their cubic discriminants
have magnitudes (2) and (3/2). Thus even a perfectly calibrated common
clock does not fix the CP reference standard.

### Spectral completion

WP824 proves that a complete Dirac spectrum faithfully records masses erased
by coarser topology. WP110 likewise transports source bounds into a normalized
CP margin. Neither operation selects the recorded eigenvalue ratios. Spectral
completion is a carrier and readout; it is not a dynamical selector.

### Isolated full-shape fixed ray

WP592 supplies the correct conditional architecture. A complete
gauge-Yukawa-scalar beta system could possess an isolated attractive fixed ray
for all independent dimensionless Yukawa spectral-shape coordinates. If its
coefficients are derived from frozen representations and the ray survives
thresholds with no relevant shape deformation, the discriminant normalization
would become hard to vary: changing it would require changing the beta law or
leaving its basin.

No declared Spin(5) packet currently supplies that full beta system. Existing
fixed-ray packets control selected coupling ratios, not the four independent
up/down eigenvalue-shape ratios required before mixing data are considered.

## Contextual partition

The current source probes consist of common-clock relations, finite spectral
records, source norm bounds, and conditional fixed-ray equations. They quotient
common scale and can faithfully record a chosen spectrum. They do not collapse
the remaining spectral-shape fiber to a source-selected class.

Normalized (J) is therefore a kinematically rigid physical16 coordinate,
not presently a source-selected value. This is a useful rigidification, but it
does not make WP360 source-derived.

## Deutschian verdict

The denominator exponent has a good explanation: it is forced by weak-basis
invariance and common-scale cancellation. The numerical denominator does not.
Its gap ratios remain easy to vary while preserving the currently claimed
mechanism.

The next sharp calculation is the spectral-shape stability block of a declared
anomaly-free Spin(5) gauge-Yukawa beta system. A relevant or zero mode is the
smallest falsifier. An isolated attractive block would be progressive, but it
would still require threshold preservation and a joint CP/mass-gap instrument.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp918_deutschian_cp_reference_standard_trichotomy.py
~~~
