# Symmetry classification of the sixteen localized wirings

## Main result

With the boundary ends individually fixed, the four attached record identities fixed, and ordered central provenance retained, **all sixteen candidates are inequivalent** under the carrier's geometric symmetries. The corresponding stabilizer contains only the identity.

Even after deliberately relaxing those requirements, the candidates do not reduce to a single shape: **two geometric families remain**, distinguished by an explicit distance invariant. Allowing boundary reversal does not merge them.

## Symmetry group and coverage

The transformations are

```
q ↦ centre + sign × permutation(q − centre),
```

for 24 coordinate permutations and two overall signs. All 48 transformations were checked against all 51 cells and all 104 shared faces, including their owner incidences. Group closure was checked.

The hull is verified to be a regular octahedron: in an orthonormal basis of the sum-zero tangent space, all carrier vertices lie in the radius-three L1 ball and its six extreme points are present. A regular octahedron has 48 Euclidean symmetries, so the verified transformations exhaust its geometric point group.

Positive-sign transformations preserve geometric P/E roles. Negative-sign transformations exchange them. This geometric duality is not automatically a physical operation or an equivalence of the full provenance-bearing packet API.

Arbitrary nongeometric graph automorphisms are not part of this classification.

## Fixed data versus weaker shape projections

| Equivalence contract | Acting subgroup | Orbits on 16 candidates |
|---|---:|---:|
| Ordered boundary, attached record identities and ordered provenance fixed | 1 | 16 singletons |
| Ordered boundary and P/E roles fixed; forget payloads/provenance and permit induced record relabelling | 4 | 4 orbits of 4 |
| Additionally allow geometric P/E duality | 8 | 2 orbits of 8 |
| Additionally allow endpoint exchange, with direction normalized by reversal | 16 | 2 orbits of 8 |

Only the first row is the primary fixed-data contract. The other rows are explicitly weaker diagnostic projections. They do not erase histories from the stored plans or justify physically identifying their packets.

Every induced action is checked to be a permutation of the sixteen candidates, to preserve the projected family, and to respect group composition. Orbit representatives and the full action tables are retained in the receipt.

### Provenance is independently restrictive

There are four role-preserving geometric symmetries fixing the two boundary ends. Their nonidentity elements move fixed reference attachments. Even if payloads are forgotten and record names are correspondingly relabelled, these elements change the ordered central construction trees.

Only the identity stabilizes those ordered trees in the canonical retained family. Thus dropping provenance is a substantive relaxation, not an unnoticed implementation detail.

## The residual two-family invariant

Each plan has two paired-tip channel groups:

- one has only one active physical occurrence; its other tip is retained but inactive;
- the other has both occurrences active, but its selected pair is placed at one of them.

Take that selected occurrence in the **two-active-member group**. Measure its squared Euclidean distances to the N sites carrying the P/P pair and the E/E pair. The unordered distance pair is one of

```
{2, 10}     or     {2, 2}.
```

These values are constant on the two broadest geometric orbits and distinguish them completely in the enumerated family. P/E duality can exchange the two same-role pair sites, but cannot change the unordered distances. Boundary reversal also cannot change them.

Thus one family places the selected split-channel tip equally near both same-role pair sites; the other places it near one and farther from the other. The distances use the native coordinate metric. They are not energies, amplitudes or transport costs.

The inactive tip alone is not sufficient to distinguish these families: each family contains candidates from all four covers. Even fixing cover 0 leaves two candidates in each of the broad geometric families.

## Reversal kept separate

Reversal is excluded from the primary equivalence contract. In the most relaxed shape action, the kernel contains the identity and the middle-plane reflection, represented by `-1032` in the signed-permutation convention. This explains why admitting endpoint exchange adds no further orbit merger for these reflected plans.

This is a symmetry statement about projected assignments. It is not a claim that native signal evolution or original preparation histories can be reversed.

## Consequence for selection

There is genuine residual structure to select. A source-supported selector must distinguish the `{2,2}` and `{2,10}` placement families if it is to pick one geometric pattern. Preserving labelled boundaries and provenance requires further distinctions among the sixteen individual candidates.

No preference for smaller distance is imposed: the present source supplies no such objective or locality-cost law. Symmetry classification identifies the choice; it does not make it.

## Reproduction

```sh
node research/strominger/checkers/check_su32_global_wiring_symmetry.mjs
```

Fresh headless execution passed, including geometric/group checks, action composition, exact reconstruction of the saved witness plan, and invariance/distinction of the two distance classes. All input receipts and sources are hash checked.

Receipt: `results/su32-global-wiring-symmetry-v1/verification.json`.

The scope is the fixed reading, binding, four covers and sixteen localized survivors. No native selection law, physical equivalence, new wiring, or altered provenance was introduced.
