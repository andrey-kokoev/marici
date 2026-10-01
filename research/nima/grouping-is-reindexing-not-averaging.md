# Correction: packet grouping is reindexing, not averaging

## Evidence and corrected identification

The local `incidence-rung-tower.md` and its checker define source and target grouping as indexing the same complete directed packet set. Each grouped view unpacks to that same set. No arithmetic reduction is performed by those operations. This note reports local source inspection, not an independent audit of public remote main.

For the completed tetrahedral carrier let E={(u,v):u!=v}, with |E|=12. Its scalar packet-value space admits bijective reindexings

    G_F: R^E -> direct-sum_u R^(E_u^+),
    G_T: R^E -> direct-sum_v R^(E_v^-).

Each target has twelve scalar coordinates overall, not four. For fixed ordering these maps are permutation matrices. Consequently

    G_F^-1 G_F = I12,
    G_T^-1 G_T = I12,
    tau = G_T G_F^-1,
    tau^-1 = G_F G_T^-1,
    G_T^-1 tau G_F = I12.

This is exact lossless regrouping. It needs no averaging, signed subtraction or restriction to a four-dimensional generated subspace. It retains all twelve arbitrary packet values.

## Separate optional copy-and-average construction

The previously studied maps

    C=S^T: R^4 -> R^12,
    R=T/3: R^12 -> R^4

are source copying and target averaging. They are not G_F and G_T. In particular, identifying them with alpha and beta when those names mean the documented grouping operations is incorrect.

The matrix results remain valid for this separate construction:

    b=RC=(J-I)/3,
    b^-1=J-3I,
    gamma=C b^-1,
    R gamma=I4,
    gamma R C=C.

The projector gamma R splits R^12 into im(C) and ker(R), of dimensions four and eight. This describes restricted inversion of an averaging readout; it is unnecessary for reversing lossless indexing.

## Withdrawn inference

We withdraw the earlier conclusion that signed subtraction is the missing operation in the documented grouping cycle. That conclusion depended on treating grouping as averaging. No information-reducing operation has been identified within the source/target regrouping steps.

Signed reconstruction is required in the stated scalar-coordinate implementation of the optional averaging inverse, not by the indexing cycle. The averaging models in `proton-electron-shared-state-comparison-hypothesis.md` are separately specified provisional dynamics; their existence does not make grouping an average.

## Current state of the construction

Established under their respective assumptions:

- Twelve directed tetrahedral packet slots can be regrouped losslessly by either endpoint.
- The six-arrow scalar seed admits exact tree-plus-cycle record reconstruction; arbitrary independent cycle sums cannot simply be discarded.
- A separately chosen four-state copy/average operator has an exact quadratic inverse and a restricted packet-space inverse.
- The shared-seed geometric pair constructs two congruent bodies with a common comparison identity, not identified proton and electron species.
- Its sparse, geometric and dense coefficient ledgers are distinct. None derives a proton-electron pruning-minimal count.

Not established:

- That the regrouping cycle performs the optional 12-to-4 averaging reduction.
- That the copy/average inverse is an operation in the documented grouping grammar.
- Reversibility of every rung transition, a proton-electron realization, its energy readout, or a physically selected n in C(n,3).

## Next structural question: promotion

The incidence tower also performs promotion: old undirected edges become vertices, and sharing an old endpoint creates adjacency in the new line graph. This is not mere regrouping, so the regrouping inverse does not settle its reversibility.

The next audit should determine exactly what promotion retains: original endpoint labels, old-edge addresses, orientation roles and incidence witnesses. Then construct a reverse on that retained data, or exhibit an ambiguity if only the bare promoted adjacency survives. Distinguish lossless reconstruction of the actual labelled presentation from reconstruction up to graph isomorphism.

No new particle count should be assigned until the actual transitions and their retained data are specified.

## Verification

`check_incidence_rung_tower.py` checks that both indexing views unpack to the original directed set through all tested promotions. `check_restricted_grouped_packets.py` verifies the separate copy/average model; its success is not evidence identifying that model with grouping.
