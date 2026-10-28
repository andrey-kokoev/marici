# Complementary marking: proton world action and a noninvariant prepared image

## Constructed action

The two locally sewn contexts differ by the tetrahedral marking permutation `(0 1)(2 3)`. Using the source's tetrahedral rotation function, its spatial action is exactly `diag(1,-1,-1)`. On the proton's36 directed-edge/vector coordinates, define Q by renaming A↔B, C↔D and applying that spatial rotation to each vector.

This uses the same coordinate-construction prescription as Strominger's geometric P-reader; it does not infer an action from matching field endpoints. Exact arithmetic verifies:

    Q* Q = I36,    Q^2 = I36,
    Q U_reader = U_reader Q.

The full Q matrix is retained in `results/ramsey-world-frame-action-v1.json`.

## The fixed prepared image is not invariant

Let B be the existing36-by5 proton embedding. The checker first verifies `B*B=I5`, then calculates

    A = B* Q B,
    D = Q B - B A.

D has36 nonzero entries. Thus no5-by5 linear map A' can satisfy `Q B = B A'`: applying B* would force A'=A, but D≠0. This excludes a coefficient-only implementation using the **same fixed embedding**, not merely one proposed five-slot permutation.

The compressed action is diagonal with first three diagonal entries1, fourth entry0, and a nontrivial exact radical fifth entry. Compression must not be presented as an invertible five-channel context transition.

There is no contradiction with the previous local sewing results. Those checks use each context's local co-moving field coordinates. The new test asks whether their identification in world coordinates preserves one fixed prepared image; it does not.

The rotated embedding `B_target = Q B` is explicitly exported. It remains isometric by the proven identities, and `Q B = B_target` holds with unchanged coefficient coordinates. This is a covariant candidate target embedding, not proof that the source's independently interpreted target coupling equals it.

## Neutron/E gate remains typed and open

The neutron36 carrier is indexed by triangle/axis pairs and carries a nonuniform metric. It is not the proton directed-edge/vector coordinate space. The source records make this distinction explicit. Reusing Q's numerical36-by36 array as a neutron geometric action has not been justified. No such commutator test is reported as a meaningful failure.

Given an invertible PN map T, one can define `Q_N := T Q T^-1`. Then `Q_N T = T Q` holds algebraically by construction. This would be a PN-transported action, not an independently geometrically sourced neutron action. Comparing it with the action of the actual marked neutron triangles is the next non-tautological gate. The joint E action and the NE square require their own analogous binding; identity on the eight E coordinates has not been assumed.

## Verification and scope

Prospective contract: `contracts/ramsey-world-frame-action-attempt.v1.json`.
Freeze: `scc-freezes/ramsey-world-frame-action-v1.ab43826909b469c6.json`.
Checker: `checkers/check_ramsey_world_frame_action.py`.

The frozen SCC challenge passes the exact action/image audit. The imported five-channel receipt's direct input hashes were checked. This is exact rational/multiradical computation, not a new proof-assistant result or a physical implementation.

The result supplies the proton geometric comparison and identifies the required embedding change. It does not establish cross-context PN/NE field intertwining, geometric edge/vertex restrictions, native higher-WG derivations, or full incidence descent. The failed all24 history extension remains failed. No owner source, graph verdict, net revision or Git checkpoint was changed.
