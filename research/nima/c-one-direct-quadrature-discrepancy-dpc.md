# c=1 direct-quadrature discrepancy — resolved

## Problem

The initial independent direct quadrature preserved positivity but disagreed with the coherent c=1 scout at value level.

## Bold conjecture

The discrepancy reflected a convention mismatch between the two implementations.

## Strongest falsification attempt and exact residual

The initial checker stopped integration at `top`, where the compactly supported profile vanishes. The integrand does not vanish there: its surviving term is

\[
\frac{f(0)e^{-x}}{1-e^{-x}}.
\]

The omitted integral is exactly

\[
-f(0)\log(1-e^{-\mathrm{top}}).
\]

Adding this term yields execution `structured_command_execution:e_11792_1788312834307204100_24`:

- baseline `2.12511463965217217`;
- cross `-0.846660221734685927`;
- determinant `3.79927870059615405`;
- eigenvalues `1.27845441791748625` and `2.9717748613868581`.

These reproduce the independent scout. The convention-mismatch conjecture is falsified; the discrepancy was a truncation defect.

## Disposition

The defect is repaired and verified. Independent direct digamma quadrature now establishes positive definiteness of the coherent c=1 two-translate numerical cell. This remains a high-precision numerical result, not directed interval certification. The latter requires translation of the closed undilated moments and total-variation tail bound `5184`.

## Evidence

- `research/nima/checkers/check_c_one_direct_quadrature_scout.py`
- `research/grothendieck/c-one-quadrature-discrepancy-is-the-omitted-f-zero-tail.md`
- `research/grothendieck/results/undilated-septic-moment-formula-check.json`
