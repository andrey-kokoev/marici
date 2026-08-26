# Independence-probe hierarchy (WP341)

## Pairwise test

WP340's first moment identifies (p) inside the iid grammar but cannot test the
grammar. A calibrated second moment supplies the pair covariance

\[
u_2-u_1^2.
\]

Nonzero covariance falsifies pairwise independence. Vanishing covariance does
not certify mutual independence.

## Exact parity hostile pair

Compare three iid fair bits with the uniform law on the four even-parity words
`000`, `011`, `101`, and `110`. Both laws have every first moment equal to
(1/2) and every pair moment equal to (1/4). All pair covariances vanish.
Their third moments are nevertheless

\[
u_3^{\mathrm{iid}}=\frac18,
\qquad
u_3^{\mathrm{parity}}=0.
\]

Third order is therefore the smallest coincidence probe that separates this
hostile pair.

## Instrument tradeoff

The hierarchy is domain-relative: first order identifies the one-parameter iid
family, second order challenges pairwise independence, and third order detects
the residual parity dependence. Detector inversion costs scale as
(\gamma^{-2}) and (gamma^{-3}) at the latter orders, so a source theorem
excluding higher-order dependence can be experimentally valuable if it is
independently justified.

Run `uv run --with sympy python
research/flavor/checkers/wp341_independence_probe_hierarchy.py` to regenerate
the exact hierarchy audit.
