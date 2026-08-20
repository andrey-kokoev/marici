---
title: "Boundary-Sum Pair Curves Split and Remove Most Elliptic Blocks"
date: 2026-08-20
entry: 1188
status: active-correction
sector: cosmology
---

# 1188 — Boundary-Sum Pair Curves Split and Remove Most Elliptic Blocks

Sequence claim: `seqclaim-89523649b1452fd8f7032763`.

## Hostile pair audit

Entries 1186--1187 used the branch-avoiding benchmark in which every pair of
distinct marked hyperplanes cuts the quartic branch in four simple points,
giving an elliptic double cover of the pair line.

That assumption fails for pairs of source boundary-sum marks.

Each boundary-sum mark contains four sign nodes. The exact termwise census
shows that any two distinct boundary-sum marks occurring together share
exactly two sign nodes. Their pair line therefore meets the branch quartic
in two double roots. A degree-four polynomial on the line with those roots
has the form

\[
\text{unit}\cdot(\ell_1\ell_2)^2.
\]

Consequently its double cover is

\[
w^2=\text{unit}\cdot(\ell_1\ell_2)^2,
\]

which splits over the existing quadratic Kummer field into two rational
components.

Thus

\[
\boxed{
\text{boundary-sum pair}
=
\text{Kummer-twisted rational deck pair},
\qquad H^1=0.
}
\]

Only a pair containing the unique zero-node single-edge mark remains
elliptic.

## Exact source census

\[
\boxed{
\begin{array}{c|c|c|c}
\text{geometric marks}&\text{elliptic pairs}&\text{split rational pairs}&\text{terms}\\
\hline
5&0&10&4\\
5&4&6&4\\
6&5&10&20.
\end{array}
}
\]

Therefore the actual elliptic \(W_5\) ranks are

\[
\boxed{0,\ 8,\ 10,}
\]

not the branch-avoiding values \(20,20,30\) printed in Entry 1186.

## Corrections to prior entries

Entry 1186 remains valid for:

- geometric mark counts;
- smooth versus four-node surface counts;
- \(W_3\) and \(W_4\) ranks.

Its \(W_5,W_6\) columns are now only a branch-avoiding benchmark.

Entry 1187's signed diagonal map remains valid for connected smooth pair
curves, but not as the complete source differential. Split rational pairs
have rank-two \(H^0\), so the source deck-point matrix must be rebuilt.

## Architectural consequence

The hostile source specialization reduces rather than enlarges coefficient
complexity:

\[
\boxed{
\text{most apparent elliptic pair systems degenerate to Tate/Kummer data}.
}
\]

No new carrier support is needed; the degeneration occurs at the already
identified shared node strata.

## Next falsifier

Rebuild the pair-to-triple differential with one \(H^0\) generator for an
elliptic pair and two deck-labelled \(H^0\) generators for a split rational
pair. Derive the maps at triple intersections from component incidence,
then recompute the true source \(W_6\) cokernel.

## Evidence

- `research/benincasa/checkers/four_site_qg_pair_curve_types.py`
- `research/benincasa/results/four-site-qg-pair-curve-types.json`
- Entries 1178 and 1183.
