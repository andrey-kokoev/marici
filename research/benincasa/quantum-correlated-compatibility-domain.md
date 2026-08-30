# Exact quantum compatibility domain for opposite-momentum Gaussian support

Use the standard-form covariance

\[
V(x)=
\begin{pmatrix}
xI&cZ\\
cZ&aI
\end{pmatrix},
\qquad
c^2=a^2-1,
\]

with scaled vacuum covariance \(I\).  Quantum positivity is

\[
V+i\Omega\succeq0.
\]

For \(a>1\), the internal block \(aI+iJ\) is invertible.  Its Schur
complement is

\[
xI+iJ
-cZ(aI+iJ)^{-1}cZ.
\]

Using

\[
(aI+iJ)^{-1}=\frac{aI-iJ}{a^2-1},
\qquad
ZJZ=-J,
\qquad
c^2=a^2-1,
\]

gives the exact result

\[
\boxed{(x-a)I.}
\]

Hence the correlated assignment is quantum-compatible exactly when

\[
\boxed{x\geq a.}
\]

The source marginal \(x=a\) lies on the boundary.  The ordinary positivity
condition of Entry 1638 was only a weaker necessary gate.

In the product degeneration \(c\to0\), purity forces \(a\to1\), and the domain
becomes \(x\ge1\): the complete physical isotropic one-mode domain.  Thus the
supported compatibility object degenerates canonically to the generic product
assignment without a chosen interpolation.
