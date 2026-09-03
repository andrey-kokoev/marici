# Total-energy descent versus conductor specialization

## Problem

The candidate descent map should identify the source-normalized leading total-energy residue with a flat-space amplitude. The strongest version also asserts compatibility with `q_G12` semistable conductor specialization without additional `kappa`-dependent renormalization.

## Bold conjecture

The source-normalized leading total-energy residue is exactly the independently normalized flat-space graph amplitude, with no additional `kappa`-dependent renormalization, and this identification commutes with `q_G12` conductor specialization.

## Named rivals

1. exact unrenormalized equality commutes with specialization;
2. generic-`kappa` equality may hold, but specialization requires a singular target or renormalization;
3. no amplitude descent exists even generically.

## Risky consequences

The strict-transform source measure must cancel every conductor pole not present in the independently normalized amplitude. In particular, the two sides must have equal valuation at `kappa=1`.

## Strongest falsification attempt and residual

The source measure audit in `research/benincasa/results/cosmology_source_contour_semistable_descent_dpc.json` gives valuation zero at `kappa=1`: its normalized exceptional factor is independent of `kappa`. The exact conductor connecting coefficient has valuation minus two.

Execution `structured_command_execution:e_32940_1788308339861136300_1` therefore computes

\[
\nu_{\kappa-1}(\text{specialized wavefunction side})=-2,
\qquad
\nu_{\kappa-1}(\text{unrenormalized amplitude side})=0,
\]

with residual minus two. The source measure cannot cancel the conductor double pole. The commutation consequence fails, so the bold conjunction is falsified.

## Disposition and residual conjecture

The failure does not test the possible total-energy residue equality at generic `kappa`. It separates two arrows that the bold conjecture conflated:

1. generic-`kappa` source-normalized amplitude descent;
2. singular specialization or renormalized comparison at `kappa=1`.

Residual conjecture: a generic-`kappa` amplitude descent may exist, but its conductor specialization lands in a target twisted by `(kappa-1)^{-2}` or requires an explicit renormalization map. The next test is the exact three-site total-energy coefficient away from `kappa=1`; no semistable commutation should be assumed.

## Evidence

- `research/nima/checkers/check_total_energy_conductor_commutation_no_go.py`
- `research/benincasa/results/cosmology_source_contour_semistable_descent_dpc.json`
- `research/nima/residue-incidence-normalization-dpc.md`
