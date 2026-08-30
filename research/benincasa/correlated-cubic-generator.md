# Complete correlated-Gaussian cubic generator

Let the collective pre-shear pair `(Q,P)` be centered Gaussian with

\[
A=\langle Q^2\rangle,
\qquad
B=\langle P^2\rangle,
\qquad
C=\langle S\rangle.
\]

For `Pi=P-t(Q^2-A)`, Gaussian regression of `P` on `Q` gives

\[
K(x,y)=tAy-\frac12\log(1+2Aty)
+\frac12\left(B-\frac{C^2}{A}\right)y^2
+\frac{A(x+Cy/A)^2}{2(1+2Aty)}.
\]

At `t=0` this reduces exactly to

\[
\frac12Ax^2+Cxy+\frac12By^2.
\]

The formula remains regular when `AB-C^2=0` provided `A` is nonzero: the
conditional residual variance simply vanishes.  Rees data are required only
when the conditioning variance itself degenerates.
