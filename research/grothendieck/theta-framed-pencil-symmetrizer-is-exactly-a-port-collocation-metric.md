# Theta framed-pencil symmetrizer is exactly a port-collocation metric

## Bounded question

Can modular reflection or another source-fixed metric make the bordered
Rosenbrock pencil self-adjoint on the real spectral axis?

## Framed pencil

At a finite carrier compression, let

\[
L(\lambda)
=
\begin{pmatrix}
0&b_f^*\\
b_0&A-\lambda I
\end{pmatrix},
\qquad
A=A^*.
\]

Write

\[
L(\lambda)=L_0-\lambda P,
\qquad
P=
\begin{pmatrix}
0&0\\
0&I
\end{pmatrix}.
\]

Seek a fixed invertible Hermitian metric \(J\) satisfying

\[
L(\lambda)^*J=JL(\lambda)
\]

for every real \(\lambda\).

## Spectral coefficient forces block diagonality

Comparing the coefficients of \(\lambda\) gives

\[
PJ=JP.
\]

Therefore \(J\) must preserve the reference coordinate and carrier space:

\[
J=
\begin{pmatrix}
j&0\\
0&G
\end{pmatrix},
\]

where \(j\) is a nonzero real scalar and \(G\) is an invertible Hermitian
carrier metric.

No off-diagonal metric term can exchange the two spaces while retaining the
same linear spectral parameter.

## Constant coefficient equations

The remaining equation

\[
L_0^*J=JL_0
\]

is equivalent to

\[
GA=AG
\]

and

\[
Gb_0=jb_f.
\]

The adjoint row equation is the Hermitian conjugate of the port equation.

Thus a fixed \(J\)-symmetry of the framed pencil exists exactly when a
carrier-commuting metric collocates the endpoint and source ports, up to the
reference scalar \(j\).

This is not a new escape from the port obstruction. It is precisely the same
obstruction expressed at the bordered-pencil level.

## Involution specialization

If \(J\) is required to be a fundamental symmetry,

\[
J^2=I,
\]

then

\[
j=\pm1,
\qquad
G^2=I.
\]

For a simple-spectrum carrier, \(G\) is diagonal with signs in the carrier
eigenbasis. The port equation then requires the source and endpoint spectral
components to agree mode by mode up to those fixed signs. Generic
noncollocated theta ports do not satisfy this.

## Modular reflection has the wrong covariance

On the logarithmic translation carrier, the native causal reflection \(R\)
satisfies

\[
RAR=-A.
\]

It exchanges the direct and reciprocal spectral orientations. It does not
commute with \(A\), as the same-sheet symmetrizer equation requires.

Therefore modular reflection cannot serve as \(G\) for

\[
L(\lambda)^*J=JL(\lambda)
\]

at fixed \(\lambda\). It can only enter a doubled relation that simultaneously
reverses the spectral parameter or exchanges reciprocal sheets.

This agrees with the seam theorem: reflection produces a common relative flag
only when the reciprocal weights coalesce.

## Status of the finite numerical request

The current research artifacts define a finite compiler
\((A_X,b_{0,X},b_{f,X})\) but do not declare a smallest explicit
source-authorized matrix fixture. Choosing a quadrature, spectral compression,
or fitted finite matrix now would introduce an unauthorized cutoff.

Consequently the numerical search for

\[
F_X(z)=0,
\qquad
\det W_X(z)\ne0
\]

is not yet well typed. Packet 245 supplies the cutoff-independent asymptotic
divisor mismatch for every independent nonorthogonal port fixture, but an
actual smallest theta witness awaits a frozen compression constructor.

## Result

The fixed-metric symmetry problem for the faithful bordered pencil is solved
algebraically. It is equivalent to the already obstructed carrier-commuting
port-collocation problem. Native modular reflection has anti-commuting rather
than commuting covariance and therefore belongs to the reciprocal double, not
to a same-sheet \(J\)-self-adjoint pencil.

The surviving options are:

1. derive a source-authorized finite compression whose spectral blocks satisfy
   the port metric equations;
2. construct a doubled parameter-reversing symmetry;
3. abandon fixed-metric self-adjointness and prove open-cell confinement by a
   different source law.

## Sharp falsifier

For any declared cutoff, solve the linear equations

\[
GA_X=A_XG,
\qquad
Gb_{0,X}=jb_{f,X}.
\]

No invertible Hermitian solution means no fixed \(J_X\)-symmetry of the
bordered pencil. A proposed modular solution also fails immediately if it
anticommutes with \(A_X\) while the claim requires fixed-\(\lambda\)
self-adjointness.
