---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Kummer-Normalized Rees Gauge Removes the Primitive Double Pole

## Narrow result

Entry 292 found, in the raw primitive two-wall frame,
\[
\nabla_E\Omega_{111}=\frac{e_6}{8E^2}+\frac{R_{\rm raw}}E+O(1).
\]
The leading class is on the established invariant algebraic line
\(\langle e_6\rangle\subset\mathcal T_7\), whose source normalization is
\[
\nabla e_6=-\frac12d\log H\,e_6,\qquad
H=z^2((E^2-y^2)(E^2-x^2)+E^2z^2).
\]
For fixed \(x,y\), with \(z=E-x-y\), the Rees lift
\[
\boxed{\widehat\Omega_{111}=\Omega_{111}+\frac{e_6}{8E}}
\]
has no double pole. The higher-normal term is therefore an
existing-coefficient Rees extension, not a new carrier stratum.

## Exact normal calculation

Put \(s=x+y\) and
\[
J(E)=(E^2-y^2)(E^2-x^2)+E^2(E-s)^2,\qquad H(E)=(E-s)^2J(E).
\]
Then
\[
J(0)=x^2y^2,\quad J'(0)=0,\quad
H(0)=s^2x^2y^2,\quad H'(0)=-2sx^2y^2,
\]
so
\[
-\frac12\partial_E\log H\big|_{E=0}=\frac1{x+y}.
\]
Consequently
\[
\nabla_E\left(\frac{e_6}{8E}\right)
=-\frac{e_6}{8E^2}+\frac{e_6}{8E(x+y)}+O(1).
\]
This fixes both the sign of the Rees correction and the induced logarithmic
coefficient
\[
\boxed{\operatorname{Res}^{e_6}_{E=0}
(\nabla\widehat\Omega_{111})=\frac{e_6}{8(x+y)}.}
\]

## Reconstructed logarithmic residue

Combining this correction with the fixed coordinates of the exact
degree-four and degree-five reductions gives
\[
\begin{aligned}
\operatorname{Res}_{E=0}(\nabla\widehat\Omega_{111})\equiv{}&
\Omega_{111}-\frac{\Omega_{101}}{2y}-\frac{\Omega_{110}}{2x}
+\frac{e_6}{8(x+y)}\\
&-\frac{(x-y)^2}{8x^2y^2}e_7
+\frac{y-x}{4x^2y^2(x+y)}e_8
+\frac{x-y}{4x^2y^2(x+y)}e_9
\end{aligned}
\]
modulo holomorphic absolute and exact-form gauge.

The quotient coefficients and final-block tail are exact rational
reconstructions from \((x,y)=(2,3),(3,2),(2,5)\), with degree-four to
degree-five stabilization at \((2,3)\). They remain finite evidence until
a cleared identity over \(\mathbb Q(x,y)\) is derived.

## Infinity-Gysin test

At \(E=0\),
\[
R_\infty^{(0)}=e_7+\frac{y^2}{2}e_8+\frac{x^2}{2}e_9,\qquad
R_\infty^{(2)}=-\frac{x^2}{2}(e_8+e_9).
\]
The displayed tail gives
\[
R_\infty^{(0)}=R_\infty^{(2)}=0.
\]
Since \(R_\infty(e_6)=0\), every fixed absolute residue term lies in
\(\mathcal T_7\). The regularization does not modify the elliptic quotient.

## Classification

\[
\begin{array}{c|c}
E^{-2}e_6/8\text{ in raw frame}&\text{Rees gauge on existing }\mathcal T_7\\
e_6/[8(x+y)]&\text{Tate/Kummer coefficient data}\\
e_7,e_8,e_9\text{ tail}&\text{algebraic kernel }\mathcal T_7\\
\mathcal Q&\text{absent from the total-energy residue}\\
\text{new carrier incidence}&\text{none}
\end{array}
\]

Thus the first higher-normal correction supports the shared-carrier,
sector-specific-coefficients hypothesis.

## Qualifications and next falsifier

Established, conditional on the already source-normalized Kummer
identification of \(e_6\): cancellation of the raw double pole, the
induced \(e_6/[8(x+y)]\) residue, zero elliptic Gysin image, and no new
carrier datum at this order.

Still open: a universal cleared reduction, uniqueness outside the normalized
\(e_6\) line, the regular \(E^0\) extension, the home of \(\mathcal Q\)
there, and compatibility with the physical chain.

The next finite falsifier is to perform the Rees-shifted two-wall reduction
over \(\mathbb Q(x,y)\), demand the displayed universal residue, and then
compute the regular term. Failure requiring a new incidence divisor rather
than an existing relative/algebraic coefficient class is the next
carrier-level falsifier.
