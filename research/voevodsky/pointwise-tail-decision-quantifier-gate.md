# Pointwise tail decision and the quantifier gate

## Question

Does eventual certification of every fixed observer packet provide the required global positivity statement, and what remains circular in the RH-conditional strictness argument?

## Claim boundary

The packet separates the quantifiers, presentation kernels, and proof routes. It does not independently verify the analytic zero-count argument or establish unconditional termination.

## Correct quantifier

The observer theorem needs

\[
\forall I\;\exists N(I):
\text{the tail margin decides packet }I.
\]

It does not require

\[
\exists N\;\forall I:
\text{one cutoff decides every packet}.
\]

The checker models rank \(r\) with limiting margin \(1/r\) and tail radius \(r/N\). The least decisive cutoff is \(r^2+1\). Every packet is eventually decided, but no fixed cutoff decides packets of arbitrary rank.

## Presentation kernels

Repeated translate labels produce identical Gram columns and exact null vectors. These are presentation relations, not failures of physical positivity. They must be quotiented before testing faithful Gram coordinates.

A two-copy repeated-label Gram fixture has rank one and determinant zero; its one-dimensional quotient is positive definite. The checker verifies this exactly.

## Conditional strictness

Grothendieck's reported argument is:

1. under RH, a null vector for a distinct finite translate packet produces a nonzero finite exponential polynomial vanishing at every distinct zero ordinate;
2. such a polynomial has only \(O(T)\) real zeros;
3. Riemann--von Mangoldt together with the classical RH multiplicity bound gives superlinear growth of distinct zero ordinates;
4. therefore the exponential polynomial must vanish identically, contradicting distinct-label linear independence.

This would make every fixed distinct-label Gram packet positive definite under RH, hence eventually decidable by tail margins. It cannot supply the missing forward proof because RH is used in step 3.

## Three noncircular routes

A proof must provide at least one of:

- unconditional packet-dependent lower eigenvalue margins;
- a direct completed semidefinite factorization that remains valid at zero margin;
- termination of a verified positive-or-negative tail algorithm for every quotient-faithful finite packet without assuming RH.

Strict finite margins are computationally convenient but stronger than positive semidefiniteness. If a genuine completed packet has a zero eigenvalue, every finite truncation may remain inside the tail uncertainty interval.

## Deeper meaning

The absence of a uniform cutoff is not a defect. The metaobserver is an inverse limit: each finite packet may have its own arithmetic witness. What matters is that witnesses are source-derived and compatible, not that their cutoff depths are bounded globally.

The actual obstruction is circular strictness. Conditional positive definiteness explains why a tail algorithm terminates if RH is true, but an RH proof needs an unconditional reason that it cannot terminate negatively and cannot remain unresolved forever.

## Disposition

The architecture supports pointwise certificates and rejects the stronger uniform-cutoff demand. Repeated-label nulls are removed by a faithful quotient. The next gate is an unconditional termination or semidefinite-factorization theorem on that quotient.

## Verification

- `research/voevodsky/pointwise-tail-decision-quantifier-gate-v1.json`
- `research/voevodsky/checkers/check_pointwise_tail_decision_quantifier_gate.py`
- `research/voevodsky/results/pointwise_tail_decision_quantifier_gate.json`
