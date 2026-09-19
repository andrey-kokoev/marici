# The projective rapid-label space carries the entire Mellin observer through the seam

## Discrete rigging

Define the projective coefficient space

\[
\mathcal S_{\mathrm{lab}}
=
\bigcap_{a>0}\ell^2(\mathbb N,n^{2a})
\]

with seminorms

\[
p_a(c)^2=\sum_{n\ge1}|c_n|^2n^{2a}.
\]

Under the logarithmic coordinate `t=log n`, this is the discrete counterpart
of the exponential radial test space.

## Entire Mellin observer

For `s` in `C`, set

\[
L_s^+(c)=\sum_{n\ge1}c_n n^{-s}.
\]

Choose `a>1/2-Re(s)`. Cauchy--Schwarz gives

\[
|L_s^+(c)|
\le
p_a(c)
\left(\sum_{n\ge1}n^{-2(a+\operatorname{Re}s)}\right)^{1/2}
=
p_a(c)\sqrt{\zeta(2a+2\operatorname{Re}s)}.
\]

Thus `L_s^+` is a continuous dual vector for every `s`, including the seam.
On a compact parameter set one choice of `a` works uniformly.

Its parameter jets are

\[
\partial_s^jL_s^+(c)
=(-1)^j\sum_{n\ge1}c_n(\log n)^j n^{-s}.
\]

For the same `a`, enlarged slightly if necessary,

\[
\sum_{n\ge1}(\log n)^{2j}n^{-2(a+\operatorname{Re}s)}<\infty.
\]

Consequently `s -> L_s^+` is weakly entire in
`S_lab'`, with every fixed jet compact-locally equicontinuous.

## Reciprocal channel

The reciprocal observer

\[
L_s^-(c)=\sum_{n\ge1}c_n n^{s-1}
=L_{1-s}^+(c)
\]

is continuous and entire on the same rigging. Reciprocal reflection exchanges
`L_s^+` and `L_s^-`; it does not identify them. On the seam their coefficient
phases are reciprocal (`n^{-1/2-it}` and `n^{-1/2+it}`), and they coincide only
at the real central point. Their oriented boundary roles remain doubled.

## Full interval energy

The logarithmic multiplier preserves the test space continuously. Indeed, for
`b>a`,

\[
(\log n)^2n^{2a}\le C_{a,b}n^{2b}.
\]

Hence

\[
\mathcal E(c)=2\sum_{n\ge1}|c_n|^2\log n
\]

is finite and continuous on `S_lab`. Its kernel remains exactly the vacuum
line.

## What this constructs

This rigging supplies an explicit exterior Mellin observer and all of its jets
through the seam without pretending that the seam row `(n^{-1/2})` belongs to
unweighted `ell^2`. It is compatible with the logarithmic full-interval
operator and with reciprocal doubling.

It does not yet prove that the completed Euler synthesis, Hardy ordered port,
and five-wall Green current act continuously on this same projective carrier.
That common-carrier comparison is the remaining arithmetic boundary gate.
