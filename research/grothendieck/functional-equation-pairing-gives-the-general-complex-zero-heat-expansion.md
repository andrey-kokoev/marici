# Functional-equation pairing gives the general complex-zero heat expansion

## Question

What exact classical identity supplies the general-complex-zero heat expansion required by the sampled-cone theorem?

## Paired logarithmic derivative

Write

\[
s=\frac12+y,
\qquad x=y^2,
\qquad a_\rho=\rho-\frac12,
\qquad \lambda_\rho=-a_\rho^2.
\]

The functional equation pairs every zero `rho` with `1-rho`, whose centered coordinates are `a_rho` and `-a_rho`. Their logarithmic-derivative terms combine as

\[
\frac1{y-a_\rho}+\frac1{y+a_\rho}
=
\frac{2y}{y^2-a_\rho^2}.
\]

After division by `2y`, the paired squared-resolvent contribution is

\[
\frac1{x-a_\rho^2}
=
\frac1{x+\lambda_\rho}.
\]

Thus the completed squared logarithmic derivative

\[
B'(x)
=
\frac{\xi'/\xi(1/2+\sqrt x)}{2\sqrt x}
\]

has the paired partial-fraction expansion

\[
B'(x)=\sum_{[\rho]}\frac{m_\rho}{x+\lambda_\rho},
\]

with one representative per functional-equation pair and the summation prescription inherited from the symmetric Hadamard product.

## Heat inversion

For `x` to the right of every pole,

\[
\frac1{x+\lambda_\rho}
=
\int_0^\infty e^{-xt}e^{-t\lambda_\rho}\,dt.
\]

Therefore inverse Laplace transformation gives the general zero-side heat identity

\[
H(t)=\sum_{[\rho]}m_\rho e^{-t\lambda_\rho},
\qquad
\lambda_\rho=-(\rho-1/2)^2.
\]

No assumption `Re(rho)=1/2` is made. Conjugate zeros give conjugate heat factors, so the completed sum is real.

## Convergence and decay

Inside the critical strip,

\[
\operatorname{Re}\lambda_\rho
=\gamma^2-(\beta-1/2)^2
\ge\gamma^2-1/4.
\]

A cited zero-free compact region below ordinate `1/2`, together with `N(T)=O(T log T)`, gives a uniform `delta>0` and normal convergence of the heat series for `t>=t_0>0`. It also gives `H(t)->0` and locally uniform interchange with finite differences and moment generating series.

## Normalization obligation

The only delicate point is counting: the Hadamard sum, functional-equation pairs, conjugate pairs, and the repository convention for positive ordinates must assign the same multiplicities as the endpoint--gamma--prime inverse Laplace kernel. This must be fixed once in a source contract.

No additional completed term may cancel an isolated zero pole after the exact identity is established: endpoint, gamma, and prime pieces are the arithmetic presentation of the same meromorphic `B'(x)`, not extra zero-side summands.

## Consequence

The nine source obligations in the sampled-cone theorem largely collapse to one classical bridge:

1. establish the symmetrically paired Hadamard partial fraction for `B'(x)` with exact multiplicities;
2. justify inverse Laplace interchange using the zero count and positive real-part bound;
3. identify it with the already derived endpoint--gamma--prime Laplace transform.

Once this bridge is cited, general-complex expansion, local uniform convergence, unconditional decay, grouped residues, and absence of completed-term cancellation follow together.

## Boundary

This packet derives the algebraic pairing but does not supply bibliographic citations or a complete Hadamard convergence proof. Those are the first missing source objects.

## Disposition

Replace nine loosely separated analytic obligations by a single source-normalized paired-Hadamard-to-Laplace theorem. Audit multiplicity conventions before any further positivity claim.