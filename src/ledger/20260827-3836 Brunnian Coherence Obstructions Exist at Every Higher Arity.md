# Brunnian Coherence Obstructions Exist at Every Higher Arity

For every \(n\ge5\), let

\[
C_{n-2}=[\cdots[[x_1,x_2],x_3],\ldots,x_{n-2}],
\qquad
P=x_1\cdots x_{n-2},
\]

and define the point-push class

\[
\beta_n=[C_{n-2},P^{-1}].
\]

It is nontrivial. If the two entries commuted, the cyclic-centralizer theorem
for free groups would make them powers of a common element, contradicting
their zero and \((1,\ldots,1)\) abelianizations. Yet deleting any marked point
trivializes \(\beta_n\).

Therefore no architecture assembled only from all proper deletion marginals
is jointly faithful uniformly in support size. Every higher arity contains a
new Brunnian filling class. The four-point endpoint-projective-central
termination is exact but arity-local.

Evidence:

- `research/strominger/brunnian-coherence-obstructions-exist-at-every-higher-arity.md`
- `research/strominger/checkers/unbounded_brunnian_marginal_obstruction_checks.py`
- `research/strominger/results/unbounded_brunnian_marginal_obstruction_checks.json`

Bounded replay for \(5\le n\le12\): 5/5 aggregate gates passed. Checker
SHA-256: `a5073552f7e6f6f13c2566665fa350ee3648b1273fca96e536549075c11bbc56`.
