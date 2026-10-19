# Arrow-seed composition and isotope-atlas attachment

[Work net](contracts/seed-composition-work-net.v1.json) · [source pins](contracts/source-pins.v1.json) · [three-vertex candidate](three-vertex-candidate.v1.json) · [Graphviz diagram](seed-composition.dot)

The [matter atlas](../../matter/README.md) and the [arrow collection](../../strominger/results/arrow_particle_collection.json) are **two evidence nodes**, not proved physical conjectures. Their authoritative files stay where they are. The atlas describes constituent/isotope claims; the collection records geometric seeds and retained stages. New collection entries do not automatically update the atlas's physical statuses. This local net is not a central registry admission.

```text
Isotope atlas ----+--> source/claim correspondence --------+
Arrow collection +                                      |
                 +--> three-vertex path candidate -------+
                                                        v
                           admissible composition and independent separation
                                                        v
                                  physical photon-channel binding
```

## Seed sources, not rewritten definitions

- [Electron and reversed positron](../../strominger/positron-reversed-electron-seed.md): ABCDEA and AEDCBA, the same completed four-simplex with reversed generator. Reversal is not yet physical charge conjugation.
- [Photon candidate](../../strominger/photon-shared-edge-seed.md): ABC and BAD, sharing AB with opposite direction. It retains two faces and conjugate continuation modes. Its primitive seed equals the proton's seed; the retained stage differs. Selection of this stage as an emitted sector remains open.
- [Earlier electron/positron cuts](../../strominger/half-electron-positron-seeds.md): the tested 2/3-edge cuts did not produce the photon continuation factor or a new assembled photon. The present three-vertex identification/path-shorthand candidate is a different supplied operation, not a refutation of that result.
- The collection also retains proton, neutron and neutrino-candidate records. This net references those records without inventing a common physical species interpretation.

## Recorded three-vertex candidate

Identify corresponding consecutive A,B,C of the opposite five-cycles; leave D,E,D',E' distinct. Display the composites CE=CDE, AD'=AE'D', AC=ABC and CA=CBA. Two directed supports then look like photon seeds:

    (ABC A, CE A C) and (AD'C A, CB A C).

Spelled as triangles: ABC and CEA; AD'C and CBA. Each pair shares AC oppositely, has four vertices and five undirected edge supports. Every displayed edge expands into retained primitive paths. The construction uses all ten primitive arrows, but eighteen times in total: AB, BC, CB and BA each occur three times across the expansions. Thus the diagrams reuse histories; they are not two independent states or disjoint output particles. Intermediate D and E' remain in those histories.

The checker verifies this precise path-support claim only. It does not supply geometric gluing, a triangle-filling coherence witness, an isometric encoder, photon-mode intertwining, independent output sectors or dynamics. The candidate is recorded rather than declared a recombination theorem. Counting these diagrams does not derive 372.

## Executable tasks

1. Compare atlas source IDs with the newer seed records, preserving their scope and discrepancies. Catalogue linkage and physical identification are separate questions.
2. Test an actual retained-state composition/separation map. Repeated use of a path in two descriptions is not automatically an independent copy of its quantum state. Find a reversible encoder with explicit residual information and validate metric, faces and continuation modes, or record the obstruction.

The [low-energy net](../low-energy/CONJECTURE-NET.md) references the composition obligation through a scoped external-dependency node. The finite E-C-2-3 merge-split model, this path-support candidate and physical e-minus/e-plus to photons are kept distinct.

Run `python research/scattering/seed-composition/check_seed_composition_net.py`. It validates the new DAG, frozen source identities, retained path counts and refusal of physical/proof promotions; it does not rerun all source-owner scientific suites. No atlas data or generated viewer assets are changed.
