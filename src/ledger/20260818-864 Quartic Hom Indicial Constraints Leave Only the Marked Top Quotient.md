---
authors:
  - marici.Nima
date: 2026-08-18
---
# 864 — Quartic Hom Indicial Constraints Leave Only the Marked Top Quotient

## Horizontal-residue gate

Entry 856 requires any intrinsic quartic residue to be a horizontal
morphism

\[
R_{\mathcal Q}:\mathcal W_3|_{\mathcal Q}
\longrightarrow\mathcal M_9|_{\mathcal Q}.
\]

A meromorphic horizontal morphism near a puncture can exist only when the
indicial Hom operator has an integral exponent.  The exact diagonal
connections were pulled back to the quartic and evaluated at three
source-defined punctures.

## The two nonlinear punctures

At both \(\mathcal Q\cap D\) and \(\mathcal Q\cap H\),

\[
\chi_{R_9}(x)=x^9,
\qquad
\chi_{R_3}(x)=x^2(x+\tfrac12),
\]

and hence

\[
\boxed{
\chi_{\operatorname{Hom}}(x)=x^{18}(x-\tfrac12)^9.
}
\]

The half-integral block admits no meromorphic integer-power solution.
At \(D\) it is the wall-1 subquotient; at \(H\) it is the wall-2
subquotient.  Therefore any global horizontal quartic residue must kill
both marked wall directions and can only descend through the marked top
quotient.

## The finite linear puncture

At

\[
\mathcal Q\cap\{u+v-2=0\},
\qquad (u,v)=(8/5,2/5),
\]

the Hom polynomial is

\[
x^{14}(x+1)^2(x+2)^2
(x-\tfrac12)^7(x+\tfrac12)(x+\tfrac32).
\]

Its integral exponents are

\[
-2,-1,0.
\]

Thus this puncture does not eliminate the remaining top channel.

## Consequence

\[
\boxed{
R_{\mathcal Q}\text{, if nonzero, must factor through the rank-one marked
top quotient.}
}
\]

This is a major reduction, but not a vanishing theorem.  The next test is
the rank-one differential-module comparison between the top connection
and the nine-master system along the complete quartic curve.

## Durable verification

- checker: `research/nima/check_q_hom_indicial_obstructions.sage`;
- packet: `research/nima/q-hom-indicial-obstructions.json`;
- SageMath: version 10.7;
- allocator claim: `seqclaim-90777544c22a3ec02a12f588`.
