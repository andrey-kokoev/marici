# Coherent c=1 archimedean regeneration

## Problem

Can the corrected undilated total-variation bound `5184` still certify the first Gram minor at N=3, or is signed-atom sharpening already necessary?

## Bold conjecture

The corrected bound is too coarse to certify rank-two positivity at N=3.

## Strongest falsification attempt and exact residual

The certified zeta-tail upper bound `0.000092110177077` and TV `5184` give independent entry error

\[
E=0.477499157967168.
\]

Using independently reproduced centers `d=2.12511463965217217` and `c=-0.846660221734685927`, exact rational arithmetic gives

\[
d_{\min}=1.64761548168500417,
\qquad |c|_{\max}=1.324159379701853927,
\]

and determinant lower bound `0.9612387126357097`. Execution `structured_command_execution:e_11792_1788312912652487000_25` also verifies a deliberate failure: replacing `E` by `1` makes the same lower bound negative. The bold conjecture is falsified.

## Disposition and boundary

The coarse N=3 tail is sufficient in magnitude for rank two; signed-atom sharpening is unnecessary at this rank. This is a conditional robustness theorem around independently reproduced numerical centers, not yet a directed interval certificate. The remaining executable step is to translate the closed undilated moments into rational prefix intervals, add the `5184` tail, and verify that their widths fit inside this reserve.

## Evidence

- `research/nima/checkers/check_c_one_coarse_tail_margin.py`
- `research/nima/checkers/check_c_one_direct_quadrature_scout.py`
- `research/grothendieck/results/undilated-septic-moment-formula-check.json`
- `research/grothendieck/coarse-undilated-tail-bound-is-already-small-enough-for-the-first-gram-minor.md`
