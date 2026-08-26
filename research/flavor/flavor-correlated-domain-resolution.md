# Correlated-domain resolution (WP335)

## Exchangeable second moments

Let (N) detector-calibrated domain indicators have common positive probability
(p) and pairwise correlation (ho). Their sample-mean variance is

\[
\operatorname{Var}(\bar X)
=\frac{p(1-p)}{N}\left[1+(N-1)\rho\right].
\]

Relative to independent trials, the exact effective sample size is

\[
N_{\mathrm{eff}}
=\frac{N}{1+(N-1)\rho}.
\]

For perfect correlation, every nominal repetition gives only one effective
sample. For fixed positive correlation, the effective count saturates at
(1/\rho) as (N) grows.

## Epistemic boundary

The mean and pairwise covariance determine this variance correction. They do
not determine the joint Bernoulli law, its tails, or its Fisher information.
WP334's independent likelihood therefore cannot be repaired merely by
substituting (N_{\mathrm{eff}}) into every statistical formula.

This packet admits only the exact second-moment result. A stronger confidence
or identification claim requires a source-derived joint domain model or a
valid worst-case bound over an explicitly declared family.

## Instrument gate

Physical use requires measurements of spatial and temporal domain
correlations, detector common-mode effects, and the preparation history that
defines distinct source trials.

Run `uv run --with sympy python
research/flavor/checkers/wp335_correlated_domain_resolution.py` to regenerate
the exact second-moment audit.
