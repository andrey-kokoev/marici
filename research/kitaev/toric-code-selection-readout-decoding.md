# Finite toric code: selection, readout, and decoding

Status: finite-cutoff theorem and typed interpretation for the frozen toric
code.  This packet covers WP4--WP6 only.

## Four non-implications

1. A cellulation fixes incidence but not a ground space: changing or omitting
   `H` leaves the same Carrier.
2. The stabilizer Hamiltonian selects a four-dimensional common eigenspace,
   not a preferred vector in it.  The four joint eigenvalue choices of a
   commuting logical `Z` pair are an exact counterexample.
3. Multiplication by local stabilizers identifies Pauli representatives on
   the code space, but does not prepare any density operator.
4. Preparation or a boundary condition may select a logical state, but this
   adds source data beyond incidence and stabilizer equivalence.

Thus cellulation, energetic subspace selection, representative equivalence,
and state preparation are distinct typed maps.

## Detection, separation, reconstruction

Local stabilizer measurements detect endpoint/face defects.  Their
independent binary rank is `2L^2-2`, and they are blind to four logical Pauli
coordinates.  Two noncontractible probes suffice only in one CSS channel,
as in the finite pilot.  For the full phase-free Pauli module, four logical
commutator probes plus the independent stabilizer syndromes give a linear map
whose kernel is exactly the stabilizer subspace.  The checker verifies this
for `2 <= L <= 5` and proves by rank deficiency that fewer than four added
binary probes cannot separate all Pauli cosets modulo stabilizers.

“Four probes” is rank-minimal after a logical frame has been included in the
experiment.  It does not define a canonical ordered probe family on an
unmarked torus.  Under `GL(2,F_2)` the three nonzero vectors form one orbit;
the ordered logical bits become physical only when a seam, mixed boundary,
preparation, or reference-loop port reduces the admissible automorphism
group to the stabilizer of that marking.

This is separation of a discrete error quotient, not reconstruction of an
unknown quantum state.  A maximal commuting logical pair supplies two bits
in one measurement setting.  Because conjugate logical loops anticommute,
all four cannot be sharp in one projective setting.  Full two-logical-qubit
tomography instead requires an informationally complete family of effects
across repeated preparations; probabilities `Tr(rho E_i)`, not a single
syndrome record, are reconstructed.

## Decoder noncanonicity and instruments

A syndrome specifies a fiber.  A recovery additionally needs a cost or
probability model (edge metric and noise likelihood), dynamics/latency,
boundary conditions, and possibly the measurement history.  The pilot's two
weight-two corrections for diagonal defects differ by a plaquette
stabilizer.  Hence they have the same syndrome and the same action on the
code space, but they are distinct Pauli operators on the ambient Hilbert
space.

Their unitary channels are distinct physical instruments off the code space:
choose a state not stabilized by their quotient stabilizer and the outputs
differ.  They become equal only after restricting to the code subspace (or
quotienting by stabilizer action).  Therefore even agreement on syndrome and
logical action does not choose an ambient recovery instrument.

## Assumptions, falsifiers, and unresolved typing

The minimality claim concerns **framed** binary linear commutator probes on
phase-free Pauli classes, with stabilizers already declared legal
equivalences and a marked logical basis.  It does
not claim minimal experimental tomography settings.  It is falsified if the
combined commutator kernel exceeds the stabilizer span or if fewer than four
logical bits separate the full quotient.

Unresolved typing for later work: a general physical-instrument equivalence
must specify its admitted state domain and whether classical measurement
records are retained.  No canonical decoder follows until a noise/dynamics
functional is supplied.  Boundaries and perturbations are outside this
packet.
