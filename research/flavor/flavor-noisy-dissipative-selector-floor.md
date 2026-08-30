# Noisy dissipative selector floor (WP274)

## Stochastic preparation

Complete WP273's relaxation channel with source noise:

\[
dz=-\gamma z\,dt+\sqrt{2D}\,dW_t.
\]

For initial variance \(v_0\), the exact variance is

\[
v(t)=v_0e^{-2\gamma t}
+\frac{D}{\gamma}\left(1-e^{-2\gamma t}\right),
\]

with stationary floor

\[
v_*=\frac{D}{\gamma}.
\]

The channel prepares a distribution rather than a distinguished point. To
reach mean-square tolerance \(\epsilon^2\) from above at finite time, the
strict condition is

\[
\frac{D}{\gamma}<\epsilon^2.
\]

## Exact packets

Freeze \(\epsilon=1/100\), \(\gamma=1\), and \(v_0=1\).

- With \(D=1/40000\), the floor is below tolerance and runtime
  \(\tfrac12\log13333\) reaches \(v=1/10000\) exactly.
- With \(D=1/10000\), the floor equals tolerance. Every finite time retains
  positive excess \((9999/10000)e^{-2t}\).
- With \(D=1/5000\), the floor exceeds tolerance and no runtime can pass.

## Classification

Finite noisy dissipation is a conditional approximate distribution selector,
not an exact point selector. Its authority requires an independently calibrated
noise floor strictly below the physical tolerance, alongside the damping,
initial-domain variance, runtime, stabilization, and readout metric.

Active cooling, non-Gaussian reservoirs, feedback, or error correction may
change the floor, but each is a new source-generated operation with its own
resource contract.

Run `uv run --with sympy python
research/flavor/checkers/wp274_noisy_dissipative_selector_floor.py` for the
exact variance solution, passing runtime, borderline obstruction, and failing
noise packet.
