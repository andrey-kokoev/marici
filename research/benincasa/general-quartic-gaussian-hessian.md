# General quartic Gaussian first variation from the averaged Hessian

Let \(R=(q,p)\), let \(V=\langle R R^T\rangle_{\rm sym}\), and take a
Weyl-ordered quartic Hamiltonian

\[
H_4=a q^4+bq^3p+cq^2p^2+dqp^3+ep^4.
\]

For a centered Gaussian state, Gaussian integration by parts gives

\[
\langle\partial_iH_4\,R_j\rangle_{\rm sym}
=
\langle\partial_i\partial_kH_4\rangle V_{kj}.
\]

Define the symmetric averaged Hessian

\[
K=\langle\operatorname{Hess}H_4\rangle.
\]

The covariance first variation is exactly

\[
\dot V=JKV+VK^TJ^T=AV+VA^T,
\qquad A=JK.
\]

Since \(K\) is symmetric, \(A\) is symplectic and traceless.  Therefore

\[
\partial_t\det V=0.
\]

For the displayed basis,

\[
K_{qq}=12aV_{qq}+6bV_{qp}+2cV_{pp},
\]

\[
K_{qp}=3bV_{qq}+4cV_{qp}+3dV_{pp},
\]

\[
K_{pp}=2cV_{qq}+6dV_{qp}+12eV_{pp}.
\]

The checker verifies every basis monomial and two mixed tensors over an exact
covariance census.  Because a quadratic observable has no third derivative,
the Moyal bracket has no higher quantum correction: the Weyl-symbol argument
is exact at this covariance grade.

Mode labels and spatial derivative tensors alter the quartic coefficient
tensor, but not this Gaussian Hessian mechanism, provided the interaction is
Hermitian and Weyl ordered.
