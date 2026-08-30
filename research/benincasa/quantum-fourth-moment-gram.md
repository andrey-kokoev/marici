# Minimal quantum Gram object for the mixed fourth cumulant

Scale canonical variables so that

\[
[Q,P]=2i
\]

and define the dilation observable

\[
S=\frac{QP+PQ}{2}.
\]

For the operator column \((1,Q^2,S)\), positivity of the density matrix gives
the Hermitian Gram matrix

\[
M=
\begin{pmatrix}
1&Q_2&R\\
Q_2&U&Z+2iQ_2\\
R&Z-2iQ_2&W
\end{pmatrix}
\succeq0,
\]

where

\[
Q_2=\langle Q^2\rangle,
\quad R=\langle S\rangle,
\quad U=\langle Q^4\rangle,
\quad Z=\operatorname{Re}\langle Q^2S\rangle,
\quad W=\langle S^2\rangle.
\]

The imaginary entry is not optional.  It follows from

\[
[Q^2,S]=4iQ^2,
\qquad
\operatorname{Im}\langle Q^2S\rangle=2Q_2.
\]

The determinant condition is

\[
\boxed{
\operatorname{Var}(Q^2)\operatorname{Var}(S)
\geq
\operatorname{Cov}(Q^2,S)^2+4Q_2^2.
}
\]

Thus the mixed fourth moment corresponding to \(\kappa_{pqqq}\) is controlled
only together with \(\langle S^2\rangle\).  It is not bounded on a
fixed-covariance/fixed-\(Q^4\) slice if the companion fourth moment is omitted:
at \(Q_2=1,R=0,U=2\), every real \(Z\) satisfies the determinant boundary by
taking \(W=Z^2+4\).

The checker verifies the exact determinant inequality and 201 such unbounded
truncated-moment witnesses.  Positive semidefiniteness of this truncated Gram
matrix is necessary, not sufficient, for a full quantum state extension.
