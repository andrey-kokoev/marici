# Central cell-to-dual-vertex handoff

## Native binding status

The subsequent [native end-to-end replay](native-fcc-end-to-end-binding.md) does **not** require this duality. Its E exit differs from the central dual vertex, and its native seven-view flag differs from the quarter-rotated bridge. The construction below remains a valid finite cellular adapter, not an established native P/E handoff. Prioritize the source-backed flag/action comparison before adding Fourier machinery.

## Constructed result

On the actual central tetrahedron **T184**, construct barycentric dual blocks from its source vertex flags. This gives an exact finite cellular handoff

    D: C_k(T184) -> C^(3-k)(dual T184, boundary).

The target is the **relative dual-cell presentation**, not cochains on the same primal faces. Its degree reversal is essential. The central tetrahedron's dual cell is the single barycenter vertex at (7/4,7/4,7/4,7/4).

All15 simplex coefficients are retained and recoverable. The map satisfies

    D boundary = coboundary D.

This resolves the finite cellular interface that failed under the earlier same-face coefficient identification. It does not by itself assign a physical E label to the dual vertex.

## Construction from the existing cell

For a primal k-simplex s in T184, take every saturated flag

    s < s_(k+1) < ... < T184.

Their barycenters form the simplices of its dual block. Orient each flag using the actual ordered central vertices. The degree-dependent normalization is (1,-1,-1,1) for k=0,1,2,3. Compute the boundaries of these explicit barycentric chains, discarding only chains in the physical boundary of T184, as required by the relative target.

The resulting dual cellular boundary coefficients are the primal coface incidence coefficients. Transposing them to the dual cochain differential yields exactly the primal boundary. This is checked on every basis vector, not inferred from equal dimension counts.

The graded counts are

    primal chains, dimensions0..3:       4,6,4,1
    relative dual chains, dimensions0..3:1,4,6,4.

Mapping each primal basis simplex to the functional on its dual cell, in complementary degree, gives the explicit inverse-recoverable coefficient map.

## Four sectors around one dual vertex

The four primal vertices give four three-dimensional dual blocks. Their intersections are exactly:

- pairs: the six dual faces;
- triples: the four dual edges;
- all four: the central dual vertex.

The24 barycentric tetrahedra partition the central tetrahedron. In the inherited FCC metric the original volume is1/3 and each of the four dual volumes is1/12. Thus each occupies exactly one quarter, without fitted scale.

These barycentric points are coordinates of a new presentation, not newly admitted FCC motion sites or new particles.

## Rotation covariance retains orientation

All24 central vertex-frame permutations transport the dual blocks with the correct signs. The duality map is natural when the ambient orientation line is carried. Omitting that line fails for all12 improper frames.

The source rho cycles the four dual volume sectors and reverses the orientation of T184. Its sign is explicitly retained; four applications restore the cellular orientation. A chart permutation is not silently treated as a proper3D rigid quarter-turn.

## Descending leg and retained whole

Rebind all24 descending central flags to nested dual-block closures rather than the old primal-face cochains. Their cochain windows have basis sizes

    15 -> 4 -> 2 -> 1.

All72 restrictions commute with coboundary. At every window the visible coefficients plus the retained complement reconstruct all15 coefficients. Restriction is therefore a readout of the retained whole, not deletion of the rest of its state.

The rank profile1,2,3,4,3,2,1 remains an incidence/depth proposal, not a claim that these vector spaces have those dimensions. Seven presentations still require an explicit convention for counting evolution stages.

## Fourier factor: what remains

The prior graded Tate-torus constructor acts on

    C_*(simplex) tensor V.

Its Pontryagin Fourier operator acts on V; it cannot alone repair a failed map on the simplex-chain factor. This audit supplies the latter factor through cellular duality. The next candidate is to combine this handoff with the existing channel Fourier/reciprocity action and check the mixed chart law, keeping both gradings and the orientation line.

The complementary degree3-k here is not the phase-wrap suspension in q^4=Sigma. No P/E readout, four-seven-stage scheduler, or esd7/Pb-208 evolution has been silently inferred.

## Tests and reproduction

```sh
python research/strominger/checkers/check_central_dual_cell_handoff.py
```

**18 exact checks passed.** Controls show that same-face identification still fails, forgetting relative-boundary terms changes the differential, and dropping the orientation twist breaks covariance.

[Receipt and complete basis map](results/central-dual-cell-handoff.json) retain all15 dual blocks and their flag coefficients, actual cellular boundaries,24 descending legs, exact volumes, rho action and source hashes.

Prior interfaces: [FCC face/flag binding](fcc-face-flag-binding-v1.md), [full graded esd7 realization](../nima/full-esd7-graded-tate-torus-realization.md), [graded Fourier lift](../nima/tetra-channel-comparison-and-graded-fourier-lift.md).
