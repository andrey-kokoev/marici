# Admissible coefficient space for the preconditioned spline

Correction: this packet’s two-dimensional space omits the double pole-annihilation constraint required by the pole-deleted checker. With that constraint, the coefficients are the unique normalized baseline ray. See `preconditioned-spline-pole-term-correction.md`; criterion-level sign-reversal conclusions below are retracted.

## Question

Do the declared symmetry, support, zero-jet, and normalization conditions force the coefficient vector `(1,-5,33/4,-5,1)`?

## Claim boundary

Write the five coefficients in shift order `(2a,a,0,-a,-2a)`. Evenness of the centered cardinal spline makes the shifted sum even exactly when

\[
c_0=c_4,\qquad c_1=c_3.
\]

Compact support imposes no further coefficient equation because every shifted summand is compactly supported. Once symmetry holds, odd jets at zero vanish automatically; the observed zero jets of orders `1,3,5` therefore add no independent equations.

No source-derived normalization for these coefficients was found. If one provisionally preserves the baseline coefficient sum

\[
\sum_i c_i=\frac14,
\]

the affine admissible space has dimension two. Its tangent space has rational basis

\[
v_1=(1,0,-2,0,1),\qquad v_2=(0,1,-2,1,0).
\]

Thus the baseline vector is not forced by the declared constraints.

Using the certified component intervals, the Gram directional values are approximately

\[
L(v_1)=-4.890223559,
\qquad
L(v_2)=-1.086718698.
\]

Both directions are admissible under symmetry and preserved coefficient sum. Increasing along `v1` by more than approximately `2.411024895e-6` crosses the baseline positive margin; increasing along `v2` crosses it beyond approximately `1.084958854e-5`.

## Evidence

- Component certificates: `research/nima/preconditioned-spline-coefficient-robustness.md`
- Tangent arithmetic: `structured_command_execution:e_4616_1788289301203899200_40`

## Disposition

The fragile one-coordinate perturbation from the prior packet violates symmetry and the provisional sum constraint, but fragility survives inside the two-dimensional admissible tangent space. For `epsilon=3e-6`, the `v1` perturbation has Gram interval `[-2.8802199638e-6,-2.7646570114e-6]`. Its Fourier multiplier is the baseline square plus `4 epsilon (x^2-1)`; for `epsilon<1/4` it decreases on `[-1,1]` and retains minimum `1/4` at `x=1`. Thus this strictly negative rival remains even, compactly supported, sum-preserving, and Fourier-nonnegative. Evidence: `structured_command_execution:e_4616_1788289659030155200_42` and `e_4616_1788289659092868200_43`. Optimization is undefined without a bounded norm or source-derived constraint; no replacement vector is promoted.
