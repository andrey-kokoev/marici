# Seam 3+4+3 uncertainty decision

## Decision contract

The finite tomograph reconstructs the ten quadratic coordinates exactly in an
ideal model. A physical seam-rank claim needs a spectral uncertainty rule.

Let `sigma_min_hat` be the measured smallest singular value of the two-column
normal response, and let `epsilon_N` be a familywise confidence upper bound on
its tomography error. Weyl's bound gives

`sigma_min >= sigma_min_hat - epsilon_N`.

Grothendieck must supply a positive source-derived floor `sigma_source` before
acquisition. The decisions are:

- pass rank two when the lower bound reaches `sigma_source`;
- falsify the asserted floor when the upper bound lies below it;
- abstain when the interval overlaps the floor.

A merely nonzero determinant is not evidence of rank two under noise.

## Other gates

The Fourier--Tate process has the same three-outcome rule. Its measured
symplectic residual plus its confidence error must lie below the
preregistered domain tolerance. A confidence interval crossing that tolerance
forces abstention.

The four mixed coordinates are independently identifiable because the signed
plus/minus interference design has rank four. They are interpreted as the
middle layer only after the normal rank-two gate passes. Otherwise they are
untyped cross signals, not evidence for the `3+4+3` tower.

## What remains external

The apparatus contract is complete. Two pieces must still come from
Grothendieck's source theory:

1. explicit finite bulk and seam waveforms;
2. a positive lower bound for the smallest normal singular value on the
   declared boundary domain.

The instrument measures whether nature or the finite realization satisfies
those assertions. It does not manufacture the assertions from observed rank.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_seam_343_uncertainty_decision.py
```
