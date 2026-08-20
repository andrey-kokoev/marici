---
title: "The Four-Site Total-Energy Boundary Is a Quartic Double Solid"
date: 2026-08-20
entry: 1167
status: active-correction
sector: cosmology
---

# 1167 — The Four-Site Total-Energy Boundary Is a Quartic Double Solid

Sequence claim: `seqclaim-d4536574c6b2e22e7b9e6cce`.

## Typing correction

Entries 1154--1155 correctly classify an **edge-dependent marked residue**.
Its nonzero edge normal eliminates one of four edge variables; projective
infinity is then \(\mathbf P^2\), and the quartic double cover is a
degree-two del Pezzo surface with Tate--\(E_7\) cohomology.

The physical total-energy residue is different:

\[
q_G=\sum_{i=1}^4x_i.
\]

It contains no edge variable. Therefore taking \(q_G=0\) eliminates no
\(y_i\), and all four edge variables remain at infinity:

\[
[y_1:y_2:y_3:y_4]\in\mathbf P^3.
\]

The quartic infinity branch consequently defines

\[
\boxed{
X_G\longrightarrow\mathbf P^3
\quad\text{as a double cover branched over a quartic surface}.}
\]

This is a quartic double solid, not a del Pezzo surface.

## Canonical class and smooth benchmark

For a double cover of \(\mathbf P^3\) branched over a quartic,

\[
K_{X_G}
=\pi^*(K_{\mathbf P^3}+2H)
=-2\pi^*H.
\]

Thus the smooth model is a Fano threefold of index two and degree two. Its
branch is a quartic K3 surface. Using

\[
\chi(X_G)=2\chi(\mathbf P^3)-\chi(K3)=8-24=-16
\]

and the generic Picard-rank-one Betti numbers gives

\[
b_3=20,
\qquad
h^{2,1}=10.
\]

These numbers are a smooth benchmark, not yet the cohomology of the actual
singular source fiber.

## Actual physical infinity point

The source leading branch is

\[
4B_4=-\Delta^T\operatorname{adj}(G)\Delta,
\qquad
\Delta=(z_2-z_1,z_3-z_2,z_4-z_3).
\]

Entry 1166 shows that the literal physical chain reaches

\[
[y_1:y_2:y_3:y_4]=[1:1:1:1].
\]

At this point \(\Delta=0\), so both \(B_4\) and its first derivatives
vanish. The physical total-energy boundary therefore meets a singular point
of the actual quartic double solid. Its resolution and vanishing-cycle
object, rather than the smooth benchmark alone, are the next coefficient
problem.

## Narrow correction

\[
\boxed{
\begin{aligned}
\text{edge-dependent residue}&:\ \text{degree-two del Pezzo surface},\\
q_G\text{ residue}&:\ \text{singular quartic double solid}.
\end{aligned}}
\]

Accordingly, Entries 1154--1155 are narrowed, not discarded. Their result
does not classify the physically distinguished \(q_G\) sector.

This materially raises the prior for non-Tate four-site coefficient data,
but it still introduces no new carrier: the geometry comes from the same
Cayley--Menger infinity divisor and total-energy support.

## Next falsifier

Compute the completed local normal form at the physical diagonal point,
its Milnor/nearby-cycle rank and inertia, and the specialization of the
source radial chain. Then determine which part survives in the global
singular quartic-double-solid coefficient object.

## Evidence

- `research/benincasa/checkers/four_site_qg_infinity_dimension.py`
- `research/benincasa/results/four-site-qg-infinity-dimension.json`
- Entries 1154--1155 and 1166.
