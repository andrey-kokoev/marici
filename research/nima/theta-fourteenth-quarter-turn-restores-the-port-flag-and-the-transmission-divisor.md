# The fourteenth theta quarter-turn restores the port flag and the transmission divisor

## Status

Exact finite-dimensional divisor correction. The locally closed conservative
colligation and its arithmetic completion describe the full two-port Weyl or
scattering object. The completed theta scalar is presently a transfer from one
distinguished source port to a different endpoint port. Forgetting that ordered
port flag changes its zero divisor into the full Weyl determinant divisor.

The fourteenth turn restores the ordered input/output flag and exteriorizes the
cross transfer by its bordered Rosenbrock pencil. This preserves the theta
divisor, but generically loses selfadjointness. The RH-bearing gate is therefore
a source-derived symmetry of the framed pencil, not generic passivity of the
unframed colligation.

## Source-derived two-port carrier

Let \(A=A^*\) be a finite source-authorized carrier compression. Retain the two
distinct rigged ports

\[
b_0,
\qquad
b_f.
\]

Here \(b_0\) is the endpoint port and \(b_f\) is the theta-source port.

For

\[
M(z)=A-zI,
\]

the theta transfer is

\[
F(z)
=
b_f^*M(z)^{-1}b_0.
\]

The ordered flag

\[
\mathfrak f
=
\left(b_0,b_f\right)
\]

is part of the observable. Interchanging, identifying, or forgetting its two
entries changes the question.

## Why the unframed Weyl rotation misses theta zeros

Set

\[
B
=
\begin{pmatrix}
b_f&b_0
\end{pmatrix}
\]

and form the full Weyl matrix

\[
W(z)=B^*M(z)^{-1}B.
\]

The theta scalar is one off-diagonal entry of \(W\), whereas

\[
\det W
=
W_{ff}W_{00}-W_{f0}W_{0f}.
\]

At a theta zero,

\[
W_{f0}(z_0)=0,
\]

the matrix \(W(z_0)\) can remain invertible. The Cayley crossing form, delay
density, Hardy defect, and characteristic-function orbit of the unframed full
Weyl object then see no singular crossing.

All those constructions remain valid, but they orient a different divisor.

## The fourteenth quarter-turn

Restore the ordered flag and form the bordered pencil

\[
L_{\mathfrak f}(z)
=
\begin{pmatrix}
0&b_f^*\\
b_0&M(z)
\end{pmatrix}.
\]

The Schur complement gives

\[
\det L_{\mathfrak f}(z)
=
-\det M(z)F(z).
\]

Away from carrier poles, rank loss of the bordered pencil is exactly rank loss
of the theta transmission channel. This is the canonical finite
exteriorization of the correct divisor.

The rotation is

\[
\left(\mathfrak C,\mathfrak f\right)
\longrightarrow
L_{\mathfrak f}(z).
\]

The new object is a framed colligation or transmission system, not an
unframed scattering system.

## The selfadjointness obstruction

On the real spectral axis,

\[
L_{\mathfrak f}(\lambda)^*
=
\begin{pmatrix}
0&b_0^*\\
b_f&A-\lambda I
\end{pmatrix}.
\]

Unless the two ports are source-collocated, this differs from
\(L_{\mathfrak f}(\lambda)\). The exact transmission determinant is therefore
not the characteristic polynomial of the selfadjoint carrier.

The chiral double

\[
\begin{pmatrix}
0&L_{\mathfrak f}(z)^*\\
L_{\mathfrak f}(z)&0
\end{pmatrix}
\]

is selfadjoint for fixed \(z\), but it depends on both \(z\) and \(\overline z\)
and carries the real-analytic divisor

\[
\left|\det L_{\mathfrak f}(z)\right|^2.
\]

It does not provide a holomorphic selfadjoint spectral pencil.

## Exact lower-minor gate

For a two-by-two holomorphic Weyl matrix

\[
W
=
\begin{pmatrix}
a&F\\
G&d
\end{pmatrix},
\]

an identity

\[
\det W=uF
\]

with a nowhere-zero holomorphic \(u\) requires

\[
ad=F(G+u).
\]

Thus every zero of \(F\) must also annihilate \(ad\). A single point satisfying

\[
F(z_0)=0,
\qquad
a(z_0)d(z_0)\ne0
\]

falsifies promotion of the cross-transfer divisor to the full Weyl divisor.

No amount of completion, phase winding, or delay positivity repairs this
finite lower-minor mismatch.

## Candidate framed symmetry

The remaining structural possibility is a source-derived indefinite metric or
port involution \(J\) that exchanges the two flag directions and makes the
bordered pencil symmetric in a typed sense. A candidate relation would have
the form

\[
L_{\mathfrak f}(\lambda)^*J
=
JL_{\mathfrak f}(\lambda)
\]

on a common source-derived domain.

Such a \(J\) cannot be fitted from the zero divisor. It must arise from modular
reflection, endpoint orientation, and the exact source/endpoint incidence.

Even a valid indefinite symmetry would not automatically force real or seam
zeros. A separate definitizability or Krein-sign law would still be required,
and hostile symmetric pencils must be tested.

## Source attachment precedes completion

The arithmetic connection and completion programme remains relevant only for
the framed object. Its fibers must be

\[
\left(
\mathfrak C_X,
\mathfrak f_X,
L_{\mathfrak f_X},
\mathcal R_X
\right),
\]

and every prime transport must preserve the ordered flag and bordered
incidence before any determinant or scalar projection.

The first source square is therefore not merely a port-gauge square. It must
intertwine the complete bordered pencils:

\[
\mathcal V_{X,Y}
L_{\mathfrak f_X}(z)
=
L_{\mathfrak f_Y}(z)
\mathcal U_{X,Y}
\]

with separately typed domain and codomain transports.

## Finite falsifiers

The framed control route fails if:

- the smallest theta compression has a cross-transfer zero with invertible
  full Weyl matrix;
- no source-derived fixed metric \(J_X\) symmetrizes the bordered pencil;
- the required \(J_X\) changes after zero inspection;
- prime transport preserves the full Weyl colligation but not the ordered
  source/endpoint flag;
- the bordered intertwining square commutes only after determinants;
- or a hostile signed source admits the same framed symmetry and completion
  laws.

## Decisive conclusion

The object being rotated is not an unframed conservative colligation. It is a
source-framed two-port relationship. Restoring the flag returns the programme
to the actual theta divisor and exposes the precise remaining conflict:

- the bordered transmission pencil preserves the correct divisor but is not
  selfadjoint;
- the full Weyl pencil has positive selfadjoint geometry but carries the wrong
  divisor.

The next decisive calculation is finite and source-local: derive or falsify a
modular port involution for the bordered pencil before any further global
completion work.
