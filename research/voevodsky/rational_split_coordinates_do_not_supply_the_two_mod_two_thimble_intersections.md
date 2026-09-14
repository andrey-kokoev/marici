# Rational split coordinates do not supply the two mod-two thimble intersections

## Question

Can the source-defined algebraic frame on the final four coordinates provide the two required intersection functionals directly?

## Source frame

The marked-extension calculation orders the final coordinates as

\[
(e_6,e_7,e_8,e_9)
\]

and gives

\[
k_0=(1,0,0,0),
\qquad
k_1=(0,\alpha,\beta,\gamma),
\]

where

\[
\alpha=(1-y^2)(y^2-u^4),
\quad
\beta=2(u^2+y^2),
\quad
\gamma=-2y^2(u^2+1).
\]

The source calls the corresponding plane

\[
\mathcal A_{--}=\mathbb Z\langle e_6,v_{\rm alg}\rangle.
\]

Over the rational function field, a vector \(b=(b_0,b_1,b_2,b_3)^T\) in this plane has coefficients

\[
c_1=\frac{b_1}{\alpha},
\qquad
c_0=b_0-hc_1,
\]

with

\[
h=\frac{u(u+v)(u+v-4)P_6}{4}.
\]

These are the apparent coordinate duals to \(v_{\rm alg}\) and \(e_6\).

## Why they are not the required intersections

The required bits are integral Betti pairings of a globally embedded relative thimble:

\[
a=\langle\widetilde{\mathcal T}_\delta,e_6^\vee\rangle\pmod2,
\qquad
b=\langle\widetilde{\mathcal T}_\delta,v_{\rm alg}^\vee\rangle\pmod2.
\]

The displayed \(c_0,c_1\) are rational de Rham split coordinates of final columns. No source comparison identifies them with integral Betti cocycles evaluated on \(\widetilde{\mathcal T}_\delta\).

Moreover, direct reduction modulo two is not defined by these formulas. The coefficient \(c_1\) requires inversion of the nonunit \(\alpha\), while \(h\) contains division by four. Reduction of the frame itself gives

\[
\beta\equiv\gamma\equiv0\pmod2,
\qquad
k_1\equiv(0,\bar\alpha,0,0),
\]

but the splitting formula for \(c_0\) does not survive as an integral mod-two functional.

## Direct-calculation attempt

If a source-normalized thimble column \(b_{\mathcal T}\) in this final frame were supplied together with an integral Betti--de Rham comparison, one could test divisibility by \(\alpha\), remove the denominator in \(h\), and compare the resulting integral coefficients with the two intersection numbers.

No current artifact supplies such a thimble column. Existing marked-extension columns concern Gauss--Manin derivatives of labelled quotient generators and prove generic support, not the integral homology class of the Picard--Lefschetz thimble.

## Disposition

The direct mod-two calculation cannot be performed from the available split frame. The source provides rational coordinate projections but not the two integral dual cocycles or the thimble's coordinates against them. Treating \(c_0,c_1\) as the desired parity pair would silently replace an integral Betti comparison by a localized de Rham splitting.
