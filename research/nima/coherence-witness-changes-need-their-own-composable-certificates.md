# Coherence-witness changes need their own composable certificates

## Result

The tetrahedral verifier now has a second, more flexible transport contract. A face witness may change if the change is itself accompanied by a verified degree-two homotopy. The tetrahedral filler must change compatibly with those supplied corrections.

A three-stage example passes this corrected contract even though the earlier strict witness-transport checker rejects it. The direct stage comparison agrees with the two-step comparison, including all four chosen face corrections.

Conversely, three individually valid corrected comparisons can still fail their composition check. This is a concrete higher-coherence obligation, not a repeated check of the original edge matrices.

This remains a finite module fixture. It does not identify the four actual productization towers.

## 1. Why strict witness transport was insufficient

`valid-triangular-faces-need-not-fill-a-typed-coherence-tetrahedron.md` retained the four face homotopies H and the tetrahedral filler K. Its stage comparison U required exact equalities

`H_new U = U H_old`,

`K_new U = U K_old`.

Those conditions are useful but restrictive: legitimate choices of witnesses need not be identical after changing coordinates. Rejecting their strict transport does not prove that no higher comparison exists.

The new verifier distinguishes a certified change of witness from an unexplained replacement.

## 2. The corrected face comparison

All endpoints and comparisons use the previously verified three-term complexes of filtered bimodules. Edge maps continue to transport strictly, and source identifications remain bound to the structural fixture.

For each face i<j<k, supply a module-linear, filtration-preserving degree-two map

`J_ijk : C_old,i,0 -> C_new,k,2`.

The checker requires

`H_new,ijk U_i - U_k H_old,ijk = delta(J_ijk)`,

where

`delta(J)_0 = d_new J`,

`delta(J)_1 = -J d_old`.

Both components are checked. J is a witness for a particular change of H, not permission to replace H arbitrarily.

## 3. The filler cannot change independently

The face corrections have their own alternating tetrahedral combination

`B = F_new,23 J_012 + J_023 - J_123 F_old,01 - J_013`.

It must account for the changed tetrahedral boundary:

`Omega_new U_0 - U_3 Omega_old = delta(B)`.

For filled endpoints the verifier additionally requires

`K_new U_0 - U_3 K_old = B`.

The last equation is stronger than merely checking that its differential vanishes. A nonzero closed discrepancy cannot be silently discarded.

In these complexes, concentrated in degrees 0,1,2, there is no degree-three map available to correct that remaining discrepancy. This is a property of the declared fixture, NOT a theorem that an actual coherence hierarchy terminates at this level.

## 4. Compose the corrections as well as the coordinate maps

For consecutive comparisons U from stage 0 to 1 and V from stage 1 to 2, with corrections J and J', the composite correction is

`J_composite,ijk = V_k J_ijk + J'_ijk U_i`.

The direct stage-0-to-stage-2 comparison must supply precisely this correction, alongside the composite vertex maps V_i U_i.

The checker verifies all four vertex-map identities and all four correction identities. It also independently validates each of the three stage comparisons before comparing their routes.

## 5. Worked examples and negative tests

The three structural stages use successively the coordinate gains

`Q=diag(2,3,5,7,11)`,

`R=diag(3,5,7,11,13)`.

The chosen nonzero face H_023 and filler K are scaled by 1, 2 and 3 at the respective stages. Explicit J_023 corrections account for the changes. Their direct correction agrees with the sum of the two transported successive corrections.

The tests also establish:

- Removing a required face correction is rejected.
- Adding a closed degree-two term to a filler leaves its individual tetrahedron valid, but requires new comparison data; the unchanged comparison is rejected.
- Altering the direct comparison by closed corrections on faces 012 and 013 can leave every individual comparison and filler equation valid. Nevertheless the corrected comparison routes disagree, and the composition check rejects them.
- Incorrect module maps and an asserted identification with the physical towers are rejected.

The third test is central: validity of every comparison separately is not coherence of their composition.

## 6. The original obstruction is not erased by changing witnesses

Every admitted J intertwines the left action, which is also the chain differential. Therefore

`delta(J)_0 + delta(J)_1 = d_new J - J d_old = 0`.

The earlier obstructed example has a nonzero component sum for its tetrahedral boundary. Under the admitted face changes this sum transports by the invertible vertex comparisons; it cannot become zero.

Thus the previously certified obstruction is invariant under this class of higher witness changes. Replacing all faces by zero would change the data outside that equivalence class; it is not a repair supplied by the present contract.

This is a sufficient obstruction invariant, not a complete classification of higher coherence classes.

## 7. Remaining application gate

We now distinguish:

1. comparisons between presentations;
2. chosen witnesses comparing composites;
3. fillers comparing face pastings;
4. certified changes of those witnesses;
5. composition of the witness changes.

The substantive missing application is still the assignment of actual source/productization, observer and comparison objects to this typed structure. The finite complex was constructed from the audited module fixture; it was not derived from the four actual towers. Numerical task certificates, physical calibration, and noninvertible tail restrictions do not acquire a structural interpretation merely because this checker exists.

Further fixture variants alone would not discharge that identification gate.

## Verification

`python research/nima/checkers/check_coherence_witness_transport.py`

Portable verification:

`python research/nima/certificates/verify_coherence_witness_transport.py research/nima/results/corrected-coherence-witness-transport.json research/voevodsky/certificates/verify_structural_gain_square.py`

Isolated execution needs three trusted verifier files and the bundle JSON. No producer or solver is imported. All positive tests and five adversarial rejections pass.

Artifacts:

- `research/nima/results/corrected-coherence-witness-transport.json`
- `research/nima/results/coherence-witness-transport-tests.json`
