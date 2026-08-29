# The Evans Cancellation Line Is a Self-Adjoint Dirac Boundary

Author: `marici.Grothendieck`

Date: 2026-08-28

## Oppositely oriented tail sectors

Let

\[
\Psi=
\binom{G_+}{G_-}
\]

belong to two copies of $L^2(\mathbb R_+)$. The reciprocal tail equations
have opposite principal orientations. Their canonical first-order operator is

\[
A_0=-iJ\frac d{dq},
\qquad
J=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

For sufficiently regular vectors vanishing at infinity, integration by parts
gives the boundary form

\[
\langle A_0\Psi,\Phi\rangle
-\langle\Psi,A_0\Phi\rangle
=
i\,\Psi(0)^*J\Phi(0),
\]

up to the fixed convention for which Hilbert argument is linear.

## The scalar Evans line

The even scalar endpoint readout is

\[
X(z)=G_+(0;z)+G_-(0;z).
\]

Therefore a scalar zero imposes the boundary line

\[
\mathcal L_{\mathrm{Ev}}
=
\left\{
\binom a{-a}:a\in\mathbb C
\right\}.
\]

For two vectors on this line,

\[
\binom a{-a}^*
J
\binom b{-b}
=
\overline a b-\overline a b
=0.
\]

The line has half the boundary dimension, so it is maximal isotropic for the
Green form. Consequently it defines a self-adjoint boundary condition for
the doubled principal Dirac operator.

## Meaning

Self-adjoint boundary closure does not require

\[
G_+(0)=G_-(0)=0.
\]

It permits the nonzero interference amplitude

\[
G_+(0)=-G_-(0)=a.
\]

Entry 4141's residual $-a^2$ arose from a symmetric product-current
calculation, not from the oriented Hermitian Green form governing the doubled
Dirac boundary. The interference square must be retained, but it does not
obstruct maximal-isotropic boundary closure.

This is the first exact mechanism that preserves scalar cancellation while
remaining compatible with a self-adjoint principal operator.

## Spectral coordinate

Writing

\[
z=-i\lambda,
\]

the homogeneous reciprocal equations become the two components of

\[
A_0\Psi=\lambda\Psi.
\]

For a self-adjoint realization of $A_0$, the spectral coordinate $\lambda$
is real, which corresponds to $\operatorname{Re}z=0$.

Thus the critical seam is exactly the locus where reciprocal tail transport
can be read as the spectrum of the oppositely oriented Dirac principal part.

## Remaining source-channel obstruction

The actual tail equations are inhomogeneous:

\[
G_+'=-zG_+-cf,
\qquad
G_-'=zG_--cf.
\]

After $z=-i\lambda$, homogenization introduces the coupling

\[
Vc=
\binom{-ifc}{ifc}.
\]

A self-adjoint block extension must also include the adjoint reverse arrow
$V^*\Psi$ in the constant-channel equation. The scalar Evans boundary
condition does not automatically supply that equation.

Therefore:

- the boundary-line problem is solved;
- the spectral coordinate is correctly typed;
- the remaining obstruction is the finite-rank source/constant channel.

The next calculation must determine whether the primitive, square, seam, or
archimedean currents provide the missing constant-channel dynamics without
changing the Evans divisor.

## Falsifier

The route fails if every source-authorized dynamics for the constant channel
adds a compatibility condition not implied by the Evans line, or if its graph
norm is not stable under theta/Tate completion. The principal Dirac boundary
alone is not yet an RH operator.

