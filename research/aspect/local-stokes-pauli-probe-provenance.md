# Local Stokes--Pauli probe provenance

## Question

Does the frozen photon instrument lane physically supply local `I`, `X`, `Y`, and `Z` polarization probes on each photon, so that all sixteen two-photon product probes are source-derived rather than merely algebraic?

## Source and detector port

The source class is a single-photon polarization qubit in the declared horizontal/vertical mode pair. Each local station contains calibrated polarization optics, a polarizing beam splitter, two complete detector outcomes, and a time-tag record. Two-photon product records are formed by a classical coincidence join using the source trial label.

The identity probe is not a fourth analyzer setting. It is the sum of the two complete outcomes of any normalized local analyzer, or equivalently the local herald/total-count record after efficiency calibration.

## Physical analyzer settings

- `Z`: direct horizontal/vertical analysis with a polarizing beam splitter.
- `X`: diagonal/antidiagonal analysis, implemented by a calibrated half-wave rotation before the same beam splitter.
- `Y`: analysis in the states `(H + iV)/sqrt(2)` and `(H - iV)/sqrt(2)`, implemented by a calibrated quarter-wave retardance and linear analysis.

The `Y` setting does not require an external local oscillator. It measures relative phase between two polarization components of the same optical mode. The wave plate supplies the calibrated internal phase conversion. It does require a declared fast-axis convention, retardance sign, and H/V phase frame. Reversing the convention swaps the two `Y` outcome labels.

A lane restricted to real Jones rotations, half-wave plates, and linear polarizers supplies only the X--Z great circle. It does not source `Y`.

## Sixteen product probes

With `I`, `X`, `Y`, and `Z` available independently at both ports, the sixteen tensor-product expectation values are obtained from nine joint nontrivial analyzer settings plus their local marginals and normalization. This is faithful on the declared two-qubit polarization density matrix.

The physical record contract requires:

1. a frozen analyzer setting at each port;
2. both detector outcomes retained;
3. local efficiency and leakage calibration;
4. a shared trial identifier for coincidence joining;
5. quarter-wave retardance and axis calibration over the admitted photon bandwidth;
6. stable per-port `Y` label conventions across the calibration epoch.

No phase relation between the distant stations is needed merely to define local Stokes `Y` measurements. A shared reference becomes necessary only for claims involving an additional cross-station optical phase beyond the polarization tensor-product state and its coincidence statistics.

## Exact missing-Y hostile

The checker constructs two real two-qubit density matrices that differ only in the `Y tensor Y` coefficient. Every product expectation drawn from local `I`, `X`, and `Z` probes agrees exactly. The joint `Y tensor Y` probe gives opposite nonzero values and separates them.

Thus local tomography is not source-derived when either port lacks its `Y` analyzer. Algebraically writing the Pauli basis does not repair that instrument omission.

## Phase and bandwidth restrictions

The quarter-wave element must realize a relative phase of one quarter turn, within a calibrated error budget, across the detected spectral and temporal modes. Unknown birefringence before the analyzer rotates the intended `Y` axis. Broadband retardance, polarization-mode dispersion, detector-dependent spectral response, and time-varying axis drift require a larger instrument model.

The current proof is therefore physical/readout at finite ideal strength with explicit calibration provenance. It is not a broadband or device-independent tomography theorem.

## Relation to existing Aspect packets

- `causal-dispersive-magneto-optic-response.md` fixes the circular basis and shows that two circular transfers require calibrated Jones analysis.
- `polarization-marker-quantum-eraser.md` supplies complementary polarization analysis and the phase-frame boundary.
- `calibrated-photon-counting-intensity-statistics.md` proves that intensity-only counters erase phase coherence.
- `phase-referenced-product-orientation-witness.md` shows when a further path reference promotes a channel-global sign to a relative-phase record.

## Verification

Run:

```text
python research/aspect/checkers/check_local_stokes_pauli_probe_provenance.py
```

The checker is dependency-free and uses exact Gaussian-rational matrices.
