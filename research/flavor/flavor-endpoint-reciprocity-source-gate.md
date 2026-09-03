# Endpoint-reciprocity source gate: WP1209

## Question

Can endpoint reciprocity be made executable from a source-level colligation?

## DPC resolution

- **Problem:** microscopically authorize the endpoint reciprocity used by the
  Kirchhoff junction instead of retaining it as an instrument assumption.
- **Bold conjecture:** an absent state plus reciprocal two-endpoint portal,
  realized as a three-Kraus channel and minimal lossless Stinespring
  colligation, derives executable endpoint reciprocity.
- **Named rivals:** \(q=0\) versus \(q=1/4\) at fixed \(z=i\); \(z=1\)
  versus \(z=i\) at fixed \(q=1/4\); unitary endpoint-heavy rotation;
  uncalibrated physical16 readout.
- **Risky consequences:** the Kraus family is trace preserving; the selected
  dark ray is uniquely stationary; the global basin has spectrum
  \(0^5,1,(1/2)^2,1/4\); complementary rows are lossless; the selected ray
  is dark in the common port and unit-bright in the complement.
- **Strongest falsification attempt:** changing \(q\) changes the basin,
  changing \(z\) changes the selected ray, and endpoint-heavy threshold
  rotation attenuates the readout.
- **Exact residual:** derive the \(q,z\) source moduli, reducing threshold
  projector, RG, and calibrated physical16 detector map from one packet.
- **Disposition:** construct a conditional endpoint-reciprocity source;
  reject modulus-free promotion.

Checker: `research/flavor/checkers/wp1209_endpoint_reciprocity_source_gate.py`

Result: `results/wp1209_endpoint_reciprocity_source_gate.json`
