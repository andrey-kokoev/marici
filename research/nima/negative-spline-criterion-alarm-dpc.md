# Negative spline criterion alarm — dilation correction

## Correction

The N=3 hybrid interval computation is independently reproduced, but its completed-zeta pole deletion is invalid under the implemented archimedean dilation. The previous statement that the pole-annihilator gate was closed is retracted.

## Bold conjecture

The N=3 negative hybrid-functional packet is already a criterion-level alarm with exact completed-zeta pole deletion.

## Strongest falsification attempt and residual

For dilation `c=1/2`, bilateral Laplace scaling gives

\[
\mathcal L(D_c\phi_a)(s)=c^{-1}\Phi_a(s/c).
\]

Holding `a=2 log 2` fixed moves the preconditioner zeros from `s=plus or minus 1/2` to `s=plus or minus 1/4`. Execution `structured_command_execution:e_11792_1788312116491807500_15` verifies this exactly. The checker nevertheless omits the completed-zeta pole cells at `plus or minus 1/2`. Therefore the negative determinant belongs only to a defective hybrid functional. The bold criterion-alarm claim is falsified.

## Disposition and residual conjecture

All five criterion comparison gates are now open. A valid regeneration must choose one consistent repair:

1. rescale the preconditioner shift to `a_c=c a=log 2`, preserving pole annihilation; or
2. retain fixed `a=2 log 2` and restore explicit pole cells.

Only after that regeneration may zero-side, direct digamma, and theorem-sign discriminators be applied. The current negative determinant remains a verified property of the implemented hybrid code, not of the completed-zeta Weil functional.

## Evidence

- `research/nima/checkers/check_spline_dilation_pole_annihilator.py`
- `research/nima/checkers/check_negative_spline_criterion_gate.py`
- `research/grothendieck/dilation-requires-rescaling-the-spline-preconditioner-to-preserve-pole-annihilation.md`
- bounded N=3 hybrid reproduction `structured_command_execution:e_11792_1788311091505719700_13`
