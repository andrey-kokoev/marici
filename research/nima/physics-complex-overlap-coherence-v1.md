# Full complex operator coherence for the conditional overlap

## Result and verification level

The Fock/occupation route and independently computed port-density route agree on the **full unnormalized output operator** for every three-bin outcome prefix on the reviewed single-excitation/classical-memory domain. This now has an exhaustive complex operator coefficient check, not only real polarization fixtures or agreement of trace probabilities.

The relevant programme assembly/transport nodes remain open. This is conditional model coherence at the supplied laws and nominal coefficients, not independent source-law selection or physical transport.

Contract: `contracts/physics-complex-overlap-coherence.v1.json`.
Checker: `checkers/check_physics_complex_overlap_coherence.py`.

## Operator domain

The optical space is vacuum plus ten one-photon modes, dimension eleven. Classical memory allows a block for R and a block for D, with no coherent off-block memory claim. The operator space in each block has complex basis `E_ab=|a><b|`, so the complete basis has `2*11²=242` units.

E_ab with a!=b is not itself a density state. It is a valid coefficient probe for a complex-linear map. Arbitrary Hermitian optical coherence is reconstructed by combining E_ab,E_ba; its imaginary part uses `i(E_ab-E_ba)`. Positive density operators are a subset of the operator domain. No numerical complex floating-point approximation is needed: the nominal channel matrices are rational and real, and their action on each complex basis unit determines all complex coefficients exactly.

## Independent routes and composition

Route A computes the passive columns by occupation-polynomial substitution, using the symmetric-power implementation restricted to vacuum/one particle. Its detector columns use the source Kraus labels as occupation predicates: local n_port=0 or 1, fixed input/output memory, destroy the detected occupation and retain every spectator.

Route B computes passive columns directly from the ordered field equations, and extends the local four-state detector matrices by the spectator tensor factor. It uses a separate sparse density-matrix CP implementation.

For each E_ab and each prefix, compare both passive output operators and both outcome-conditioned operators entry by entry. Equal traces are also checked, but are not used as a substitute for operator equality. Taking all E_ab establishes equality of the complex-linear maps on the complete admitted domain. Induction over the prefix tree gives every complete outcome word, with memory retained.

Both routes keep the complete outcome word as a separate index. Equal numerical maps or zero operators do not erase distinct histories. Previously checked occurrence and segment-attachment policies remain in force; this packet does not invent an equivalence of differently labelled operations.

## A trace-only hostile

The checker propagates the exact coefficient of the imaginary optical coherence `i(|vac><1_x|-|1_x><vac|)` through a cavity round and no-click operation. Its output is nonzero but has trace zero.

Deleting off-diagonal terms gives a different operator with the **same trace**. Thus agreement of outcome probabilities at this prefix would miss the coherence loss. The coefficient probe need not be mistaken for a physical state: adding it with a sufficiently small real coefficient to a strictly positive density matrix gives a positive state with a detectable operator difference under the same dephasing map.

This strengthens the earlier comparison at the stated complex optical scope. It does not identify a coherent-memory CP completion or authorize any physical coherence reader.

## Domain and assembly boundaries

All tested initial operators are in total-N<=1, so passive evolution and destructive detection remain in the local detector domain. The separate 52-dimensional N=2 schedule-safe candidate remains a separate packet; it is not silently substituted into this coefficient theorem. Arbitrary multi-bin/multiphoton preparations still require their specific domain guard.

The carrier ID is the same reviewed conditional Fock/memory candidate. Matching two presentations of its imported laws is not a derivation of those laws from Bool, exchange, marked137 or another native source. Physical preparation, clock/energy and authority bindings remain unfilled.

## Fresh checks

- 242 complex operator basis units;
- 1694 passive prefix coefficient squares;
- 3388 outcome prefix full-operator squares;
- 242 complete coefficient trace-preservation checks;
- explicit preservation of imaginary optical coherence and detection of the trace-only dephasing alias.

Each full-word tree retains all eight C/N words. Inputs are hashed before and after execution. The test is exhaustive for the finite operator basis; complex linearity supplies arbitrary coefficients, not extrapolation from selected physical fixtures.

```
python research/nima/checkers/check_physics_complex_overlap_coherence.py
python research/aspect/scc/scc.py check physics-programme-v18
```

Measurement work remains parked.
