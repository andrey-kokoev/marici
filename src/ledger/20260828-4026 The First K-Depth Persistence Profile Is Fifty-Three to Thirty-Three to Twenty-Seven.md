# 4026 — The First K-Depth Persistence Profile Is Fifty-Three to Thirty-Three to Twenty-Seven

## Status

Established at prime (32009) in residue charts (G_{12}) and (G_{31}).

## Consecutive continuation

Entry 4020 constructed the canonical quotient map

[
Q_{le3}^{m reach}longrightarrow Q_{le4}^{m reach}
]

and found

[
53longrightarrow33
]

with kernel rank (20).

The next source-derived map

[
Q_{le4}^{m reach}longrightarrow Q_{le5}^{m reach}
]

also passes kernel-pair descent. It has

[
1386longrightarrow1366
]

with kernel rank (20).

Thus a rank-20 boundary-loss mechanism recurs at two consecutive extensions.

## Two-step persistence

The composite source map

[
Q_{le3}^{m reach}longrightarrow Q_{le5}^{m reach}
]

passes exact-relation descent and has image rank

[
27.
]

Equivalently,

[
53=26+27,
]

where (26) depth-three classes vanish after two legal extensions.

Since the one-step image has rank (33), exactly six of those 33 classes die at the second extension:

[
33=6+27.
]

The complete persistence profile presently known is therefore

[
53supset33supset27.
]

Both charts give the same ranks.

## Narrow conclusion

The recurring rank-20 kernel of consecutive maps does not imply that each finite source stage loses an independent rank-20 block from every earlier stage. Persistence must be computed by composites.

The rank-27 two-step image is the first candidate for stable finite coefficient content, but it is not yet an eventual-image theorem.

No new carrier divisor appears. The phenomenon belongs to continuation and exact-relation transport.

## Next falsifier

Compute one of the following equivalent finite gates:

1. the image of (Q_{le3}^{m reach}) in (Q_{le6}^{m reach});
2. the image of the known rank-27 subspace under (Q_{le5}	o Q_{le6}).

The second is preferable if a basis for the rank-27 image can be exported, because it avoids reducing all 4800 depth-three generators again.

Possible outcomes:

- rank (27): first evidence of stabilization;
- smaller positive rank: persistence filtration continues;
- rank (0): all finite-depth classes are boundary artifacts.

Do not identify rank (27) with a physical coefficient system before this gate.

## Artifacts

- `research/benincasa/checkers/check_consecutive_kdepth_source_quotient_transition.py`
- `research/benincasa/results/kdepth4-to5-source-quotient-transition-g12-p32009.json`
- `research/benincasa/results/kdepth3-to5-source-quotient-transition-g12-p32009.json`
- `research/benincasa/results/kdepth3-to5-source-quotient-transition-g31-p32009.json`

Sequence claim: `seqclaim-1f42fd415e1bc3e8d95803cc`.
