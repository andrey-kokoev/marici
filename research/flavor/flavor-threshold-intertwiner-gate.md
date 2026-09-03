# Threshold-intertwiner gate: WP1205

## Question

Can reciprocal endpoint flow survive threshold transport?

## DPC resolution

- **Problem:** intertwine the referenced boundary channel through physical16
  thresholds without losing orientation or absence.
- **Bold conjecture:** reciprocal endpoint flow gives a global nonzero basin
  whose oriented current can be transported through thresholds.
- **Named rivals:** endpoint exchange covariance; arbitrary symmetric
  threshold; fixed-point preservation; isometric marked-port threshold
  matching.
- **Risky consequences:** endpoint exchange forces equal rates; \(p^*=1/2\)
  has the entire probability interval as basin for \(\kappa>0\); zero seed
  is not fixed; \(T_r\) scales \(J\) by \(2r-1\); \(r=3/4\) preserves
  \(p^*\) but halves \(J\); only \(r=1\) preserves \(J\) exactly.
- **Strongest falsification attempt:** a threshold can preserve the uniform
  fixed packet while attenuating or erasing the oriented current.
- **Exact residual:** flavor RG derivation, coherent kinetic normalization,
  isometric marked-port matching, and calibrated readout remain open.
- **Disposition:** construct the reciprocal-basin and threshold audit;
  reject fixed-point preservation as threshold authority.

Checker: `research/flavor/checkers/wp1205_threshold_intertwiner_gate.py`

Result: `results/wp1205_threshold_intertwiner_gate.json`
