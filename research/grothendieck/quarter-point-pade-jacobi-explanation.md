# Jacobi compression is the Stieltjes--Pade pole extractor

The quarter-point expansion is

\[
 S(1/4+h)=\sum_{k\ge0}(-1)^kA_kh^k.
\]

Given moments through `A_(2n-1)`, the `n`-node Gaussian quadrature measure
matches those moments and has resolvent

\[
 R_n(h)=\sum_{j=1}^n\frac{w_j}{1+h u_j}.
\]

Consequently `R_n` is the `[n-1/n]` Stieltjes--Pade approximant to `S`, and
its poles are

\[
 h_j^{(n)}=-u_j^{-1}.
\]

The Jacobi eigenvalues and Pade poles are therefore the same construction in
operator and analytic languages. The blind first-ordinate estimate comes from
the nearest negative Pade pole, not from fitting or importing a zero table.

For `n=5`, numerical Gaussian weights reconstruct all ten source moments
`A_0,...,A_9` with maximum relative residual below `3e-15`; the residual is
ordinary eigensolver rounding, while the moment inputs themselves are
interval-certified.

This supplies a Deutschian explanation of the rapid spectral-edge recovery:
the completed source jet fixes a rational resolvent whose nearest pole must
approximate the nearest true singularity. Positivity upgrades generic Pade
approximation to a nested real Jacobi/Ritz process with directional edge
convergence.

## Scope

Finite Pade matching does not establish that the limiting function is
Stieltjes; that is the all-order RH-equivalent claim. The moment-reconstruction
regression is numerical, and RH is not proved.

## Durable verification

- Checker: `checkers/quarter_point_pade_gaussian_identity.py`
- Result: `results/quarter-point-pade-gaussian-identity.json`
