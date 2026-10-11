# Reversed coefficient attachment: an exact frame mismatch

## Input and question

Test reversal on the complete retained proton coefficient protocol, not on the previous host-depth or belt construction. The source is `results/proton_merkle_store.json`, root `f7bd09c2a515ac4ac9f2bcb33105767c6ed8a4fcf93bdc1c22719228585c7e02`. Its 1836 arrows and 108 typed ports are freshly verified before calculation.

The protocol is

```text
raw --L--> local --G--> aligned --N--> raw.
```

Each stage has 36 coordinates over K = Q(sqrt(-3)). Exact source identities give GL=N, N*=N, and N²=N. Thus the complete return NGL is N. The ranks are L:12, G:3, N:1.

The geometric flag reversal does not uniquely specify what happens to complex coefficients. Test two explicit candidates:

1. Reverse arrow endpoints and keep weights: linear dualization, giving return E=L^T G^T N^T=N^T on dual coordinate spaces.
2. Reverse endpoints and conjugate weights: Hermitian adjoint reversal, giving return E=L* G* N*=N under the standard Hermitian coordinate identification.

Neither candidate is an inverse. The coordinate identifications are specified choices, not implicit identifications of typed spaces.

## Result 1: adjoint reversal closes directly on the retained image

For the adjoint candidate, EN=N²=N. No inserted identity stage is needed. Inserting one and removing it leaves the return unchanged.

This only returns states already in im(N). It is not the identity on all 36 possible raw inputs.

## Result 2: unchanged-weight reversal has a fixed-frame mismatch

For the linear-dual candidate:

```text
E = N^T != N,
E N != N,
rank(E N) = 1,
trace(E N) = 16/25.
```

The last number is an exact matrix trace, not an assigned energy, mass, or probability.

All 24 rigid vertex permutations were tested. The action sends each triangle label AB to its permuted label and transforms its x/y/z coefficient coordinates by the induced orthogonal tetrahedral symmetry. None satisfies S N^T S^(-1)=N. Thus this mismatch is not removed by any of those rigid tetrahedron alignments.

## An explicit repair, and its removal test

Let w be the first column of N; every entry is nonzero. Define

```text
D_ii = w_i / conjugate(w_i).
```

Then exactly:

```text
D*D = I,
N D = D N^T,
D N^T D^(-1) = N.
```

The 36 diagonal entries take three values, each appearing twelve times:

```text
1,
-13/14 + (3/14)sqrt(-3),
-13/14 - (3/14)sqrt(-3).
```

D identifies the reversed frame with the proton frame without adding a new state space. Its inverse supplies the return identification. Under those identifications the coupled return is N.

Removing D while holding those frames fixed breaks matching. D also fails to commute with N, so it is not a symmetry of the fixed proton return. A changed diagonal entry fails the intertwining equation.

This is a concrete attachment requirement, stronger than the earlier removable identity stage. However, whether D belongs to the definition of the electron's frame or must be implemented by an additional retained complex remains a choice of attachment contract. The calculation has not constructed a neutron carrier or proved that any particular implementation of D is indispensable.

## A separate obstruction: restoring all raw information

The checker supplies a nonzero z with Nz=0. Consequently no map receiving only Nz can reconstruct every original z. An intermediate stage inserted after this loss cannot fix it.

Keeping (Nz,(I-N)z) is sufficient: addition reconstructs z. The complement has rank 35 over K. That is information retained before it is lost, not evidence of 35 new particles or a neutron assignment. It is also not the same contract as preserving the selected return N.

## What this resolves and what remains

There is now a specific distinction to investigate:

- adjoint reversal already matches the selected return;
- unchanged-weight reversal requires a nontrivial coefficient-frame identification that rigid tetrahedron alignment does not supply.

These are two alternative reversal rules, not established hydrogen and deuterium states of a single rule. To distinguish isotopes, keep the same electron reversal law in both cases and specify when an implementation of the required attachment data must itself remain as an observable complex. Merely naming D “neutron” would not supply that construction.

The next geometric obligation is to derive the coefficient rule and attachment identification from the outward flag construction, then test its retained implementation rather than only its composite return. The present calculation does not claim a full path-preserving pullback or minimal retained-history realization.

## Verification

```text
python research/voevodsky/checkers/check_reversed_coefficient_attachment.py
```

25 exact checks pass. Output: `results/reversed_coefficient_attachment.json`, including source and checker hashes, ranks, all 24 alignment results, the explicit diagonal map, and the nonzero lost-state witness. The source packet is unchanged.
