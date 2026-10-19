# Proton source spin candidates and the remaining joint binding

## Result

The two actual affine proton generators admit exact spin-lift candidates in an
explicit source-metric realization. **28 exact checks pass.** Each generator has
two opposite SU(2) lifts; together they recover precisely the six supplied moving
correspondences AB, BC, CA, AD, DB, BA.

This advances the proton side from an unspecified extra spin factor to concrete
source-compatible candidates. It does not select the physical lifts or establish
the raw proton-mode/request intertwiner.

## Construction

Realize the four affine source vertices by the regular tetrahedron

    (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1).

Differences from the first vertex have Gram matrix exactly equal to the supplied
proton metric. Each affine generator determines a permutation of these vertices.
Enumerate the 24 binary-tetrahedral unit quaternions and retain precisely those
whose Pauli conjugation maps every vertex to its prescribed image:

    U sigma(v) U* = sigma(R v).

There are exactly two, U and -U, for each generator. Both are unitary with
determinant one. Their cubes are respectively +I and -I. No sign is selected by
the affine rotation itself.

The explicit tetrahedral frame is a mathematical realization, not a derived
alignment with the electron backend's spin frame. A choice of common frame
matters to a joint vertex and must not be hidden in matching matrix indices.

## Interaction control

Using the existing logical singlet, the checker verifies for every candidate:

- U tensor I changes its projector;
- U tensor U preserves the singlet exactly.

The second statement does not identify the existing electron five-cycle action
with U. Thus common-rotation invariance cannot be used to silently synchronize
the two independent source schedules.

The two lift signs differ at amplitude level but induce the same conjugation on
projectors. A complete source binding must state which level of information it
retains, particularly for interference between histories.

## Relative-position inspection

The existing contact construction supplies a relative-coordinate space l2(Z^d),
a nearest-neighbour kinetic operator K_d, a contact projector C and a mediator
Hamiltonian. Those are additional model inputs. Its checker does not bind any
of the eleven geometric arrow requests to a lattice displacement, a duration of
Hamiltonian evolution or a mediator update.

A Hamiltonian on relative position is not itself a deterministic displacement
rule for each internal arrow. Setting the displacement to zero, choosing a
lattice direction from an endpoint label, or selecting an evolution time would
add a policy not supplied by the inspected interface. No such update was added.
This is a bounded finding about these sources, not an exhaustive repository-wide
claim of absence.

## Exact remaining obligations

- Bind the chosen proton lift to the existing 72-row extended proton mode under
  the actual geometric request, with a checked intertwiner as on the electron side.
- Supply a proton/electron relative spin-frame identification and lift policy.
- Supply the joint preparation and the action of requests on relative position
  and mediator records, or a justified separation of internal and spatial steps.
- State which shared relation is protected as an admission condition, rather than
  merely present as an operator in the model.

The electron side already has checked cell and face intertwiners. The proton
side now has source-compatible candidate matrices. The contact action remains
an unbound interface. Therefore a claimed complete joint restricted graph would
still be premature.

## Verification

    python research/nima/checkers/check_predictive_pair_proton_spin_candidates.py

Receipt: `results/predictive-pair-proton-spin-candidates.json`.
It exports all candidate matrices, vertex permutations, return signs and input
hashes. Owner sources and receipts were not modified. This checker does not
replay the geometric quotient or the full contact energy calculation.
