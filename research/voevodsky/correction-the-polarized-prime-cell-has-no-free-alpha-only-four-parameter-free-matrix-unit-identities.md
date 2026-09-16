# Correction: the polarized prime cell has no free alpha, only four parameter-free matrix-unit identities

## Question

Is the first missing input for the Evans residual a source-derived even scalar \(\alpha_p\), as stated in the previous blocker packet?

## Claim boundary

No in the latest source state. The completed-theta wall normalization and odd Stokes normalization already determine the full local linear comparison \(Q_p^{\rm lin}\). The notation \(\operatorname{diag}(\alpha_p,\lambda_p)\) is useful in an abstract two-output model, but \(\alpha_p\) is not a remaining adjustable datum in the actual completed-theta construction. The open gate is parameter-free quadratic representation equality on four matrix units.

## Fixed even column

The completed theta wall is

$$
w_\theta=
\begin{pmatrix}1/2\\1/2\end{pmatrix},
$$

with

$$
-\mathbf1_\partial=-2w_\theta.
$$

In endpoint metric \(2I\),

$$
\|w_\theta\|_{2I}^2=1.
$$

Therefore the even wall column has no free amplitude or metric scalar.

## Fixed odd column

The completed odd column is

$$
j_\theta=
\begin{pmatrix}1/4\\-1/4\end{pmatrix}
=\frac14S_{\rm ord}.
$$

The source Stokes identities give

$$
j_\theta\Omega=A,
\qquad
Bj_\theta=-\frac12H_K.
$$

Hence odd magnitude, sign, curvature return, and derivative-tail propagation are also fixed.

## Unique linear map

Together, these columns determine

$$
Q_p^{\rm lin}:
\mathcal B_p^{\rm bi}
\longrightarrow
\mathcal B_p^\theta
$$

without a free coefficient. Any rescaling would violate at least one wall, curvature, or tail identity.

Thus the former abstract diagonal notation

$$
T_p=\operatorname{diag}(\alpha_p,\lambda_p)
$$

must not be read as evidence that \(\alpha_p\) remains to be selected. In the actual source chart, its role is already represented by the fixed even column of \(Q_p^{\rm lin}\).

## Exact remaining test

Let \(e_1,e_2\) denote the ordered endpoint generators mapped to \(W_L,W_{2L}\). The open quadratic theorem is

$$
\mathfrak G_p^{\rm St}(e_j,e_k)
=
\mathfrak G_p^\theta
\left(Q_p^{\rm lin}e_j,Q_p^{\rm lin}e_k\right),
\qquad j,k\in\{1,2\}.
$$

Equivalently, all four rank-one matrix units must satisfy

$$
\Gamma_{\pi_\theta}
\left(
Q_p^{\rm lin}|e_j\rangle\langle e_k|
(Q_p^{\rm lin})^\sharp
\right)
=
\Gamma_{\pi_{\rm St}}
\left(
|W_{jL}\rangle\langle W_{kL}|
\right).
$$

The diagonal tests determine endpoint energies; the off-diagonal tests independently determine real cross-correlation and oriented imaginary linking.

## Fixture boundary

The file

`research/nima/contracts/g4-linking-fourier-poisson-candidate.v1.json`

contains explicit numerical matrices and \(\alpha=2\), but it is marked `test_fixture_only`. Its successful identity demonstrates checker shape, not the authoritative prime cell. It cannot source the Evans residual.

## Revised blocker

The missing object is not another coefficient. It is the proof that two independently constructed quadratic representations agree under an already fixed linear map. Defining the source metric as the pullback metric would make the equality tautological and is therefore circular.

## Disposition

The previous statement that a source-derived \(\alpha_p\) remains missing is superseded. All local linear Adams/Stokes data are fixed. The exact unresolved local gate is the parameter-free four-matrix-unit equality between the Stieltjes and completed theta-history Green representations, followed by uniform closure.