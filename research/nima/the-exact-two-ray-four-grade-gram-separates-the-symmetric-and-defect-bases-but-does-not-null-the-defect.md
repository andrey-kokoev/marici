# The exact two-ray four-grade Gram separates the symmetric and defect bases but does not null the defect

## Source-fixed two-ray packet

Use the four-grade vectors

\[
E=-2\pi L^2f_0+4\pi^2L^2f_2,
\qquad
O=8\pi Lf_1-8\pi^2Lf_3,
\]

and the directed rays

\[
g_+=U_L(E+O),
\qquad
g_-=U_{-L}(E-O).
\]

Their exact ordinary Hilbert Gram is

\[
G(L)=
\begin{pmatrix}
D(L)&C(L)\\
C(L)&D(L)
\end{pmatrix},
\]

where

\[
D(L)=\frac{3\pi^2L^4+7\pi L^2}{\sqrt2}
\]

and

\[
C(L)=\frac{e^{-2\pi L^2}}{\sqrt2}
\left(
16\pi^4L^8-72\pi^3L^6+67\pi^2L^4-7\pi L^2
\right).
\]

No coefficient is adjustable.

## Symmetric/defect diagonalization

The codiagonal and boundary coordinates

\[
g_{\rm sym}=g_++g_-,
\qquad
g_{\rm def}=g_+-g_-
\]

are orthogonal in the ordinary Hilbert metric and satisfy

\[
\|g_{\rm sym}\|^2=2(D+C),
\qquad
\|g_{\rm def}\|^2=2(D-C).
\]

Thus the exact source packet already realizes the proposed common-mode and
antisymmetric defect bases. The fourth Gaussian grade contributes to both
`D` and `C`; deleting it changes this decomposition.

## Finite first-prime check

For the source scale `L=log 2`,

\[
D\approx12.30398815999857,
\qquad
C\approx-0.7762358469493861,
\]

and therefore

\[
\|g_{\rm def}\|^2
=2(D-C)
\approx26.160448013895913>0.
\]

The ordinary four-grade Hilbert carrier retains a substantial antisymmetric
base. It does not turn the crossing defect into a null direction. The value is
not identified with the unchanged-Evans scalar `-0.150851...`; they have
different source types and normalizations.

## Consequence for the higher cell

The proposed complexity increase is real: the two rays produce independent
symmetric and defect coordinates. Closure can only occur after passage to the
completed relative Green form and its declared radical quotient. The missing
statement is precisely

\[
\mathfrak G_p^{\rm St}(e_j,e_k)
=
\mathfrak G_p^\theta
(Q_p^{\rm lin}e_j,Q_p^{\rm lin}e_k)
\]

for all four matrix units.

Ordinary Hilbert cancellation cannot substitute for this quadratic
representation theorem.