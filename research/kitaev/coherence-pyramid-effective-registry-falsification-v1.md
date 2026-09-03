# Falsification attempt on effective registry completeness

## Question

Can a fixed, versioned predicate presentation with explicit acceptance tests reproducibly classify every typed transfer by a relative minimal failure antichain?

## Claim boundary

This packet attacks total effective classification. It does not deny relative semantic classification when proofs or counterexamples are supplied.

## Bold conjecture under test

After fixing predicate definitions and acceptance tests, every typed transfer can be reproducibly assigned its passing predicates and relative minimal antichain.

## Halting reduction

For a program `e`, define a computable coefficient sequence

\[
a_n(e)=
\begin{cases}
1,&\text{if `e` has not halted within its first }n\text{ steps},\\
0,&\text{otherwise}.
\end{cases}
\]

Each coefficient is obtained by a finite simulation. Define on finite sequences

\[
F_e(x)=\sum_{n\geq1}a_n(e)x_n.
\]

If `e` halts after `N` steps, only finitely many coefficients are nonzero, so `F_e` extends continuously to `l2`. If `e` never halts, every coefficient is one, and the exact unit-vector family used in the previous falsification gives functional norm at least `sqrt(N)` on the first `N` coordinates. Hence `F_e` has a continuous `l2` completion exactly when `e` halts.

A total acceptance test that decides `completed_or_unbounded` for every such finitely specified source map would decide the halting problem. No such total algorithm exists.

## Consequence

Even with a fixed registry version and mathematically precise predicates, a complete operational assignment need not terminate. A transfer can have a definite semantic status while no registry checker can always produce its minimal antichain. Adding `unknown` avoids false classification but falsifies the claim that every transfer is reproducibly assigned a pass/fail antichain.

## Named rivals

- Proof-carrying partial registry: admit pass or fail only with a certificate; otherwise record `unknown`.
- Bounded-domain registry: restrict constructors to a decidable fragment.
- Semidecision pair: run proof and counterexample searches concurrently, accepting that either may diverge.

## Strongest residual

The effective-completeness conjecture is false. Versioning removes presentation ambiguity but not undecidability.

## Surviving conjecture

For a fixed registry version, every admitted `pass` or `fail` status is reproducible from a stored certificate and checker. The registry is intentionally partial and includes `unknown`, `test_inconclusive`, and `test_nonterminating` as epistemic statuses distinct from mathematical failure. Minimal antichains are asserted only for certified failures within the decidable or proved fragment.

## Disposition

Revise. Require certificate references for every non-unknown predicate status, checker termination evidence for executable tests, and explicit bounded constructor domains. Never interpret timeout or absence of proof as a failed transfer predicate.
