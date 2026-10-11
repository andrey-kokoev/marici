# A concrete retained-record shape progression: face promotion and flags

## What was reused and what is new

Freshly inspected `NestedExchangeNextCell.agda` and `TetrahedralComparisonFeedback.agda`. They already construct comparisons of retained packages, including a nonvacuous filled typed tetrahedron, exact return recovery and history-sensitive comparison changes. Reimplementing that promotion as a new discovery would be redundant.

For the operator's shape-growth question, this turn instead tests an explicit geometric successor policy:

1. Retain the current finite simplicial complex K.
2. Promote every nonempty face of K to a vertex carrying its exact old face record.
3. A new simplex is a strict inclusion chain of those records.

This is the order complex of the nonempty face poset, equivalently barycentric subdivision. Once chosen, the policy is deterministic and equivariant under relabelling. It requires no singled-out bottom face or fitted numerical coefficient.

It is NOT proved to be selected by the native WG rules. The face-incidence witnesses are inclusions, not automatically the path equalities used in the earlier tetrahedral coherence specialization. Representing this finite successor in a native runtime would require a declared interpretation and admitted operation.

## Exact progression

Start with one filled tetrahedron. Its vertices, edges, faces and volume cell become fifteen vertex records at the next level. Maximal flags have the form

    old vertex < old edge < old triangle < old tetrahedron.

There are 4*3*2=24 such flags. Exact enumeration gives:

| Level | Vertices | Edges | Triangles | Tetrahedra |
|---|---:|---:|---:|---:|
| 0 | 4 | 6 | 4 | 1 |
| 1 | 15 | 50 | 60 | 24 |
| 2 | 149 | 796 | 1224 | 576 |

At each step the next vertex count is the total number of old nonempty faces, and each tetrahedron has 24 maximal child flags. The alternating counts remain one.

For the existing twelve-cone realization of the proton-like boundary, one step gives

    (9,26,30,12) -> (77,400,612,288).

Thus this policy does not naturally stop at 137. These counts cannot be interpreted as electron symmetry capacities without an independently specified observation domain.

## Retention and geometry

Every new vertex remembers the exact old face that produced it. Every new maximal flag identifies its old parent tetrahedron as its largest face record. Original vertices can be recovered through their singleton-face records. Recovery uses these records, not an attempted inversion of averaged coordinates.

The abstract construction needs only incidence. For the existing affine realization, place each new vertex at its face centroid. Each old tetrahedron partitions into 24 equal-volume tetrahedra, preserving the filled body and total volume. Starting from volume 8/3, the first two subdivision levels have cell volumes 1/9 and 1/216.

Exact controls verify all 24 relabellings of the initial tetrahedron and the child-parent incidence, face recovery, cell volumes and total volumes for the enumerated examples. The usual subdivision interpretation explains preservation of the underlying space; Euler characteristic or volume equality alone is not being used as its proof.

## What kind of growth this is

This is **growth of retained presentation and geometric resolution**, not expansion of the outer body. Its top dimension stays three. It is also not the same operation as raising the dimension of a coherence comparison.

The distinction gives two legitimate but different research directions:

- **Coherence growth:** compare routes/packages and construct higher witnesses when their boundaries are supplied; existing formal adapters already implement bounded examples.
- **Shape refinement:** promote incident faces and build flags, preserving the body while generating a finer retained description; the present experiment implements this policy.

Neither operation alone creates a persistent independent particle, selects an energy, or determines an electromagnetic coupling. Exterior growth would need an attachment law specifying which boundary receives a new cell and why; physical excitation would need a state/response law.

## Verification

`python research/nima/checkers/check_retained_flag_shape_growth.py` passes using exact rational geometry and finite incidence enumeration. Receipt: `results/retained-flag-shape-growth.json`. The existing native modules and geometric source were not modified, and no new Agda admission, physical electron interpretation or ledger entry is claimed.
