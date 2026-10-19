# T and native 12/3 channel structure

## Source comparison

Each tetrahedral facet has twelve face/corner flags (choose an omitted vertex
and then one of its three face vertices) and three opposite-edge partitions.
The canonical flag-to-partition map has four flags over each partition. It is
equivariant under all 24 vertex permutations (288 checks).

This produces natural 12->3 and 3->12 incidence maps, but their rank is 3,
whereas exact elimination on the saved native baryon matrices gives rank 1.

| Interface | Input/output size | Rank | Nonzero coefficients |
|---|---|---:|---:|
| Geometric incidence | 12->3 | 3 | 12 |
| Native proton | 12->3 | 1 | 36 |
| Native neutron | 3->12 | 1 | 36 |
| Native electron image map | 4->2 | 2 | 6 |

An all-to-all uniform 3-by-12 matrix is also symmetry-compatible and has rank
1. Symmetry alone therefore does not select between the rank-three incidence
map and rank-one mixing. The native complex coefficients and induced metrics
must be derived, not replaced with a matrix chosen for the right rank.

More precisely, matching/flag pairs have two S4 orbits, of sizes 12 and 24.
Equivariant scalar maps have an incident and a nonincident coefficient. The
geometric projection chooses one pair of weights; uniform mixing chooses
another. The underlying symmetry has not selected the native amplitude law.

## A direct connection to the fixed-coordinate conjecture

The existing electron sector labels already have the form

```
(omitted axis, sign on first remaining axis, sign on second remaining axis).
```

The checker confirms exactly all 3*2*2=12 labels occur. This is the same
combinatorial pattern as three fixed-coordinate choices with two signed
varying directions. It supports the proposed organization of configuration
charts more directly than merely counting twelve tetrahedral flags.

However, the electron sector dictionary spans all three omitted axes. Assigning
E itself to one fixed axis would retain four of these sectors; a common T model
must explain why an E presentation carries the entire twelve-sector atlas.
The omitted-axis signs are source-specific chart labels, not yet identified
with the geometric a,b,c axes of the newly glued simplex.

The 144 sector-to-sector connections have six distinct frame matrices and
eight distinct transfer matrices in the saved source. They are chart transport,
not 144 independent scalar coefficients. Native E image-channel dimensions
remain 4->2, distinct from its 12-sector dictionary.

## Outcome

T supplies a promising chart-incidence organization, including the exact
three-choice/two-sign pattern already present in the source sectors. The simple
geometric incidence map does not reproduce the native baryon transfer. A common
field/projector/metric law over T remains the missing step that could produce
the rank-one baryon interfaces and rank-two electron interface together.

No isotope generator or viewer changed.

```sh
python research/strominger/checkers/check_T_channel_incidence.py
```

Evidence: `results/T-channel-incidence/verification.json`. Native ranks are
recomputed exactly from saved source matrices, not copied from their metadata.
