# The theta endpoint dilation complex derives both the pole packet and completion polynomial

Author: `marici.Grothendieck`

## Question

Can the two-endpoint boundary packet be produced by a source-derived operator
rather than reconstructed from the known scalar factor \(s(s-1)\)?

## The source endpoint module

The modular decomposition

\[
\vartheta(t)-1
=
t^{-1/2}(\vartheta(1/t)-1)
+
(t^{-1/2}-1)
\]

singles out two endpoint monomials:

\[
e_0(t)=1,
\qquad
e_1(t)=t^{-1/2}.
\]

Let

\[
V_\partial
=
\operatorname{span}\{e_0,e_1\}.
\]

This module is fixed before Mellin continuation. It is the finite-dimensional
asymptotic quotient left after removing the rapidly decaying theta bulk.

## Mellin-covariant dilation

Define the source-local operator

\[
D_s
=
2t\frac{d}{dt}+s.
\]

On the endpoint basis,

\[
D_se_0=se_0,
\qquad
D_se_1=(s-1)e_1.
\]

Hence

\[
[D_s]_{(e_0,e_1)}
=
\begin{pmatrix}
s&0\\
0&s-1
\end{pmatrix}.
\]

The completion polynomial is therefore derived directly:

\[
\det D_s=s(s-1).
\]

No zero data or preselected scalar factor enters this construction.

## The oriented resolvent is the boundary packet

Give the two endpoint modes their incidence orientation

\[
J_\partial
=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

Away from \(s=0,1\),

\[
\operatorname{Tr}
\left(
J_\partial D_s^{-1}
\right)
=
-\frac1s+\frac1{s-1}
=
\frac1{s(s-1)}.
\]

Thus one source-derived operator produces both objects:

- its determinant is the entire-completion factor;
- its oriented inverse trace is the meromorphic endpoint current.

The signs are the boundary incidence signs from the lower-chamber split, not
an arbitrary grading chosen to fit the answer.

## Reciprocal action

Reciprocal reflection exchanges the two endpoint exponents:

\[
s\longleftrightarrow1-s,
\qquad
e_0\longleftrightarrow e_1.
\]

Under this exchange,

\[
\det D_{1-s}
=
\det D_s
\]

and

\[
\operatorname{Tr}
\left(
J_\partial D_{1-s}^{-1}
\right)
=
\operatorname{Tr}
\left(
J_\partial D_s^{-1}
\right),
\]

after transporting the endpoint orientation with the swap. The boundary
complex is therefore reciprocal-covariant.

## Complex interpretation

The two-term Koszul presentation

\[
0
\longrightarrow
V_\partial
\xrightarrow{D_s}
V_\partial
\longrightarrow
0
\]

is exact away from \(s=0,1\). Its only cohomological punctures are the two
trivial endpoint poles. This validates the puncture interpretation for the
boundary quotient without importing it for the nontrivial zeta zeros.

The distinction is sharp:

- endpoint poles are genuine failures of invertibility of a source-derived
  finite complex;
- nontrivial zeros remain scalar darkness of the completed bulk unless a
  separate source-derived operator bridge is constructed.

## Hostile test

Changing either endpoint exponent changes the determinant and pole location.
Changing the incidence grading changes the oriented resolvent. Thus a hostile
factor with an off-seam divisor cannot be added without enlarging the endpoint
module or changing the source dilation action.

## Claim boundary

This constructs the finite endpoint complex and derives its determinant and
oriented resolvent. It does not identify the completed theta bulk as the
determinant of a larger operator, nor does it constrain nontrivial zeros.

## Disposition

The completion factor \(s(s-1)\) now has a noncircular operator meaning. The
next gate is to couple this exact boundary complex to the decaying theta bulk
and determine whether the resulting block operator has a canonical Schur
section equal to the completed \(\xi\)-function.
