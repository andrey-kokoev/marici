# Local E/P counterparts already have N-mediated connections

At k=4 after the local face–opposite-vertex assignment (step 11), examine the
actual counterpart relation recorded by that operation, not just adjacency
between the two new cells along the original edge.

## Existing local connections

The newly assigned E cell 132 corresponds to face P cell 341. Both routes
below consist entirely of shared triangular faces and already assigned N cells:

    E132 → N339 → N340 → P341
    E132 → N339 → N342 → P341

The newly assigned P cell 127 corresponds to face E cell 311:

    P127 → N313 → N312 → E311
    P127 → N313 → N314 → E311

Every intermediate cell is already N. No new cell or assignment is required
to establish these geometric N-mediated connections. The same result holds
for both original second-ray choices.

Thus the absence of a directly adjacent opposite charged cell is not an
obstruction to the recorded local face/vertex correspondence. Interpreting
that correspondence as requiring an additional direct face partner was too
restrictive. This audit checks geometric mediation, not equality of native
coefficient maps or histories.

Pairing must remain tagged by its interface/witness. A graph path through N
is not by itself a globally unique matching rule: for example P341 already
has its direct face partner E134 as well as its face/vertex counterpart E132.
The exact-one *direct face-neighbor* check and the local face/vertex pairing
are different scopes; replacing one with unrestricted reachability would
lose that distinction.

## A different question: filling the central gap

Connecting new E132 directly through a new N complex to new P127 would use:

    E132 → 333 → 332 → 331 → P127
    E132 → 333 → 334 → 331 → P127

Those four intermediate cells are currently unassigned and form octahedral
group 53. The half-turn exchanges the two routes. Their union has a boundary
face on E132 and one on P127, and every constituent has at least two supports
once the entire group is included. But the existing single-cell two-prior-face
rule cannot start it. Such a simultaneous group attachment would be a separate
construction operation; it is not needed to resolve the local counterpart
connections above.

## Verification

    node scripts/check-neutron-mediated-connection.mjs
    node --test tests/neutron-mediated-connection.test.mjs

[Receipt](results/neutron-mediated-connection-v1.json) retains all shared-face
witnesses, both local routes, the distinct central-gap routes and the attachment
counts. No viewer state or particle assignment was changed by this audit.
