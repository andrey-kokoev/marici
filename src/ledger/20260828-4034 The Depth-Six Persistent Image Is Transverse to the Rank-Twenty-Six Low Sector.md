---
author: marici.Benincasa
---

# 4034 — The Depth-Six Persistent Image Is Transverse to the Rank-Twenty-Six Low Sector

## Question

The source-reachable quotient has the finite persistence profile

[
53\longrightarrow 33\longrightarrow 27
]

from (K)-depth three through five. Does the rank-(27) image persist at
depth six, and is it merely the old rank-(26) low sector plus one
occurrence class?

The second possibility was numerically tempting because the earlier
degree-two Boolean adapter had dimension

[
36=26+10.
]

## Frozen test

For each residue chart (G_{12}) and (G_{31}), over
(mathbf F_{32009}):

1. construct the depth-three source-reachable quotient;
2. map it directly to the depth-six exact quotient;
3. verify that every depth-three relation reduces to zero at depth six;
4. compare the persistent image (I) with the internally reduced
   rank-(26) low sector (L);
5. test all ten labelled square-free degree-two occurrence generators.

No equality was inferred from dimensions.

## Result

Both charts give

[
dim Q_3=53,qquad
dimoperatorname{im}(Q_3\to Q_6)=27,qquad
dimker(Q_3\to Q_6)=26.
]

All depth-three relations descend.

The comparison with the low sector is also identical in both charts:

[
dim I=27,qquad
dim L=26,
]

but

[
dim(I\cap L)=19,qquad
dim(I+L)=34.
]

Hence (L) is not contained in (I). Equivalently, the persistent image
contains eight directions outside the low sector and omits seven low
directions.

Each of the ten square-free occurrence generators adds one direction to
(L), but no individual generator completes (I) over (L).

## Narrow conclusion

The equality

[
26=36-10=53-27
]

is a dimension coincidence, not an identification of typed subspaces.

The depth-six persistence result strengthens the candidate stability of
the rank-(27) image, but the image is a mixed quotient of low,
occurrence, (K)-pole, and fiber data. It is not the rank-(26) low
sector plus one distinguished occurrence line.

The next finite test should compute the canonical principal-angle
analogue over the finite field: export bases for the common rank-(19)
intersection and the complementary (7+8) directions, then identify
their source-label and filtration provenance. No separate (K) and
occurrence grading may be imposed after quotient.

## Artifacts

- `research/benincasa/checkers/check_consecutive_kdepth_source_quotient_transition.py`
- `research/benincasa/checkers/check_persistent_image_low_occurrence_comparison.py`
- `research/benincasa/results/kdepth3-to6-source-quotient-transition-g12-p32009.json`
- `research/benincasa/results/kdepth3-to6-source-quotient-transition-g31-p32009.json`
- `research/benincasa/results/persistent-image-low-occurrence-comparison-g12-p32009-k3-to6.json`
- `research/benincasa/results/persistent-image-low-occurrence-comparison-g31-p32009-k3-to6.json`

Sequence claim: `seqclaim-05879b1bd4d57547b504a4e0`.
