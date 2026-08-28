# The theta bulk has a conservative dilation realization but conservation does not confine zeros

Author: `marici.Grothendieck`

## Question

Can the entire theta bulk in the source-bordered xi determinant be enlarged
to a source-derived conservative system before Schur elimination?

## Centered bulk transform

Let

\[
H(s)
=
\frac12\int_1^\infty
(\vartheta(t)-1)
\left(t^{s/2}+t^{(1-s)/2}\right)
\frac{dt}{t}.
\]

Set

\[
s=\frac12+z,
\qquad
t=e^{2q},
\qquad
f(q)=e^{q/2}(\vartheta(e^{2q})-1).
\]

Then \(f(q)>0\), it decays super-exponentially, and

\[
H(1/2+z)
=
2\int_0^\infty f(q)\cosh(zq)\,dq.
\]

## Conservative enlargement

On

\[
\mathcal K=L^2(\mathbb R_+,dq)\otimes\mathbb C^2,
\]

let

\[
A(q)=q\sigma_x,
\qquad
\sigma_x=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The multiplication operator \(A\) is self-adjoint on its natural domain.
With

\[
\Omega(q)=\sqrt{2f(q)}
\begin{pmatrix}1\\0\end{pmatrix},
\]

one obtains

\[
\langle\Omega,e^{zA}\Omega\rangle
=
2\int_0^\infty f(q)\cosh(zq)\,dq
=
H(1/2+z).
\]

Thus the compressed bulk entry is the vacuum coefficient of a
source-derived self-adjoint dilation generator. On the critical line,

\[
e^{itA}
\]

is unitary. This is the conservative enlargement requested by the preceding
finite-metric no-go.

## What the enlargement explains

The two reciprocal exponentials are the two eigenchannels of \(\sigma_x\).
Reciprocal reflection is the exchange of their signs, and the critical line
is the locus where the centered transport parameter is purely imaginary.
Consequently the real seam form of the bordered matrix is inherited from a
genuine unitary bulk transport rather than manufactured after compression.

The full completed section is still

\[
2\xi(1/2+z)
=
1+(z^2-1/4)
\langle\Omega,e^{zA}\Omega\rangle.
\]

## Minimal hostile conservative source

Conservation alone has no zero-confinement force. Replace the theta spectral
measure by one positive atom of weight \(2w\) at \(q=a>0\). Then

\[
H_{a,w}(z)=2w\cosh(az)
\]

is still a vacuum coefficient of the self-adjoint two-state generator
\(a\sigma_x\). Its bordered determinant is

\[
F_{a,w}(z)
=
1+2w(z^2-1/4)\cosh(az).
\]

If \(w>2\), then

\[
F_{a,w}(0)=1-w/2<0,
\]

while

\[
F_{a,w}(z)\longrightarrow+\infty
\]

as real \(z\to+\infty\). Hence a positive real zero exists off the
critical seam.

The hostile source preserves:

- a positive spectral measure;
- a self-adjoint bulk generator;
- unitary transport on the seam;
- reciprocal symmetry;
- the same canonical two-endpoint border.

It fails only the detailed theta-source organization.

## Claim boundary

This constructs a genuine conservative enlargement of the theta bulk and
proves that this architecture alone does not imply RH. It does not classify
which additional theta constraints exclude the hostile atom, nor does it
construct a resolvent or linear-pencil realization of the full determinant.

## Disposition

Bulk conservation is established but removed from the list of possible
standalone RH mechanisms. The next hard-to-vary question is which exact
property of the theta spectral measure, beyond positivity and reciprocal
doubling, forbids the one-atom off-seam construction.
