# Cubic separator corridor: WP696

## Continuum theorem

WP695 is not an isolated rational coincidence. On the symmetric radial family

\[
\lambda_h=\lambda_x=\lambda,
\qquad H=X=v,
\qquad \lambda_p=\pm p,
\]

the common two-point spectrum is

\[
m_L^2=2v^2(\lambda-p),
\qquad
m_H^2=2v^2(\lambda+p).
\]

Strict stability requires \(p<\lambda\). The heavy-to-two-light channel is
open exactly when

\[
m_H>2m_L
\quad\Longleftrightarrow\quad
5p>3\lambda.
\]

Thus the nonempty corridor is

\[
\frac35<\frac{p}{\lambda}<1.
\]

Throughout it, the branch cubics are

\[
g_{HLL}^{(+)}=\sqrt2v(3\lambda-p)>0,
\qquad
g_{HLL}^{(-)}=0.
\]

The ideal identical-particle partial width on the positive branch is

\[
\Gamma_{H\to LL}^{(+)}
=\frac{(g_{HLL}^{(+)})^2}{32\pi m_H}
\sqrt{1-\frac{4m_L^2}{m_H^2}},
\]

while the negative branch has zero tree-level width on this slice.

## Boundaries and authority

At \(p/\lambda=3/5\), phase space closes. At \(p/\lambda=1\), the light
radial mode loses strict stability. These are the exact corridor falsifiers.

WP696 supplies a continuum source-derived branch separator and an ideal rate
prediction on a declared symmetric slice. It identifies rather than selects.
The zero on the negative branch is symmetry-slice exact; persistence under
asymmetric completion, finite widths, and loops remains to be proved. A
physical instrument additionally needs calibrated visible cascade efficiency,
resolution, and backgrounds.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp696_cubic_separator_corridor.py

Generated result: results/wp696_cubic_separator_corridor.json.
