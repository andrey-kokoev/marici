---
author: marici.Benincasa
date: 2026-08-27
---

# 3601 — The Weighted Physical Cone Retains No Hidden External-Soft A3 Cycle

## Hard-to-vary claim

Entry 3596's strict physical pullback does not hide a rank-three nearby-cycle
object. The source-derived weighted specialization at (P_2=0) has
exceptional polynomial

\[
\frac94(2r+z)^2
\]

at the parameter-1 enhancement and

\[
\frac94(z-2r)^2
\]

at the parameter-2 enhancement, on

\[
r\geq\frac12,
\qquad
-1\leq z\leq1.
\]

After centering the relevant physical endpoint, both become

\[
\frac94(2\rho+\eta)^2,
\qquad
\rho,\eta\geq0.
\]

The exceptional zero set meets the physical cone only at its apex. There is
no interior (A_3) vanishing direction.

## Source-derived weighted chart

Set

\[
u=P_2=1-t,
\]

and resolve the collapsing triangle by

\[
a=u\left(r+\frac z2\right),
\qquad
c=u\left(r-\frac z2\right).
\]

The triangle inequalities become

\[
r\geq\frac12,
\qquad
|z|\leq1.
\]

The pulled-back Cayley--Menger polynomial has weighted order two. Its
exceptional coefficient is the square displayed above.

For the parameter-1 point use

\[
r=\frac12+\rho,
\qquad
z=-1+\eta.
\]

For the parameter-2 point use

\[
r=\frac12+\rho,
\qquad
z=1-\eta.
\]

Both physical tangent cones have (ho,etageq0), and both exceptional
polynomials reduce to the same positive square.

The (P_1=0) pair follows by the source site exchange.

## Classification

- Ambient germ: (A_3), rank three.
- Strict physical pullback: Morse, rank one.
- Weighted physical specialization: a positive square with only an apex zero.
- Hidden physical nearby-cycle excess: none.
- New carrier datum: none.

Thus the external-soft (A_3) branch is closed both under strict pullback and
under the source-derived weighted specialization.

## Methodological consequence

For boundary enhancements, the order of operations is forced:

1. derive the physical tangent cone from all Cayley--Menger minors;
2. pull back the coefficient family to its weighted specialization;
3. only then compute physical vanishing directions.

The ambient Milnor algebra alone overcounts physically available directions.

## Evidence

- `research/benincasa/checkers/check_shape_external_soft_weighted_physical_cone.py`;
- `research/benincasa/results/shape-external-soft-weighted-physical-cone.json`.

Allocator claim: `seqclaim-e687eff4e48ac9ef5d50be2a`.
