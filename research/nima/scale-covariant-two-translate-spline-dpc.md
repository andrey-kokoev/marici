# Scale-covariant two-translate spline test — implementation retraction

## Problem

Can the old interval evaluator implement the `c=1/2`, `a_c=log 2` repair by changing only its public shift argument?

## Bold conjecture

Passing `a_c=log 2` to the old `integral_shift` implements a coherent scale-covariant profile and can decide the repaired Gram sign.

## Strongest falsification attempt and exact residual

Execution `structured_command_execution:e_11792_1788312348687035200_18` returned a large negative baseline and determinant. Static audit `structured_command_execution:e_11792_1788312725279144500_23` shows that this output has no coherent integral interpretation:

- support boundaries use the supplied `a`;
- exponential endpoint factors remain hard-coded as powers of two derived under `a=2 log 2`;
- the source comment explicitly relies on that specialization.

Thus changing `a` mixes two incompatible profiles. The bold conjecture is falsified, and every sign from execution 18 is retracted as an implementation defect rather than a mathematical residual.

## Disposition

The scale-covariant branch requires generalized exponential endpoint enclosures before rerunning. The coherent `c=1` branch instead has a closed undilated moment formula independently checked against quadrature, but its directed tail must use total-variation bound `5184`; the diluted bound `81/2` understates it by a factor of 128.

No repaired interval Gram sign is currently certified.

## Evidence

- `research/nima/checkers/check_scale_covariant_kernel_no_go.py`
- `research/grothendieck/results/undilated-septic-moment-formula-check.json`
- `research/grothendieck/undilated-spline-tail-variation-is-5184-not-81-over-2.md`
