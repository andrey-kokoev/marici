# Unitary vacuum overlap equals the excited-compression defect determinant

## 1. Abstract coupled theorem

Let \(\mathcal H=\mathbb C\Omega\oplus\mathcal K\), with
\(\|\Omega\|=1\), and let \(U\) be unitary. Write its block decomposition as

\[
  U=
  \begin{pmatrix}
    a & \beta\\
    \gamma & D
  \end{pmatrix},
\]

where

\[
  a=\langle\Omega,U\Omega\rangle,
  \qquad
  D=P_{\mathcal K}U|_{\mathcal K}.
\]

Unitarity gives

\[
  D^*D=I_{\mathcal K}-\beta^*\beta,
\]

and

\[
  \|\beta\|^2=1-|a|^2.
\]

Therefore \(I-D^*D\) has rank at most one, and its only possible nonzero
eigenvalue is \(1-|a|^2\). The Fredholm determinant is exactly

\[
  \boxed{
  \det(D^*D)=|a|^2
  =
  |\langle\Omega,U\Omega\rangle|^2.}
\]

This is the first universal coupled positivity theorem in the present
two-sector programme.

## 2. Kernel equivalence

If \(a\ne0\), then

\[
  D^*D\ge |a|^2I
\]

on the one possible defect direction and equals the identity on its
orthogonal complement. Hence \(D\) is boundedly invertible.

If \(a=0\), the vector representing \(\beta\) lies in \(\ker D\), while the
vector representing \(\gamma\) spans the cokernel. Thus

\[
  \boxed{
  \langle\Omega,U\Omega\rangle=0
  \quad\Longleftrightarrow\quad
  \ker(P_{\mathcal K}U|_{\mathcal K})\ne0.}
\]

A vacuum zero is exactly a loss of transversality in the complete excited
sector.

## 3. Theta application on the critical axis

For real character parameter \(x\),

\[
  U_x=e^{ixQ}
\]

is unitary. With the completed normalized theta vacuum,

\[
  \widehat X(x)
  :=
  \frac{X(x)}{X(0)}
  =
  \langle\Omega,U_x\Omega\rangle.
\]

Therefore the excited compression

\[
  D_x
  =
  (I-P_\Omega)U_x|_{\Omega^\perp}
\]

satisfies

\[
  \boxed{
  \det(D_x^*D_x)
  =
  |\widehat X(x)|^2
  =
  \frac{|X(x)|^2}{X(0)^2},}
\]

and every critical-line zero is precisely a kernel event of \(D_x\).

This removes the earlier vacuum-minor gap on the unitary axis. Infinite Schur
dressing is not an uncontrolled correction there; unitarity packages it into
one rank-one defect whose determinant is the physical overlap modulus.

## 4. Why the real axis is special

For complex \(z=x+iy\) with \(y\ne0\),

\[
  U_z=e^{izQ}
\]

is not unitary. The identities

\[
  D_z^*D_z=I-\beta_z^*\beta_z
\]

and

\[
  \det(D_z^*D_z)=|\widehat X(z)|^2
\]

no longer follow. An invertible nonunitary block operator can have vanishing
vacuum entry while its excited compression remains invertible.

Thus the critical axis is selected by an exact conservation law:

\[
\boxed{
\text{real character transport is unitary}
\Longrightarrow
\text{scalar zero equals full-sector defect}.}
\]

Off-axis transport loses precisely this meaning-preserving equivalence.

## 5. Relation to RH

The theorem explains what a critical-line zero *is*. It does not prove that
off-axis zeros are absent. RH now takes the sharper form:

> The completed analytic continuation has no scalar zeros outside the domain
> where the vacuum overlap possesses its unitary full-sector defect meaning.

Equivalently, modular completion must prevent the analytic overlap from
vanishing after the coupled determinant interpretation has ceased to be
unitarily protected.

## 6. Strongest next target

Find a two-sided or Krein-space continuation of the defect identity in which
complex transport remains \(J\)-unitary:

\[
  U_z^*JU_z=J.
\]

If a source-derived indefinite metric \(J\) exists and its positive sector is
selected exactly on the critical axis, a generalized defect determinant may
exclude off-axis kernel events. The metric must arise from reciprocal
adelic sewing, not be manufactured from \(X\).

The hostile test is immediate: generic positive Fourier-stable sources share
ordinary unitarity on the real axis. They must fail the proposed
\(J\)-unitary modular continuation before their off-line zeros are examined.

## 7. Scope

The unitary block identities, Fredholm determinant formula, and kernel
equivalence are exact. Their theta application identifies real-axis overlap
zeros with excited-compression defects. No \(J\)-unitary continuation,
off-axis zero exclusion, or RH theorem is established.
