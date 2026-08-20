---
title: "Five-Site Occurrence Differences Begin in the First Rees Grade"
date: 2026-08-20
entry: 1204
status: active-filtered-occurrence-result
sector: cosmology
---

# 1204 — Five-Site Occurrence Differences Begin in the First Rees Grade

Sequence claim: `seqclaim-6cff4e0c6f28b61ec746cdab`.

## Radial strict transforms

Entry 1203's kernel generators pair complementary connected-subgraph labels
(g_A,g_{A^c}) that define the same infinity hyperplane. Introduce the
radial coordinate (ho) and write their strict transforms as

\[
\widehat q_A=L+\rho X_A,
\qquad
\widehat q_{A^c}=L+\rho X_{A^c}.
\]

At total energy zero,

\[
X_A+X_{A^c}=0.
\]

Therefore

\[
\boxed{
\widehat q_A-\widehat q_{A^c}
=2\rho X_A.}
\]

The occurrence difference vanishes at grade zero but is generically nonzero
in the first radial/Rees grade.

## Complete source census

All 240 generators of (K_{\rm occ}) are complementary partitions. They
split into

\[
\boxed{
\begin{array}{c|c|c}
\text{partition type}&\text{generators}&C_5\text{ orbits}\\
\hline
1|4&200&40\\
2|3&40&8.
\end{array}}
\]

Their first symbols are respectively

\[
2X_i
\]

and

\[
2(X_i+X_j)
\]

with the source occurrence labels retained.

## Coefficient action

At (ho=0), complementary labels define the same geometric hyperplane and
the same restriction of the Cayley--Menger branch. Hence (K_{\rm occ})
acts trivially on the leading infinity coefficient object.

At first Rees order, the source energies separate the two occurrences. Thus

\[
\boxed{
\text{occurrence data}
=
\text{filtered normal information, not extra grade-zero geometry}.}
\]

This is the five-site version of the recurring Marici distinction between a
coarse geometric divisor and its labelled resolved normal directions.

## Next falsifier

Construct the first-Rees extension of Entry 1202's seven OS carrier types by
the 48 regular occurrence modules. Test whether multiplication by the
symbols (2X_A) gives an exact Koszul attachment away from their soft
support. A surviving generic class would be new coefficient complexity; a
new carrier claim would require an independently missing incidence stratum.

## Artifacts

- `research/benincasa/checkers/five_site_qg_occurrence_rees_separation.py`
- `research/benincasa/results/five-site-qg-occurrence-rees-separation.json`
