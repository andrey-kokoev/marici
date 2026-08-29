# The shear gate is quantitatively derived once absolute scales are frozen

## Relation to the loading operator

On reduced supports define

\[
L=D^{-1/2}C^{*}A^{-1/2}
\]

and

\[
X=CD^{-1}.
\]

The exact relation is

\[
X
=
A^{1/2}L^{*}D^{-1/2}.
\]

Consequently,

\[
\|X\|
\le
\|A^{1/2}\|\,\|L\|\,\|D^{-1/2}\|.
\]

Thus triangular shear boundedness is not algebraically implied by the dimensionless loading margin alone. But it is quantitatively derived once three inputs are uniform:

\[
\sup\|A\|<\infty,
\qquad
\sup\|L\|<1,
\qquad
\inf\lambda_{\min}(D)>0.
\]

For the reciprocal auxiliary pair,

\[
D_\pm\ge s_0\delta_{\mathrm{aux}}I,
\]

so

\[
\|X_\pm\|
\le
\sqrt{
\frac{\|A\|}{s_0\delta_{\mathrm{aux}}}
}
\,
\|L_\pm\|.
\]

Therefore the shear is best recorded as an explicit realization gate, but it need not be treated as independent source data if the absolute endpoint upper scale and auxiliary lower scale have already been proved.

## Exact triangular condition number

Let

\[
T_X=
\begin{pmatrix}
I&X\\
0&I
\end{pmatrix}.
\]

On Hilbert direct sums,

\[
\|T_X\|
=
\|T_X^{-1}\|
=
\frac{
\sqrt{\|X\|^2+4}+\|X\|
}{2}.
\]

This follows by restricting to singular-vector pairs approaching the top singular value of \(X\). Hence

\[
\|T_X^{-1}\|^{-2}
=
\frac{4}{
\left(\sqrt{\|X\|^2+4}+\|X\|\right)^2
}.
\]

If

\[
m_{\mathrm{diag}}
=
\min\{
\lambda_{\min}(G_{\mathrm{eff}}),
\lambda_{\min}(D)
\},
\]

then the exact norm-based lower estimate is

\[
\mathcal G
\ge
m_{\mathrm{diag}}
\frac{4}{
\left(\sqrt{\|X\|^2+4}+\|X\|\right)^2
}
I.
\]

The simpler \((1+\|X\|)^{-2}\) factor is valid but nonsharp.

## Source-frame inventory

A complete local certificate can therefore be organized as:

- dimensionless internal margin \(\delta_{\mathrm{aux}}\);
- dimensionless loading margin \(\delta_{\mathrm{load}}\);
- lower auxiliary scale \(s_0\);
- lower endpoint scale \(a_0\);
- upper endpoint scale \(a_1=\sup\|A\|\).

Then

\[
M_{\mathrm{shear}}
\le
\sqrt{
\frac{a_1}{s_0\delta_{\mathrm{aux}}}
}
(1-\delta_{\mathrm{load}}).
\]

This formula closes the shear gate if all five quantities are source-normalized uniformly. Otherwise \(M_{\mathrm{shear}}\) remains an independent obligation.

## Why the endpoint upper scale matters

The loading operator normalizes incidence by \(A^{-1/2}\). Increasing \(A\) can keep \(\|L\|\) fixed or small while making the unnormalized incidence and shear arbitrarily large.

This is exactly the hostile

\[
D=I,
\qquad
G_{\mathrm{eff}}=I,
\qquad
C=nI,
\qquad
A=(n^2+1)I.
\]

Here

\[
\|L\|=\frac{n}{\sqrt{n^2+1}}\to1,
\]

so the loading margin actually collapses. A sharper hostile with a fixed loading margin \(\ell<1\) takes

\[
A_n=n^2I,
\qquad
C_n=\ell n I,
\qquad
D=I.
\]

Then \(\|L_n\|=\ell\) is fixed, while \(\|X_n\|=\ell n\to\infty\), and the full-block coercivity in the original source frame collapses despite fixed dimensionless margins.

## Completion statement

The local realization theorem should either:

1. prove \(A\) uniformly bounded above and derive the shear estimate from the nested margins and auxiliary scale; or
2. retain \(M_{\mathrm{shear}}\) as a separate bound when the source topology allows endpoint scale growth.

This prevents double-counting the shear as a new conceptual margin while preserving its indispensable role in source-frame completion.
