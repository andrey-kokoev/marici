# A relative spin-frame choice cannot synchronize the existing local actions

## Result

**1708 exact checks pass.** Exhausting the proton binary-tetrahedral action group
against every electron cycle power in all four existing variants gives **960
comparisons**. Only **16** have matching projective rotation invariants, and all
are scalar/scalar pairs.

Thus a fixed relative spin frame cannot make nontrivial operations from these
two local action families jointly preserve a fixed singlet projector. This is
a conditional compatibility obstruction, not selection of a physical admission
policy or a no-go for an interacting pair.

## Existing bindings used

The checker freshly reruns both species' embedding checks. Proton source
rotations intertwine the 72-row extended mode for both spin-lift signs. Electron
cycle actions intertwine the existing cell and face encodings for both
chiralities and both lift choices.

All proton candidate generators lie in the 24-element binary tetrahedral group.
Its multiplication closure is checked exhaustively. Therefore every finite
proton request word has its action in this group, even though not every abstract
group word need be admitted at a given endpoint. Testing this supergroup makes
the negative result stronger, without claiming every tested pair is a valid
simultaneous endpoint request.

Each electron action is tested through powers zero to nine, covering its order
five or ten. Interleaving independent local requests only changes their two
local products; it does not generate an entangling operator.

## Frame-independent test

For any unitary doublet action U, use

    r(U) = trace(U)^2 / determinant(U).

This is unchanged by conjugating the spin frame or multiplying U by a scalar
phase. Preservation of a maximally entangled singlet projector by U_p tensor
U_e, in some fixed relative spin frame, requires projective conjugacy of the
two actions and hence equality of r.

In detail, in aligned frames let J be the antisymmetric singlet coefficient
matrix. Projector preservation implies U_p J U_e^T = z J for a unit-modulus z.
The two-by-two identity J U_e^T J^-1 = det(U_e) U_e^-1 then gives U_p proportional
to U_e. A fixed relative frame conjugates one side and does not change r.

The exact enumeration finds:

- proton r belongs to {0,1,4};
- a non-scalar electron cycle power never has any of these proton values;
- common values occur only at r=4, with both matrices scalar.

For these scalar/scalar matches, direct action on the singlet projector is also
checked, establishing sufficiency in the only surviving cases. No conclusion
is inferred from matching traces alone in an unchecked general carrier.

## Consequence for the proposed shared relation

If a policy requires the fixed singlet projector to be preserved at each atomic
step, the nontrivial single-species steps fail. Nor can one proton action and one
electron action be synchronized by choosing a more convenient fixed frame.
Closed local words can return to scalar actions and preserve the projector at
checkpoints, but their intermediate states need not preserve it.

This removes one tempting but unsupported repair: a relative frame choice alone
cannot supply the missing interaction. A richer source operation, evolution of
the pair state, or a checkpoint rather than atomic preservation policy would
need to be supplied and checked on its own terms.

The existing contact Hamiltonian already permits spin-selective response; it
does not state that all dynamics must remain in the fixed singlet line. Therefore
this diagnostic neither falsifies that Hamiltonian nor licenses deleting all
current geometric transitions.

## Still not supplied

No relative-position displacement, elapsed time or mediator update is assigned
to the eleven internal arrow requests. The inspected relative-motion Hamiltonian
and contact projector do not determine that scheduling interface. A time-varying
comparison frame could trivially transport a relation but would not establish
preservation of the fixed relation tested here.

The result is a concrete boundary: both species have checked local action
bindings, but the source still needs joint preparation and interaction/scheduling
semantics. This is not another missing normalization calculation.

## Verification

    python research/nima/checkers/check_predictive_pair_joint_spin_compatibility.py

Receipt: `results/predictive-pair-joint-spin-compatibility.json`.
It records exact electron invariants, comparison totals and source receipt hashes.
Owner artifacts are not modified. No physical units or new admission policy are
introduced.
