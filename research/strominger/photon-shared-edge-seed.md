# Photon: the recovered shared-edge two-triangle seed

Added the prior photon construction to the six-model arrow collection, replacing the proposed ABA segment.

## Seed and retained stage

    A -> B -> C -> A
    B -> A -> D -> B

The triangles share AB with opposite orientations. The retained faces are ABC and BAD. Their shared edge cancels in the boundary, leaving the four-edge outer loop B -> C -> A -> D -> B.

The seed has four vertices, five edge supports, six directed occurrences and two faces: f=(4,5,2), Betti=(1,0,0). It is a two-triangle disk hinged along AB in the existing tetrahedral metric, not a newly supplied flat diamond. CD is absent from the seed support.

## Comparison with proton

The primitive arrow set is exactly the existing proton seed. The source coordinates and metric are also reused. What differs in this record is the **retained stage and selected continuation plane**:

- photon record: the two-face seed and its existing conjugate cyclic modes;
- proton assembly: completed tetrahedral structure and its retained native protocol.

Running the unchanged geometric assembler to completion still produces four tetrahedral facets. We do not alter that processor to stop only for a particle label; the two-face stage is recorded explicitly. Why this stage is selected as a separate emitted sector remains the next construction question.

## Recovered continuation

The six-occurrence registry is `(AB,BC,CA,BA,AD,DB)`. Endpoint-compatible extension gives ten composable-pair rows. Prefix copying L has rank six; final aggregation A has rank six; K=A L has rank four.

The prior exact vectors

    g_plus=(1,-1,-omega^2,-1,1,omega^2),
    g_minus=conjugate(g_plus)

obey K g_plus=omega g_plus and K g_minus=conjugate(omega) g_minus. Their real plane has dimension two, a three-step aggregate return, and the existing averaged invariant metric diag(3,1). Nothing new is attached to manufacture these modes.

Freshly reran Nima's source checker and then verified 17 exact collection-entry checks, including topology, arrow identity, occurrence order, retained-span factorization, both modes, metric invariance and unchanged full completion.

## Collection

`research/strominger/results/arrow_particle_collection.json` now contains:

1. proton;
2. neutron;
3. electron;
4. neutrino #1;
5. reversed-electron positron;
6. shared-edge photon.

The collection builder checks source hashes and keeps the photon stage separate from full geometric closure.

## Reproduce

```sh
python research/nima/checkers/check_photon_two_packet_candidate.py
python research/strominger/checkers/check_photon_shared_edge_seed.py
python research/strominger/checkers/check_positron_reversed_seed.py
python research/strominger/checkers/build_arrow_particle_collection.py
```

Source manifest: `research/strominger/inputs/photon-shared-edge-seed.json`.
Result: `research/strominger/results/photon_shared_edge_seed.json`.

Prior sources: `research/nima/photon-two-packet-construction.md` and `research/nima/photon-tetrahedron-octahedron-witness-helix.md`.
