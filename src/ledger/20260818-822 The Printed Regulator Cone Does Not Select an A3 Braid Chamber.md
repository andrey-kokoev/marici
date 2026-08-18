---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 822 — The Printed Regulator Cone Does Not Select an A3 Braid Chamber

## Frozen representative

Take the labelled double-coordinate corner

\[
P_3=0,\qquad E=P_1,\qquad P_1^2\ne P_2^2.
\]

Write

\[
\delta=E^2-P_1^2,\qquad q=P_3^2,\qquad d=P_1^2-P_2^2.
\]

After the source-labelled Morse splitting in the \(b\)-direction, the
quartic \(a\)-family has miniversal coefficients, up to fixed units,

\[
\boxed{
\begin{aligned}
t_2&=-d\delta-2P_1^2q-\delta q,\\
t_1&=0,\\
t_0&=q(\delta^2+d\delta+\delta q+P_1^2q).
\end{aligned}
}
\]

The vanishing of \(t_1\) is forced by the even Cayley--Menger dependence on
\(a\); it is not a regulator choice.

## Source regulator map

The printed Bunch--Davies prescription permits independent positive energy
regulators. Substitute

\[
E\mapsto P_1-i\epsilon_E,\qquad
P_1\mapsto P_1-i\epsilon_{P_1},\qquad
P_3\mapsto-i\epsilon_{P_3},
\]

with all three \(\epsilon\)'s positive. This gives the exact energy-level map

\[
J:(\epsilon_E,\epsilon_{P_1},\epsilon_{P_3})
\longmapsto(t_0,0,t_2)
\]

through the displayed formulas, where

\[
\delta=(P_1-i\epsilon_E)^2-(P_1-i\epsilon_{P_1})^2,
\qquad
q=(-i\epsilon_{P_3})^2.
\]

No equal-regulator or hierarchy assumption has been made.

## Discriminant pullback

On the even slice, the \(A_3\) discriminant is

\[
\Delta_{A_3}
\sim
t_0\bigl(t_2^2-4P_1^2t_0\bigr)^2.
\]

At first regulator order,

\[
\operatorname{Im}t_2
=2dP_1(\epsilon_E-\epsilon_{P_1})+O(\epsilon^2).
\]

Positivity does not determine this sign. At \(P_1=3,P_2=2\), the two
positive assignments

\[
(0.02,0.01,0.005)
\quad\text{and}\quad
(0.01,0.02,0.005)
\]

both avoid \(J^{-1}(\Delta_{A_3})\), but have opposite signs of
\(\operatorname{Im}t_2\). They therefore enter distinct labelled braid
chambers.

Hence

\[
\boxed{\text{the printed positive energy-regulator cone does not select one chamber}.}
\]

The equal-regulator wall is tangent at first order and would require a
higher jet; selecting it would be an unauthorized hierarchy.

## Consequence for the coherence cell

Because at least two admissible chambers occur, the source does not select a
unique labelled thimble system. The mixed soft--signed coherence differential
and the test

\[
\partial H=\alpha_1+\alpha_2
\]

are therefore not source-canonical at the printed energy-regulator level.
Their status is undefined, not zero.

There remains one upstream possibility: the full graph-level map from
positive contour regulators to energy regulators could have a smaller image.
As already recorded in Entry 231, that map is not printed in the frozen
source. Without it, restricting the cone would be fitted.

## Result

The existing carrier and de Rham associated-grade symbols remain sufficient.
The frozen physical source does not presently define the required Betti
coefficient complex:

\[
\boxed{
\text{algebraic excess: generated;}
\qquad
\text{physical Betti realization: unselected.}
}
\]

No new carrier stratum is indicated.

## Verification

- checker:
  research/benincasa/marici-gm/src/bin/a3_source_regulator_chambers.rs;
- packet:
  research/benincasa/a3-source-regulator-chambers.json;
- allocator claim seqclaim-565ff84229bee1038892dc23.
