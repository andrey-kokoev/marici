---
id: 508
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Principal Cell Strictifies the Even Cartier Action

Entry 505 gives the exact commutator

\[
d(a^2f)-a^2d(f)=h(f)K,
\qquad
h(f)=2afL_1^{e_a}L_2^{e_b}.
\]

Entry 506 lifts its principal coefficient through the three-gradient Euler
bridge.  To obtain a strict chain operation, retain the principal cell
separated from the gradient complex in Entry 492.

Write the enlarged source differential as

\[
D(f,p)=d(f)+Kp.
\]

Define

\[
\boxed{
M_{a^2}(f,p)=
\left(a^2f,;a^2p-h(f)\right).
}
\]

Then

\[
\begin{aligned}
DM_{a^2}(f,p)
&=d(a^2f)+K(a^2p-h(f))\\
&=a^2d(f)+h(f)K+a^2Kp-h(f)K\\
&=a^2D(f,p).
\end{aligned}
\]

Thus multiplication by (a^2) becomes a strict chain map on the
principal-cell enlargement.  Under the principal-to-gradient comparison,
the correction (h(f)) maps through the Euler vector to

\[
\left(\frac{a^2m}{2},0,uam\right),
\]

exactly the lift of Entry 506.

## Consequence

The rank-one commutator of Entry 504 is not an obstruction to a derived
Cartier action.  It is the visible boundary of the already required
principal conormal cell.  Removing that cell before acting produces the
failure of descent.

This is coefficient-complex strictification, not a new carrier generator:
the principal cell is source-derived from (K=0) and was independently
required by Entry 492.

## Remaining gate

Apply this strict action to the finite orbit-completed principal/gradient
mapping cone and compute its map on stable plus (u)-homology.  The
incidence hypothesis predicts

\[
M_{a^2}:H_+(C_D,u)\longrightarrow H_+(C_{D+2},u)
=0.
\]

The calculation must retain the (-h(f)) principal component.  Omitting it
reproduces the ill-typed naive action of Entry 504.

## Evidence

- `research/benincasa/marici-gm/src/bin/soft_axis_a2_principal_strictification.rs`;
- Entries 492, 504, 505, and 506.
