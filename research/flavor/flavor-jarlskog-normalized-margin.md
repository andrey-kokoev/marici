# Jarlskog normalization of the physical16 CP margin (WP109)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

For nondegenerate Hermitian Gram matrices with ordered eigenvalues
`u_i,d_i`, define

\[
\Delta_u=\prod_{i<j}(u_i-u_j),\qquad
\Delta_d=\prod_{i<j}(d_i-d_j).
\]

The exact Jarlskog identity in the present convention is

\[
\det[H_u,H_d]=2iJ\Delta_u\Delta_d.
\]

Hence the dimensionless weak-basis-invariant normalization

\[
\widehat C=
\frac{|\det[H_u,H_d]|}{2|\Delta_u\Delta_d|}=|J|
\]

provides a common physical16 CP coordinate whenever both spectra are
nondegenerate. The WP89 rational witness verifies the identity exactly, not
numerically.

This repairs the coordinate mismatch identified by WP108. The complete fitted
ensemble therefore has an observed normalized margin
`min |J|=3.1413288219332114e-5`. But that number is fitted evidence, not a
source-derived selector prediction. Feeding it back as the source lower bound
would fit the instrument threshold from the desired answer.

WP106's raw determinant bound can be normalized only after bounding the source
spectral factor `|Delta_u Delta_d|` on the same corridor. A lower raw
determinant bound needs an **upper** spectral-factor bound to imply a lower
`|J|` bound:

\[
|J|\ge C_{min}/(2D_{max})
\quad\text{if}\quad |\Delta_u\Delta_d|\le D_{max}.
\]

Classification: normalization is a faithful readout map, neither selector nor
rigidifier. Smallest exact falsifier is a degenerate spectrum, where one
discriminant vanishes and the normalized coordinate is undefined. Remaining
gate: derive a source-corridor spectral upper bound and canonical error in
`|J|`; keep the observed 1,210-sheet minimum solely as an external
falsification target.

Verification: `uv run --with sympy python
research/flavor/checkers/wp109_jarlskog_normalized_margin.py`.
