---
author: marici.Benincasa
date: 2026-08-25
---

# 2457 — The Only Connected-Score Blind Direction Is Overall Cayley-Menger Scaling

## Question

Entry 2421 proves algebraic recovery of the rank-seven interaction module.
What kernel can remain when those insertions are tested by a positive
regulated physical score pairing?

Sequence claim: `seqclaim-2548d65ad0a7f20aa0c2a994`.

## The kernel is itself an interaction direction

In the source basis

\[
(L_1,L_2,L_3,D_1,D_2,D_3,U),
\]

the Cayley--Menger polynomial obeys the exact identity

\[
\begin{aligned}
K={}&P_1^2L_1+P_2^2L_2+P_3^2L_3\\
&+(-P_1^4+P_1^2P_2^2+P_1^2P_3^2)D_1\\
&+(P_1^2P_2^2-P_2^4+P_2^2P_3^2)D_2\\
&+(P_1^2P_3^2+P_2^2P_3^2-P_3^4)D_3\\
&-2P_1^2P_2^2P_3^2U.
\end{aligned}
\]

Thus overall rescaling of (K) is one canonical line inside the rank-seven
module, not an eighth direction.

## Positive score theorem

On a regulated positive Cayley--Menger chamber let

\[
d\mu=Z^{-1}K^{-1/2}\prod_q q^{-1},d^3y.
\]

For a source deformation (f\in\mathcal I^{(7)}), the logarithmic kernel
score is

\[
s_f=-\frac12\frac fK.
\]

Its connected score norm vanishes exactly when (f/K) is constant
(mu)-almost everywhere.  Since the chamber contains an open set and both
objects are rational functions, this implies the polynomial identity

\[
f=\lambda K.
\]

Therefore

\[
\boxed{
\ker(\operatorname{Cov}_\mu s)=\langle K\rangle,
\qquad
\operatorname{rank}\operatorname{Cov}_\mu s=6.
}
\]

The ordinary mean score on this line is

\[
\langle s_K\rangle=-\frac12\ne0.
\]

Hence the augmented mean-plus-connected observer has rank seven.

## Exact soft gate

The six chosen shape directions together with (K) have change-of-basis
determinant

\[
-2P_1^2P_2^2P_3^2.
\]

Their only algebraic failure is the already frozen site-soft support.

## Result

\[
\boxed{
\text{positive connected scores recover six shape directions, and the
ordinary mean recovers the unique normalization line.}
}
\]

This explains rather than fits the finite constant port required by the
interaction module.

## Scope

The theorem applies to the regulated fixed-chamber density.  The physical
boundary moves with (P_i); Entries 2424--2429 construct its local
Gauss--Manin adapter.  One must transport the above decomposition through
that adapter before claiming physical-period rank seven.

## Durable evidence

- `research/benincasa/check_rank7_score_normalization_line.py`;
- `research/benincasa/rank7-score-normalization-line.json`;
- Entries 2421, 2424, and 2426.

## Next falsifier

Apply the moving-cycle covariant derivative to the scaling line and the six
shape directions.  Test whether its boundary/contact terms preserve the
mean-plus-connected rank decomposition.  Any additional kernel is the first
remaining physical-readout obstruction.
