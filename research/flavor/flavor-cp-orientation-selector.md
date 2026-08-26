# CP-orientation selector (WP327)

## Spontaneous branch formation

Represent the conjugate WP326 branches by a CP-odd coordinate (c). The
CP-even source potential

\[
V_0(c)=(c^2-c_0^2)^2
\]

has two stable minima at (c=\pm c_0), with equal curvature (8c_0^2). It
selects a proper two-point vacuum fiber but does not select its CP orientation.

This distinction persists even if a CP-sensitive instrument identifies which
domain was observed. Readout of a realized branch is not a theorem that the
source uniquely selected that branch.

## Minimal orientation bias

Adding

\[
V_\epsilon(c)=V_0(c)-\epsilon c
\]

splits the two branch energies by (2c_0\epsilon). A positive bias favors the
positive branch, and reversing the bias reverses the selection. The bias is
therefore a genuine sign selector, but it carries new CP-odd source authority.

## Disposition

The CP-even theory is a selector of a finite conjugate fiber, not a singleton
`physical16` point. The biased theory can select an orientation only after the
origin, sign, and magnitude of its odd coefficient are independently derived.
A cosmological domain history would instead define a preparation channel and
must be typed as such.

Run `uv run --with sympy python
research/flavor/checkers/wp327_cp_orientation_selector.py` to regenerate the
exact audit.
