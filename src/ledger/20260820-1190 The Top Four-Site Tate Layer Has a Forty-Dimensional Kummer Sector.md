---
title: "The Top Four-Site Tate Layer Has a Forty-Dimensional Kummer Sector"
date: 2026-08-20
entry: 1190
status: superseded-by-higher-concurrence-complex
sector: cosmology
---

# 1190 — The Top Four-Site Tate Layer Has a Forty-Dimensional Kummer Sector

Sequence claim: `seqclaim-304f18a26d053d87bf97b2cb`.

> **Supersession notice.** The forty-dimensional anti-invariant cokernel is
> an intermediate pair-to-triple quotient, not full Čech cohomology. Entry
> 1192 includes the fourfold-concurrence boundary and reduces this sector.

## Deck decomposition

Entry 1189's component-resolved differential commutes with the double-cover
deck involution. It therefore splits into two exact matrices.

The invariant matrix is the ordinary signed incidence map from all pair
curves to all triple points.

The anti-invariant matrix has:

- one column for every split rational pair;
- one row for every off-branch triple;
- no row at a ramification-node triple.

The exact cokernels are

\[
\boxed{
\begin{array}{c|c|c|c}
\text{geometric marks}&W_{6,+}&W_{6,-}&\text{term count}\\
\hline
5&4&0&8\\
6&10&2&20.
\end{array}
}
\]

Thus the Kummer character occurs only in the six-mark source profile.

## Cyclic assembly

Entry 1159's 28 terms form seven free \(C_4\)-orbits. The eight five-mark
terms form two orbits; the twenty six-mark terms form five. Therefore every
representative eigencokernel assembles as a regular occurrence module:

\[
\mathbf Q[C_4]\otimes W_{6,\pm}^{\rm rep}.
\]

Summing all terms gives

\[
\boxed{
W_6^{\rm all\ terms}
=
\mathbf Q_+^{232}
\oplus
\mathbf Q_-^{40}.
}
\]

The corresponding \(C_4\) characters are

\[
\chi_+=(232,0,0,0),
\qquad
\chi_-=(40,0,0,0).
\]

The vanishing nonidentity traces are a consequence of free labelled
occurrence transport, not an unlabelled symmetry quotient.

## Architectural meaning

The top source coefficient layer is now completely typed at generic
kinematics:

\[
\boxed{
\text{Tate invariant incidence cokernel}
+
\text{rank-40 quadratic Kummer packet}.
}
\]

This is coefficient data over the existing marked/deck carrier. It is not a
new carrier incidence and does not enlarge the list of H2 coefficient
types.

## Next falsifier

Test Gauss--Manin extension between the surviving elliptic \(W_5\) systems
and \(W_6\). Since the Kummer sector exists only in six-mark terms, first
compute whether its two local generators per term are horizontal quotients
or receive a nonzero connecting morphism from the five elliptic pair
systems. A nontrivial map is allowed as sector-specific extension data; a
new singular divisor is not.

## Evidence

- `research/benincasa/checkers/four_site_qg_w6_deck_cyclic.py`
- `research/benincasa/results/four-site-qg-w6-deck-cyclic.json`
- Entries 1159 and 1188--1189.
