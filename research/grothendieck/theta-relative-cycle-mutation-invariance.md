# Relative-cycle mutation invariance of the cone numerator

## Coordinate-free observable

Let \(H_z\) be the relative homology group appropriate to the completed
Mellin integrand at a parameter \(z\), and let

\[
I_z(\Gamma)=\int_\Gamma x^{z/2}G(x)\,\frac{dx}{x},
\qquad
J_z(\Gamma)=\int_\Gamma (\log x)x^{z/2}G(x)\,\frac{dx}{x}.
\]

Both are linear functionals on \(H_z\). For
\(\lambda=\beta-i\alpha\), define the real quadratic functional

\[
\boxed{
Q_z(\Gamma)=
\Re\!\left(\lambda J_z(\Gamma)
\overline{I_z(\Gamma)}\right).
}
\]

Whenever \(I_z(\Gamma)\ne0\),

\[
\frac{Q_z(\Gamma)}{|I_z(\Gamma)|^2}
=
\beta\Re\frac{J_z(\Gamma)}{I_z(\Gamma)}
+\alpha\Im\frac{J_z(\Gamma)}{I_z(\Gamma)}.
\]

Thus the desired cone readout belongs to the total relative cycle, not to a
chosen thimble decomposition.

## Mutation-invariance theorem

Choose a thimble basis \(\gamma=(\gamma_1,\ldots,\gamma_r)^T\), and write the
physical cycle as

\[
\Gamma=n^T\gamma,
\qquad n\in\mathbb Z^r.
\]

Let a Picard--Lefschetz wall crossing replace it by

\[
\gamma'=A\gamma,
\qquad A\in GL_r(\mathbb Z).
\]

The same cycle has coefficients

\[
n'=A^{-T}n.
\]

If \(p=(I_z(\gamma_j))_j\) and \(q=(J_z(\gamma_j))_j\), then

\[
p'=Ap,
\qquad q'=Aq,
\]

and consequently

\[
n'^Tp'=n^Tp,
\qquad n'^Tq'=n^Tq.
\]

Therefore

\[
\boxed{Q_z(n'^T\gamma')=Q_z(n^T\gamma).}
\]

This is exact. It does not assume positivity of individual thimbles, common
phase, orthogonality, or a fixed number of contributors.

Equivalently, put

\[
H_{jk}=\frac12\left(
\lambda q_j\overline{p_k}
+\overline{\lambda}\,p_j\overline{q_k}
\right).
\]

Then \(H\) is Hermitian and

\[
Q_z(\Gamma)=n^TH\overline n.
\]

Under mutation,

\[
H'=AH A^*,
\qquad n'=A^{-T}n,
\]

so the quadratic value is unchanged. This is the finite-dimensional
correspondence object behind all self and cross terms in a multi-thimble
expansion.

## Consequence for Stokes walls

A wall may change:

- the thimble basis;
- the number of basis edges used by a convenient presentation;
- the signs and sizes of individual self terms; and
- the allocation of cross interference.

It cannot change \(Q_z(\Gamma)\) merely by changing coordinates for the same
relative cycle. Hence the first two-to-three-thimble mutation is not a new
positivity obligation. Its mathematical obligation is the integral mutation
identity and correct reconstruction of \(\Gamma\). Once those hold, the cone
value is inherited continuously from the physical contour.

The numerical three-edge reconstruction at \((a,b)=(1/2,9.66)\) is evidence
for precisely this identification: it reproduces the direct contour and its
positive cone within the path-quadrature error.

## What remains nontrivial

Mutation invariance is not a proof of global positivity. It removes artificial
wall-by-wall discontinuities, but one must still prove that along the
Gauss--Manin continuation of the physical class

\[
Q_z(\Gamma_z)>0
\]

throughout the target parameter domain, and that \(I_z(\Gamma_z)\ne0\).
In fact the second statement is not an additional hypothesis: if
\(I_z(\Gamma_z)=0\), then the definition forces \(Q_z(\Gamma_z)=0\).
Consequently strict denominator-free positivity simultaneously proves the
cone inequality wherever the quotient is defined and excludes every zero of
the Mellin transform in the target domain. This is exactly where the
Riemann-zero problem enters, and no nonvanishing premise may be assumed.

The sharper program is therefore:

1. construct the physical relative class and its integral wall mutations;
2. prove a chamberwise differential or integral positivity law for the
   basis-free quantity \(Q_z(\Gamma_z)\);
3. use mutation invariance to sew those laws across Stokes walls.

If these steps cover the required outer domain, strict positivity itself
supplies the zero exclusion.

There is now an even more compressed formulation. On the undecomposed
physical contour, \(Q=(\beta\partial_a-\alpha\partial_b)|B|^2/2\). Thus the
same target is a Lyapunov law for the scalar theta energy along a fixed
source-independent vector field. See
`theta-denominator-free-energy-flow.md`.

## Falsifiers

The mechanism fails if any wall computation yields one of the following:

1. the proposed post-wall chain is not the same relative class;
2. its coefficients are not related by an integral Picard--Lefschetz
   transformation;
3. a moving singularity invalidates the relative Gauss--Manin continuation;
4. \(Q_z(\Gamma_z)\) reaches zero inside a chamber.

The first three are topological falsifiers. The last is the analytic one; it
includes any transform zero because such a zero necessarily makes \(Q_z=0\).
