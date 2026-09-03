# Analytic admissibility of the preconditioned spline

## Question

Does the baseline spline satisfy the source-independent analytic conditions usually needed before an explicit-formula positivity test can be considered?

## Claim boundary

The centered degree-7 cardinal spline is even, compactly supported, and `C^6`. Its Fourier transform is a positive scale factor times an eighth power of a sinc function, hence is nonnegative.

For the five-shift coefficients `(1,-5,33/4,-5,1)`, the Fourier multiplier is

\[
M(\theta)=2\cos(2\theta)-10\cos\theta+\frac{33}{4}.
\]

Writing `x=cos(theta)` gives

\[
M=4x^2-10x+\frac{25}{4}=\left(2x-\frac52\right)^2.
\]

On `x` in `[-1,1]`, the minimum is attained at `x=1` and equals `1/4`. Therefore the shifted spline has nonnegative Fourier transform and is positive definite. Its evenness, compact support, and regularity follow directly from the symmetric finite shift sum.

A deliberate rival changes only the central coefficient from `33/4` to `6`. Its multiplier is `4x^2-10x+4`, whose value at `x=1` is `-2`; Fourier nonnegativity fails.

## Evidence

- Checker: `research/nima/checkers/preconditioned_spline_admissibility.py`
- Result: `research/nima/results/preconditioned_spline_admissibility.json`
- Execution: `structured_command_execution:e_4616_1788289467556079800_41`

## Disposition

The baseline passes this source-independent analytic admissibility gate. This does not supply the missing convention map to an authoritative Weil criterion, and it does not turn one positive explicit-formula evaluation into RH or all-test positivity.
