---
author: marici.Benincasa
date: 2026-08-25
---

# 2413 — The Generic Lower Direct Image Is Faithful on the Rank-Seven Interaction Module

## Question

Entry 2400 freezes ten nonconstant labelled coefficients in the generic
six-scale Cayley–Menger normal tower: three linear, six quadratic, and one
cubic.  The first direct-image test is whether these ten labels remain
independent in the generic rank-thirty-four four-wall twisted de Rham
quotient.

Sequence claim: `seqclaim-778da6c52b11f20914ba165b`.

## The source module already has three relations

Write

\[
D_1=a^2,
\qquad D_2=b^2,
\qquad D_3=c^2
\]

for the diagonal quadratic coefficients, and

\[
\begin{aligned}
C_{12}&=P_3^2-a^2-b^2,\\
C_{13}&=P_2^2-a^2-c^2,\\
C_{23}&=P_1^2-b^2-c^2
\end{aligned}
\]

for the square-free coefficients.  Let \(U=1\) denote the coefficient of
\(\nu_1\nu_2\nu_3\).

Before any cohomological reduction, exact polynomial identities give

\[
\boxed{
P_3^2(D_1+D_3+C_{13})
-P_2^2(D_1+D_2+C_{12})=0,
}
\]

\[
\boxed{
P_3^2(D_2+D_3+C_{23})
-P_1^2(D_1+D_2+C_{12})=0,
}
\]

and

\[
\boxed{
P_3^2U-(D_1+D_2+C_{12})=0.
}
\]

These are simply the three presentations of the constant coefficient:

\[
D_1+D_2+C_{12}=P_3^2,
\]

and its cyclic images.  Together with the three linear coefficients, the
generic source interaction module has rank

\[
\boxed{3+4=7.}
\]

Thus a raw ten-to-seven collapse is not automatically information loss.
Faithfulness must be tested against this source quotient, not against the
free ten-label presentation.

## Source-normalized quotient computation

The existing generic lower reducer was extended without changing its
divisors, exponent convention, monomial order, or kinematic samples.  In the
rank-thirty-four quotient, \(K^{-1}\) is represented by the already frozen
localization coordinate

\[
K^{-1}=z\prod_{i=1}^4L_i.
\]

Each of the ten normal coefficients is multiplied by this common
representative and reduced in one shared Groebner basis.  No primitive
section or post-hoc quotient is selected.

Two independent runs give

\[
\begin{array}{c|c|c|c}
\text{point}&\text{prime}&\operatorname{rank}H_{\rm low}
&\operatorname{rank}\langle K_\alpha/K\rangle\\
\hline
A&32003&34&7\\
B&32009&34&7.
\end{array}
\]

The three computed modular kernel vectors agree coefficientwise with the
three source identities above after normalizing respectively the
\(C_{13}\), \(C_{23}\), and \(U\) coordinates to one.

## Generic theorem

The source identities give a universal upper bound seven.  A rank-seven
minor at one exact finite-field specialization proves that the generic rank
is at least seven.  Hence the generic lower direct-image class rank is
exactly seven.  Because the modular kernel is exactly the specialization of
the source relation module, there is no additional direct-image kernel:

\[
\boxed{
\ker(\mathcal I_{\rm source}\to H_{\rm low})
=\langle\text{the three exact source relations}\rangle.
}

Equivalently, on the correctly typed source quotient,

\[
\boxed{
\mathcal I_{\rm source}^{(7)}
\hookrightarrow H_{\rm low}^{(34)}
}

is generically injective.

## Interpretation

The apparent loss of three labels is another instance of the program's
faithful-coordinate rule: ten presentation coordinates describe a
seven-dimensional source object.  The direct image forgets nothing beyond
the relations already true in the source kernel.

This is a nonhomogeneous scalar contextual-faithfulness theorem at the
algebraic coefficient level.  It does not yet prove physical observability
of all seven classes.

## Classification

- raw interaction labels: ten;
- exact source relations: three;
- faithful source interaction rank: seven;
- generic lower cohomology rank: thirty-four;
- interaction class rank in lower cohomology: seven;
- additional cohomological kernel: zero;
- new Carrier support: none.

## Scope

The calculation covers the generic four-wall lower twisted Jacobian
quotient.  It does not yet include the rank-twenty-six
\(q_{\mathcal G_{12}}\)-restricted summand, the full rank-sixty connection,
the physical relative cycle, or tensor polarization ports.

## Durable evidence

- `research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs`
  with `NORMAL_TOWER=1`;
- `research/benincasa/check_generic_lower_interaction_class_faithfulness.py`;
- `research/benincasa/generic-lower-interaction-class-faithfulness.json`;
- independent runs at points A/B and primes 32003/32009.

## Next falsifier

Repeat the same source-quotient test on the rank-twenty-six restricted
summand at \(q_{\mathcal G_{12}}=0\), then verify compatibility of the two
rank-seven images through the deletion–restriction boundary map.  A kernel
appearing only after that gluing is an extension/readout obstruction; a
class lost separately in the restricted quotient is a coefficient-level
specialization obstruction.
