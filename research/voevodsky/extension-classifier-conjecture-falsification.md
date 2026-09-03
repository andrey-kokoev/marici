# Falsification of the single extension-classifier conjecture

## Question

Can every Marici attachment be represented contravariantly by a source-authorized extension class in \(\operatorname{Map}(X,K[1])\)?

## Claim boundary

This packet tests the conjecture against the bounded flag/log cone cell. It does not exclude contravariant extension classifiers for Green extensions or other genuinely over-category attachments.

## Bold conjecture under test

For a fixed classifying object \(K\), attachments over \(X\) form

\[
\operatorname{Att}_K(X)=\operatorname{Map}(X,K[1]),
\]

with contravariant reindexing by precomposition.

## Named rival

Marici contains at least two attachment variances:

1. extensions over a base, classified by maps out of the base and pulled back contravariantly;
2. cell attachments under a base, classified by attaching maps into the base and transported covariantly by pushout.

A single functor on \(\widehat{\mathcal C}^{op}\) cannot represent both without changing the base category to spans, correspondences, or a bifibration.

## Strongest falsification attempt

In the minimal flag/log bridge, \(X=\mathbb Z[-2]\) with nonzero generator \(\xi\). The formal cone cell adjoins \(h\) in degree one with

\[
dh=\xi.
\]

This is the cofiber or cell attachment determined by the map from the degree-two sphere into \(X\). Under a chain map \(f:X\to Y\), the attaching map is sent forward to \(f(\xi)\), and the cell attachment is transported by pushout. Its variance is covariant.

By contrast, an extension

\[
K\longrightarrow E\longrightarrow X
\]

is pulled back along \(f:X'\to X\) and is contravariant in \(X\). These are different universal properties.

For the specific minimal complex over \(\mathbb Z\), the proposed fixed-coefficient extension classifier also misses the cone cell. The object \(\mathbb Z[-2]\) is projective in the derived category, so the ordinary degree-one extension group by \(\mathbb Z[-2]\) vanishes. Yet the universal cell attachment killing \(\xi\) exists after adjoining \(h\). Therefore existence of the cell does not imply a nonzero class in the proposed extension space.

## Exact residual

The conjecture fails for the formal cone cell because it assigns the wrong universal property and variance. The cell is an under-category construction; the proposed classifier describes over-category extensions.

This does not falsify the narrower claim that genuinely source-derived extensions are classified by a contravariant mapping-space family.

## Revised conjecture

The attachment architecture is a typed coproduct or bifibration with at least two sectors:

\[
\operatorname{Att}^{\rm over}_K(X)=\operatorname{Map}(X,K[1])
\]

for extensions pulled back contravariantly, and

\[
\operatorname{Att}^{\rm under}_L(X)=\operatorname{Map}(L,X)
\]

for cells transported covariantly by pushout. A unified Grothendieck construction requires a variance tag and Beck–Chevalley coherence for any interaction between the sectors.

## Disposition

The single extension-classifier conjecture is rejected. Retain it only for the over-extension sector. The first next test is to classify one actual Marici Green extension as an object of \(\operatorname{Att}^{\rm over}\), while keeping the formal cone cell in \(\operatorname{Att}^{\rm under}\).

## Verification

- `research/voevodsky/checkers/check_extension_classifier_conjecture.py`
- `research/voevodsky/results/extension_classifier_conjecture.json`
- `research/voevodsky/displayed-attachment-flag-log-bridge-audit.md`
