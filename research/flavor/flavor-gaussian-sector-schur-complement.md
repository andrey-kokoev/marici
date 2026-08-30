# Gaussian-sector Schur-complement theorem (WP265)

## General finite mediator sector

Let \(S\) be any finite real mediator vector with positive-definite quadratic
form \(K\), coupled linearly to the nonnegative mixing invariant \(x\):

\[
V(S,x)=\frac12S^TKS-xg^TS.
\]

Eliminating the mediator gives

\[
S_*=K^{-1}gx,
\qquad
V_{\mathrm{eff}}(x)=-\frac12x^2g^TK^{-1}g.
\]

If \(K=LL^T\) is its Cholesky factorization, then

\[
g^TK^{-1}g=\lVert L^{-1}g\rVert^2\geq0.
\]

Hence the induced quadratic coefficient is always nonpositive, and it is
strictly negative for nonzero coupling. Mediator mixing cannot reverse the
WP264 sign.

## Exact mixed witness

For

\[
K=\begin{pmatrix}4&1\\1&3\end{pmatrix},
\qquad
g=\begin{pmatrix}1\\2\end{pmatrix},
\]

the positive principal minors are \(4\) and \(11\), while tree-level
elimination produces coefficient \(-15/22\) and curvature \(-15/11\).

## Consequence and scope

No finite stable Gaussian mediator sector with real linear couplings can
generate WP262's positive commutator-square stabilizer. The full class closes
by the Schur-complement sign theorem, not merely by the one-field example.

Progress requires a direct positive operator, nonlinear mediator interaction,
loop or nonperturbative contribution, or a constrained auxiliary construction.
Its sign and normalization must be derived independently. The theorem does not
cover those non-Gaussian additions.

Run `uv run --with sympy python
research/flavor/checkers/wp265_gaussian_sector_schur_complement.py` for the
exact diagonal family, mixed witness, Cholesky identity, curvature, and hostile
positive-sign claim.
