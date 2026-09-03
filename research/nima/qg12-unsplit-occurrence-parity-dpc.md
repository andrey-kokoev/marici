# Unsplit occurrence parity: third conjecture cycle

## Problem

Only the unsplit `q_g31+q_g23` combination has a source-authorized boundary value. Regulator chambers change its signed current, so they might also change nearby-cycle branch parity.

## Bold conjecture

Regulator hierarchy can change the mod-two branch parity of the unsplit two-occurrence object.

## Named rivals

1. chamber signs change both current and parity;
2. signs disappear mod two, so retaining each occurrence once forces even parity;
3. occurrence labels do not correspond to the two local split branch points, so occurrence parity has no nearby-cycle meaning.

## Risky consequences

Across the four sign chambers, at least one chamber must have odd total branch parity if the bold conjecture is correct.

## Strongest falsification attempt and residual

Represent the occurrence orientations by

\[
(s_{31},s_{23})\in\{+1,-1\}^2.
\]

Execution `structured_command_execution:e_31668_1788303692433204500_2` reproduces the three signed chamber currents

\[
2,\quad0,\quad-2.
\]

Modulo two, however, both signs reduce to one in every chamber. The unsplit boundary vector is always

\[
(1,1),
\]

with even total parity. Regulator hierarchy changes the signed current but cannot change occurrence-label parity. The bold conjecture is falsified.

## Disposition and residual conjecture

The source-authorized unsplit object has chamber-independent even parity at the occurrence-label level. This does not yet prove nearby-cycle evenness: it requires a typed correspondence sending `q_g31` and `q_g23` to the two distinct split branch points. If both labels map to the same branch, the occurrence calculation does not construct the desired cycle.

The residual conjecture is that the two denominator occurrences are the two branch labels of the local nodal smoothing. The next test must derive their distinct branch images from the exact denominator equations.

## Evidence

- `research/nima/checkers/check_qg12_unsplit_occurrence_parity.py`
- `research/benincasa/occurrence-resolved-physical-period-no-go.md`
- `research/nima/qg12-positive-geometry-boundary-dpc.md`
