# Corrected two-translate negativity robustness

## Correction

The former N=1 cross interval was defective and is retracted. The corrected N=3 cross term is positive, so the negative direction is disagreement, not coherence.

## Bold conjecture

The corrected negative determinant is a near-null diagonal instability removable by modest baseline correction.

## Strongest falsification attempt and residual

Using the corrected N=3 intervals, execution of `research/nima/checkers/check_two_translate_negativity_margin.py` shows that the cross lower bound exceeds the diagonal upper bound by a factor greater than 300. Even multiplying the full diagonal interval by 100 leaves `d-c` strictly negative.

The bold conjecture is falsified. The corrected obstruction is robust, although weaker than the retracted factor-3000 claim.

## Disposition and residual conjecture

The explicit negative packet is `g-tau_delta g`. Repair requires an off-diagonal change exceeding two orders of magnitude, not ordinary enclosure tightening. All independent reproduction must use the N=3 generalized tail and verify exact baseline regression.

## Evidence

- `research/nima/checkers/check_two_translate_negativity_margin.py`
- `research/nima/two-translate-spline-positivity-dpc.md`
