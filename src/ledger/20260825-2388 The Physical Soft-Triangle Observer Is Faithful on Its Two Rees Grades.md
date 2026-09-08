---
author: marici.Benincasa
date: 2026-08-25
---

# 2388 — The Physical Soft--Triangle Observer Is Faithful on Its Two Rees Grades

## Typing correction

Entries 2359--2362 left the physical gate in the form

\[
\lambda_{\rm BD}|_{M_{16}^{\rm deleted}}\stackrel?\ne0
\]

on a generic \(X_1=0\) algebraic fiber. A literal massless physical triangle
cannot reach that generic fiber: positivity forces

\[
\boxed{X_1=0\quad\Longrightarrow\quad X_2=X_3=p>0.}
\]

Therefore the physical question is the weighted soft--triangle pullback, not
activation of all sixteen generic deletion directions.

Sequence claim: `seqclaim-f76217b192be106159140b68`.

Epistemic graph: `ev-000000003271-bba15995-3f4b-434a-914d-c5f79aaa17b1`.

## Correct graded object

The source-derived calculations give:

\[
\begin{array}{c|ccc}
\text{Rees grade}&0&1&2\\
\hline
\text{physical source rank}&1&0&1.
\end{array}
\]

- Grade zero is the ordinary physical soft--triangle tangent line.
- The first normal grade vanishes at every physical endpoint node.
- Grade two is the supported node line first smoothed by the second normal
  coefficient.

The strict-transform measure has unit leading ratio after the normal Jacobian
cancels the Cayley--Menger square root. The normalized source factor is exact.

## Physical readout

At grade zero, the positive-cut period has one fixed nonzero phase and the
source factor is nonzero in the open chamber.

At grade two, the four oriented endpoint costalks map to

\[
(1,1,1,1)\longmapsto4\alpha_+\ne0.
\]

The source factor is strictly positive on

\[
p>0,qquad1<t<3,qquad-1<\xi<1,
\]

and none of the four node restrictions annihilates the line.

Because the two classes occupy distinct Rees grades, their readouts form a
graded diagonal map of rank two:

\[
\ker\mathcal O_{\mathrm{phys}}^{\mathrm{soft\text{-}tri}}=0.
\]

## Result

\[
\boxed{
\text{the correctly pulled-back rank-two physical soft--triangle object is}
\text{ jointly faithful under its source scalar ports.}
}
\]

This does not activate the generic rank-twenty \(X_1\)-soft algebraic module.
That module lives over a larger algebraic support than the literal physical
triangle reaches.

## Classification

- Carrier support: existing soft and triangle intersection;
- coefficient object: ordinary line plus second-normal vanishing line;
- physical observer kernel: zero;
- generic soft algebraic directions: outside the literal physical pullback;
- new Carrier datum: none;
- tensor completion: still source-underdetermined.

## Durable verification

- `research/benincasa/check_physical_soft_triangle_graded_observer.py`;
- `research/benincasa/physical-soft-triangle-graded-observer.json`;
- Entries 2363--2377 and their frozen packets.

## Next falsifier

Repeat the physical-pullback classification at total energy and the remaining
soft/Gram/Landau intersections. For each locus, compare only the coefficient
object actually reached by the source relative cycle with its admitted scalar
ports. Keep algebraic ambient ranks separate from physical observer ranks.