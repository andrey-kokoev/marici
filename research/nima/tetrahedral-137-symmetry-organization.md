# How the four-state comparison symmetries organize 137 slots

## Question and physical boundary

The operator asks how electron symmetries organize to reach a maximum of 137. Test the existing tetrahedral/four-state comparison hypothesis rather than assuming an identified electron or fitting an electromagnetic constant.

The four-state candidate is not yet proved to have electron charge, spin or statistics. Its finite relabelling groups are not automatically the electron's physical symmetry groups. The two factors below are comparison factors, not necessarily two particles; their physical roles still require identification.

## Build-up in the existing declared domain

Each factor retains four states and twelve directed nonidentity arrows. Mark one directed arrow as its reference, leaving eleven arrow legs in the counted view, without deleting the reference from storage.

Compare arrows with arrows and states with states:

    D=(E'_A x E'_B) disjoint-union (S_A x S_B),
    |D|=11*11+4*4=121+16=137.

This uses all eligible slots in this specified domain. One marked reference per factor, two comparison factors and the exclusion of cross-typed comparisons are explicit hypotheses, not conclusions of the number itself.

## Exact symmetry organization

Fix reference 0->1 in each factor. Under bare-set S4 relabellings, only the exchange of vertices 2 and 3 survives locally, giving S2 on each factor. The two independent actions form S2 x S2.

The eleven remaining arrows have one singleton orbit (the reverse reference) and five two-element orbits. The four states have two singleton orbits (the reference endpoints) and one two-element orbit. Taking products gives:

| Slot block | Singleton orbits | Two-element orbits | Four-element orbits | Slots |
|---|---:|---:|---:|---:|
| Arrow pairs | 1 | 10 | 25 | 121 |
| State pairs | 4 | 4 | 1 | 16 |
| Total | 5 | 14 | 26 | 137 |

Thus

    137 = 5 + 14*2 + 26*4,

organized into 45 symmetry orbits. The five individually fixed slots are the reverse-reference pair and the four ordered pairs of reference-endpoint states. This is organization of records, not 137 group elements or 137 independent generators.

## The symmetry policy matters

If the two factors must share one common relabelling rather than transform independently, the diagonal S2 gives 71 orbits: five singletons and 66 pairs.

If the underlying tetrahedron retains orientation and admits only proper rotations A4, fixing a directed edge leaves no nonidentity stabilizer. There are then 137 singleton orbits. The same slot count has different symmetry organization under these policies.

The bare unmarked S4 carrier has no preferred directed reference: its orbit contains all twelve directed arrows. The reference must therefore be supplied, selected by additional retained data, or kept as a family of contexts. Prior reference-family work already handles this distinction.

## What maximum can mean

137 is the full cardinality of the selected four-state, like-typed, excluded-reference view—not a universal maximum implied by electron symmetry.

For the same counting rule with n states,

    N(n)=[n(n-1)-1]^2+n^2.

The exact sequence for n=2,3,4,5,6 is 5,34,137,386,877. Four states must be selected independently to stop at 137.

Even at four states, retaining all arrow pairs in the counted view gives 160 like-typed slots. Admitting both cross-typed blocks in addition to the selected view would give 225, but would require additional typed adapters. These controls distinguish a policy-dependent capacity from an absolute bound.

The earlier response audit also finds rank 28, not 137, for scalar factorized leg perturbations at the all-unit baseline. That is a particular response model, not a general dimensional bound. Likewise the 45 orbits leave 44 free normalized orbit masses; reference symmetry does not enforce uniform per-slot coupling.

## Disposition

The conditional combinatorial organization is now explicit and freshly checked under three different symmetry policies. It gives a concrete candidate architecture for the proposed electron comparison, but not its physical selection or electromagnetic normalization. The next source obligation is to identify what the two factors and their reference arrows physically represent before reading this cardinality as a particle property.

## Verification

`python research/nima/checkers/check_tetrahedral_137_symmetry_organization.py` passes exact permutation/orbit enumeration and count controls. Receipt: `results/tetrahedral-137-symmetry-organization.json`.

Fresh prior sources: `reference-choice-family-under-carrier-symmetry.md`, `reference-semantics-carrier-versus-counted-domain.md`, `137-comparison-fibration-weight-audit.md`, and `checkers/check_137_reference_symmetry.py`. Existing artifacts were not modified. No new ledger entry or physical electron identification is claimed.
