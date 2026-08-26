# CP-detector calibration (WP329)

## Raw detector channel

Let (p) be the true positive-domain probability, (alpha) the false-positive
rate, and (delta) the false-negative rate. The observed positive frequency is

\[
q=\alpha+(1-\alpha-\delta)p.
\]

Raw repeated counts identify only (q). Their response to
((p,\alpha,\delta)) has rank one and a two-dimensional kernel.

## Calibration ports

A known-negative preparation measures (q_0=\alpha), while a known-positive
preparation measures (q_1=1-\delta). The response Jacobian of
((q,q_0,q_1)) has determinant

\[
-(1-\alpha-\delta).
\]

Away from zero contrast it is full rank, and

\[
p=\frac{q-q_0}{q_1-q_0}.
\]

At (alpha+\delta=1), the detector is exactly blind to (p).

## Typing

The two known-domain preparations are reference ports. They create a new
calibrated experiment and can make the detector readout faithful to (p).
They do not select (p), nor do they remove WP328's two-dimensional kernel in
the source parameters ((\beta,\epsilon,c_0)).

Physical admission requires traceable calibration preparations, uncertainty
and drift bounds, and a nonzero contrast margin on the same domain history.

Run `uv run --with sympy python
research/flavor/checkers/wp329_cp_detector_calibration.py` to regenerate the
exact audit.
