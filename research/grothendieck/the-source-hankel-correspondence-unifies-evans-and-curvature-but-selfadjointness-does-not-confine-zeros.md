# The source Hankel correspondence unifies Evans and curvature, but selfadjointness does not confine zeros

## Complete history operator

For a half-line source `f`, define the Hankel history operator

\[
(\mathsf H_f\varphi)(q)
=
\int_0^\infty f(q+a)\varphi(a)\,da.
\]

Its kernel depends only on the sum `q+a`. For the exponential character

\[
e_z(a)=e^{za},
\]

one obtains

\[
(\mathsf H_fe_z)(q)
=
\int_0^\infty f(q+a)e^{za}\,da
=
\int_q^\infty f(v)e^{z(v-q)}\,dv
=G_z(q).
\]

Thus one source-derived operator produces the full tail history before any
observer is chosen.

## Two boundary faces

Endpoint evaluation gives the Evans transform:

\[
E_0\mathsf H_fe_z
=G_z(0)
=\int_0^\infty f(a)e^{za}\,da
=F(z).
\]

The source-adjoint face gives

\[
B_f^\times\mathsf H_fe_z
=\langle f,G_z\rangle,
\]

the ordered autocorrelation or separation transform.

Therefore Evans and curvature are not rival operators. They are two covector
faces of one history correspondence:

```text
                       endpoint face -> Evans transform
character -> H_f -> history
                       source face   -> autocorrelation
```

This is the larger object required by the preceding obstruction.

## Source-derived selfadjointness

For real `f`, the kernel is symmetric:

\[
f(q+a)=f(a+q).
\]

Whenever

\[
\int_0^\infty t|f(t)|^2\,dt<\infty,
\]

the operator is Hilbert--Schmidt because

\[
\int_0^\infty\int_0^\infty|f(q+a)|^2\,dq\,da
=
\int_0^\infty t|f(t)|^2\,dt.
\]

The theta source satisfies this by superexponential decay. Hence
`mathsf H_f` is a genuine compact selfadjoint operator on the half-line
Hilbert space. Endpoint evaluation remains a rigged covector rather than an
ordinary Hilbert vector.

## Smallest selfadjoint hostile

Take the positive two-cell source moments

\[
f_0=1,
\qquad f_1=2,
\qquad f_2=0.
\]

The associated finite Hankel carrier is

\[
H=
\begin{pmatrix}
1&2\\
2&0
\end{pmatrix},
\]

which is real symmetric. For the character vector

\[
e(r)=\begin{pmatrix}1\\r\end{pmatrix},
\]

the endpoint face is

\[
E_0He(r)=1+2r.
\]

It vanishes at `r=-1/2`. Writing `r=e^z` gives

\[
z=-\log2+(2k+1)\pi i,
\]

an off-seam family of zeros. The carrier remains selfadjoint and the source
coefficients remain positive.

## Consequence for Hilbert--Polya

We have now constructed a canonical selfadjoint operator directly from the
source, but the Riemann zeros are not its eigenvalues. They are zeros of one
rigged matrix coefficient

\[
E_0\mathsf H_fe_z.
\]

Selfadjointness constrains the spectrum of `mathsf H_f`; it does not generally
prevent a matrix coefficient against a moving character from vanishing away
from the seam.

This precisely separates the valid Hilbert--Polya resemblance from the
missing theorem.

## New singular gate

The source Hankel correspondence is now the correct common object. RH would
require an additional law tying its distinguished endpoint covector and
character orbit to a positive or de Branges geometry. Candidate formulations
must explain why the endpoint matrix coefficient of this particular theta
Hankel operator can vanish only when the character is unitary.

The hostile matrix above is the acceptance test. Any law implied merely by:

- a real symmetric Hankel carrier;
- positive source coefficients;
- a character orbit;
- endpoint evaluation;

has no RH force.

## Scope

This constructs the common history correspondence and proves its
selfadjointness under the theta decay hypothesis. It also proves that these
facts alone do not confine endpoint zeros. It does not establish the extra
theta/modular law needed to reject the hostile two-cell carrier.
