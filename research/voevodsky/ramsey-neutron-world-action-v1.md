# Complementary marking transports the neutron belt to a different carrier

## Source recovery

The existing neutron rotation work (`research/strominger/neutron-canonical-rotation-frame.md`) derives a genuine C3 permutation of all18 ordered native triangles and36 intrinsic coordinates. That action is tied to its supplied belt generator. It is not automatically the complementary tetrahedral rotation `(0 1)(2 3)`.

This audit uses the actual belt geometry, its ordered18-triangle registry, and the established conversion to the proton Cartesian frame in `check_belt_operator_inputs.py`. The latter already separates the belt's geometric symmetry group from arbitrary tetrahedral rotations. No proton36-coordinate permutation is applied to the unlike neutron triangle/axis labels.

## Exact fixed-carrier test

Apply Q=diag(1,-1,-1), the complementary marking's spatial rotation, to every belt point in that common Cartesian frame. All six rim points and all six face centers leave the original point set; only the origin remains. In particular, writing each component as a+b sqrt(2), U0 is

    (4/3 + 7 sqrt(2)/30, -2/3 + 7 sqrt(2)/30, -2/3 + 7 sqrt(2)/30).

Its image has the last two components negated and is absent from the fixed registry. Therefore no point-induced permutation of this fixed ordered triangle registry implements Q. The existing C3 triangle/axis permutation cannot stand in for it.

This does not exclude arbitrary abstract linear operators on the36-dimensional field, or say that the neutron cannot be rotated. It says that this rotation has a different geometric target carrier.

## Constructed moving target

The receipt explicitly supplies the rotated points, preserving all triangle labels and ordered occurrences. Evaluating the ordered-mode formula on those target points independently verifies

    mode(Q triangle) = Q mode(triangle)

for all18 modes, both real and imaginary components. All1,296 pairings among those36 real/imaginary spatial vectors agree with their originals, and Q applied twice recovers every source point.

These are exact Q(sqrt(2)) geometric calculations. The spatial Gram of these vectors is **not** the native36-dimensional diagonal field metric: the vectors occupy a common three-dimensional spatial frame and do not constitute36 independent spatial basis vectors. Consequently these Gram checks are not a new proof of the full intrinsic field metric or its PN intertwiner.

## The actual next missing cell

A cross-context PN square needs correctly typed maps

    T_A : P_A -> N_A,
    T_B : P_B -> N_B,
    Q_P : P_A -> P_B,
    Q_N : N_A -> N_B,

and the equality `Q_N T_A = T_B Q_P`. The two N carriers must include their different geometric mode frames. Treating both targets as one fixed registry hides that datum.

One can define the target PN map by conjugation to make this square commute. That is a covariant candidate definition, not a verification that an independently source-bound target PN construction produces it. Reconstruct the target's intrinsic coordinate/phase conventions and its ordered-rotation PN completion, then compare the two routes. The source selection of that completion remains explicit, as in Strominger's original global PN candidate.

The E carrier action, shared-edge/vertex readouts, native higher-WG comparisons and general descent remain open. Neither the earlier local sewing result nor this moving geometry supplies them automatically.

## Verification

The prospective contract and checker were frozen at `scc-freezes/ramsey-neutron-world-action-v1.c407926c5f067a58.json`; the SCC challenge passes. The checker verifies the geometry hash and retained triangle-record root before calculating. Result: `results/ramsey-neutron-world-action-v1.json`; checker: `checkers/check_ramsey_neutron_world_action.py`.

No source geometry was modified, no full PN commutator was claimed, and no graph verdict, net revision or Git checkpoint was changed.
