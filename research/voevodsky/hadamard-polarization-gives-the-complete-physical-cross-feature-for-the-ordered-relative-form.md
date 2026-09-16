# Hadamard polarization gives the complete physical cross feature for the ordered relative form

## Finite physical data

Fix a finite regulator and write

\[
P=P_\Lambda,
\qquad
A=P_R-P_\Lambda,
\qquad
R=P+A=P_R.
\]

Let \(Q^T\) and \(Q^0\) be the Tate and pure-reference Fourier projections on the same physical carrier. For an observer amplitude \(g\), put

\[
U_g=U_S(g).
\]

For \(q\in\{T,0\}\), define the two ordered physical rows

\[
x_q(g)=Q^qPU_g,
\qquad
y_q(g)=Q^qRU_g.
\]

Their cross Gram is

\[
\langle x_q(h),y_q(g)\rangle_{HS}
=
\operatorname{Tr}
\left(
U_h^*P Q^qR U_g
\right).
\]

Its Hermitian polarization is the physical ordered form

\[
H_q(g,h)
=
\frac12
\left(
\langle x_q(h),y_q(g)\rangle
+
\langle y_q(h),x_q(g)\rangle
\right).
\]

## Hadamard legs

Define

\[
\boxed{
X_q^+(g)
=\frac{x_q(g)+y_q(g)}2,
\qquad
X_q^-(g)
=\frac{x_q(g)-y_q(g)}2.
}
\]

The polarization identity gives

\[
\begin{aligned}
&\langle X_q^+(h),X_q^+(g)\rangle
-
\langle X_q^-(h),X_q^-(g)\rangle\\
&\qquad=
H_q(g,h).
\end{aligned}
\]

Thus each ordered physical form has a canonical positive-minus-positive realization derived from its actual two rows.

Because \(R=P+A\), the legs can also be written

\[
X_q^+(g)
=Q^q\left(P+\frac A2\right)U_g,
\]

\[
X_q^-(g)
=-\frac12Q^qAU_g.
\]

The sign of the second formula is irrelevant to its ordinary Gram but is retained for the cross-polarized chart.

## Tate/reference relative feature

The centered ordered relative form is

\[
D_{ord}=H_T-H_0.
\]

Define the complete positive legs

\[
\boxed{
X_{cross}^T
=X_T^+\oplus X_0^-,
}
\]

\[
\boxed{
X_{cross}^0
=X_T^-\oplus X_0^+.
}
\]

Their positive Grams are

\[
G_{cross}^T
=(X_T^+)^*X_T^+
+(X_0^-)^*X_0^-,
\]

\[
G_{cross}^0
=(X_T^-)^*X_T^-
+(X_0^+)^*X_0^+.
\]

Consequently

\[
\boxed{
G_{cross}^T-G_{cross}^0
=H_T-H_0
=D_{ord}.
}
\]

This is an exact finite-regulator identity. It requires no limit, trace asymptotic, commutation of the observer with a cutoff, or packetwise Jordan decomposition.

## Recovery of every window block

Expanding the four Hadamard Grams recovers the Hermitian combinations of

\[
P Q^qP,
\qquad
P Q^qA,
\qquad
A Q^qP,
\qquad
A Q^qA.
\]

Thus the complete feature retains the inside--annular cross seam omitted by the diagonal two-channel feature.

The ordered form itself uses

\[
H_q
=U^*
\left[
P Q^qP+
\frac12(P Q^qA+A Q^qP)
\right]U.
\]

The annular square \(AQ^qA\) appears equally in the positive and negative Hadamard legs and cancels in the signed readout. It remains available as common positive mass.

## Canonical common annular bulk

Indeed, direct expansion gives

\[
(X_q^+)^*X_q^+
=
H_q+
\frac14U^*AQ^qAU,
\]

\[
(X_q^-)^*X_q^-
=
\frac14U^*AQ^qAU.
\]

Hence the annular square is the positive bulk that makes the cross term into a difference of ordinary Grams.

For the Tate/reference doubled feature, the total common Hadamard mass is assembled from the two annular rows

\[
\frac12Q^TAU_g,
\qquad
\frac12Q^0AU_g.
\]

It is source-derived from the second physical cutoff and is not an arbitrary equal summand.

## Identification with the transported eight-leg residual

The eight-leg feature is obtained by applying the same two Hadamard operations:

1. Tate/reference common--difference splitting;
2. left/right placement common--difference splitting.

Therefore its positive legs \(E_+\Theta\) and \(E_-\Theta\) have the same source Grams as \(X_{cross}^T\) and \(X_{cross}^0\), respectively, provided both use the exact transported regulator and the same factor \(1/2\) convention.

Equality of source Grams gives canonical source-labelled partial isometries

\[
U_\alpha^T X_{cross}^T=E_+\Theta_\alpha,
\]

\[
U_\alpha^0 X_{cross}^0=E_-\Theta_\alpha
\]

on their generated ranges.

Thus, for the ordered **relative** physical feature,

\[
\boxed{
G_{cross}^{T,0}
=\widehat G^{T,0}.
}
\]

The common-remainder identity holds with zero remainder at the residual level.

## Absolute physical feature

If the physical Tate/reference features also retain an extensive common volume or mismatch-strip row \(B_\alpha\), define

\[
X_{phys}^T
=B_\alpha\oplus X_{cross}^T,
\]

\[
X_{phys}^0
=B_\alpha\oplus X_{cross}^0.
\]

Then

\[
\boxed{
G_{phys}^T
=B_\alpha^*B_\alpha+
\widehat G^T,
}
\]

\[
\boxed{
G_{phys}^0
=B_\alpha^*B_\alpha+
\widehat G^0.
}
\]

Therefore

\[
\boxed{
G_{phys}^T-
\widehat G^T
=
G_{phys}^0-
\widehat G^0
=B_\alpha^*B_\alpha
\succeq0.
}
\]

The only remaining analytic task for the absolute feature is to identify the retained extensive row \(B_\alpha\) with the independently normalized physical mismatch/volume feature. The cross-polarized relative alignment itself is exact.

## Polarity-cube interpretation

The two Hadamard legs are the opposite positive faces of the fixed-regulator polarity cube. The annular/common-volume rows form its shared central bulk. The signed ordered form is the Krein readout across the two faces.

No individual \(r\)-indexed sub-tetrahedron carries this identity. It is the metric filler over the full presentation tetrahedron at fixed regulator.

## Disposition

The authoritative complete physical relative features are

\[
\boxed{
X_{cross}^T=X_T^+\oplus X_0^-,
\qquad
X_{cross}^0=X_T^-\oplus X_0^+.
}
\]

They satisfy exactly

\[
\boxed{
G_{cross}^T-G_{cross}^0=D_{ord}.
}
\]

With the same Hadamard normalization as the transported eight-leg feature, their Grams agree with the Krein residual Grams. The formerly symbolic common-remainder theorem is therefore reduced to identification of one explicit extensive physical bulk row \(B_\alpha\), rather than positivity of an unnamed difference.
