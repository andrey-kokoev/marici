# Primitive density and seam image share a diagonal, not a carrier

## The typing collision

Finite Cauchy observation of the primitive Euler carrier produces the diagonal
operator

\[
D_{pq}=
\begin{pmatrix}
p^{-1}&0\\
0&q^{-1}
\end{pmatrix}.
\]

The universal Dirichlet image term on the same two prime labels is the
rank-one operator

\[
B_{pq}=bb^*,
\qquad
b=
\begin{pmatrix}
p^{-1/2}\\
q^{-1/2}
\end{pmatrix},
\]

so

\[
B_{pq}=
\begin{pmatrix}
p^{-1}&(pq)^{-1/2}\\
(pq)^{-1/2}&q^{-1}
\end{pmatrix}.
\]

They have identical diagonals and identical ordinary traces:

\[
\operatorname{diag}D_{pq}=\operatorname{diag}B_{pq},
\qquad
\operatorname{Tr}D_{pq}=\operatorname{Tr}B_{pq}.
\]

They are not the same carrier.

## Exact separator

Their determinants are

\[
\det D_{pq}=\frac1{pq},
\qquad
\det B_{pq}=0.
\]

The residual

\[
R_{pq}=D_{pq}-B_{pq}
=
\begin{pmatrix}
0&-(pq)^{-1/2}\\
-(pq)^{-1/2}&0
\end{pmatrix}
\]

has zero diagonal and zero trace but determinant \(-1/(pq)\). Its two
eigenvalues are opposite and nonzero. Therefore diagonal and scalar-trace
readouts annihilate a genuine indefinite cross-prime coherence channel.

## Source interpretation

The repeated coefficient \(1/p\) has two distinct proven origins:

- as the observed primitive density produced by the Cauchy moment;
- as the diagonal shadow of the rank-one seam image term.

One occurrence does not authorize deleting the other, and their equality does
not authorize adding them twice. The programme needs a typed incidence or
comparison map explaining whether the two channels:

- are two presentations of one state;
- are coupled components of a relative Green identity;
- cancel after an oriented boundary operation;
- or remain independent before a later scalar quotient.

Until that map exists, scalar bookkeeping cannot decide between coincidence,
identification, cancellation, and double counting.

## Categorical form

Let \(\Delta\) be diagonal projection. Then

\[
\Delta(D_{pq})=\Delta(B_{pq})
\]

while \(D_{pq}\neq B_{pq}\). Thus \(\Delta\) is not faithful on the common
two-prime boundary carrier. The missing comparison lives in
\(\ker\Delta\), represented minimally by \(R_{pq}\).

This is the smallest state-valued boundary residual demanded by the previous
corona analysis. It already appears on two labels; no infinite completion is
needed to witness the information loss.

## Finite falsifier

For \(p=2\) and \(q=3\), both carriers have diagonal \((1/2,1/3)\) and trace
\(5/6\). The diagonal carrier has determinant \(1/6\); the seam image has
determinant zero; their residual has determinant \(-1/6\). Any proposed
grade-identification law based only on the shared \(1/p\) diagonal fails this
two-prime test.

## Verdict

The observed primitive density and the seam-image square share a scalar
shadow, not an object identity. Their cross-prime residual is the minimum
state-valued comparison port. The next theta--Tate audit must derive the
coefficient and sign of this off-diagonal seam channel before taking diagonal,
trace, Mertens, or BSY readouts.

