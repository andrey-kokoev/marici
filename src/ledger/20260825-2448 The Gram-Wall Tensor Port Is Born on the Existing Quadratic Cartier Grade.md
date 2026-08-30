---
author: marici.Benincasa
date: 2026-08-25
---

# 2448 — The Gram-Wall Tensor Port Is Born on the Existing Quadratic Cartier Grade

## Question

Entry 2447 proves generic Gauss--Manin compatibility but its adapted tensor
frame ceases to exist when the external momentum triangle becomes collinear.
Does the tensor observer require new support there, or is it recovered by the
weighted Gram/Rees coordinate already frozen in Entries 2433--2439?

## Stabilizer at the wall

At a collinear external configuration, rotations around the common momentum
axis form an $SO(2)$ stabilizer. A nonzero ordinary spin-two vector cannot be
invariant under this stabilizer. Hence the ordinary physical tensor fiber and
its first normal jet vanish.

Let

\[
u=(u_y,u_z)
\]

be the labelled transverse departure from collinearity. The first admissible
spin-two object is quadratic:

\[
\boxed{
u\longmapsto
(u_y^2-u_z^2,\;2u_yu_z).
}
\]

As a map

\[
\operatorname{Sym}^2N_{\rm Gram}
\longrightarrow
\operatorname{Sym}^2_0N_{\rm Gram},
\]

it has rank two. Its one-dimensional kernel is the radial trace
$u_y^2+u_z^2$.

## Physical weighted path

The source-labelled physical triangle approaches the wall in one transverse
direction. Put

\[
u=(\theta,0),
\qquad
w=\theta^2.
\]

Then

\[
(u_y^2-u_z^2,2u_yu_z)=(w,0).
\]

Thus:

- the ordinary value at $\theta=0$ vanishes;
- the first ordinary $\theta$ jet vanishes;
- the first $w$-Cartier grade maps to the parity-even plus port by the unit
  coefficient $1$.

The local physical-path complex is therefore

\[
\mathbb Q\langle[w]\rangle
\xrightarrow{1}
\mathbb Q\langle\epsilon^+\rangle,
\]

with zero kernel and cokernel.

## Compatibility with the interaction action

The coordinate $w=\theta^2$ is exactly the weighted Gram coordinate used in
Entries 2436 and 2439. Entry 2439 proves that weighted base change preserves
the faithful rank-seven interaction action and has exceptional determinant
$-P_1P_2$. Therefore

\[
\boxed{
\ker_{\rm tensor,Gram}^{\rm additional}=0
}
\]

away from existing soft support.

## Result

\[
\boxed{
\text{the Gram-wall tensor response is a quadratic Cartier grade on the
existing weighted carrier, and its physical supported cone is locally exact.}
}
\]

The frame failure at $\Lambda=0$ is not a new tensor divisor. It is the
representation-theoretic reason that first-jet data are insufficient and the
already frozen second normal/Rees grade is required.

## Scope

This is the universal local spin-two normal representation and its
source-labelled one-direction physical path. It does not normalize a global
tensor period or activate the cross port on the rotational quotient. At
$P_1P_2=0$, the weighted chart itself degenerates and the separate soft
analysis is required.

## Durable evidence

- `research/benincasa/check_spin2_weighted_gram_cartier_grade.py`;
- `research/benincasa/spin2-weighted-gram-cartier-grade.json`;
- Entries 2433--2439 and 2447;
- sequence claim `seqclaim-c12fc8d09c24c551796af958`.

## Next falsifier

Audit the tensor coefficient and observer complex on the soft--Gram
intersections, then on marked-wall, Cayley--Menger/Landau, total-energy, and
elliptic-degeneration support. Retain the Tate anti-trace costalk even though
the generic parity-even cycle annihilates it.
