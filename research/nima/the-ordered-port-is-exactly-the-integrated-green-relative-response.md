# The ordered port is exactly the integrated Green relative response

## Reciprocal tails

For a source `f` on the positive scale line, define

\[
u(q)=\int_q^\infty e^{z(v-q)}f(v)\,dv,
\qquad
v(q)=\int_q^\infty e^{-z(v-q)}f(v)\,dv.
\]

Then

\[
u'=-zu-f,
\qquad
v'=+zv-f.
\]

Their difference is

\[
u(q)-v(q)
=\int_q^\infty
2\sinh(z(v-q))f(v)\,dv.
\]

The relative Green response is

\[
r_\Delta(q)=-f(q)(u(q)-v(q)).
\]

## Ordered source port

Extend `f` by zero to the negative half-line and define

\[
a_z(q)=f(q)e^{-zq},
\qquad
b_z(v)=f(v)e^{zv}.
\]

For the order operator

\[
(Sh)(q)=\int_{\mathbb R}\operatorname{sgn}(v-q)h(v)\,dv,
\]

the ordered pairing is

\[
C_f(z)=\langle a_z,Sb_z\rangle.
\]

Antisymmetry across the diagonal gives

\[
C_f(z)
=
2\int_{v>q}
f(q)f(v)\sinh(z(v-q))\,dq\,dv.
\]

Substituting the reciprocal-tail difference yields

\[
C_f(z)=-\int_0^\infty r_\Delta(q)\,dq.
\]

Thus the inverse-derivative ordered port is not merely analogous to the forcing defect. It is its integrated source realization, with sign fixed by the response convention.

## Atomic labelled form

For

\[
f=\sum_i f_i\delta_{q_i},
\qquad q_1<\cdots<q_n,
\]

one has

\[
C_f(z)
=
\sum_{i<j}f_if_j
\left(e^{z(q_j-q_i)}-e^{-z(q_j-q_i)}\right),
\]

and

\[
\sum_i r_{\Delta,i}=-C_f(z).
\]

The diagonal contributes zero because the order kernel is antisymmetric.

## Analytical gate

The identity extends whenever Fubini is valid for

\[
|f(q)f(v)\sinh(z(v-q))|
\]

on the ordered half-plane. The completed theorem must place the order operator and both reciprocal Green tails on one common rigged core and preserve the relative response coordinate through Fourier--Tate transport.

## Verification

`research/nima/checkers/check_two_shell_ordered_port_equals_green_relative_response.py` verifies the identity as an exact Laurent-polynomial equality on a nontrivial three-shell rational fixture.
