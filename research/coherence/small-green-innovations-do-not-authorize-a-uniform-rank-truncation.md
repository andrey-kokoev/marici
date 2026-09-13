# Small Green innovations do not authorize a uniform rank truncation

## Tempting but invalid inference

When neighboring contexts approach each other, the raw innovation

\[
r_i=k_i-\rho_{i-1}k_{i-1}
\]

has squared norm

\[
\|r_i\|^2=1-\rho_{i-1}^2\to0.
\]

This does not imply that its state line can be removed with small uniform error.

## Unit hostile

Normalize the innovation:

\[
e_i=\frac{r_i}{\sqrt{1-\rho_{i-1}^2}}.
\]

It has norm one and lies entirely in the new orthogonal summand. If \(P\) is any earlier-stage projection that discards this line, then

\[
Pe_i=0,
\qquad
\|(I-P)e_i\|=1.
\]

Therefore every proper finite-stage orthogonal truncation satisfies

\[
\|I-P\|=1.
\]

No spacing threshold produces an operator-norm approximation of the identity on the complete state space.

## What becomes large

Representing the normalized hostile in the original kernel basis requires coefficients of order

\[
(1-\rho^2)^{-1/2}.
\]

Equivalently, its squared coefficient amplification is

\[
(1-\rho^2)^{-1}.
\]

Near-collision directions are small only for bounded raw coefficients. The full Hilbert unit ball includes compensating large coefficients.

## Authorized approximate quotients

A close-context truncation becomes valid only after adding one of:

- a bound on source coefficients in the kernel basis;
- a probability law controlling innovation energy;
- a measurement noise floor;
- a restricted context or source class;
- a weaker topology that suppresses normalized collision directions.

Without such data, conditioning describes numerical sensitivity but does not authorize rank reduction.

## Consequence

```text
small innovation norm
+ unrestricted coefficients
!= small uniform state error
```

The exact unbounded realization remains minimal. Any effective finite rank is prior-relative or noise-relative, just as the two-state hyperbolic rank is protocol-relative.

## Verification

```text
python research/coherence/check_innovation_threshold_uniform_no_go.py
```

The checker tracks exact innovation variances and inverse-variance amplification as \(\rho\to1\), and records the normalized unit hostile.

Artifacts:

- `check_innovation_threshold_uniform_no_go.py`
- `innovation-threshold-uniform-no-go.v1.json`
