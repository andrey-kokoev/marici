# Robustness margin of the negative loop witness

## Question

How much bounded contamination can the exact value \(-1/8\) tolerate while still excluding positive commutative multiplicative factorization?

## Claim boundary

This packet gives deterministic witness margins under explicitly stated additive and convex-contamination models. It does not supply a statistical sampling theorem, hardware noise model, or shared-control fault bound.

## Witness cone and gap

The rival positive commutative model predicts a loop value in the closed cone

\[
\Omega_{\mathrm{comm}}\ge0.
\]

The ideal ordered noncommutative witness is

\[
\Omega_*=-\frac18.
\]

Its signed distance to the rival boundary in the scalar coordinate is \(1/8\). If a deterministic error satisfies

\[
|\delta|<\frac18,
\]

then \(\Omega_*+\delta<0\), so rival exclusion survives. At equality the observation may reach zero and strict exclusion is lost.

## Convex contamination

Suppose the observed scalar is

\[
\Omega_{p,b}=(1-p)\left(-\frac18\right)+pb,
\]

where \(p\in[0,1]\) is contamination weight and \(b\in[0,1]\) is a positive commutative background value. Negativity holds exactly when

\[
p<\frac{1}{1+8b}.
\]

For zero baseline \(b=0\), every \(p<1\) retains a negative value. For worst-case bounded baseline \(b=1\), the uniform guarantee is

\[
p<\frac19.
\]

These thresholds concern the scalar rival witness only. They do not imply that the contaminated process implements the intended ordered loop.

## Statistical gate

An experiment estimates \(\Omega\) from bounded observations. Rival exclusion requires a confidence interval whose upper endpoint is strictly below zero. Reporting a negative point estimate is insufficient. The interval construction, trial independence, drift model, and multiple-loop correction are separate certificates.

## Correlated faults

Shared-control faults can produce a biased negative scalar while implementing the wrong route composite. Such a result may still exclude the positive commutative cone but fail to verify the intended associator loop. Therefore records need separate fields for:

- witness negativity;
- route-identity verification;
- additive systematic bound;
- contamination model and bound;
- statistical upper confidence bound;
- shared-control fault residual;
- resulting rival-exclusion scope.

## Pyramid consequence

Rival exclusion has a quantitative margin independent of coordinate faithfulness. The registry should store `witness_gap` and `robustness_model`, not only the ideal value. Physical coherence verification remains a conjunction of witness separation and constructor identity.

## Disposition

The exact negative loop has additive margin \(1/8\) and worst-case positive-background contamination threshold \(1/9\). These are rigorous scalar no-go margins, not physical implementation certificates.

## Verification

- `research/voevodsky/checkers/check_negative_loop_robustness.py`
- `research/voevodsky/results/negative_loop_robustness.json`
