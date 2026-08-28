# Spin(5) pair-independence hostile (WP908)

## Question

Do replayability, correct one-event marginals, and semantic address stability
authorize WP907's binomial pair-count law?

## Hostile constructor

No. Let one hidden Bernoulli variable \(Z\) with parameter

\[
p_0=\frac{389}{2937600}
\]

be drawn once for the entire run, and set every pair-discordance indicator to
\(D_e=Z\). This generator is exactly replayable. It can be exposed through
stable event and semantic addresses, and every individual event has the
correct marginal \(\Pr(D_e=1)=p_0\). Yet all events are perfectly dependent.

For (n) nominal event pairs, the count (K) is supported only at zero and
(n):

\[
\Pr(K=0)=1-p_0,\qquad \Pr(K=n)=p_0.
\]

At WP907's first look, the false-certification probability under this null is
\(1-p_0\), not \((1-p_0)^n\). It therefore greatly exceeds the allocated
\(1/160\). The covariance matrix of the \(D_e\) has every entry equal to
\(p_0(1-p_0)\) and rank one, irrespective of nominal \(n\).

This is the smallest structural hostile: one run-level latent bit gives every
event the right marginal while reducing the effective stochastic dimension
to one.

## Consequence

WP904's deterministic replay tests and WP905's marginal-validity test do not
imply event-pair independence. WP907 is exact only under its declared iid-pair
assumption. Empirical autocorrelation tests cannot prove independence; they
can only falsify particular dependence patterns.

An admissible acquisition contract must name the stochastic unit. One valid
route is independently randomized event keys acquired from a declared entropy
instrument, followed by a frozen deterministic per-event transform. Another
is a source theorem for a counter-based generator under an explicit randomized
key model. A single fixed key plus a cryptographic hash supplies an
algorithmic pseudorandomness assumption, not an exact physical independence
theorem.

The contract must record entropy source and health tests, key scope, event-key
provenance, rejection and retry rules, collision handling, and run boundaries.
Until then, WP907 is conditional and WP901/WP906 share the same independence
gate.

This packet concerns detector-response inference only. It is neither selector
nor rigidifier.

Run:

~~~text
uv run python research/flavor/checkers/wp908_spin5_pair_independence_hostile.py
~~~
