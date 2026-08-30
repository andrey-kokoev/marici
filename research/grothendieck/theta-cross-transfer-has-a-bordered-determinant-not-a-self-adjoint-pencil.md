# Theta cross-transfer has a bordered determinant, not a self-adjoint pencil

## Bounded question

Can the source-to-endpoint cross transfer be exteriorized without changing its
divisor, and does that exteriorization produce a self-adjoint spectral pencil?

## Canonical bordered exteriorization

Let a finite source-authorized compression have carrier matrix \(A=A^*\), ports
\(b_0,b_f\), and

\[
M(z)=A-zI,
\qquad
F(z)=b_f^*M(z)^{-1}b_0.
\]

There is a canonical bordered pencil using exactly these data:

\[
L(z)=
\begin{pmatrix}
0&b_f^*\\
b_0&M(z)
\end{pmatrix}.
\]

The Schur complement gives

\[
\det L(z)=-\det M(z)F(z).
\]

Thus the cross transfer already has an exact exteriorization. It is derived
before zero inspection, uses no fitted coefficient, and preserves the transfer
divisor away from carrier poles. At finite cutoff, determinant authority is
not the missing issue.

## The self-adjointness obstruction

The border remembers that forcing and observation are different ports:

\[
L(z)^*=
\begin{pmatrix}
0&b_0^*\\
b_f&A-\bar zI
\end{pmatrix}.
\]

Unless \(b_f=b_0\), this is not a self-adjoint pencil on the real spectral
axis. The exact determinant section is a noncollocated transmission
determinant, not the characteristic polynomial of a fixed self-adjoint
operator.

The chiral double

\[
Q(z)=
\begin{pmatrix}
0&L(z)^*\\
L(z)&0
\end{pmatrix}
\]

is self-adjoint for each fixed \(z\), and is singular exactly when \(L(z)\) is
singular. But it depends on both \(z\) and \(\bar z\). Its determinant is
proportional to

\[
|\det L(z)|^2.
\]

It is real analytic rather than a holomorphic characteristic section and does
not construct a fixed operator whose eigenvalues are the Riemann ordinates.

## Full two-port exteriorization changes the divisor

Set

\[
B=\begin{pmatrix}b_f&b_0\end{pmatrix},
\qquad
W(z)=B^*M(z)^{-1}B.
\]

Then

\[
\det W=W_{ff}W_{00}-W_{f0}W_{0f}.
\]

This is not the bordered determinant. A zero of \(F=W_{f0}\) need not make
\(\det W\) vanish. Definiteness of the imaginary part of a Hermitian Weyl
matrix can exclude nonreal zeros of \(\det W\) while leaving cross-transfer
zeros untouched. The gain in orientation is obtained by changing the readout.

The two exteriorizations therefore have complementary defects:

1. The bordered determinant preserves the theta divisor but is not a
   self-adjoint holomorphic pencil.
2. The full Weyl determinant has self-adjoint Herglotz geometry but generally
   has a different divisor.

## Finite mismatch test

At any finite theta compression compute

\[
F_X(z)=b_{f,X}^*(A_X-zI)^{-1}b_{0,X}
\]

and

\[
D_X(z)=\det\left(B_X^*(A_X-zI)^{-1}B_X\right).
\]

The first point with

\[
F_X(z)=0,
\qquad
D_X(z)\ne0
\]

is a divisor-mismatch witness against full-port promotion. This calculation
decides whether the actual theta ports possess an extra Pluecker relation; the
generic determinant identity alone supplies none.

## Completion gate

For full-line transport, \(A-z\) is not determinant class. Passing the bordered
identity to the completed source requires a relative determinant or a
source-authorized spectral compression. Its denominator must be a proven
nowhere-zero unit on each reciprocal sheet, with winding retained.

## Result

The cross transfer possesses a canonical determinant section: its bordered
determinant. The remaining Hilbert--Polya gate is not exteriorization alone.
It is a source-derived identification of the two ports, or a holomorphic
self-adjoint linearization that preserves the bordered divisor.

## Sharp falsifier

Any claimed self-adjoint exteriorization must derive a fixed self-adjoint
operator \(H\) and a nowhere-zero holomorphic unit \(u\) satisfying

\[
\det L(z)=u(z)\det(H-zI)
\]

on the declared sheet. Failure of port colocation, holomorphicity, or unit
authority rejects the claim. Replacing \(\det L\) by \(\det W\) is a different
observable, not a repair.
