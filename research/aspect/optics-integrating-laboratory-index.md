# Optics integrating laboratory

Owner: `marici.Aspect`

## Identity boundary

`marici.Aspect` is an internal Marici research persona inspired by Alain
Aspect's published work. It does not represent the real person and carries no
claim of participation, approval, authorship, or endorsement.

## Objective

Use optical systems as common physical realizations of multiple typed Marici
views. The laboratory preserves source, route, phase, polarization, temporal,
loss, and detector distinctions until their authorized physical interaction or
projection.

## Apparatus inventory

The canonical machine-readable instrument subset is maintained in
`contracts/instrument-registry.v1.json` and explained in
`instrument-registry.md`. This portfolio index is broader: inclusion here does
not by itself supply an SCC profile, nine-factor matrix, or physical execution
artifact.

- coherent and single-photon sources;
- free propagation and Green transfer;
- beam splitters and ordered path networks;
- phase shifters and frame calibration;
- polarization preparation, transport, and analysis;
- reciprocal and nonreciprocal elements;
- cavities, delay lines, feedback, and memory;
- absorption, decoherence, leakage, and environmental ports;
- homodyne, heterodyne, counting, and intensity detection;
- bandwidth, continuum-mode, and infinite-time completion.

## Required packet contract

Every packet must identify source authority, typed ports, constructor order,
phase and calibration frame, conserved or dissipated quantities, detector
kernel, completion gates, and the smallest scalar-preserving hostile.

## First milestone

1. Minimal two-path interferometer: `minimal-two-path-interferometer.md`.
2. Polarization marker and quantum eraser:
   `polarization-marker-quantum-eraser.md`.
3. Reciprocal lossy cavity as an ordered feedback system:
   `reciprocal-lossy-cavity-plant.md`.
4. Free propagation and Green transfer:
   `free-propagation-green-transfer.md`.
5. Selected-channel transmission-zero classification:
   `selected-channel-transmission-zero.md`.
6. Nonreciprocal polarization transport and scattering:
   `nonreciprocal-polarization-scattering.md`.
7. Calibrated homodyne and heterodyne detection:
   `calibrated-homodyne-heterodyne-detection.md`.
8. Finite-bandwidth and continuum-mode completion gates:
   `finite-bandwidth-continuum-completion.md`.
9. Cross-sector optics machinery audit:
   `cross-sector-optics-machinery-audit.md`.
10. Calibrated photon counting and intensity statistics:
    `calibrated-photon-counting-intensity-statistics.md`.
11. Programme-wide requirements and verification audit:
    `optics-machinery-programme-audit.md`.
12. Causal dispersive magneto-optic response:
    `causal-dispersive-magneto-optic-response.md`.
13. Positive-real impedance versus dark reflection:
    `positive-real-impedance-versus-dark-reflection.md`.
14. Reciprocal denominator-sewing network:
    `reciprocal-denominator-sewing-network.md`.
15. Directional double-triangle moving-fiber interferometer:
    `directional-double-triangle-moving-fiber-interferometer.md`.
16. Two-frontier optical instrument build audit:
    `two-frontier-optical-instrument-build-audit.md`.
17. Two-instrument calibration robustness:
    `two-instrument-calibration-robustness.md`.
18. Finite lossy photodetection quantum instrument:
    `finite-lossy-photodetection-quantum-instrument.md`.
19. Finite dead-time photodetection memory instrument:
    `finite-dead-time-photodetection-memory-instrument.md`.
20. Calibrated six-port scale identification instrument:
    `calibrated-six-port-scale-identification-instrument.md`.
21. Quantum bath dilation of magneto-optic loss:
    `quantum-bath-dilation-of-magneto-optic-loss.md`.
22. Finite multibin quantum bath dilation:
    `finite-multibin-quantum-bath-dilation.md`.
23. Dyadic passive bath refinement:
    `dyadic-passive-bath-refinement.md`.
24. Markov oscillator loss-noise identity:
    `markov-oscillator-loss-noise-identity.md`.
25. Thermal sideband detailed-balance instrument:
    `thermal-sideband-detailed-balance-instrument.md`.
26. Multifrequency KMS coherence instrument:
    `multifrequency-kms-coherence-instrument.md`.
27. Dual-clock coprime anti-alias instrument:
    `dual-clock-coprime-antialias-instrument.md`.
28. High-Q cavity completion escape:
    `high-q-cavity-completion-escape.md`.
29. Robust dual-clock jitter observability:
    `robust-dual-clock-jitter-observability.md`.
30. Reciprocal cross-sheet phase interferometer:
    `reciprocal-cross-sheet-phase-interferometer.md`.
31. Closed-loop boundary Schur-zero instrument:
    `closed-loop-boundary-schur-zero.md`.
32. Boundary-mode lift determinant-control instrument:
    `boundary-mode-lift-determinant-control.md`.
33. Minimal optical transfer-identifiability instrument:
    `minimal-optical-transfer-identifiability.md`.
34. Live calibration-epoch interlock:
    `live-calibration-epoch-interlock.md`.
35. Cross-run optical witness-splicing test:
    `cross-run-optical-witness-splicing.md`.
36. Frame-transport joint-witness audit:
    `frame-transport-joint-witness-audit.md`.
37. Marici joint-witness composition coverage:
    `marici-joint-witness-composition-coverage.md`.
38. Controlled Clifford-phase interferometer:
    `controlled-clifford-phase-interferometer.md`.
39. Poisson monitor-port rank restoration:
    `poisson-monitor-port-rank-restoration.md`.
40. Reciprocal ordered-current heterodyne witness:
    `reciprocal-ordered-current-heterodyne-witness.md`.
41. Phase-reset Blackwell trace audit:
    `phase-reset-blackwell-trace-audit.md`.
42. Revision-binding deletion replay:
    `revision-binding-deletion-replay.md`.
43. Mixed-grade two-axis lock-in interferometer:
    `mixed-grade-two-axis-lockin-interferometer.md`.
44. Source-fixed pilot phase connection:
    `source-fixed-pilot-phase-connection.md`.
45. Optical Carrier source-relation audit:
    `optical-carrier-source-relation-audit.md`.
46. Optical Carrier route identity and direction audit:
    `optical-carrier-route-identity-direction-audit.md`.
47. Energy-normalized optical criticism margin:
    `energy-normalized-optical-criticism-margin.md`.
48. Programmable optical criticism engine:
    `programmable-optical-criticism-engine.md`.
49. Repairable complexity in optical probe libraries:
    `repairable-complexity-optical-probe-libraries.md`.

Each packet has a dependency-free exact checker under `checkers/` and a
machine-readable result under `results/`.

## Open machinery frontier

- source-derived physical instantiations of the cross-sector templates remain
  owned by their respective sectors.
- continuum quantum-bath completion of absorptive dispersive devices remains
  open; the finite magneto-optic dilation restores commutators in one frequency
  bin but does not derive fluctuation-dissipation or material-specific
  microscopic authority.
