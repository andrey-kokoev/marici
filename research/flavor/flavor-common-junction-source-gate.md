# Common-junction source gate: WP1208

## Question

Can the common junction and spectral ordering be derived from a source-level
instrument?

## DPC resolution

- **Problem:** derive the common junction and its dark/bright spectral
  ordering rather than retaining its phase as a reference.
- **Bold conjecture:** reciprocal normalized Kirchhoff incidence with a
  positive Gram derives the common junction and its ordering.
- **Named rivals:** weighted junction; finite-temperature reverse jump;
  non-isometric threshold; missing endpoint-reciprocity authority.
- **Risky consequences:** the positive Kirchhoff Gram is a rank-one
  projector; reciprocity and normalization force primitive weights
  \(1/\sqrt 2\); the selected ray is the unique zero mode; the bright
  difference ray has unit cost; the lossless completion is unitary; the
  lowering dissipator has a unique dark fixed point and a global gap.
- **Strongest falsification attempt:** a weighted junction selects a
  different ray, finite temperature introduces reverse jumps, and lossy
  threshold transport is non-isometric.
- **Exact residual:** microscopically authorize endpoint reciprocity, then
  identify the flavor RG, transport isometrically through thresholds, and
  calibrate the physical16 realization.
- **Disposition:** construct a conditional common junction; reject weighted,
  thermal, and lossy rivals.

Checker: `research/flavor/checkers/wp1208_common_junction_source_gate.py`

Result: `results/wp1208_common_junction_source_gate.json`
