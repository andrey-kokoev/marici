# 2697 — The Differentiated Euler Identity Distinguishes Dual Source Lifts

## Frozen datum

Entry 2694 establishes only the degree-28 source identity

\[
E(S)=28S.
\]

It does not select a first-order extension of (S) over a dual-number parameter.

## Two-lift falsifier

Let (H_{\rm can}=\partial_jS). Compare

\[
S_{\rm can}=S+\epsilon H_{\rm can}
\]

with

\[
S_{\rm alt}=S+\epsilon(H_{\rm can}+S),
\qquad \epsilon^2=0.
\]

Both reduce to the same frozen source (S) modulo (epsilon), but their first-order coefficients differ.

Since differentiation lowers Euler weight by one,

\[
(E-27)H_{\rm can}=0.
\]

For the alternative lift,

\[
(E-27)(H_{\rm can}+S)
=(28-27)S
=S.
\]

Thus the differentiated degree-27 identity rejects the alternative lift by a defect equal to the frozen source itself.

## Result

The scalar degree-28 recurrence does not retroactively authorize a unique dual-number derivative. The differentiated recurrence is a genuine discriminator between first-order source extensions.

This proves only the logical independence and discriminating power of the next gate. It does not yet derive (H_{\rm can}) from the unspecialized source coefficients.

## Artifacts

- `research/benincasa/check_rank26_dual_lift_falsifier.py`
- `research/benincasa/rank26-dual-lift-falsifier.json`

## Next falsifier

Construct the canonical coefficient derivative of the complete unspecialized five-pole source and its de Rham relations. Then verify, in all three parameter directions,

\[
P_1^2\nabla_jD_0+P_2^2\nabla_jD_1+P_3^2\nabla_jD_2
=27D_j.
\]

A failure would show that the source homogeneity theorem does not lift to the proposed Gauss--Manin jet system.
