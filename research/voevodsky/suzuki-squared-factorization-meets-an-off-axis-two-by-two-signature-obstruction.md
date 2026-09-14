# A Suzuki-squared factorization meets an off-axis two-by-two signature obstruction

## Question

Can the unconditional Suzuki carrier be applied a second time to obtain either

\[
Q_W(\varphi)=\|T P_\varphi\|^2
\qquad\text{or}\qquad
Q_W(\varphi)=Q_S(\varphi)+\|R\varphi\|^2,
\]

where

\[
Q_S(\varphi)=\|P_\varphi\|_{L^2(\mathbb R)}^2?
\]

This note performs the first construction attempt using Suzuki's exact formulas.

## The unconditional first-stage operator

Write

\[
E(z)=\xi(1/2-iz)+\xi'(1/2-iz),
\qquad
\Theta(z)=E^\#(z)/E(z).
\]

On the real axis, `|Theta|=1` unconditionally. Consequently multiplication by `Theta`, reflection, and Fourier transform define Suzuki's unconditional isometric involution

\[
K=\mathcal F^{-1}M_\Theta J\mathcal F
\]

on `L^2(R)`. Also, the explicitly completed source formula defines

\[
P_D:C_c^\infty(\mathbb R)\longrightarrow L^2(\mathbb R),
\qquad Q_S(\varphi)=\|P_D\varphi\|_2^2.
\]

Thus the first Suzuki stage is already a legitimate positive operator factorization

\[
Q_S=P_D^*P_D.
\]

The missing operation is not another norm. It is the replacement of the ambient boundary metric by the arithmetic zero-pairing metric.

## Off-axis zero pair gives the minimal obstruction

Let `rho` be a nonreal zero coordinate of `xi(1/2-iz)`. Functional-equation symmetry supplies the conjugate partner `bar(rho)`. On tests localized so that only the two evaluations at this pair survive, the Weil form has, up to a positive multiplicity and convention, the Hermitian block

\[
J_\rho=
\begin{pmatrix}
0&m_\rho\\
m_\rho&0
\end{pmatrix}.
\]

Indeed Suzuki's converse to Theorem 4.4 chooses test values at a nonreal zero pair so that the Weil/screw value is negative. Diagonalizing the displayed block gives eigenvalues

\[
+m_\rho,
\qquad -m_\rho.
\]

By contrast, every second-stage Hilbert construction from the Suzuki feature vector has a block of the form

\[
G_\rho=T_\rho^*T_\rho\succeq0.
\]

No choice of Hilbert operator `T_rho` can satisfy `G_rho=J_rho`. This is the smallest possible obstruction: one off-axis conjugate pair already requires a Krein signature `(1,1)`, whereas a squared norm has signature `(2,0)`, `(1,0)`, or `(0,0)`.

## The additive positive-remainder ansatz also fails off RH

Suppose one had the source identity

\[
Q_W=Q_S+\|R\varphi\|^2.
\]

The right-hand side is nonnegative for every test. But Suzuki's localized test at an off-axis zero makes the left-hand side negative. Hence such an identity is incompatible with every off-axis zero configuration. Equivalently, constructing it unconditionally would itself prove RH; it cannot follow from the formal unitarity `|Theta|=1` on the boundary.

At block level the obstruction is immediate:

\[
J_\rho-G_\rho\not\succeq0
\]

for every `G_rho >= 0`, because on a negative eigenvector `v` of `J_rho`,

\[
v^*(J_\rho-G_\rho)v
=-m_\rho\|v\|^2-v^*G_\rho v<0.
\]

Thus the proposed positive remainder cannot hide in cross terms or in a larger Hilbert space.

## Why boundary unitarity does not supply the second stage

The identity `|Theta(x)|=1` for real `x` makes `M_Theta` unitary on boundary `L^2`. What is needed for Suzuki's Parseval step is stronger: `Theta` must be inner in the upper half-plane, so that

\[
K(\Theta)=H^2\ominus\Theta H^2
\]

is the appropriate model space and the zero-indexed functions form an orthonormal basis. Upper-half-plane innerness is the analytic condition carrying the zero-location theorem. Applying `K` twice only gives the tautology

\[
K^2=I;
\]

it does not imply Hardy-space invariance or positivity of the model-space kernel.

The canonical candidate second-stage kernel is the de Branges--Rovnyak kernel

\[
k_\Theta(z,w)
=
\frac{1-\Theta(z)\overline{\Theta(w)}}{-i(z-\bar w)}.
\]

A Hilbert factorization of this kernel exists exactly when `Theta` is Schur in the upper half-plane. In the present completed-zeta specialization, that is the same missing Hermite--Biehler/zero-location gate. Therefore this candidate correctly reproduces the desired geometry but is not unconditionally positive.

## What can still be constructed unconditionally

There is an unconditional **Krein** factorization. Pair each off-axis orbit in a two-dimensional space with fundamental symmetry

\[
\mathcal J_\rho=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Then the arithmetic form has the schematic realization

\[
Q_W(\varphi)
=\langle A\varphi,\mathcal J A\varphi\rangle_{\mathcal H},
\]

where `A` is the zero-evaluation map and `mathcal J` is positive on real-zero sectors but has signature `(1,1)` on every off-axis pair. This preserves the exact cross-zero polarization that an ordinary square erases.

However, passing from this Krein factorization to a Hilbert factorization requires proving that the negative spectral subspace is absent. That statement is RH.

## Consequence for the Gaussian observer

For a fixed finite-dimensional Gaussian family, a useful non-tautological computation remains possible. Form the two Gram matrices

\[
G_S=(\langle P_D\varphi_i,P_D\varphi_j\rangle),
\qquad
G_W=(W(D\varphi_i*D\varphi_j^*)).
\]

Then diagonalize the certified interval enclosure of

\[
G_W-G_S.
\]

A positive remainder on one compact parameter box would prove local observer positivity there. It cannot extend to all tests merely from the Suzuki construction, because an off-axis zero would force a negative direction in the two-point localization limit.

## Disposition

The direct `Suzuki squared` construction closes only in a Krein space:

\[
\boxed{
Q_W=\langle A\varphi,\mathcal J A\varphi\rangle,
\quad
\mathcal J^2=I,
}
\]

not as an unconditional Hilbert norm. The first irreducible obstruction is the `(1,1)` signature of one off-axis conjugate zero pair. The only viable positive continuation is finite-family/finite-width defect certification, not universal squaring.
