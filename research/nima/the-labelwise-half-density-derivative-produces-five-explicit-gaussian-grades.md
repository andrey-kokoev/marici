# The labelwise half-density derivative turns the four-grade packet into five explicit Gaussian grades

## Source packet

For \(L=\log p\), let

\[
g_{p}
=
c_0f_0+c_1f_1+c_2f_2+c_3f_3,
\]

with

\[
(c_0,c_1,c_2,c_3)
=
(-2\pi L^2,\,8\pi L,\,4\pi^2L^2,\,-8\pi^2L).
\]

At theta label \(n\), the packet is

\[
\Psi_{p,n}=\mathcal M_ng_p.
\]

The source-typed logarithmic derivative satisfies

\[
B_n\mathcal M_n=\mathcal M_nD_x,
\qquad
B_n=\frac1n e^{-u}\left(D_u-\frac12\right).
\]

Hence

\[
B_n\Psi_{p,n}
=
\mathcal M_n(D_xg_p).
\]

## Five-grade calculation

For

\[
f_j(x)=x^je^{-\pi x^2},
\]

one has

\[
D_xf_j
=
jf_{j-1}-2\pi f_{j+1}.
\]

Collecting grades gives

\[
D_xg_p
=
a_0f_0+a_1f_1+a_2f_2+a_3f_3+a_4f_4,
\]

where

\[
a_0=8\pi L,
\]

\[
a_1=12\pi^2L^2,
\]

\[
a_2=-40\pi^2L,
\]

\[
a_3=-8\pi^3L^2,
\]

and

\[
a_4=16\pi^3L.
\]

Therefore

\[
B_n\Psi_{p,n}
=
\mathcal M_n
\left(
8\pi Lf_0
+
12\pi^2L^2f_1
-
40\pi^2Lf_2
-
8\pi^3L^2f_3
+
16\pi^3Lf_4
\right).
\]

This is the exact differentiated one-label comparison packet.

## Grade consequence

The correct derivative does not preserve the earlier four-grade carrier. It
produces the consecutive grades

\[
0,1,2,3,4.
\]

A comparison checker that retains only the original grades \(0,1,2,3\)
necessarily drops the \(f_4\) term

\[
16\pi^3Lf_4.
\]

Likewise, a parity-compressed checker misses that the differentiated packet
contains both even grades \(0,2,4\) and odd grades \(1,3\).

## Label synthesis

The transported label series is now explicitly

\[
\mathcal B_p(u)
=
\sum_{n\ge1}\mathcal M_n(D_xg_p)(u).
\]

On compact \(u\)-sets it converges with all derivatives by the same Gaussian
majorant as the four-grade packet. No abstract graph argument is needed for
local synthesis.

The factor \(n^{-1}\) in \(B_n\) has already been consumed by the exact
intertwining identity. It must not be applied a second time to the synthesized
five-grade formula.

## Wall-routing caveat

The common Mellin-wall residue is visible only after label assembly, while
\(B_n\) is labelwise. Therefore a complete constructor theorem must prove that
coefficient-wall routing commutes with the family

\[
\{B_n\}_{n\ge1}
\]

in the declared relative quotient. The five-grade calculation proves the
bulk action; it does not silently authorize exchanging wall subtraction and
labelwise differentiation.

## Revised finite target

For \(p=2\), the first finite comparison is no longer between an unspecified
theta derivative and the four-front boundary. It is between:

- the explicit five-grade label packet above;
- the source tail/Green propagation;
- the four-front Stieltjes packet
  \[
  b_2
  =
  U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0.
  \]

Thus the remaining unknown is the propagation/comparison map, not the input
column.

## Hostile

Differentiate the four coefficient grades formally while keeping a
four-dimensional target. The omitted \(f_4\) output is invisible at the
original truncation but changes label synthesis, wall asymptotics, and the
Green polarization.
