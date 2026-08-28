# Spin(5) two-stratum discordance escalation (WP911)

## Question

Can WP907 remain valid when the paired experiment contains two retained run
states with different discordance rates?

## Conservative stratified repair

Let the two preregistered run strata be (c_1,c_2). Within each stratum and
pole, require WP910's product-law factorization: frozen state, independent
event keys, and an event-local transform. Do not pool the discordance counts.

For every stratum-pole cell use four cumulative looks with discordance caps
(0,1,2,3). Allocate failure probability (1/320) to each look. Across two
strata, two poles, and four looks, the union bound is

\[
2\cdot2\cdot4\cdot\frac1{320}=\frac1{20}.
\]

At each cell and look (k), certify only when the exact lower binomial tail at
the target

\[
p_0=\frac{389}{2937600}
\]

is at most (1/320) and the cumulative discordance count is at most (k).
All eight stratum-pole cells must certify. An unregistered stratum fails
closed.

If both stratum rates obey (p_s\leq p_0), then for any declared mixture
weights (w_s\geq0) with (sum_s w_s=1),

\[
\sum_s w_sp_s\leq p_0.
\]

Thus the mixture conclusion no longer requires equal stratum rates or removal
of the run label.

## Exact budgets and boundary

The checker derives the four per-cell look counts by exact integer binomial
tails. Every reported count passes and one fewer fails. This construction is
conservative: it demands the target in every retained stratum rather than only
for one weighted average.

WP911 does not discover or calibrate the stratum partition. The nuisance
domain, support, weights, transition rules, and event-locality manifest must be
fixed independently. Hidden or adaptively merged strata falsify the contract.

This is a detector-response inference repair, neither selector nor rigidifier.

Run:

~~~text
uv run python research/flavor/checkers/wp911_spin5_two_stratum_escalation.py
~~~
