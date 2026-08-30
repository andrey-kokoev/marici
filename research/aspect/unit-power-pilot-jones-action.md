# Unit-power optical pilots with nontrivial Jones action

## Zero insertion loss is not neutrality

Freeze the alpha pilot as the identity Jones operator and the beta pilot as the
polarization swap

```text
X = ((0,1),(1,0)).
```

Both preserve total power for every input. Nevertheless, beta maps horizontal
polarization to vertical, flipping the corresponding Stokes component from
`+1` to `-1`. It also reverses circular handedness.

The disturbance is maximal on these observables despite exactly zero insertion
loss.

## One representative probe can miss the action

The diagonal polarization `(H+V)/sqrt(2)` is an eigenvector of the swap and is
unchanged. A pilot audit using only that probe declares alpha and beta
identical. The conclusion is true on the one-dimensional probe domain and
false on the full polarization space.

This repeats the context-saturation rule: neutrality must be tested on a probe
set spanning every future optical context in scope.

## Operator calibration

Complex field records for horizontal and vertical basis probes reconstruct the
two columns of the Jones operator exactly. The inverse swap then recovers the
pre-pilot horizontal field. This is an operator calibration, not a scalar gain
correction.

If only polarization intensities or Stokes vectors are measured, the global
Jones phase remains invisible: `I` and `-I` have identical Stokes action. A
coherent dual-character reference is needed only when that global phase becomes
relative in a larger interferometric context.

## Minimal optical instrument

For a deterministic lossless two-mode pilot, use a phase-stable polarization
process-tomography arm with a spanning probe basis and balanced coherent
readout. If depolarization is possible, Jones calibration is insufficient and
a Mueller or quantum-process instrument is required.

The pilot operator should be calibrated for every codeword and operating
condition before the scientific contrast is examined. A source-dependent
operator cannot be repaired by one fixed inverse.

## Claim boundary

The checker treats exact pure-state Jones optics. Depolarization, nonlinear
response, source-dependent pilot action, detector calibration, and phase drift
remain outside the claim.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_unit_power_pilot_jones_action.py
```
