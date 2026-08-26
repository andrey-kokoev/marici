# Feedback observability kernel (WP276)

## One-port hostile model

Let the flavor-deviation module be two-dimensional and let the only admitted
sensor be

\[
C_1=\begin{pmatrix}1&0\end{pmatrix}.
\]

For arbitrary positive feedback gains collected in a column \(F\), the
measurement-based closed-loop generator with zero uncontrolled drift is

\[
A_{\mathrm{cl}}=-FC_1.
\]

The direction \(z=(0,1)^T\) satisfies

\[
C_1z=0,
\qquad
A_{\mathrm{cl}}z=0
\]

for every gain. Increasing gain cannot control information the sensor never
acquires. The observation Gram matrix is singular and the closed loop retains
a zero mode.

## Complementary source-derived port

Adjoin

\[
C_2=\begin{pmatrix}0&1\end{pmatrix}.
\]

The stacked sensor has rank two and Gram determinant one. With independently
positive diagonal gains, the closed-loop eigenvalues are \(-k_1\) and
\(-k_2\). Formal observability and damping are restored in this finite model.

This repair is admissible only if the complementary sensor is source-derived.
Writing down the missing row is algebraic span, not an executable flavor
measurement.

## Classification

The first nonfaithful arrow is from the physical deviation module to the
sensor record. Rank-one feedback is neither a full deviation selector nor a
complete physical instrument. Rank-two observation is necessary but still not
sufficient: actuator reachability, noise, latency, bandwidth, and stabilization
must be established in the same frame.

Run `uv run --with sympy python
research/flavor/checkers/wp276_feedback_observability_kernel.py` for the exact
sensor kernel, gain-independent blind direction, complementary Gram determinant,
and closed-loop spectrum.
