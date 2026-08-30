# Finite-exposure source-identification audit (WP245)

## Correction

WP243 proves that the calibrated trace-adjoint rate map is injective in
`(kappa_A_squared,kappa_D_squared)`. WP244 proves that its ideal pole-support
law separates the frozen WP129 constructor family away from zero residues.
Neither rank result by itself establishes operational source identification at
finite exposure.

CMS Open Data record 1059 supplies the certified 2016 recorded luminosity

\[
{\cal L}_{2016}=36.313753344\ \mathrm{fb}^{-1}
\]

with a declared 1.2% luminosity uncertainty. This is an optimistic exposure
for the local WP240 collision shard.

## Exact upper bound

Orthogonal scalar mixing gives `theta_i_squared <= 1`. Combining this absolute
upper bound with WP243's calibrated selected rates yields

\[
\mu_A\le0.71741,\qquad \mu_D\le0.12670
\]

selected events over the entire certified 2016 exposure. Even with zero
background, the Poisson probability of observing at least one event from both
sources is only

\[
(1-e^{-\mu_A})(1-e^{-\mu_D})=0.06093.
\]

Hence finite-2016 source identification is rejected before background or
detector systematics are introduced. The rate map remains asymptotically
injective; the physical instrument lacks adequate exposure.

For a 95% probability of at least one selected event, the required exposures
are approximately `151.6 fb^-1` and `858.6 fb^-1`. Ten expected selected events
require `506 fb^-1` and `2.866 ab^-1`. These are necessary count thresholds,
not sufficient background-aware identification thresholds.

## Disposition

- admitted domain: the WP243 two-pole universal-mixing source domain;
- faithful source coordinate: `(kappa_A_squared,kappa_D_squared)` only in the
  asymptotic response law;
- contextual partition: algebraically discrete away from zero residues;
- finite experiment: nonfaithful with overwhelming no-event probability;
- smallest physical falsifier: both maximally mixed source columns yield fewer
  than one expected selected event in full 2016 data;
- remaining instrument gate: substantially larger exposure or a higher-rate
  source-derived channel, then background-aware power and systematic tests.

This correction distinguishes algebraic span, calibrated response, and
executable identification. No reference port repairs insufficient event rate.

## Reproduction

Run `uv run python
research/flavor/checkers/wp245_finite_exposure_source_id_audit.py`. The checker
uses checksum-pinned CMS luminosity summaries and regenerates
`results/wp245_finite_exposure_source_id_audit.json`.
