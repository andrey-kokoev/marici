---
authors:
  - marici.Nima
date: 2026-08-18
---
# 703 — The Five-Pole Euler Defect Splits Across Deletion and Restriction

## Hard-to-vary consequence

Entry 702 proves the generic and homogeneous Euler ranks

\[
(M_{\rm low}^{\rm gen},M_{4|G}^{\rm gen},M_5^{\rm gen})=(34,26,60)
\]

and

\[
(M_{\rm low}^{\rm hom},M_{4|G}^{\rm hom},M_5^{\rm hom})=(15,20,35).
\]

Therefore the total Euler-rank change has the canonical arithmetic split

\[
\boxed{
60-35=(34-15)+(26-20)=19+6.
}
\]

This is more informative than the undifferentiated number 25. Nineteen
units occur already in the lower deletion family; only six occur in the
restriction to \(q_{\mathcal G_{12}}=0\).

## Morphism-of-triangles formulation

Let the generic and homogeneous five-pole objects sit in their respective
deletion--restriction triangles. The desired base-change comparison must be
a morphism of these triangles:

\[
\begin{array}{ccc}
M_{\rm low}^{\rm gen}&\longrightarrow&M_5^{\rm gen}
  \longrightarrow M_{4|G}^{\rm gen}\xrightarrow{+1}\\
\downarrow\beta_{\rm low}&&\downarrow\beta_5
  \qquad\downarrow\beta_{4|G}\\
M_{\rm low}^{\rm hom}&\longrightarrow&M_5^{\rm hom}
  \longrightarrow M_{4|G}^{\rm hom}\xrightarrow{+1}.
\end{array}
\]

If this diagram is typed, the octahedral axiom supplies a triangle among
the three comparison cones. Consequently their Euler characteristics must
satisfy

\[
\boxed{
\chi\operatorname{Cone}(\beta_5)
=
\chi\operatorname{Cone}(\beta_{\rm low})
+
\chi\operatorname{Cone}(\beta_{4|G}),
}
\]

with numerical constraint \(25=19+6\), up to the single global sign fixed
by the convention for the cone.

## What this does not prove

The equality is a necessary Euler-characteristic constraint. It does not
construct any \(\beta\), determine degreewise cone dimensions, or show that
either summand is supported on \(\mathcal Q=0\). In particular, the
nineteen-dimensional lower change cannot be attributed to the fifth pole.

## Efficient construction order

The minimal typed calculation is now:

1. construct \(\beta_{\rm low}\) for the four-pole lower family;
2. construct \(\beta_{4|G}\) on the restricted surface;
3. verify compatibility with the deletion--restriction connecting maps;
4. obtain \(\beta_5\) as the middle map of the resulting morphism of
   triangles.

This is strictly smaller than constructing an unstructured rank-sixty
matrix. It also detects a faulty model immediately: failure to reproduce
the split \(19+6\) means that the comparison or its truncation has lost the
deletion--restriction typing.

## Consequence for \(\mathcal Q\)

The first admissible \(\mathcal Q\)-test should be performed separately on
the two cones. A factor supported throughout \(I=0\) belongs to the
universal homogeneous degeneration. Only residual support inside the
homogeneous locus can be compared with \(\mathcal Q=0\).

## Evidence

- Entries 596 and 700--702;
- `research/benincasa/check_generic_five_pole_base_change_rank.py`;
- `research/benincasa/check_deletion_restriction_base_change_split.py`;
- allocator claim `seqclaim-78cf7ca519dc5dd52095e7b4`.

## Next falsifier

Construct the smaller restricted comparison \(\beta_{4|G}\) first and
test whether its cone has Euler characteristic six. If not, the proposed
finite model is not compatible with the source-derived
deletion--restriction triangle. If it does, locate its support before any
comparison with \(\mathcal Q\).
