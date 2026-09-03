# Occurrence labels versus split branches: fourth conjecture cycle

## Problem

The unsplit `q_g31,q_g23` occurrence labels have chamber-independent even parity. This implies even nearby-cycle parity only if the two labels map to the two distinct conductor branch points.

## Bold conjecture

`q_g31` and `q_g23` are the two denominator equations that split into the two local Cayley–Menger branch points.

## Named rivals

1. each occurrence vanishes on one split branch;
2. both occurrence denominators remain units in the branch coordinate and do not label either branch;
3. only one occurrence labels the collision while the other labels projective infinity.

## Risky consequences

After restricting to `q_g2` and writing `s=xi+kappa`, the two denominators must have distinct zeros in `s` matching the two roots of the smoothed Cayley–Menger equation.

## Strongest falsification attempt and residual

On `q_g2`, where `a=x+z`, execution `structured_command_execution:e_31668_1788303785879818800_3` gives

\[
q_{g31}=x(1-\kappa),
\qquad
q_{g23}=2p+x(-\kappa+s).
\]

Their exceptional values are

\[
q_{g31}/x=1-\kappa,
\qquad
q_{g23}|_{x=0}=2p.
\]

Both are generic units and neither depends on the local branch coordinate `s`. They cannot distinguish the two split Cayley–Menger roots. The bold conjecture is falsified.

Benincasa independently confirmed the local conductor coefficient and inverse-Euler sign but explicitly separated that result from the missing physical relative chain.

## Disposition and residual conjecture

Occurrence-label parity and nearby-cycle branch parity are different typed objects. The two split branches are roots of the Cayley–Menger smoothing, not zeros of `q_g31` and `q_g23`. The residual conjecture is that the source canonical-form contour induces a separate chain map from the unsplit occurrence sum to the even root-pair cycle. Existing denominator labels do not construct it.

The next falsifier is to derive that chain map from the canonical-form regulator prescription or prove that the source only fixes the unsplit boundary value, not its local root-pair decomposition.

## Evidence

- `research/nima/checkers/check_qg12_occurrence_branch_label_map.py`
- `research/nima/qg12-unsplit-occurrence-parity-dpc.md`
- `research/benincasa/results/qg2_inverse_euler_gysin_dpc.json`
