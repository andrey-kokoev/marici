# Optical–Material Hamiltonian Equivalence Cell

Owner: marici.Aspect

## Question

Can one parameter transport carry several independent material observables into
the optical apparatus, or do the channels agree only because each was fitted
separately?

The cell retains four reduced observable families: gap, phase stiffness,
screening, and relaxation. It searches for one common transport of the reduced
control coordinate. Separate per-channel transports are computed only as a
hostile diagnostic.

Admission requires:

1. every channel is individually identifiable;
2. one shared transport fits the joint packet;
3. independently inferred transports agree within the preregistered spread.

The decisive hostile fits every channel essentially exactly when independent
coordinate maps are allowed, but fails both the shared-map residual and the
transport-spread gate. This distinguishes curve resemblance from Hamiltonian
equivalence.

Passing this finite cell would still be evidence for a declared reduced model,
not proof that an unknown material realizes that Hamiltonian. Hardware data,
uncertainty propagation, and source-derived observable selection remain.

Run:

python research/aspect/checkers/check_optical_material_hamiltonian_equivalence.py
