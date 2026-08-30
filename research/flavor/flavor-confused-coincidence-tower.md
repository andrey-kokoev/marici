# Confused coincidence tower (WP338)

## Background-sector transform

For a binary detector with false-positive background (alpha) and calibrated
contrast (gamma), let (u_j) be the normalized source coincidence moment of
order (j). The observed moment is

\[
r_j=\sum_{\ell\leq j}
\binom j\ell\alpha^{j-\ell}\gamma^\ell u_\ell.
\]

Every raw correlator therefore contains lower-order background sectors. The
second order already reads

\[
r_2=\alpha^2u_0+2\alpha\gamma u_1+\gamma^2u_2.
\]

The complete order-six transform is triangular with determinant

\[
\gamma^{21}.
\]

For calibrated nonzero contrast, its exact inverse is

\[
u_j=\gamma^{-j}\sum_{\ell\leq j}
\binom j\ell(-\alpha)^{j-\ell}r_\ell.
\]

## Authority boundary

The subtraction requires independently derived negative and positive
calibration channels. Fitting (alpha) and (gamma) from the desired source
tower would fit the projector from the answer. Distinct source/detector packets
can have identical complete raw towers.

This exactly mirrors the requirement that Benincasa's contact score be typed
through its contact-normal channel before inversion.

## Instrument gate

Physical use requires traceable calibration ports, background and contrast
drift bounds, and tests of conditional independence and occupancy dependence
at every admitted coincidence order.

Run `uv run --with sympy python
research/flavor/checkers/wp338_confused_coincidence_tower.py` to regenerate the
exact audit.
