# Coincidence-tower robustness (WP339)

## Contrast conditioning

WP338 proves algebraic invertibility for every nonzero detector contrast. WP339
tests whether that inverse is experimentally stable. In the background-free
specialization, the order-(j) response is simply

\[
r_j=\gamma^j u_j.
\]

The sixth-order inverse therefore has gain

\[
\frac{\partial u_6}{\partial r_6}=\gamma^{-6},
\]

and its Gram eigenvalue is (gamma^{12}). The logarithmic sensitivity to
contrast calibration is

\[
\frac{\partial\log u_6}{\partial\log\gamma}=-6.
\]

## Exact benchmarks

At contrast (1/2), sixth-order detected-moment error is amplified by 64. At
contrast (1/10), it is amplified by one million. The gain diverges as contrast
approaches zero.

False-positive background subtraction can add cancellation and calibration
errors, so this background-free result is a baseline obstruction rather than a
worst-case bound for the full WP338 channel.

## Physical gate

Robust faithfulness needs an independently certified contrast floor, noise and
calibration covariance at every coincidence order, and a minimum source-law
separation exceeding the propagated inverse error. Bare nonzero determinant is
insufficient.

Run `uv run --with sympy python
research/flavor/checkers/wp339_coincidence_tower_robustness.py` to regenerate
the exact conditioning audit.
