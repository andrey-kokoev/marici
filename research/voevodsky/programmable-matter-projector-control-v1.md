# Programmable coherent matter-projector interface

Contract: `research/conjecture_net/contracts/programmable-matter-projector-control.v1.json`.
Checker: `research/voevodsky/checkers/check_programmable_matter_projector_control.py`.
Receipt: `research/voevodsky/results/programmable-matter-projector-control-v1.json`.
Run: `python research/voevodsky/checkers/check_programmable_matter_projector_control.py`.

## Conditional implementation class

Assume a universal coherent quantum processor with seven matter qubits, one record qubit and clean reversible-work ancillas. This is a declared engineering/simulation framework, NOT an independently verified apparatus or derivation of control from native geometry. The record qubit may separately be transported through the optical-block encoding only if that coherent hardware interface is supplied; a digital circuit diagram alone does not supply optical controlled gates.

Encode the native pair in computational indices 0..99; index 100 is separate matter vacuum. Indices 101..127 are invalid padding, never relabelled as physical states. The native matter-plus-record subspace has dimension 202 inside a 256-dimensional data register; work ancillas are additional resources.

## Source-addressed sorter

For each of the four actual chirality/doublet cases obtain W from the native adapter receipt. Set J=W tensor conjugate(W), v=J(1,0,0,1)/sqrt(2), extended by zeros outside the first 100 coordinates. The native scalar projector is Pi=|v><v| and c is the first-100-state projector.

The actual v0 is real and not one. With w=e0-v and alpha=1-v0 define

    U=I-w w†/alpha.

Exact source arithmetic verifies w†w=2 alpha, U†=U, U²=I, Ue0=v and Uv=e0. U acts identically on matter vacuum and padding. Thus in the sorted basis

    U† Pi U=|0><0|,
    U† c U=c,
    U†(c-Pi)U=sum_(j=1..99)|j><j|.

This is a synthesized basis change tied to actual native coefficients, not an arbitrary new scalar preparation or a native cycle word. Finite-dimensional unitary synthesis supplies a route to elementary gate compilation under the universal-gate assumption; no hardware gate list or calibration has been produced here.

## Coherent control protocol

1. Apply U† to matter, retaining all amplitudes.
2. Compute a predicate into a clean work bit: index=0 for primary, index in 1..99 for rival.
3. Apply exp(+i theta X_record), theta=g delta_t_model, controlled by that bit.
4. Uncompute the predicate and apply U to matter.

No measurement of matter or work bit occurs. The resulting gate is exactly

    (I-P) tensor I + P tensor exp(+i theta X),

with P=Pi or c-Pi. On matter vacuum and padding both interaction gates are identity. The reversible equality/range predicates use the explicit computational index; they do not infer particle identity from a coarse readout. Complement dimensions 99 and all original source amplitudes remain present.

The record occupation term is separate: [N_record,X] != 0. One must not multiply its exponential and the interaction exponential and call that the exact total evolution. Either use a declared product-formula simulator with error bounds, or multiplex the exact active record block exp[-it(N-gX)] and inactive exp[-itN] by the same predicate. The preceding optical-block note provides the active two-by-two spectral formula.

The frozen native K commutes with c and Pi under the completed selected-source theorem. Therefore its separately implemented exp(-it K) commutes with the whole controlled record Hamiltonian, and may be composed with the exact record-block evolution. This is conditional on that K and its actual implementation; changing K or introducing sector mixing requires a new interface proof. No K circuit is synthesized here.

## What the checker establishes

Rehydrates native hashes and all four source encodings, verifies the padded scalar normalization and exact sorter identities, then tests primary, rival and carrier-presence squares on all 128 basis vectors for every case. It also exhausts the reversible flag partition and flag uncomputation truth tables. These source-bound matrix identities justify the controlled-gate formula; the checker does not compile or execute a physical quantum processor.

## Resource and physical boundaries

The optical record's vacuum flag is not matter index 100. The record gap still acts in inactive matter sectors; only the interaction vanishes. Retain the common empty reference, K, record energy, carrier/optical offsets and control work. Predicate ancilla uncomputation is reversible logic, not proof that hardware ancilla initialization, error correction, cooling or gate control is free.

Constructed: a source-addressed coherent control specification for both complementary projectors in a declared programmable register model. Missing: hardware compilation, physical native-pair encoding/identification, calibrated K/control/time/record implementation, optical interface if selected, and preparation/readout/resource validation. Thus it strengthens the record-only simulator into an explicit abstract matter-control interface without claiming the full physical reaggregation rule.

Next concrete implementation task: compile one source case's U and reversible predicates to a named gate set, with accuracy/resource bounds, while retaining other cases as source-bound variants. Native-only selection and physical particle identification remain separate gates.
