# The electron seed: a persistent unit relation inside the 144 transfers

## Finding

The existing construction contains a natural **one-dimensional scalar relation with weight one**. It is not a norm-12 seed and not one selected transfer out of 144.

For the existing logical seed z=(a,b), define

    C z=(-conjugate(b), conjugate(a)),
    B(z,w)=a w_1-b w_0.

Then exactly

    B(z,Cz)=|a|²+|b|²=||z||².

For a unit seed this scalar is **1**. C is a mathematical relation on that same seed, not an independently occupied second electron or an implemented spin-flip gate.

This is a concrete candidate for the operator's proposed electron reference arrow weight. Calling it mass weight would be the proposed valuation of this persistent relation; no charging term has been added in this audit.

## Actual construction, not a new seed

The retained coefficient construction takes a two-component complex seed and four tetrahedral face projectors:

    P_i=(I-n_i.sigma)/2,
    sum P_i=2 I,
    Jz=(P_0z,P_1z,P_2z,P_3z)/sqrt(2).

The logical carrier is the full doublet, not a specially selected spin direction. Its exact encoding satisfies J†J=I2.

The actual operators L=diag(P_i), G=N and N=JJ† all satisfy

    LJ=GJ=NJ=J.

Thus the same seed, its norm and its paired scalar survive the three-stage protocol. A seed of norm one stays norm one; 144 is not an amplification to squared norm 144.

The separate geometric electron source supplies one affine generator and one attachment point, whose orbit is a five-cycle with primitive squared edge lengths 8. That geometric source is not silently identified with the tetrahedral coefficient compiler. Neither inspected source contains an amplitude seed of norm 12.

## Why the scalar relationship is one-dimensional

The retained binary tetrahedral spin rotations preserve the bilinear form

    B(z,w)=z^T epsilon w,
    epsilon=[[0,1],[-1,0]].

The prior pairing research already identifies this invariant. Fresh averaging of U tensor U over all 24 retained rotations yields exactly the rank-one antisymmetric projector. There is only one invariant bilinear contraction, up to scalar.

There is no rotation-invariant spinor line to choose as a special electron component: the retained central commutator acts as -I. A scalar relationship between the components avoids selecting or discarding either spin component.

## Carry the relation through the actual raw coordinates

Take the exterior square of the EXISTING encoder:

    w=J e_0 wedge J e_1.

It is a relation between the two basis components of the one doublet, not an occupied two-electron state. In the 28 exterior coordinate slots of the eight-component carrier,

    ||w||²=det(J†J)=1,
    exterior_square(N)=w w†.

The latter projector has rank one and trace one. It has 24 nonzero components in the chosen exterior chart, so the unit relation is coherent rather than a literal singleton coefficient entry.

The exterior lifts of all three stages fix w. Every actual retained rotation lift also fixes w; its logical determinant is one. This gives a source-traced persistent relation with unit weight across the entire construction.

For any unit seed z, the orthogonal companion Cz produces the same encoded exterior relation:

    Jz wedge J(Cz)=w.

No new reference spin orientation is needed. Global phase cancels in B(z,Cz). Amplitude is not hidden: doubling z gives scalar 4 rather than 1.

## What the 144 coefficients measure

| Stage | Nonzero transfers | Sum of squared coefficient magnitudes |
|---|---:|---:|
| L | 16 | 4 |
| G | 64 | 2 |
| N | 64 | 2 |

These are actual exact weighted sums in the inherited Euclidean metric, not unit weights assigned to the arrows. They are Hilbert–Schmidt operator norms, not momentum norms.

The decomposition 144=4²+8²+8² is a decomposition of support counts. It does not recover a physical seed (4,8,8). The norm-12 suggestion in the conversation was therefore not a reconstruction of the stored seed.

## Status within the working conjecture

The proposed separation now has a concrete object on the electron side:

- **complex transfer sector:** the retained 144 coefficients;
- **persistent scalar reference:** the unique bilinear relation, with value 1 for a unit seed.

This advances the search for the unit electron arrow without inventing an offset or another seed. It does not yet identify 144 with |p|². The remaining structural task is to apply one common valuation of persistent relationships to the electron, proton and neutron, rather than switch from a unit scalar on one carrier to support-entry counting on another without a connecting construction.

## Fresh verification

```sh
python research/strominger/checkers/check_electron_seed_unit_relation.py
```

Twelve checks passed using exact arithmetic. The native producer was freshly rerun in a temporary output directory: all 16 of its checks passed and the complete retained store was reproduced exactly. The existing upstream frontier receipt was reused, not regenerated.

The historical producer receipt pins a different source revision. The new audit records that mismatch and resolves the local coefficient-reproduction question through the fresh isolated replay; it does not pretend that the old hash matches. All shared source and store files remained unchanged.

Receipt: `research/strominger/results/electron-seed-unit-relation.json`, including the exact transported unit relation and its rank-one projector.
