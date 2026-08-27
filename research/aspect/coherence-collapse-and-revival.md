# Reduced coherence can vanish and later revive

## A zero reduced margin need not be a permanent horizon

Consider two orthogonal phase probes, `|+>` and `|->`, coupled unitarily to a
hidden memory. Let their reduced-system trace distance follow the exact sequence

```text
1, 1/2, 0, 1/2, 1.
```

At the middle step their reduced density matrices are identical. No channel
acting only on that reduced state can later map the single identical input to
two different outputs. Yet the distinction returns perfectly at the final step.
Therefore the later reduced dynamics cannot factor through the middle reduced
state. The missing state variable is the retained system-memory correlation.

Globally, the two joint states remain orthogonal throughout because the complete
evolution is unitary. Information leaves the chosen subsystem and returns; it is
not recreated from the collapsed reduced record.

## Closure is relative to the admitted state object

This separates two claims:

- reduced closure: the next reduced state is determined by the present reduced
  state;
- enlarged closure: the next joint state is determined by the present joint
  system-memory state.

The pilot falsifies reduced closure at the collapse step while preserving
enlarged closure exactly. A monotone “coherence lifetime” is justified only
after testing divisibility or ruling out accessible memory and recurrence.

## Optical instrument

Split a phase-encoded photon into delayed paths that become distinguishable at
an intermediate plane and recombine later. Tomograph polarization at several
planes while retaining path coherence. The middle polarization visibility can
be zero and the final visibility one. Blocking or phase-randomizing one path
distinguishes genuine recurrence from estimator artifacts.

For a memory witness, prepare `|+>` and `|->` and track their trace distance.
Any increase after a decrease rules out a divisible reduced-channel model for
that interval under the frozen preparation and measurement assumptions.

## Claim boundary

The checker uses an ideal exact trace-distance sequence compatible with global
unitarity. It does not construct a hardware Hamiltonian or include loss,
imperfect interference, preparation drift, or finite-sample uncertainty.

## Verification

```text
python research/aspect/checkers/check_coherence_collapse_and_revival.py
```
