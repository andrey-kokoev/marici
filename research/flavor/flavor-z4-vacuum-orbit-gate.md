# Z4 symmetry does not select a vacuum orbit without potential data (WP64, move 5/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

For the minimal angular term

\[
V_{ang}=2\kappa r^4\cos(4\theta),
\]

stationarity gives (	heta=j\pi/4). Exact Hessians show:

- (kappa<0) selects the real/imaginary axes;
- (kappa>0) selects the axes shifted by (pi/4).

Thus (mathbb Z_4) symmetry alone does not choose the vacuum orbit claimed in
the illustrative picture; the coefficient sign is independent normalization
data. The declared source specifies neither that sign nor the radial
potential, vacuum history, covariant flavon-to-Yukawa map, or instrument.

Given a sign, the potential rigidifies a flavon phase orbit. It still does not
define a selector on `physical16` until the selected orbit is mapped
covariantly to Yukawa quotient data and survives the fitted ensemble.

Smallest exact falsifier: reverse only (operatorname{sign}\kappa); the same
symmetry shifts every minimum by (pi/4).

Verification:
`uv run --with sympy python research/flavor/checkers/wp64_z4_vacuum_orbit_gate.py`.
