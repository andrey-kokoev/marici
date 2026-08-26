# Optics machinery programme audit

Owner: `marici.Aspect`

## Audit scope

The authoritative laboratory objective and apparatus inventory are in
`optics-integrating-laboratory-index.md`. This audit asks whether every named
machinery class has a bounded packet, dependency-free exact checker, passing
machine-readable result, and explicit claim boundary. It does not claim that
every optical phenomenon or continuum model has been constructed.

## Requirement-to-artifact evidence

| Inventory requirement | Primary evidence |
|---|---|
| coherent and single-photon sources | `minimal-two-path-interferometer.md`; `polarization-marker-quantum-eraser.md`; `calibrated-photon-counting-intensity-statistics.md` |
| free propagation and Green transfer | `free-propagation-green-transfer.md` |
| beam splitters and ordered paths | `minimal-two-path-interferometer.md` |
| phase shifters and frame calibration | `minimal-two-path-interferometer.md`; `calibrated-homodyne-heterodyne-detection.md` |
| polarization preparation, transport, analysis | `polarization-marker-quantum-eraser.md`; `nonreciprocal-polarization-scattering.md` |
| reciprocal and nonreciprocal elements | `reciprocal-lossy-cavity-plant.md`; `nonreciprocal-polarization-scattering.md` |
| cavities, delay, feedback, memory | `reciprocal-lossy-cavity-plant.md`; Sontag's separately owned control audit |
| absorption, decoherence, leakage, environment | cavity, quantum-eraser, polarization-scattering, and calibrated-detection packets |
| homodyne, heterodyne, counting, intensity | both calibrated-detection packets |
| bandwidth, continuum modes, infinite time | `finite-bandwidth-continuum-completion.md` |
| selected-channel zero taxonomy | `selected-channel-transmission-zero.md` |
| cross-sector integration | `cross-sector-optics-machinery-audit.md` |

## Packet-contract audit

Every bounded packet is required to state source/calibration authority, typed
ports or maps, constructor order where applicable, phase/frame conventions,
conserved or dissipated quantities, detector kernels, completion gates, and a
hostile falsifier. The programme checker tests the presence of those contract
families and records any missing field by packet rather than treating a passing
local arithmetic check as sufficient.

## Verification topology

Each packet has one checker under `checkers/` and one JSON result under
`results/`. The programme checker reads every result, requires `status=pass`,
and executes separately from the local checker suite. The local suite remains
the authority for exact residuals; this audit establishes coverage and
pairing, not a second derivation of every formula.

## Completion disposition

The finite exact optics machinery named by the laboratory inventory is
present and mechanically verified. The following boundaries remain explicit
and are not defects in that bounded claim:

- continuum quantum stochastic field construction and microscopic detector
  instruments remain conditional on the completion contract;
- causal dispersive magneto-optic response requires a source model beyond the
  finite Jones apparatus;
- physical instantiation of cross-sector templates remains owned by each
  source sector;
- no optical packet supplies an RH proof, zero-exclusion theorem for theta, or
  authority to alter another sector's carrier.

Run `python research/aspect/checkers/optics_machinery_programme_audit.py`.
The result is `research/aspect/results/optics_machinery_programme_audit.json`.
