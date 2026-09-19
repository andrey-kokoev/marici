# The ordered-port Green-response identity extends entirely on the completed theta source

## Weighted source domain

Let `f` be a measurable source on the positive scale line satisfying

\[
\int_0^\infty |f(q)|e^{Aq}\,dq<\infty
\]

for every `A>0`. The completed theta forcing has this property because its logarithmic-coordinate tail is superexponential.

For `z` in a compact set `K`, put

\[
A_K=\sup_{z\in K}|\operatorname{Re}z|.
\]

On the ordered half-plane `v>q`,

\[
|\sinh(z(v-q))|
\le e^{A_K(v-q)}.
\]

Therefore

\[
\int_{v>q}
|f(q)f(v)\sinh(z(v-q))|\,dq\,dv
\le
\left(\int_0^\infty|f(q)|e^{-A_Kq}\,dq\right)
\left(\int_0^\infty|f(v)|e^{A_Kv}\,dv\right).
\]

The right side is finite and independent of `z` in `K`.

## Entire ordered port

Absolute Fubini is valid, and

\[
C_f(z)
=
2\int_{v>q}f(q)f(v)\sinh(z(v-q))\,dq\,dv
\]

is entire. Every parameter derivative is obtained under the integral because each factor `(v-q)^n` is absorbed by a slightly stronger exponential majorant.

## Green incidence

Define

\[
u_z(q)=\int_q^\infty e^{z(v-q)}f(v)\,dv,
\qquad
v_z(q)=\int_q^\infty e^{-z(v-q)}f(v)\,dv.
\]

The same majorants place both tails and their parameter derivatives on the common weighted source core. Since

\[
u_z(q)-v_z(q)
=2\int_q^\infty\sinh(z(v-q))f(v)\,dv,
\]

absolute Fubini yields

\[
C_f(z)
=-\int_0^\infty r_\Delta(q;z)\,dq,
\qquad
r_\Delta(q;z)=-f(q)(u_z(q)-v_z(q)).
\]

Thus the finite labelled identity extends to the completed theta forcing as an identity of entire functions.

## Scope

This closes the analytic-domain and Fubini gate for the ordered source port. The remaining comparison is functorial: prove that Fourier--Tate completion transports this ordered current into the declared relative boundary line while retaining its odd reciprocal character and degree-minus-one dilation law.
