# The four-front Stieltjes boundary requires both completion curvature and a transported base channel

## Translation boundary operator

Let

\[
T_L
=
U_{-2L}-U_{2L}-U_{-L}+U_L,
\]

so that

\[
b_p=T_Lf_0,
\qquad
L=\log p.
\]

Let

\[
P=A(A+1),
\qquad
A=xD_x.
\]

Applying \(P\) to the boundary gives the exact decomposition

\[
Pb_p
=
T_LPf_0+[P,T_L]f_0.
\]

The first term is the transported base completion channel. The second is the
translation-curvature channel.

## Base channel

On the Gaussian seed,

\[
Af_0=-2\pi f_2,
\]

and

\[
A^2f_0=-4\pi f_2+4\pi^2f_4.
\]

Therefore

\[
Pf_0
=
-6\pi f_2+4\pi^2f_4.
\]

The base contribution is explicitly

\[
T_LPf_0
=
T_L
\left(
-6\pi f_2+4\pi^2f_4
\right).
\]

It is nonzero and cannot be reconstructed from a commutator packet alone.

## Curvature channel

For any signed displacement \(a\),

\[
[P,U_a]f_0
=
U_ag_a,
\]

where

\[
g_a
=
-2a(A+1)Df_0+a^2D^2f_0.
\]

Hence

\[
\begin{aligned}
[P,T_L]f_0
={}&
U_{-2L}g_{-2L}
-
U_{2L}g_{2L}\\
&-
U_{-L}g_{-L}
+
U_Lg_L.
\end{aligned}
\]

Thus the full curvature target requires both scales \(L\) and \(2L\), on both
reciprocal rays. The single \(g_L\) packet is only one cell increment.

## Exact reconstruction form

On a reduced support where the Green inverse of \(P\) is source-authorized,

\[
b_p
=
P_{\mathrm{red}}^{-1}
\left(
T_LPf_0+[P,T_L]f_0
\right).
\]

If \(P\) has a radical, this formula must instead be stated in the quotient
form, after proving that the complete right-hand side annihilates the radical.
No pseudoinverse may be inserted before that check.

This identifies the intended tail/Green propagation much more sharply: it is
a reduced completion resolvent applied to the sum of a base channel and a
curvature channel.

## Consequence for the five-grade packet

The five-grade differentiated packet computed from \(g_L\) resolves one
curvature increment. It cannot by itself equal \(b_p\), even after a bounded
tail convolution, unless the constructor also supplies:

1. the reciprocal \(g_{-L}\) packet;
2. the outer-scale packets \(g_{\pm2L}\);
3. the transported base term \(T_LPf_0\);
4. the reduced inverse or equivalent Green solution operator.

This is the exact missing assembly inventory.

## Reciprocal typing

The base term and commutator term have different internal characters, but
their sum has the character of \(Pb_p\). Projecting to the odd curvature
channel before adding the base channel changes the complete Green source and
cannot reconstruct the even Stieltjes boundary.

## New finite target at \(p=2\)

At \(L=\log2\), every source vector in

\[
T_LPf_0+[P,T_L]f_0
\]

is an explicit translated polynomial Gaussian. The first-prime test can
therefore be performed entirely on a finite list of grades and translations
before theta-label synthesis.

The unresolved theorem is no longer an unspecified equality. It is whether
the source relative Green inverse transports this explicit complete source to
\(b_2\) while preserving the wall and reciprocal ports.

## Hostile

Use only \([P,T_L]f_0\) and invert \(P\). This reproduces the transport defect
but omits \(T_LPf_0\). The result can have the correct odd orientation and
still fail the exact boundary identity because curvature measures failure of
commutation, not the transported state itself.
