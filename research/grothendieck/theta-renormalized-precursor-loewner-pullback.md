# Pullback of the Loewner form to the renormalized theta precursor

## Transform kernels

Inside \(|\Re z|<1/2\), let

\[
F(z)=\int_{\mathbb R}e^{zu}K(u)\,du,
\qquad
K(u)=\cosh(u/2)-\frac12e^{u/2}\Theta(e^{2u}).
\]

Since \(K\) is even, write \(F(z)=\mathcal F(w)\), \(w=z^2\), and define

\[
\phi_w(u)=\cosh(\sqrt w\,u),
\qquad
\psi_w(u)=\partial_w\phi_w(u)
=\frac{u\sinh(\sqrt w\,u)}{2\sqrt w},
\]

with the removable value \(\psi_0(u)=u^2/2\). Then

\[
\mathcal F(w)=2\int_0^\infty K(u)\phi_w(u)\,du,
\qquad
\mathcal F'(w)=2\int_0^\infty K(u)\psi_w(u)\,du.
\]

Put \(c=1/4\) and \(\zeta_w=w-c\). The exact completion identity is

\[
C(w)=-\frac12\zeta_w\mathcal F(w).
\]

## Exact two-copy pullback

The denominator-free Loewner kernel satisfies

\[
\boxed{
L_C(x,y)=
\frac{\zeta_x\zeta_y}{4(x-y)}
\left[
\zeta_x\mathcal F'(x)\mathcal F(y)
-\zeta_y\mathcal F'(y)\mathcal F(x)
\right].
}
\]

Substitution of the theta transforms gives

\[
\boxed{
L_C(x,y)=
\frac{\zeta_x\zeta_y}{x-y}
\int_0^\infty\!\!\int_0^\infty
K(u)K(v)
\left[
\zeta_x\psi_x(u)\phi_y(v)
-\zeta_y\psi_y(u)\phi_x(v)
\right]du\,dv.
}
\]

The asymmetric integrand may be symmetrized under \(u\leftrightarrow v\)
without changing the integral. This is the exact source-side object that a
Gram proof must factor.

No Xi zeros, thimbles, logarithmic quotients, or meromorphic precursor terms
occur. The endpoint null modes have already been subtracted in \(K\).

## Diagonal source identity

Taking \(y\to x\) yields

\[
\boxed{
L_C(x,x)=\frac14\left[
\zeta_x^2\mathcal F(x)\mathcal F'(x)
+\zeta_x^3
\left(\mathcal F(x)\mathcal F''(x)-\mathcal F'(x)^2\right)
\right].
}
\]

Thus even the one-point Loewner condition couples a first moment to a
Wronskian/covariance term. Positivity of \(K\) alone does not determine its
sign, because \(\zeta_x\) changes sign at the source-forced center and the
bracket contains a difference of products.

## What a genuine Gram factorization must do

A successful source proof must transform the displayed two-copy kernel into

\[
L_C(x,y)=\langle R(x),R(y)\rangle
\]

using identities of the special modular precursor \(K\), not generic
positivity of \(K\). In particular it must:

1. preserve the centered factors \(\zeta_x,\zeta_y\);
2. couple the \(w\)-derivative kernel \(\psi_w\) to the transform kernel
   \(\phi_w\);
3. remain regular when \(C\) vanishes on the real axis; and
4. explain how the sign-changing divided difference becomes a positive
   inner product only after the complete two-copy integration.

This is substantially more specific than the instruction "find a Gram
factorization."

## Immediate falsifier

Pointwise positivity of the bracket is neither expected nor required. The
first legitimate local obstruction is instead a finite signed test function
\(a_j\) and real parameters \(x_j\) for which the fully integrated quadratic
form

\[
\sum_{j,k}a_ja_kL_C(x_j,x_k)
\]

is negative. Any proposed rearrangement that takes absolute values before the
\(u,v\) integration changes the object and is inadmissible.

The next algebraic attack is to use
\((1/4-\partial_u^2)K=\Phi\) and the differential equations
\(\partial_u^2\phi_w=w\phi_w\) to perform a Green transfer inside this
two-copy formula. On the half-line, evenness predicts
\(K'(0)=\phi_w'(0)=0\), so the finite endpoint form should cancel; that
cancellation must be shown explicitly rather than assumed.

The transfer has now been completed. The endpoint form vanishes, the pure
precursor terms cancel, and the result is a mixed Bezoutian between the
\(K\)-transform and the differentiated \(\Phi\)-transform—not a manifest
square. See `theta-green-transfer-mixed-bezoutian.md`.
