# Anomaly-Inflow Relational Orientation Audit

## Question

Can anomaly inflow supply WP806's missing source-derived CP-odd datum while
fixing its magnitude and protecting it under RG and thresholds?

## Source typing

Callan--Harvey inflow relates a chiral boundary anomaly to a bulk topological
term. Its level (k) is quantized by the anomaly packet and cannot vary
continuously while the symmetry and gap remain intact. Let (eta=\pm1) denote
the oriented boundary normal and let (J=\pm1) denote the sign of a faithful
weak-basis flavor orientation. The minimal odd bias is

\[
E_{\rm odd}=-k\eta J.
\]

For (k=3), fixing (eta=+1) selects (J=+1), and fixing (eta=-1)
selects (J=-1). Inflow therefore supplies a quantized magnitude and an exact
relative sign selector.

## Mirror-pair obstruction

If boundary orientation is part of the admitted source state rather than an
externally fixed port, the joint minima are

\[
(\eta,J)=(+1,+1),qquad(-1,-1).
\]

The simultaneous mirror action exchanges them. The relational observable
(eta J) equals one on both, while the absolute flavor sign takes both values.
Thus anomaly inflow does not select an absolute (J); it locks flavor
orientation to boundary orientation.

Fixing (eta=+1) leaves one state, but that operation restricts the physical
groupoid to the stabilizer of a reference orientation. It creates a new
relational experiment. It does not reveal an absolute sign of the original
unoriented source.

## RG and threshold protection

Anomaly matching preserves the integer level between ultraviolet and infrared
descriptions. A gapped vectorlike threshold pair contributes opposite shifts
and cannot change (k). This is stronger threshold survival than any previous
flavor candidate: the relative orientation coefficient is topologically
protected, subject to the declared symmetry and gap assumptions.

The protection has a strict boundary. If the admitted flavor channel is
anomaly-free, (k=0) and inflow supplies no orientation bias. If a threshold
closes the gap, breaks the symmetry, or changes the anomaly-supporting domain,
the matching claim no longer applies.

## Instrument gate

The inflow current (j=k\eta J) is a physical relative probe when a boundary
normal and current detector are declared. It gives the same value on the two
mirror-related minima and therefore cannot read absolute (J) without the
orientation port. It also does not calibrate the complete physical16 flavor
response. Relevant masses and detector calibration remain in its contextual
kernel.

## Classification

- CP-odd magnitude: source-quantized.
- RG and gapped-threshold survival: protected by anomaly matching.
- Flavor sign: selected relative to boundary orientation.
- Absolute sign: paired under the full mirror groupoid.
- Reference port: defines a stabilizer-groupoid experiment.
- Physical16 instrument: absent.

## Smallest exact falsifier

The two joint minima ((+1,+1)) and ((-1,-1)) have the same energy and the
same inflow current but opposite (J). This is the smallest exact
absolute-sign ambiguity. In an anomaly-free channel, (k=0) is the still
smaller falsifier of any claimed inflow bias.

## Disposition

Anomaly inflow is the first candidate to fix a CP-odd coefficient magnitude
and protect it through RG and gapped thresholds. It is not yet the complete
source principle because its sign is relational to an unselected boundary
orientation. A positive successor must internalize the orientation port by
selecting a unique oriented defect from the same source without retaining a
kink--antikink or mirror pair, and then couple the protected current to a
calibrated physical16 detector response.

Verification:

- checker: research/flavor/checkers/wp807_anomaly_inflow_relational_orientation_audit.py
- generated result: research/flavor/results/wp807_anomaly_inflow_relational_orientation_audit.json
- exact invocation: uv run --with sympy python research/flavor/checkers/wp807_anomaly_inflow_relational_orientation_audit.py
- anomaly inflow source: [Callan and Harvey](https://doi.org/10.1016/0550-3213(85)90489-4)
