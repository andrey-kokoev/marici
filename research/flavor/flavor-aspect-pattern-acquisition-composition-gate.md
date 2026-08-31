# Aspect-pattern acquisition composition gate: WP1078

## Question

Can the cited Aspect calibration patterns compose with WP1077's acquisition
gate without claiming source selection?

## Aspect sources

- `research/aspect/calibrated-six-port-scale-identification-instrument.md`
- `research/aspect/source-monitor-gain-calibration.md`
- `research/aspect/calibrated-homodyne-heterodyne-detection.md`
- `research/aspect/two-instrument-calibration-robustness.md`

## Composed exact gates

### Independent scale reference

For six pole channels with \(c_i=(1,2,3,5,7,11)\), the unreferenced log-scale
rows are

\[
J_i=(c_i,-c_i),
\]

with rank \(1\). Adding the independent reference row \((0,1)\) raises the
rank to \(2\). This identifies the instrument unit; it does not select a
source coordinate.

### Source-monitor affine calibration

The monitor record is

\[
y=gx+o.
\]

A dark row fixes \(o\), and a bright-minus-dark contrast fixes \(g\). In the
exact fixture

\[
g=2,\qquad o=\frac1{10},\qquad x=\frac18,
\]

the calibrated records recover \(g=2\) and \(x=1/8\). With only one bright
reference, the alias

\[
g'=3,\qquad o'=-\frac9{10}
\]

preserves the reference record but infers \(x'=5/12\), not \(1/8\).

### Coherent phase rows

One phase row has rank \(1\). Two independent calibrated phase rows have rank \(2\). A
nonzero calibrated local oscillator and gain balance are required before interpreting
coherent phase data.

### Robustness margin

With predeclared noise floor \(\eta=1/1000\), coupling \(1/100\) is
detectable, while \(1/10000\) is unresolved by that instrument. Coherent rows
must be reconstructed before threshold comparison.

## Constructor order

1. Calibrate dark and bright monitor rows at each epoch.
2. Prepare the independent scale reference.
3. Calibrate gain balance and common phase frame.
4. Retain two phase rows and environment/noise ports.
5. Calibrate momentum in the same frame.
6. Reconstruct coherent rows before threshold comparison.
7. Compare residuals with the predeclared noise floor.

## Boundary

These patterns close instrument hostiles only. They do not derive the
localized physical16 production/decay kernel, the WP1075 mixing matrix, or
the source gain.

## Classification

Conditional Aspect-pattern composition. D1 now has an exact instrument
contract and a clean authority boundary.

Checker: `research/flavor/checkers/wp1078_aspect_pattern_acquisition_composition_gate.py`

Result: `results/wp1078_aspect_pattern_acquisition_composition_gate.json`
