# Inclusive-Higgs adaptive-closure no-go

Work package: WP585  
Owner: marici.Figueiredo

## Question

WP584 proves that one inclusive-Higgs trial is blind to the portal invariant
\(q\) at fixed \(z\). This packet tests whether contextual closure under
repetition, null records, mixtures, scores, or adaptive selection between the
two exact \(q\)-settings can repair that kernel.

## Factorization theorem

Let every authorized completed-trial kernel factor as

\[
P(o\mid z,\lambda_s,a)=K_a(o\mid z),
\]

where the action \(a\) may be chosen from the preceding record history. The
probability of any finite history is a product of such kernels and policy
weights. Summation over latent actions, mixture, and conditioning on a
positive-probability record preserve dependence on \(z\) alone. Induction on
history length therefore gives

\[
P(o_1,\ldots,o_n\mid z,\lambda_s)=P(o_1,\ldots,o_n\mid z).
\]

Every derivative along \(q\) at fixed \(z\), every corresponding score, and
every Fisher entry containing that direction is zero. Null records remain
informative about \(z\), but not about \(q\).

This is the hostile counterpart of finite score-tower faithfulness: closure
can reconstruct distinctions present in the authorized route coefficients,
but cannot manufacture a distinction absent from every primitive trial
kernel.

## Exact hostile pair

The WP584 endpoints

\[
(z,\lambda_s)=\left({1\over4},{1\over2}\right),
\qquad
\left({1\over4},{3\over2}\right)
\]

have the same one-trial kernel with \(p=1-z=3/4\). Consequently their laws
agree for every finite adaptive experiment assembled only from that kernel.
The checker enumerates every binary history through length four; the proof is
the factorization induction for arbitrary finite length.

## Classification and repair

Adaptive closure of the present instrument is still a physical rank-one
readout. It is neither a selector nor a presentation rigidifier. Adding a
policy, retaining null records, or computing a complete score tower does not
change its contextual partition.

The repair must occur before closure: admit a source-derived and experimentally
calibrated primitive trial kernel with nonzero dependence on \(q\) at fixed
\(z\). Only then can repeated or complementary records test joint
faithfulness.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp585_inclusive_higgs_adaptive_closure.py

The generated result is
research/flavor/results/wp585_inclusive_higgs_adaptive_closure.json.
