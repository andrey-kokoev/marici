# Photon alternating ordinary/complex halves: first source test

## Question and operator conjecture

The operator proposed: a photon is half in the complex plane and half in the ordinary plane; the halves exchange roles each cycle, perhaps as one filled triangle and one unfilled triangle, or one triangle plus one complex arrow. This is a search conjecture, not an established identification of a complex coefficient with an unfilled face.

Test the existing six-occurrence candidate and its actual endpoint continuation before introducing any exchange operator. Rivals: an order-three phase rotation with both triangles present; ordinary/complex encoding as two representations of the same data rather than two alternating sectors; a genuinely different source operation supporting a swap.

## Source and exact calculation

Primitive order is `(AB, BC, CA, BA, AD, DB)`, imported from `check_natural_tower_return`. The continuation is `K[b,a]=1` exactly when the target of occurrence a equals the source of b. The existing photon checker validates the candidate

    g = (1, -1, -omega^2, -1, 1, omega^2),
    K g = omega g.

Write g=u+i sqrt(3)w and U=(u,w). The exact induced real-plane operation satisfies K U=U T, with

    T = ((-1/2, 1/2), (-3/2, -1/2)).

Fresh rational checks prove T^3=I, T^2!=I and rank(T^2-I)=2. A complete three-step return is identity, not an exchange.

A genuine binary role that flips at every K-step also conflicts with the odd return: three flips would reverse the role while returning to the same state. In the linear formulation, solving JT=-TJ on this plane gives only J=0 (constraint rank four). There is no nontrivial fixed ordinary/complex grading exchanged by this operation. Adding an independent role bit or a new step operator would change the source.

## The triangles do not alternate under this step

Their coefficient triples are exact negatives:

    (g_BA, g_AD, g_DB) = -(g_AB, g_BC, g_CA).

This relation holds throughout the entire invariant plane. Neither triple can vanish unless the plane state vanishes: each three-row restriction of U has rank two. For the complex eigenmode with any nonzero common complex amplitude, neither whole triangle can be purely real or purely imaginary; both associated real constraint matrices have rank two.

These are coefficient statements. A face filler is a typed witness, not the real part of a coefficient. The inspected source has no operation that deletes/creates face fillers when the phase changes. The common centroid-mode wrapper likewise encodes and decodes retained facet data; it does not alternate which face is filled.

## What survives of “one triangle plus one complex arrow”

On the declared **real** candidate plane, one complex coordinate z=x+i sqrt(3)y can retain both real parameters, provided the decoder U and occurrence labels are kept. The triangle triple is

    (x, -x, (x+y)/2),

with exact inverse x=AB and y=2 CA-AB. Thus either triangle already recovers the entire real candidate-plane state; the other is its negative, not an independently alternating half.

This provides a lossless coordinate representation, not a derived geometric arrow. If both conjugate modes instead have independent complex amplitudes, their complexified span has complex dimension two; one complex-linear scalar cannot faithfully encode it. The explicit AB readout loses the nonzero vector g-conjugate(g).

## Falsification and boundary

A hand-added swap S=((0,1),(1,0)) passes S^2=I but differs from T. This positive control distinguishes a manufactured alternating model from the existing source operation.

**Disposition:** the simple two-sector swap is refuted for the existing order-three candidate continuation. The one-complex-coordinate representation survives with its decoder and real-plane restriction. No photon/proton selector, emission mechanism, physical oscillation, or face-filling exchange follows from this test.

This is not a refutation of every possible meaning of “cycle.” A different source-derived operation, such as a separately defined cross-grade transition, would be a new test. Merely renaming spectral encode/decode as alternating physical sectors does not supply that operation.

## Verification

```sh
python research/strominger/checkers/check_photon_alternating_halves.py
```

All 12 checks passed. Receipt: `research/strominger/results/photon_alternating_halves.json`, including four exact plane-action states and source hashes. The checker imports the existing packet registry and photon validation functions rather than invoking the source checkers' main routines. Transitive imports also execute existing labelled-path assertions and print their results.
