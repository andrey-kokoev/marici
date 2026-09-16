# Coercivity and the skew history resolvent bound the complement-energy transfer off the seam

## Setup

Let \(A\) be the closed skew-adjoint history generator, let \(R_H(z)=(A-z)^{-1}\), let \(B_\Sigma:U\to H\) be the bounded centered arithmetic incidence, and let \(V:\mathbb C_\theta\to H\) be the theta forcing column.

Assume that the arithmetic complement \(Q_U(z)\) is positive on the selected chart and satisfies \(Q_U(z)\ge\delta_K I\) for every \(z\) in a compact set \(K\).

Assume that \(K\) stays a positive distance \(\varepsilon_K\) from the critical seam, so \(|\operatorname{Re}z|\ge\varepsilon_K\) on \(K\).

## Estimate

Skew-adjointness gives

\[
\left\|R_H(z)\right\|
\le
\frac{1}{|\operatorname{Re}z|}
\le
\frac{1}{\varepsilon_K}.
\]

Complement coercivity gives

\[
\left\|Q_U(z)^{-1/2}\right\|
\le
\delta_K^{-1/2}.
\]

Therefore

\[
\left\|
Q_U(z)^{-1/2}
B_\Sigma^\dagger
R_H(z)V
\right\|
\le
\frac{\left\|B_\Sigma\right\|\left\|V\right\|}
{\sqrt{\delta_K}\,\varepsilon_K}.
\]

If the finite-cutoff incidences satisfy \(\sup_X\|B_{\Sigma,X}\|\le C_B\), the forcing columns satisfy \(\sup_X\|V_X\|\le C_V\), and the complement coercivity constant \(\delta_K\) is cutoff-uniform, then

\[
\sup_X\sup_{z\in K}
\left\|
Q_{U,X}(z)^{-1/2}
B_{\Sigma,X}^\dagger
R_{H,X}(z)V_X
\right\|
\le
\frac{C_BC_V}{\sqrt{\delta_K}\,\varepsilon_K}.
\]

Reciprocal transport preserves this estimate because the source, history, and complement transports are unitary and exchange \(z\) with \(-z\).

## Strength boundary

This proves compact-local boundedness of the complement-energy transfer on every chart separated from the critical seam.

The estimate degenerates as \(\varepsilon_K\) tends to zero and therefore supplies no seam boundary value.

The estimate gives no strict comparison between the correction energy and the bare theta Weyl value.

The divisor theorem still requires the source identity

\[
F_\theta(z)=E_\theta(z)\tau(z)
\]

with \(E_\theta\) nowhere zero, together with limiting absorption at the seam.

## Disposition

The off-seam compact-local complement-energy boundedness gate follows from the already constructed bounded incidence, skew-adjoint resolvent estimate, and cutoff-uniform arithmetic coercivity.

The remaining complement questions are seam limiting absorption and the relative defect identity controlling equality at the Xi divisor and strictness away from it.
