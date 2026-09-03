# Channel/gain gate: WP1256

## Question

Can current rows and gains calibrate the Physical16 two-port ratio law?

## DPC resolution

- **Problem:** derive calibrated momentum and ratio law while the
  compactification-clock handoff remains active.
- **Bold conjecture:** the exact two-port rows, vector gain chain, or common
  reweighting gain may calibrate Physical16 channels and production maps.
- **Named rivals:** two-port Physical16 channels; vector-KK gain chain;
  common scalar gain; rank-one complete mixing; rank-two/localized map.
- **Risky consequences:** soft and vector rows have ratios 1 and 4 with
  responses \(1/2\) and \(1/5\); the vector event cell reconstructs
  uniquely at \(g=1,L=1/5\); \(g=3/2\) changes \(S,D\) to
  \(9/20,3/5\); the reweighting family \(M=U+A\) has affine dimension 24.
- **Strongest falsification attempt:** zero Physical16 channels or
  production maps exist; event-cell gain 1 is incompatible with reweighting
  gain \(3/2\) as one scalar; \(q\) and \(r\) do not uniquely select
  complete mixing.
- **Exact residual:** materialize `physical16_channel_packet` and
  `physical16_gain_cascade_certificate`, then select a production-local
  map.
- **Disposition:** retain exact rows and map classification conditionally;
  reject current channel/gain authority.

Checker: `research/flavor/checkers/wp1256_channel_gain_gate.py`

Result: `results/wp1256_channel_gain_gate.json`
