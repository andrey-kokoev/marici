# Gaussian counterterm–Cut uncertainty split

Use the one-mode covariance convention

\[
V=
\begin{pmatrix}
n+\frac12+x&y\\
y&n+\frac12-x
\end{pmatrix},
\qquad
\det V-\frac14=n+n^2-x^2-y^2.
\]

A frozen Hermitian local quadratic counterterm has a symmetric Hamiltonian
matrix \(H\) and infinitesimal symplectic generator \(A=JH\).  It acts by

\[
\dot V_{\rm ct}=AV+VA^T.
\]

Because \(\operatorname{tr}A=0\),

\[
\frac{d}{dt}\det V
=2\operatorname{tr}(A)\det V=0.
\]

The labelled Cut contribution has the form \(N=CC^\dagger\succeq0\).  For
physical \(V\succeq0\),

\[
\left.\frac{d}{d\epsilon}\det(V+\epsilon N)\right|_{\epsilon=0}
=\operatorname{tr}(\operatorname{adj}(V)N)\geq0.
\]

The checker verifies the first identity for a finite exact census of symmetric
integer \(H\) and covariance matrices, and the second inequality for rank-one
integer Cut vectors.

This proves preservation only for counterterms whose source action is a
Hermitian local quadratic Hamiltonian/canonical renormalization.  It does not
license arbitrary finite covariance subtraction, nor prove a cutoff-free
renormalized theorem.
