# Inner-face birth trial: existing horns recover cells or coarsen the body

## Actual test

Freshly read the geometric trial and `agda/MarkedTetrahedronCoherence.agda`. The latter supplies contractible completion spaces for all four missing-face choices, given the remaining marked inputs. This lets us ask a concrete preliminary question: which tetrahedral horn-shaped incidences already exist near the proposed inner face, without supplying a new apex or new faces?

Use the previously declared center-cone realization of the twelve-triangle proton-like surface. It has nine vertices including its center O. This remains a geometric adapter, not an identification of those points with native path-coherence vertices.

The retained seed arrow A->B permits the declared incidence selector

    (A->B) -> triangle OAB.

This uses an actual source mark rather than camera height. It is equivariant when the source mark is transported. It is not a theorem that this is the uniquely intended physical face-selection rule; reversal B->A picks the same underlying triangle, with reversed orientation.

## Exhaustive result

Enumerate all 126 four-vertex subsets. Retain those with at least three faces in the existing complex:

| Candidate type | Count | Volume |
|---|---:|---:|
| Existing cone tetrahedron | 12 | 2/9 |
| Union of three existing cone tetrahedra | 4 | 2/3 |
| Coplanar candidate on an outer face | 4 | 0 |

No candidate has strictly positive volume smaller than 2/9.

At the selected OAB face there are exactly four candidates:

- OABF_ABC and OABF_ABD: its two existing neighboring cells, already having all four faces.
- OABC and OABD: three known inward faces, with the unsplit outer triangle missing. Completing that geometric boundary makes a coarse cell equal to the union of three existing cells, not a new smaller tetrahedron.

The corresponding outer triangle is partitioned by its already-existing face center. Coning that partition to O proves the union geometrically; volume equality alone is not being used as a proof of equal regions.

## Native-constructor interpretation remains explicit

The native source's `unique023`, `unique012`, `unique013`, and `unique123` complete supplied *path-coherence* horns, not arbitrary drawings. The geometric triangle records do not by themselves provide a typed interpretation into those inputs. This enumeration is therefore a necessary incidence reconnaissance, not a fresh Agda admission or proof that a spatial tetrahedron has been generated natively.

When a horn actually comes from an existing retained package, the established completion/forget equivalence recovers that package up to its proved equality. That operation cannot be described as adding an independent spatial cell merely because its missing face was temporarily omitted. A deterministic excitation could still be a function of retained inputs; it would require its own observable and dynamics. Contractible completion does not rule out every such physical interpretation.

## Outcome

The literal no-new-input version of the proposed birth fails in this finite geometric realization: the inner neighborhood supplies old cells, larger coarse cells, and degenerate cells, but no new smallest tetrahedron.

Two distinct hypotheses remain, neither silently adopted:

1. A genuine source operation creates a new vertex/refinement, with a rule fixing when and where it happens and what distinguishes the new cell from bookkeeping subdivision.
2. The electron-like object is a new persistent *mode or witness* supported on an existing internal cell/interface, rather than an additional spatial simplex.

The second avoids assuming geometric growth, but still needs a source-derived response and a particle-identifying observable. No electron mass, charge, spin, detachment law or gravitational coefficient has been assigned by this test.

## Verification

`python research/nima/checkers/check_inner_face_native_horn_candidates.py` passes exact exhaustive incidence and rational-volume checks. Receipt: `results/inner-face-native-horn-candidates.json`, containing all twenty candidates. Existing geometry, viewer, native constructor and historical receipts are unchanged. No formal closure or physical electron identification is claimed.
