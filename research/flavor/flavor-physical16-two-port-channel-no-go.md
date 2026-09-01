# Physical16 two-port channel no-go: WP1139

## Question

Do the two-port momentum rows realize physical16 channels?

## DPC resolution

- **Problem:** derive a calibrated physical16 ratio law from the two-port
  momentum lock.
- **Conjecture:** WP1063's two-port lock is realized by physical16
  production/decay channels.
- **Rivals:** soft instrument reference; vector KK channel; physical16
  production/decay channels; no physical16 realization.
- **Risky consequences:** two typed physical16 channels, source-derived
  production or decay maps, ratios \(1\) and \(4\) in one frame, and responses
  \(1/2\) and \(1/5\).
- **Falsification attempt:** the exact rows exist, but the soft row is a WP770
  instrument reference and the vector row is a WP771 bulk KK mode. Zero
  physical16 channels or production/decay maps are sourced.
- **Residual:** a future physical16 channel packet may realize both rows.
- **Disposition:** reject current physical16 channel realization and record
  the typed blocker.

## Typed blocker

`physical16_channel_packet` must carry soft and vector channels,
production/decay maps, and a same-frame certificate. Acceptance requires
ratios \(1,4\) and responses \(1/2,1/5\) in one frame.

Checker: `research/flavor/checkers/wp1139_physical16_two_port_channel_no_go.py`

Result: `results/wp1139_physical16_two_port_channel_no_go.json`
