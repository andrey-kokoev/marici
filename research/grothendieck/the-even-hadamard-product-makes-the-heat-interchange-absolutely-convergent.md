# The even Hadamard product makes the heat interchange absolutely convergent

## Question

Can the infinite paired-Hadamard and inverse-Laplace steps be proved without a conditionally rearranged genus-one zero sum?

## Even completed function

Put

\[
\Xi(y)=\xi(1/2+y).
\]

The functional equation makes `Xi` even. Its zeros occur in pairs `a` and `-a`, where

\[
a=\rho-1/2.
\]

The classical zero count implies

\[
\sum_{[\rho]}\frac{m_\rho}{|a_\rho|^2}<\infty.
\]

Therefore the paired product

\[
\Xi(y)=\Xi(0)
\prod_{[\rho]}
\left(1-\frac{y^2}{a_\rho^2}\right)^{m_\rho}
\]

converges normally on compact sets. Any zero-free exponential quotient allowed by the order-one Hadamard theorem is `exp(A+By)`; evenness forces `B=0`, and evaluation at zero fixes the constant.

This paired product avoids the individual genus-one regularizers `exp(s/rho)`. No conditionally rearranged linear zero sum is needed.

## Logarithmic derivative

Away from zeros, normal differentiation gives

\[
\frac{\Xi'(y)}{\Xi(y)}
=
\sum_{[\rho]}
\frac{2ym_\rho}{y^2-a_\rho^2}.
\]

With `x=y^2` and

\[
\lambda_\rho=-a_\rho^2,
\]

we obtain the absolutely locally convergent squared-resolvent identity

\[
\frac{\xi'/\xi(1/2+\sqrt x)}{2\sqrt x}
=
\sum_{[\rho]}
\frac{m_\rho}{x+\lambda_\rho}.
\]

Each index is one orbit under `rho -> 1-rho`, with multiplicity retained. On RH this orbit is the conjugate pair associated with one positive ordinate.

## Absolute Laplace interchange

Use the critical-strip bound

\[
\operatorname{Re}\lambda_\rho
\ge\gamma^2-1/4
\]

and a classical zero-free compact region giving a uniform positive lower bound `delta`. For `x>0`,

\[
\sum_{[\rho]}m_\rho
\int_0^\infty
 e^{-xt}|e^{-t\lambda_\rho}|dt
=
\sum_{[\rho]}
\frac{m_\rho}{x+\operatorname{Re}\lambda_\rho}
<\infty.
\]

The final convergence follows again from the zero count. Tonelli applied to absolute values therefore permits termwise Laplace transformation:

\[
\int_0^\infty e^{-xt}
\sum_{[\rho]}m_\rho e^{-t\lambda_\rho}dt
=
\sum_{[\rho]}\frac{m_\rho}{x+\lambda_\rho}.
\]

Laplace uniqueness identifies the general-complex-zero heat sum with the endpoint--gamma--prime inverse transform already derived from the Euler-product half-plane.

## Consequences

This simultaneously supplies:

- the exact complex-zero expansion;
- locally uniform convergence for every positive heat scale;
- unconditional completed heat decay;
- finite-difference and moment-series interchange;
- nonzero grouped residues with multiplicity;
- absence of additional completed terms on the zero side.

## Source boundary

A publication-ready theorem still needs bibliographic citations for the order-one Hadamard factorization, the zero count, the low-ordinate zero-free region, and Laplace uniqueness. The mathematical convergence mechanism and counting convention are now explicit.

## Disposition

Use the even paired product in `y`, not the unpaired genus-one product in `s`. It turns the remaining infinite bridge into an absolutely convergent theorem and closes the normalization contract up to classical citations.