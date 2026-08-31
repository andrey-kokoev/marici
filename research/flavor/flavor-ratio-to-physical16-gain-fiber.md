# Ratio-to-physical16 gain fiber: WP1042

## Question

Would a source-locked threshold ratio by itself give a `physical16` portal
prediction?

## Granted upstream repairs

Grant every missing upstream repair isolated by WP1038--WP1041:

- the integer labels \((k,C)=(2,23)\) are selected;
- the operator is typed as one degenerate pole;
- the physical momentum port is calibrated;
- the dimensionless threshold ratio is selected as \(p^2/M^2=1\).

The threshold shape is then fixed:

\[
\frac{R(p^2)}{R(0)}=\frac{1}{1+p^2/M^2}=\frac12.
\]

## Interface gain hostile

Let the `physical16` portal row be the threshold shape multiplied by a
source-detector interface gain \(g\). The packets

\[
g=1,
\qquad
g=2
\]

share the selected integer labels, pole type, momentum calibration, and
threshold ratio. Their portal rows are

\[
\frac12,
\qquad
1.
\]

The difference is \(1/2\). A normalized one-port fraction collides exactly:

\[
\frac{gR}{gR}=1
\]

for both gains.

## Classification

The first nonfaithful arrow is

\[
\{\text{threshold shape}\}
\longrightarrow
\{\text{calibrated `physical16` portal row}\}
\]

without a source-detector gain law. A source-locked threshold ratio would be a
shape selector, not an absolute `physical16` normalization selector.

## Disposition

Negative for ratio-only completion of the integer-pole branch. Reopening
requires the same source to derive the source-to-Yukawa or source-to-detector
coupling gain in the frame used by the threshold ratio, together with an
absolute or interference-calibrated `physical16` instrument.

Checker: `research/flavor/checkers/wp1042_ratio_to_physical16_gain_fiber.py`

Result: `results/wp1042_ratio_to_physical16_gain_fiber.json`
