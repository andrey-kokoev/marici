# Gaussian reciprocal seam sewing: Lean packet

## Source boundary

This increment formalizes the convention-fixed algebraic identities in
Grothendieck's packets `the-gaussian-derivative-comb-current-reduces-to-one-seam-port.md`
and `reciprocal-sewing-makes-the-gaussian-seam-port-an-observable-not-a-barrier.md`.
It does not construct the Gaussian half-Mellin transforms or assert a zero
confinement theorem.

## Formal objects and assumptions

The coefficient type is an arbitrary field `R` of characteristic zero. The
objects `forward` and `reverse` represent the two half-line amplitudes,
`seam` represents their common value at the seam, and `spectral` is the
algebraic slot occupied by `i z` in the source calculation.

`symmetricChannel forward reverse` is `forward + reverse`, while
`antisymmetricChannel forward reverse` is `forward - reverse`. The two number
channels are

\[
 ((1/2)+q)H_+ + a,
 \qquad
 ((1/2)-q)H_- + a.
\]

No topology, integral, differentiability, decay, Fourier covariance, or
positivity assumption occurs in the Lean theorem.

## Theorems

- `numberChannel_sum_sewing`: the sum is
  `(1/2) X + q Y + 2 a`.
- `numberChannel_difference_sewing`: the difference is
  `(1/2) Y + q X`; the seam term cancels.
- `at_symmetric_zero_sum_retains_seam_and_route` and
  `at_symmetric_zero_difference_retains_route`: specialize the identities at
  `X = 0` without concluding that the remaining channels vanish.
- `symmetric_zero_with_nonzero_transverse_route`: over the rationals,
  `H_+ = 1`, `H_- = -1`, `q = 0`, and `a = 0` give `X = 0`, `Y = 2`, and a
  nonzero number-channel difference equal to `1`.

## Missing interfaces

Faithful formalization of the analytic packet still needs a chosen function
space for the scaled Gaussian comb, convergence and differentiability of the
half-Mellin integral, the boundary term at zero, and the decay theorem used in
integration by parts. The claim that this is the only new oscillator-ladder
datum additionally needs a typed finite ladder and an induction proving its
factorization through seam jets. None is inferred here.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/GaussianSeamSewing.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
