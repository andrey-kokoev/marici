# The half-density covariant derivative kills the leading Mellin-wall tail

## Correction to the naive derivative comparison

For one theta label,

\[
(\mathcal M_nf)(u)
=
\sqrt n\,e^{u/2}f(ne^u).
\]

The additive derivative is not transported to \(D_u\). The exact
intertwining law is

\[
\mathcal M_nD_x
=
\frac1n e^{-u}
\left(
D_u-\frac12
\right)
\mathcal M_n.
\]

Thus the source-typed logarithmic derivative is the half-density covariant
operator

\[
\nabla_{1/2}
=
D_u-\frac12,
\]

followed by the label-dependent factor \(n^{-1}e^{-u}\).

The prior asymptotic mismatch with \(D_u\Psi_p^{\mathrm{rel}}\) correctly
rejects the identity chart, but \(D_u\) is not itself the transported
Stieltjes derivative.

## Wall annihilation

The relative theta packet begins

\[
\Psi_p^{\mathrm{rel}}(u)
=
a_{0,p}e^{u/2}
+
a_{1,p}e^{3u/2}
+
O(e^{5u/2}),
\]

where

\[
a_{0,p}
=
-2\pi L^2\zeta\!\left(-\frac12\right),
\]

and

\[
a_{1,p}
=
8\pi L\zeta\!\left(-\frac32\right).
\]

Since

\[
\nabla_{1/2}e^{u/2}=0,
\]

the leading relative wall jet is annihilated exactly:

\[
\nabla_{1/2}\Psi_p^{\mathrm{rel}}(u)
=
a_{1,p}e^{3u/2}
+
O(e^{5u/2}).
\]

After the physical factor \(e^{-u}\),

\[
e^{-u}\nabla_{1/2}\Psi_p^{\mathrm{rel}}(u)
=
a_{1,p}e^{u/2}
+
O(e^{3u/2}).
\]

The half-density connection therefore removes the first wall jet before the
additive derivative is reconstructed.

## Labelwise order is forced

The remaining factor \(n^{-1}\) is attached to each theta label:

\[
B_n
=
\frac1n e^{-u}\nabla_{1/2}.
\]

There is no source authority for replacing all \(B_n\) by one common operator
after summing labels. Hence the correct comparison order is

\[
\text{label packet}
\longrightarrow
B_n
\longrightarrow
\text{label synthesis},
\]

not

\[
\text{label synthesis}
\longrightarrow
D_u.
\]

This is exactly the grade-minus-one shifted connection channel found earlier.

## Revised comparison target

Let \(\Psi_{p,n}^{\mathrm{rel}}\) denote the labelwise relative packet. The
source candidate for the differentiated theta side is

\[
\mathcal B_p
=
\sum_{n\ge1}
B_n\Psi_{p,n}^{\mathrm{rel}},
\]

with the wall subtraction performed in the declared coefficient packet.

The remaining first-edge identity must compare the transported and
tail-propagated form of \(\mathcal B_p\) with

\[
b_p
=
U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0.
\]

This is narrower than an arbitrary scale transport: its differential part is
already fixed by half-density covariance.

## Analytic benefit

The factor \(n^{-1}\) improves label summability, and the covariant derivative
kills the slowest \(e^{u/2}\) relative jet before multiplication by
\(e^{-u}\). The output still has an \(e^{u/2}\) negative-end tail, so tail
propagation or the final Green comparison remains nontrivial.

## Hostile

Differentiate the synthesized scalar packet with \(D_u\). This preserves
local smoothness but:

- retains a wall jet that the half-density connection must kill;
- loses the label factor \(n^{-1}\);
- uses the wrong completion grade.

It therefore cannot define the Adams comparison even if a fitted bounded map
later sends its output to the Stieltjes boundary.
