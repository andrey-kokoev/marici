# Timing, amplitude, phase, and branch-weight errors

Owner: `marici.Kitaev`

Status: exact finite coherent-error formulas and rigorous bounds; no hardware
noise distribution is assumed.

## Bounded question

How do calibration and random-source errors deform the compiled controls?

## Eight-branch central pulse

For sector eigenvalue difference `Delta`, a common fractional timing or
amplitude error `epsilon` gives the exact cross-sector multiplier

\[
R_\Delta(\epsilon)=\frac{1-e^{-2\pi i\Delta\epsilon}}
{8\left(1-e^{-2\pi i\Delta(1+\epsilon)/8}\right)}.
\]

Its leading squared magnitude coefficient is

\[
\frac{\pi^2\Delta^2}{64\sin^2(\pi(\Delta\bmod8)/8)}.
\]

This depends on the full integer lifts
`(-8,1,2,3,6,7,20,5)`, not only their residues.  Thus two ideal-equivalent
central generators can have different calibration robustness.

A common additive phase offset factors out of every branch and leaves the
ideal zero character sum zero.  Branch-dependent offsets `delta_k` instead
give

\[
\frac18\sum_k\zeta^{k\Delta}e^{-i\Delta\delta_k},
\qquad
|R|\le\frac{|\Delta|}{8}\sum_k|\delta_k|.
\]

## Branch weights

For weight errors `e_k` summing to zero, the resurrected coherence is their
discrete Fourier coefficient

\[
\sum_ke_k\zeta^{k\Delta},
\]

bounded by `sum |e_k|`, twice total-variation distance.  The one-branch
overweight pattern `(eta,-eta/7,...,-eta/7)` has exact magnitude
`8|eta|/7` in every nontrivial mode.

## Local-port angle errors

If `theta=Jt`, simultaneous amplitude/time errors give exactly

\[
\delta\theta=t\,\delta J+J\,\delta t+\delta J\,\delta t.
\]

Insert `theta+delta theta` into the exact leakage formulas

\[
\frac89\sin^2\frac{\theta+\delta\theta}{2},
\qquad
\sin^2\frac{\theta+\delta\theta}{2}.
\]

For the `G/H` current, whose norm is `sqrt(3)/2`, an angle error has exact
unitary operator-norm distance

\[
2\left|\sin\frac{\sqrt3\,\delta\theta}{4}\right|.
\]

## Verification and falsifiers

Run

```text
uv run --with sympy python research/kitaev/checkers/check_s3_control_error_budget.py
```

The checker catalogs every nonzero eigenvalue difference, records all exact
leading coefficients, proves the additive-offset cancellation and overweight
residual, and emits eight aggregate gates.  Saved result:
`research/kitaev/results/s3-control-error-budget.json`.

Falsifiers include disagreement with direct branch summation, a nonzero
common-offset residual, violation of either rigorous bound, or hardware error
mechanisms not reducible to the stated coherent angle/weight model.
