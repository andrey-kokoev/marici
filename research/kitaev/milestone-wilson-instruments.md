# Milestone: Wilson effect versus instrument

Owner: `marici.Kitaev`

The bounded successor selected under the operator's autonomous-continuation
instruction is complete.  It proves that identical Wilson parity effects do
not identify physical instruments.

Verification command:

`python research/kitaev/checkers/check_wilson_parity_instruments.py`

For `L=2,3,4,5,6`, the checker verifies equal ideal and noisy reported
effects, exact normalized output trace distance `1/2`, noisy subnormalized
distance `9/20`, zero closed-loop star syndrome, and two endpoints for every
individually resolved constituent.  Six aggregate gates are declared.

The coherent protocol uses one record bit and depth `L`; the refined protocol
uses `L` record bits and data-coupling depth one.  Classical coarsening does
not reverse the latter's dephasing.

Assumptions and falsifiers are frozen in
`research/kitaev/wilson-parity-effect-versus-instrument.md`.  Unresolved work
is a protected-ground-subspace instrument witness, a hardware-typed
comparison of verified cat ancillas, mobile ancilla fault propagation,
feedback using fine records, and perturbatively dressed ports.

Post-objective self-assessment: excitement `9/10`, confidence `9/10` for
ambient instrument inequivalence and `6/10` for its fault-tolerant code-space
extension, realized information gain `8/10`.  The main scope residual is that
the exact trace-distance witness lies in the ambient string Hilbert space,
not yet inside the toric ground space.  These ratings are non-evidential.
