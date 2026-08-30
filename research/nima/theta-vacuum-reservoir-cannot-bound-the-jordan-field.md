# A vacuum reservoir cannot bound the Jordan field

## Status

Exact finite-level no-go theorem correcting the first Fock-square proposal. The
factorially prolonged Green diagonal is the identity on jet Fock space, while
the Jordan current is an unbounded field quadrature. No finite vacuum reservoir
can make their sum positive. A source-derived number energy is necessary.

## Two-level compression

Let

\[
P=i(a^*-a)
\]

on the finite-jet core. Compress to

\[
V_m=\operatorname{span}\{e_{m-1},e_m\}.
\]

The compressed matrix is, up to the orientation convention,

\[
P|_{V_m}
=
\begin{pmatrix}
0&-i\sqrt m\\
i\sqrt m&0
\end{pmatrix}.
\]

Its eigenvalues are

\[
\pm\sqrt m.
\]

Therefore the field quadrature has arbitrarily large positive and negative
Rayleigh values on finite jet packets.

## Finite vacuum failure

Let \(c\) and \(\lambda\neq0\) be real. On a suitable unit vector in \(V_m\),

\[
\langle cI+\lambda P\rangle
=
c-|\lambda|\sqrt m.
\]

Whenever

\[
m>\frac{c^2}{\lambda^2},
\]

this value is negative.

Thus every proposed finite vacuum repair has a finite jet-order falsifier. The
failure does not require completion.

## Required number energy

The number operator

\[
N=a^*a
\]

grows like \(m\) on level \(m\), fast enough to control the \(\sqrt m\) field
coupling. The exact square is

\[
N+\lambda P+\lambda^2I
=
(a+i\lambda I)^*(a+i\lambda I)
\geq0.
\]

Both additions relative to the native identity-plus-field form are essential:

- \(N\) controls high jet order;
- \(\lambda^2I\) supplies the vacuum shift.

## Source gate

The native factorial Green prolongation supplies

\[
I+\lambda P,
\]

not the oscillator square. A valid theta construction must identify a labelled
current whose jet-level weight is exactly \(m\).

The prime-square Tate current is a natural candidate because it is the first
Hilbert-level non-trace-class boundary current, but this role is not proved. Its
incidence with the jet module and its normalization must be derived at finite
cutoff.

The primitive forcing reservoir can supply only an identity-type vacuum line;
it cannot replace the missing number growth.

## Agreement with the band obstruction

The globally negative terminal current

\[
Q_a(R)<0
\]

for all finite \(R>0\) shows that increasing consecutive-band width never
creates the missing positive bulk. The Fock theorem gives the jet analogue:
increasing jet depth eventually defeats every identity-only reservoir.

Both filtrations demand a scale-growing control term rather than a fixed
boundary constant.

## Finite falsifier

Given claimed coefficients \(c\) and \(\lambda\), choose

\[
m>rac{c^2}{\lambda^2}.
\]

The negative eigenvector of the displayed two-level matrix falsifies
positivity. A compiler need not construct the full infinite Fock space.

## Decisive conclusion

The jet-Fock algebra organizes the Jordan residual but does not orient it with
the native Green norm. A fixed primitive vacuum reservoir is categorically the
wrong growth type. The next source question is exact: which arithmetic boundary
operation, if any, supplies the number operator on spectral jets?

Without that operation, every proposed positive completion fails at a finite
jet order.
