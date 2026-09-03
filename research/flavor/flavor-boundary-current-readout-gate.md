# Boundary-current readout gate: WP1204

## Question

Can a boundary-current readout separate orientation and absence?

## DPC resolution

- **Problem:** construct a readout for the oriented boundary current derived
  by WP1203.
- **Bold conjecture:** a dimensionless readout separates positive
  orientation, negative orientation, and absent boundary source.
- **Named rivals:** ordinary sum port; downstream contact; loop product;
  unreferenced difference intensity; coherent referenced difference pair.
- **Risky consequences:** the sum port gives zero for all three states; loop
  product erases boundary orientation; difference intensity detects presence
  but erases orientation; two referenced difference settings form three
  singleton classes.
- **Strongest falsification attempt:** \(p=(1,-1)/\sqrt 2\) and \(p=0\)
  both have zero sum-contact response, and no downstream contact repairs
  that kernel.
- **Exact residual:** derive a source pre-projection difference channel,
  calibrate the coherent reference, and transport the channel through
  thresholds.
- **Disposition:** construct the readout hierarchy; reject sum-port or
  intensity-only authorization.

Checker: `research/flavor/checkers/wp1204_boundary_current_readout_gate.py`

Result: `results/wp1204_boundary_current_readout_gate.json`
