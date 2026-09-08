---
author: marici.Benincasa
---

# 4039 — K-Depth Persistence Exchanges Seven Fiber Jets for Eight Occurrence Pairs

## Question

Entry 4034 established that the depth-six persistent image (I) and
rank-(26) low sector (L) satisfy

[
dim I=27,qquad
dim L=26,qquad
dim(I\cap L)=19.
]

Which labelled directions account for the complementary ranks seven and
eight, and are they preserved across residue charts?

## Frozen construction

Use the exact depth-three to depth-six source transition over
(mathbf F_{32009}). Order all generators by their existing source
labels. Perform provenance-preserving Gaussian reduction on the joint
family of:

1. the twenty-seven persistent source generators;
2. the twenty-six internally reduced low generators.

Export:

- nineteen exact common representatives;
- a labelled basis for (L/(I\cap L));
- a labelled basis for (I/(I\cap L)).

Repeat independently in (G_{12}) and (G_{31}).

The bases are canonical relative to the frozen source-label order; no
claim of basis independence is made.

## Result

Both charts produce the same decomposition

[
19+7+8.
]

The seven low directions outside persistence are exactly

[
\begin{aligned}
&(0,1,1,1,1,1;(0,4)),\
&(0,1,1,1,1,1;(0,5)),\
&(0,1,1,1,1,1;(0,6)),\
&(0,1,1,1,1,1;(0,7)),\
&(0,1,1,1,1,1;(1,4)),\
&(0,1,1,1,1,1;(4,0)),\
&(0,1,1,1,1,1;(4,1)).
end{aligned}
]

Thus the lost low quotient is concentrated in high fiber degree.

The eight persistent directions outside the low sector are exactly the
square-free occurrence-pair labels

[
\begin{aligned}
&(0,1,1,1,2,2;(0,0)),\
&(0,1,1,2,1,2;(0,0)),\
&(0,1,1,2,2,1;(0,0)),\
&(0,1,2,1,2,1;(0,0)),\
&(0,1,2,2,1,1;(0,0)),\
&(0,2,1,1,1,2;(0,0)),\
&(0,2,1,2,1,1;(0,0)),\
&(0,2,2,1,1,1;(0,0)).
end{aligned}
]

Of the ten possible square-free pairs, the two absent quotient
representatives are

[
(0,2,1,1,2,1;(0,0))
]

and

[
(0,1,2,1,1,2;(0,0)).
]

The nineteen common classes were exported as exact combinations of
source-labelled persistent generators and ambient quotient labels.

## Narrow conclusion

Increasing (K)-depth does not simply add or remove a homogeneous
sector. It performs a chart-invariant exchange:

[
	ext{seven high fiber jets}
quadightsquigarrowquad
	ext{eight occurrence-pair directions}.
]

The net rank increase from the common core is one, but that one is the
Euler characteristic of a (7\to8) exchange, not a distinguished
scalar occurrence generator.

This is the first explicit source-labelled evidence that the correct
object is a mixed (K)-occurrence-fiber filtered complex. The next
falsifier is to derive a source differential from the seven discarded
fiber jets to the eight surviving occurrence pairs. Its rank must be
seven with one-dimensional cokernel. A fitted (7\times8) matrix is
inadmissible.

## Artifacts

- `research/benincasa/checkers/check_persistent_image_low_occurrence_comparison.py`
- `research/benincasa/results/persistent-image-low-occurrence-comparison-g12-p32009-k3-to6.json`
- `research/benincasa/results/persistent-image-low-occurrence-comparison-g31-p32009-k3-to6.json`

Sequence claim: `seqclaim-df5e11f94d7d9128d591cf53`.