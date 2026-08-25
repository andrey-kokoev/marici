# Muon–tau signal-grid shape (WP254)

## Frozen grid test

Import the smallest official 130- and 160-GeV CMS signal files selected before
response inspection. Apply WP251 and WP253 unchanged and adjoin the existing
140-GeV and simulated-background columns in the same six-bin visible-mass
frame.

The raw signal templates are

\[
\begin{aligned}
S_{130}&=(56,492,314,33,0,0),\\
S_{140}&=(11,199,159,20,0,0),\\
S_{160}&=(16,232,286,141,3,0).
\end{aligned}
\]

All menu joins have zero length mismatches.

## Exact contextual faithfulness

\[
\operatorname{rank}[S_{130},S_{140},S_{160}]=3,
\qquad
\operatorname{rank}[S_{130},S_{140},S_{160},B]=4.
\]

A signal-only minor is `626824`; adjoining background gives the nonzero minor
`1880472`. Summing every bin reduces the same four columns to rank one. The
140–200 GeV bin also separates 160 GeV by support: `(0,0,3)` across the signal
grid.

## Claim boundary

WP254 is a **finite-grid physical/readout theorem** on three labelled CMS pilot
samples and the admitted simulated-background pilot. It does not authorize
interpolation to the actual 133.774 and 151.287 GeV poles, full-sample weighted
precision, QCD control, systematic completion, or finite-power identification.
The next constructor must validate the transport from the mass grid to those
physical poles without fitting it from the desired rank.

Run `uv run --with sympy python
research/flavor/checkers/wp254_mu_tau_signal_grid_shape.py` for exact ranks,
minors, tail support, and rate-collapse failure.
