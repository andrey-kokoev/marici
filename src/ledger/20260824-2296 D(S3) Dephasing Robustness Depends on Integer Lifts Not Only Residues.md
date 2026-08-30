---
author: marici.Kitaev
---

# 2296 — D(S3) Dephasing Robustness Depends on Integer Lifts Not Only Residues

## Result

For sector eigenvalue difference `Delta`, a common fractional timing or
amplitude error `epsilon` leaves exact residual

\[
R_\Delta(\epsilon)=\frac{1-e^{-2\pi i\Delta\epsilon}}
{8(1-e^{-2\pi i\Delta(1+\epsilon)/8})}.
\]

Its leading sensitivity depends on the full integer difference, not only its
residue modulo eight.  The frozen generator has 16 distinct nonzero absolute
differences from 1 through 28 as catalogued in the result packet.

A common additive phase offset remains harmless.  Branch-dependent phase
errors obey

\[
|R|\le\frac{|\Delta|}{8}\sum_k|\delta_k|.
\]

Weight bias contributes its discrete Fourier coefficient; the one-overweight
pattern has exact magnitude `8|eta|/7`.  Local amplitude/time errors propagate
through `dtheta=t dJ+J dt+dJ dt` into the exact leakage formulas.

## Scope

These are coherent-error formulas and deterministic bounds.  No stochastic
hardware noise law or calibration-optimal integer lift is claimed.

## Durable verification

- Packet: `research/kitaev/s3-timing-amplitude-phase-and-weight-errors.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_control_error_budget.py`
- Result: `research/kitaev/results/s3-control-error-budget.json`
- Eight aggregate gates pass
- Epistemic graph: `ev-000000003166-f5c7be00-3e03-400b-a270-b677ed09ee4f`
- Ledger allocation: `seqclaim-ca0541cea6bd2d954a311a19`
