# The strong-feature and minimal-product sewing routes are two functorial completions with a strict implication

## Common angular carrier

For each character \(\chi\), let

\[
\mathcal S_{2,\chi}
\]

be the Hilbert--Schmidt boundary carrier and let

\[
\mathcal S_{1,\chi}
\]

be its trace-class product carrier.

The finite regulated sewing data are

\[
B_{\lambda,\chi}(g),
C_{\lambda,\chi}(g)
\in
\mathcal S_{2,\chi}.
\]

The target relative data are

\[
B_\chi^{rel}(g),
C_\chi^{rel}(g).
\]

## Strong-feature completion

Define the doubled positive feature

\[
\mathcal F_\lambda(g)
=
\bigoplus_\chi
\left(
B_{\lambda,\chi}(g),
C_{\lambda,\chi}(g)
\right)
\]

in

\[
\mathcal K^{str}
=
\bigoplus_\chi
\left(
\mathcal S_{2,\chi}
\oplus
\mathcal S_{2,\chi}
\right).
\]

Assume

\[
\|B_{\lambda,\chi}-B_\chi^{rel}\|_2
\longrightarrow0,
\qquad
\|C_{\lambda,\chi}-C_\chi^{rel}\|_2
\longrightarrow0
\]

and a common bound

\[
\|B_{\lambda,\chi}\|_2
+
\|C_{\lambda,\chi}\|_2
\le
M_G(\chi),
\qquad
\sum_\chi M_G(\chi)^2<\infty.
\]

Dominated convergence gives

\[
\mathcal F_\lambda(g)
\longrightarrow
\mathcal F^{rel}(g)
\]

in \(\mathcal K^{str}\).

Its positive Gram is

\[
G^{str}(g,h)
=
\sum_\chi
\left[
\langle B_\chi^{rel}(g),B_\chi^{rel}(h)\rangle_2
+
\langle C_\chi^{rel}(g),C_\chi^{rel}(h)\rangle_2
\right].
\]

The signed sewing readout is the bounded cross-polarization

\[
\mathcal E^{rel}(g,h)
=
\sum_\chi
\operatorname{Tr}
\left[
(B_\chi^{rel}(h))^*
C_\chi^{rel}(g)
\right].
\]

## Minimal-product completion

Define

\[
Z_{\lambda,\chi}(g,h)
=
B_{\lambda,\chi}(h)^*
C_{\lambda,\chi}(g)
\in
\mathcal S_{1,\chi}.
\]

Assume

\[
\|Z_{\lambda,\chi}-Z_\chi^{rel}\|_1
\longrightarrow0
\]

and

\[
\|Z_{\lambda,\chi}\|_1
\le
N_G(\chi),
\qquad
\sum_\chi N_G(\chi)<\infty.
\]

Then

\[
Z_\lambda
=
\bigoplus_\chi
Z_{\lambda,\chi}
\longrightarrow
Z^{rel}
\]

in trace norm, and

\[
\mathcal E_\lambda(g,h)
=
\operatorname{Tr}Z_\lambda(g,h)
\longrightarrow
\operatorname{Tr}Z^{rel}(g,h).
\]

This constructs the signed sewing modification directly.

## Strong implies product

Hölder's Schatten inequality gives

\[
\begin{aligned}
\|B_\lambda^*C_\lambda-B^*C\|_1
&\le
\|B_\lambda-B\|_2\|C_\lambda\|_2\\
&\quad+
\|B\|_2\|C_\lambda-C\|_2.
\end{aligned}
\]

Therefore every strong-feature certificate induces a minimal-product certificate.

This defines a forgetful completion map

\[
\mathsf{Sew}^{str}
\longrightarrow
\mathsf{Sew}^{prod}.
\]

## Strictness

The converse fails. On a one-dimensional source, set

\[
B_n=n,
\qquad
C_n=n^{-1}.
\]

Then

\[
B_n^*C_n=1
\]

for every \(n\), so the product route is constant and convergent. The first leg has unbounded Hilbert--Schmidt norm, so no strong-feature limit exists.

Hence minimal-product completion retains the signed trace while forgetting positive leg geometry.

## Functoriality

For a bounded observer map \(T:E'	o E\), pullback acts by

\[
B_\chi\longmapsto B_\chi T,
\qquad
C_\chi\longmapsto C_\chi T,
\]

and

\[
Z_\chi(g,h)
\longmapsto
T^*Z_\chi(g,h)T.
\]

Schatten ideal inequalities preserve both completion modes. Thus conductor restrictions and bounded convolution successors act functorially whenever their phase-energy multiplier bounds are supplied.

## Application target

For the semilocal sewing problem:

- the strong route is the desired positive rung-four lift;
- the product route is the signed relative Tate--Hardy comparison;
- the forgetful map records exactly which positive data are lost when only the trace-class product is completed.
