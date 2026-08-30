# Log-instrument robust margin (WP332)

## Calibrated log coordinates

On the strictly positive WP331 domain, use logarithmic source coordinates

\[
(\log\beta,\log\epsilon,\log c_0)
\]

and calibrated logarithmic readouts derived from (A), (C), and (L). Their
constant local response matrix is

\[
J=
\begin{pmatrix}
1&0&0\\
0&0&1\\
1&1&1
\end{pmatrix}.
\]

Its Gram spectrum is

\[
\left\{2-\sqrt3,1,2+\sqrt3\right\},
\]

so

\[
\sigma_{\min}(J)=\sqrt{2-\sqrt3}.
\]

## Robust gate

Any additive perturbation of the response Jacobian whose spectral norm is
strictly smaller than this value preserves full rank. This replaces the bare
nonzero-determinant statement with a uniform conditioning certificate on the
positive log domain.

The certificate does not cover (epsilon=0), where the log-odds coordinate
vanishes and its logarithm is undefined. Zero or sign-indefinite bias requires
a separate nonlogarithmic chart.

## Physical status

The remaining task is experimental: translate calibration, sampling,
freeze-out mismatch, drift, and detector errors into a justified response
perturbation norm below the exact margin. The algebra does not establish that
such an instrument exists, and identification still does not imply selection.

Run `uv run --with sympy python
research/flavor/checkers/wp332_log_instrument_robust_margin.py` to regenerate
the exact margin audit.
