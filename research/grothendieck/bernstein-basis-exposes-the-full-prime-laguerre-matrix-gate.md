# Bernstein basis exposes the full prime Laguerre matrix gate

## Question

Does positivity of every near-null diagonal direction `(1-y)^m` control the prime quadratic form on arbitrary polynomials?

## Claim boundary

No. In the basis `e_m(y)=(1-y)^m`, every matrix entry is a high difference, but off-diagonal entries involve both even and odd orders. The termwise Laguerre sign theorem controls selected diagonal entries only. Full prime positivity would require a matrix inequality for a coupled Laguerre kernel.

## Exact basis transform

Let

\[
e_j(y)=(1-y)^j,
\qquad 0\le j<N.
\]

For any scalar heat kernel `F`, polarizing the difference Hankel form gives

\[
\mathcal Q_F(e_i,e_j)
=\Delta_h^{i+j+1}F(t).
\]

Indeed, multiplication by `(1-y)^i` and `(1-y)^j` contributes `i+j` finite differences, while the endpoint-free moment contributes one more. Therefore the Newton/Bernstein congruence transforms the full matrix into

\[
M_F(t,h)=
\left(
\Delta_h^{i+j+1}F(t)
\right)_{0\le i,j<N}.
\]

The near-null theorem treats only its diagonal entries, whose orders `2i+1` are odd.

## Prime Laguerre entries

For one prime displacement `a=log n`, set `c=a^2/4` and

\[
\phi_c(s)=s^{-1/2}e^{-c/s}.
\]

The prime atom contributes

\[
-\frac{\Lambda(n)n^{-1/2}}{2\sqrt\pi}
\Delta_h^q\phi_c(t),
\qquad q=i+j+1.
\]

Using the finite-difference cube and the derivative formula gives an exact integral with

\[
L_q^{-1/2}\!\left(
\frac{c}{t+u_1+\cdots+u_q}
\right).
\]

When `q` is odd and the argument lies beyond the largest Laguerre root, the completed prime diagonal contribution is nonnegative. For even `q`, the prefactor and Laguerre tail have the opposite parity needed for an off-diagonal entry; an entrywise sign has no implication for positive semidefiniteness.

## First matrix obstruction

The first transformed prime block is

\[
\begin{pmatrix}
\Delta_hK_P(t)&\Delta_h^2K_P(t)\\
\Delta_h^2K_P(t)&\Delta_h^3K_P(t)
\end{pmatrix}.
\]

The diagonal Laguerre theorem may make the first and third entries nonnegative, but positivity additionally requires

\[
\Delta_hK_P(t)\,\Delta_h^3K_P(t)
-\bigl(\Delta_h^2K_P(t)\bigr)^2\ge0.
\]

No prior termwise sign estimate proves this determinant. The same Schur defect recurs: positive diagonal observers do not control their couplings.

## Frequency interpretation

The entry of order `q` has Fourier envelope

\[
e^{-t\xi^2}(1-e^{-h\xi^2})^q,
\]

with saddle

\[
\xi_q^2
=\frac1h\log\left(1+\frac{qh}{t}\right).
\]

Different matrix entries therefore probe different nearby frequency windows. A full proof needs positivity of the regularized prime cosine distribution across these coupled envelopes, not independent estimates at one saddle.

## Strongest falsification attempt

Diagonal positivity for every basis vector is still insufficient: a Hermitian matrix can have positive diagonal and negative determinant. Absolute bounds on even-order cross entries reintroduce the conditioning loss unless they are compared with the geometric mean of the adjacent odd-order margins.

## Disposition

The next nonredundant target is the rank-two Turán inequality for the prime-plus-gamma high-difference sequence in the Bernstein basis. Do not promote the near-null diagonal rank window to a matrix rank window.