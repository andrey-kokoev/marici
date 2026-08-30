# Spin(5) conditional product-law gate (WP910)

## Question

When do independently acquired event keys actually justify the binomial count
law used by WP907?

## Sufficient factorization

For a fixed declared run state (c), let event keys (U_1,\ldots,U_n) be
independent under an admitted acquisition law, and let

\[
D_e=f(c,U_e)
\]

with no cross-event state. Then the discordance indicators are independent
conditional on (c). If the same transform and support apply to every event,
they are conditionally iid Bernoulli with parameter (p(c)).

This is the minimal constructive product-law theorem. It requires all three
parts: independent keys, a frozen run state, and an event-local transform.
Replay establishes the transform; it does not establish the key law.

## Shared-nuisance hostile

Conditional independence does not imply unconditional independence when the
run state is random and then forgotten. Let (C) be a fair binary run state
and, conditional on (C), generate iid discordances with

\[
p_- = p_0-\delta,qquad p_+=p_0+\delta,qquad
\delta=\frac{p_0}{2}.
\]

Every event still has marginal discordance probability (p_0), but for two
different events

\[
\operatorname{Cov}(D_e,D_f)=\operatorname{Var}(p_C)=\delta^2>0.
\]

The count variance becomes

\[
\operatorname{Var}(K)=np_0(1-p_0)+n(n-1)\delta^2,
\]

and the zero-discordance probability is

\[
\frac12(1-p_-)^n+\frac12(1-p_+)^n>(1-p_0)^n.
\]

At WP907's first look this mixture exceeds the allocated (1/160) exactly,
despite correct marginals and iid keys conditional on the run state.

## Instrument rule

The paired experiment may use WP907 only within a stratum whose complete
run-level nuisance packet is frozen before event-key acquisition and held
fixed. If several run states are sampled, their labels must be retained and
the analysis must use a preregistered stratified or mixture-valid count law.
Marginalizing the labels and applying one binomial test is prohibited unless a
source theorem proves (p(c)) constant over the admitted run-state domain.

The event-locality manifest must also exclude mutable caches, adaptive tuning,
shared rejection counters, stateful detector conditions, and cross-event
feedback. These are possible hidden arrows from (U_e) into later events.

## Boundary

WP910 supplies a conditional product theorem and exact hostile. It does not
instantiate the independent event-key acquisition law or calibrate the run
state. Those remain the physical-instrument gates. The operation is neither a
flavor selector nor a presentation rigidifier.

Run:

~~~text
uv run python research/flavor/checkers/wp910_spin5_conditional_product_law.py
~~~
