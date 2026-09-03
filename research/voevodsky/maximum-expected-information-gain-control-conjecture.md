# Maximum expected information-gain control conjecture

## Question

Which admissible probe or source-perturbation experiment should control the next research action when the raw completed-heat form may be bounded, unbounded but closable, or nonclosable?

## Claim boundary

This packet proposes an epistemic feedback policy over a declared finite hypothesis family at one research stage. It does not assign physical probabilities to arithmetic states, select a physical record, prove a global optimum over all possible experiments, or imply RH.

## Problem

The live alternatives are

\[
\Theta
=
\{\theta_B,\theta_C,\theta_M\},
\]

where:

- \(\theta_B\): \(q_H\) is bounded relative to the order norm;
- \(\theta_C\): \(q_H\) is unbounded but semibounded and closable;
- \(\theta_M\): the closed feature relation has a nonzero multivalued residual.

Let \(\mathcal U_{\rm adm}\) be a declared finite set of currently executable experiments. Each \(u\in\mathcal U_{\rm adm}\) has a finite record set \(\mathcal R_u\), likelihood model \(P(r\mid\theta,u)\), and cost \(c(u)\).

## Bold conjecture

At each bounded research stage, choose an admissible experiment maximizing expected Shannon entropy reduction per declared cost:

\[
u^*
\in
\operatorname*{argmax}_{u\in\mathcal U_{\rm adm}}
\frac{I(\Theta;R_u\mid u)}{c(u)},
\]

where

\[
I(\Theta;R_u\mid u)
=
H(\pi)
-
\sum_{r\in\mathcal R_u}
P(r\mid u)H(\pi(\cdot\mid r,u)).
\]

For the current closure problem, the maximizer is conjectured to be a discriminating sequence search that jointly measures

\[
\lVert f_n\rVert_{\rm ord},
\qquad
q_H(f_n-f_m),
\qquad
q_H(f_n),
\]

rather than further finite positivity sampling. These three records directly separate a multivalued residual from mere unboundedness and boundedness.

## Named rivals

1. maximize the probability of a positive finite Gram test;
2. minimize computational cost without weighting information gain;
3. refine the largest existing packet regardless of hypothesis discrimination;
4. choose the experiment with the largest expected numerical change;
5. assign probability directly to RH and optimize that posterior.

The fifth rival is inadmissible here because the likelihood model has not been calibrated to RH and finite records do not define a probability distribution on its truth.

## Risky consequences

The conjecture predicts:

1. finite positivity tests receive low value once they cease distinguishing \(\theta_B\) from \(\theta_C\);
2. an experiment receives zero information value when all hypotheses induce the same record distribution;
3. a successful null/form-Cauchy witness sharply favors \(\theta_M\);
4. a uniform source bound sharply favors \(\theta_B\);
5. observed unbounded generalized gains without a form-Cauchy witness distinguish \(\theta_C\) from neither rival by themselves;
6. the selected experiment changes when priors, likelihoods, admissible records, or costs change.

## Strongest falsification attempt

Preregister a finite experiment menu containing:

- additional finite positivity samples;
- generalized-eigenvalue growth tests;
- direct searches for base-null/form-Cauchy sequences;
- source-bound extraction attempts.

Specify likelihoods before executing the menu. Reject the conjectured policy if another declared policy yields lower posterior entropy at equal or lower total cost across matched stages, without increasing unsupported promotions or omitted residuals.

## Exact residual

No calibrated likelihood model \(P(r\mid\theta,u)\) currently exists. Therefore no numerical expected-information ranking is yet authorized. The first missing typed object is a preregistered likelihood table tied to executable record-producing tests.

## Disposition

The maximum expected information-gain rule is adopted as a falsifiable experiment-selection conjecture, not as evidence about \(q_H\) or RH. Until likelihoods are supplied, it orders the design criteria qualitatively but does not select a unique experiment.
