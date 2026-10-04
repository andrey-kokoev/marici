# Coherence of successive barycentric presentations

## Question and disposition

Does each barycentric refinement admit a contractible type of witness-preserving comparisons with the previous presentation?

The checked answer depends on what the comparison type retains. A package containing refined annotations together with their preservation witnesses is contractible when the source annotations and carrier map are fixed. Comparisons between already-fixed annotations can retain distinct automorphisms.

Active SCC obligations: forward realization, route/coherencer compatibility, and readout descent.

## The specified preservation rule

Every refined cell has a carrier: the smallest source cell containing it. The refined cell receives the witness type associated with that source cell. A preservation package contains one refined annotation in that type and a path from the supplied source annotation to it, for every refined cell.

`agda/BarycentricRefinementCoherence.agda` defines this type as `Preservation`. Its source index type, payload family, supplied annotations, refined index type, and carrier function are explicit inputs.

`canonical` pulls back the existing source annotations. `unique` proves contractibility of the complete preservation-package type. It contracts each annotation together with its comparison path; higher payload types require no set-truncation assumption.

`PacketRefinement` applies the theorem to the actual Layer 2 tetrahedron's face types and witnesses. It retains each carrier mark and proves preservation of its supplied witness.

These are source-cell annotations. The construction does not synthesize new triangle or tetrahedron fillers relative to all newly introduced geometric vertices.

## Successive refinement

`Compose.pull-composes` proves that direct and successive pullback agree definitionally. `combine` composes two preservation packages. `comparison` compares that composition with the canonical direct package.

`comparisons-contractible` proves that the path type between any two complete preservation packages is contractible. `higher` supplies the higher certificate of the preservation-package type.

These formal results apply to arbitrary supplied carrier maps. Geometric validity of the carriers remains a separate condition. The finite checker verifies it for the two refinements below.

## Two exact geometric refinements

| Stage | Vertices | Edges | Triangles | Tetrahedra |
|---|---:|---:|---:|---:|
| First subdivision | 15 | 50 | 60 | 24 |
| Second subdivision | 149 | 796 | 1224 | 576 |

The checker verifies minimal carriers, their compatibility with every cell boundary, and all 2,745 direct-versus-successive original carrier comparisons at the second stage. Both routes select the same typed source reference.

Exact rational checks verify positive oriented child volumes, total volume 1/6, and cancellation of internal triangular interfaces. The second boundary has 74 vertices, 216 edges, and 144 triangles.

The maximum small-simplex squared diameter, measured in four barycentric coordinates, decreases from 3/4 to 21/64. Every child satisfies the usual three-quarter diameter bound relative to its parent.

Original vertices persist as singleton-face barycenters. Distinct original corners remain at squared distance 2. Refinement makes the mesh finer while preserving the original domain; these checks provide no convergence of the whole tetrahedron to one distinguished point.

## Falsifiers

### Incorrect carrier

Assigning the full source tetrahedron as the carrier of an original corner still gives a containing face. The checker rejects it because it is not the smallest carrier.

A contractible annotation-preservation package could be formed over that wrong carrier too. Hence the geometric carrier check and the typed preservation proof are separate obligations.

### Changed annotation

The negative Agda module replaces a false Boolean annotation by true while claiming reflexive preservation. The compiler rejects it with the intended false/true mismatch.

### Both annotations already fixed

`FixedAnnotations` fixes the source and target annotation to Bool, considered as a term of the universe of types. Identity and Boolean flip give distinct comparison paths. `not-contractible` refutes contractibility of this comparison space.

This is compatible with `unique`: the latter allows the refined annotation and its comparison to vary together in one complete package. After complete preservation packages have been specified, the comparisons between those packages are contractible.

## Verification

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module BarycentricRefinementCoherence -ReceiptStem barycentric-refinement-coherence -NegativeModules RefinementBadWitness
```

Fresh safe compilation and the intended rejection passed. Execution reference: `structured_command_execution:e_25120_1791070647652120800_256`.

The geometry checker reruns the previous source-bound barycentric audit before computing the two refinements.

- Checker: `checkers/check_barycentric_refinement.py`.
- Formal receipt: `results/barycentric-refinement-coherence-formal-audit.json`.
- Exact finite results: `results/barycentric-refinement.json`.
- SCC model: `nima-barycentric-refinement-coherence`.

## Scope

Established: canonical typed annotation preservation along fixed, geometrically validated carriers; compatibility under two refinement steps; contractibility of the complete preservation packages and their comparison types.

Open: a general typed geometric realization assigning new fillers to every refined boundary, an automatic contraction/clearing operation, and an infinite-refinement comparison theorem. The preservation rule is part of this construction's specification, rather than a consequence of geometric refinement alone.
