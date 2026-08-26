# Entangled positivity as a handedness sewing witness

## Question

Can two independently calibrated polarization analyzers synchronize their
relative handedness without importing a transported chiral reference?

## Local ambiguity

Complex conjugation fixes the local Stokes axes `X` and `Z` and reverses `Y`.
An isolated analyzer's locally admissible state space is preserved by this
operation. Disjoint local records therefore do not distinguish the two
relative frame sewings.

On a composite state, reversing `Y` on only the second port is partial
transpose on that subsystem. It preserves every separable state's positivity:
each product projector is sent to another product projector, and convex
mixtures remain positive. Separable packets therefore retain the relative
`C2` ambiguity.

## Endogenous witness on the NPT locus

For the polarization Bell state `Phi+`, partial transpose is half the swap
operator. Its antisymmetric polarization vector has eigenvalue `-1/2`.
Consequently the reversed sewing would turn a source-authorized physical Bell
projector into a nonpositive operator. Composite positivity selects the
relative handedness on this locus.

For the Werner family with Bell weight `p`, the same eigenvalue is
`(1 - 3p)/4`. The witness becomes decisive only for `p > 1/3`; at and below
the threshold this positivity test does not resolve the sewing.

## Optical realization

The required instrument is a polarization-entangled pair source, independently
adjustable local Stokes analyzers, coincidence detection, and a joint
tomographic positivity audit. The entangled state is not merely another probe
setting. Its admissibility under composition supplies the shared handedness
constraint.

This conclusion is conditional on the source authorizing the composite state
and the analyzer-to-record maps. Without that authority, a negative
reconstruction can also indicate calibration error or an invalid tomography
model. A physically transported noncoplanar Stokes triad remains the global
criterion outside the NPT locus.

## Verification

Run:

```text
python research/aspect/checkers/check_entangled_handedness_sewing.py
```

The checker uses dependency-free exact rational arithmetic. It verifies the
Bell negative eigenvalue, both sides of the Werner threshold, and a separable
packet that remains positive under the local reversal.

## Bounded-error decision rule

Full density-matrix reconstruction is unnecessary for this sewing decision.
For the Werner line, measure the three joint Stokes correlations `XX`, `YY`,
and `ZZ` and form the witness

```text
(1 - <XX> + <YY> - <ZZ>)/4.
```

If every correlation has calibrated absolute error at most `eta`, the witness
error is at most `3 eta / 4`. Handedness is certified whenever the measured
witness plus that radius is negative. This is a one-sided decision: failure to
cross zero leaves the sewing unresolved rather than selecting the opposite
orientation.

At `eta = 1/100`, a nominal Werner estimate is decisive above `p = 103/300`.
To guarantee decisiveness for every estimate inside the error box requires
`p > 53/150`. The benchmark `p = 1/2` retains worst-case certificate upper
bound `-11/100`.

Bounding three reconstructed matrix elements separately by `1/100` gives a
larger witness radius `1/50` and a correspondingly weaker guaranteed threshold
`p > 29/75`. Direct joint Stokes acquisition is therefore the preferred
instrument for this specific question.

Run:

```text
python research/aspect/checkers/check_robust_entangled_handedness_sewing.py
```

## Finite-count confidence contract

A prospective protocol can derive the statistical part of the error budget
without borrowing authority from a fitted density matrix. Acquire `30000`
binary coincidence products in each of the `XX`, `YY`, and `ZZ` settings. For
each sample mean, variance is at most one. Chebyshev's inequality bounds the
probability of an error at least `1/10` by `1/300`; a union bound makes the
three-setting failure probability at most `1/100`.

Keep a separately calibrated systematic correlation bound of `1/100`. The
combined per-correlation radius is then `11/100`, and the witness radius is
`33/400`. The one-sided certificate has confidence at least `99/100` whenever
the measured witness plus `33/400` is negative.

As a benchmark only, the independently audited maximum-likelihood witness
`-0.478675` from the historical tomography record would give certificate upper
bound `-15847/40000`. The historical record does not thereby inherit this
prospective confidence contract; its own acquisition assumptions and error
model remain source-specific.

Run:

```text
python research/aspect/checkers/check_finite_count_handedness_sewing.py
```

This conservative contract assumes stationary binary trials within each
setting. It does not repair fair-sampling failure, analyzer misalignment, or
untyped drift.

## Hoeffding acquisition reduction

When trials are independent and stationary within each setting, the bounded
binary outcomes support a sharper prospective contract. With `2000` trials
per setting and statistical radius `1/10`, the two-sided Hoeffding exponent is
exactly `10`. A union bound over the three settings gives failure probability
at most `6 exp(-10)`.

The checker avoids floating-point evaluation of that exponential. The degree
four Taylor partial sum proves `exp(10) > 1933/3 > 600`, so the family failure
probability is strictly below `18/1933`, which is itself below `1/100`.
Consequently `6000` total coincidence events retain greater than `99/100`
confidence and the same combined witness radius `33/400`: a fifteen-fold
reduction from the Chebyshev contract.

Run:

```text
python research/aspect/checkers/check_hoeffding_handedness_sewing.py
```

This gain is conditional on independence. The Chebyshev contract remains the
fallback when only bounded variance and stationarity are authorized.
