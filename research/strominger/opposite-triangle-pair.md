# Does a filled photon mean opposite directed triangles?

## Question

Operator conjecture: a photon is the pair ABC and ACB on the same three vertices, while the neutrino candidate is one directed triangle. Test existing assembly without adding a particle-specific face rule.

Rivals: the extra occurrences survive only in primitive records; the generated action and assembled geometry coincide; an apparent two-step exchange is just application of an action followed by its inverse.

## Fresh result

| Measure | ABC only | ABC and ACB |
|---|---:|---:|
| Primitive directed occurrences | 3 | 6 |
| Incidence rank | 2 | 2 |
| Directed-occurrence kernel dimension | 1 | 4 |
| Raw endpoint-continuation outdegree | 1 | 2 |
| Generated permutation group order | 3 | 3 |
| Scheduled centroid return applications | 3 | 2 |
| Coefficient-network transfers | 135 | 135 |

The unchanged relative assembler returns identical geometry in the two runs. The unchanged directed-triangle coefficient constructor returns **identical transfer manifests**, including weights and stage-labelled endpoints, not merely equal counts. Their reports still retain different input arrow/cycle lists.

Both constructions use the existing declared equilateral metric, not an arrow-only inference of a spatial scale. The coefficient frontend uses the same offset 3D triangle coordinates in both runs, so the centroid-edge frame is nonsingular. The relative assembler uses its existing two-dimensional affine metric presentation.

## Why the two-step return is real but not the proposed swap

With a single generator R, the shared wrapper schedules R,R,R. Adding the reverse cycle supplies R and its inverse; the wrapper schedules R,R^-1. The action word is identity after two applications. Spectral encoding and reverse recovery pass for both inputs.

Thus there is a genuine schedule distinction, but no exchange of filled and unfilled face records has been constructed. These are generator applications under a supplied list, not physical oscillation periods. Nor is the raw six-occurrence continuation the same operation as that isometry schedule: it branches to two successors per occurrence.

## Filling versus reversal

An oriented triangle's boundary consists of three signed edge terms. Reversing orientation negates that boundary chain; it does not require six independent primitive occurrences. A face witness and a reversed arrow set remain distinct input types. The single directed triangle already becomes a filled triangular disk under the common center-cone rule.

Consequently adding reverse arrows is not what the current processor means by filling.

## Check against Voevodsky's recombination proposal

The edge-link note lists:

    ACE + BDF
    ACF + BDE
    ADE + BCF
    ADF + BCE

Each output consists of two disjoint three-vertex supports, collectively using six vertices. None is ABC plus ACB on the same three vertices. The retained correspondence exchanges separate output triangles; it is not evidence that each photon contains an opposite-direction pair internally. The note does not supply a directed-occurrence extraction rule that would imply that doubling.

## Disposition

The one-cycle and opposite-pair records are distinguishable at primitive incidence and at the declared generator schedule. They are **not distinguished by the existing geometric output or coefficient-network transfer measure**. No photon/neutrino classifier follows from this test, and the recorded two-photon recombination does not derive the proposed internal pairing.

## Verification

```sh
python research/strominger/checkers/check_opposite_triangle_pair.py
```

All 11 exact checks passed. Receipt: `research/strominger/results/opposite_triangle_pair.json`, containing both sources, geometry, coefficient reports, source hashes and the tested output supports. The checker imports existing constructors and does not alter their algorithms or regenerate shared stores.
