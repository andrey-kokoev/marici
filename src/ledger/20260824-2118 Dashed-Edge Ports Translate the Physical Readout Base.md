# 2118 — Dashed-Edge Ports Translate the Physical Readout Base

## Hard-to-vary claim

The dashed-edge Kummer adapter commutes with the source site-energy convolution only after translating the external-energy base at both endpoints of the deleted edge.

It is therefore not an endomorphism of a fixed-kinematics physical readout.

## Source objects

Equation (2.26) of arXiv:2401.05207 maps a universal correlator integrand to a physical correlator by the site convolutions

\[
(I_Xf)=\int_{\mathbb R}dx\,\widetilde\lambda(x-X)f(x).
\]

For an edge `e=(s,t)`, Entry 2115 typed the dashed operation as

\[
(T_ef)(x_s,x_t,y_e)
=
\frac1{y_e}f(x_s+y_e,x_t+y_e).
\]

## Exact comparison

Changing variables

\[
u_s=x_s+y_e,
\qquad
u_t=x_t+y_e
\]

gives

\[
\boxed{
I_{X_s,X_t}\,T_e
=
\frac1{y_e}
I_{X_s+y_e,X_t+y_e}.
}
\]

The real integration chain translates without a boundary term, but the convolution kernel is evaluated at translated external energies.

## Consequence

The source adapter has three typed layers:

\[
\text{deleted graph coefficient}
\xrightarrow{\text{endpoint pullback}}
\text{common kinematic base}
\xrightarrow{\mathcal K_{y_e^{-1}}}
\text{dashed integrand}
\xrightarrow{I_X}
\text{translated physical readout}.
\]

Thus edge deletion does not compare two coefficient objects over the same physical base point. Any fixed-kinematics comparison requires an additional transport back from

\[
(X_s+y_e,X_t+y_e)
\quad\text{to}\quad
(X_s,X_t).
\]

The primary source does not identify this return transport with a cube differential.

## Relevance to \(\mathcal Q\)

The pre-integration deletion carrier remains \(\mathcal Q\)-free. However, the adapter samples coefficient systems along translated external-energy loci before loop integration. A polynomial may therefore enter the **integrated pushforward discriminant** even though it is absent from every static deletion port.

This is a legitimate surviving home for a successor of \(\mathcal Q\), provided it is derived from the pushforward critical locus rather than fitted to the known quartic.

## Next falsifier

For the homogeneous three-site loop, form the source-derived map

\[
(X_1,X_2,X_3;y_{12},y_{23},y_{31})
\mapsto
(X_1+\Sigma_1,X_2+\Sigma_2,X_3+\Sigma_3),
\]

where `Sigma_i` is the sum of deleted incident-edge energies. Compute the critical/discriminant locus of this translated family under the frozen loop pushforward. Test whether it produces the source quartic or only existing soft, energy, Gram, and Landau support.

No conclusion about \(\mathcal Q\) is authorized before that elimination.

