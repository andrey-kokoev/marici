# Genuine finite cyclic transport closes the residue bridge

`agda/ObserverSignedCyclicCover.agda` constructs the state type Fin(suc n) for every positive period. Forward rotation adds the residue of1; backward rotation adds its additive inverse. Both inverse laws are proved, yielding an actual equivalence and a univalent cover of the original comparison loop.

A first-order signed language contains stay, up, down and composition. Its interpreter agrees with actual transport for EVERY state and expression. Backward correctness uses inverse transport, not absolute winding. Thus the signed action is now supplied directly by finite-state permutations.

## Checked bridge and obstruction

Transport of the origin through k positive turns gives the residue of k. Its numerical projection agrees with the preceding positive-power residue observer. The bridge transfers the common-period invisibility theorem to joint observations in these genuine finite state spaces, including equality of their bound proofs.

Every finite family of these cyclic covers therefore misses an actual nontrivial common-period path. No decoder of its joint readings faithfully reconstructs all positive-power paths. The integer-cover separation proof remains the semantic witness of nontriviality; it is not a replacement for the finite observers.

This closes the specific signed-cover construction gap from the previous leaf. It does not prove a signed-integer normal-form theorem for all possible paths, completeness of the expression language, or limitations of every conceivable observer. The primitive up/down labels denote mathematical comparison directions, not admitted reverse machine runs or physical time.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-signed-cyclic-cover.log. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Characterize finite sufficiency when a domain bound IS supplied. A period larger than a positive winding bound should support faithful reconstruction of the bounded powers; conversely the existing unbounded-family obstruction remains. Test pairwise separation by a sufficiently large finite cyclic probe, distinguishing a bound-dependent finite observer from an observer complete for all unbounded comparisons.
