# The first mixed D-V square is Fourier reciprocity, not literal commutation

## Question

Does the Fourier quarter-turn direction commute literally with the source-to-geometric semilocal presentation map?

## Claim boundary

No. The exact first mixed square is twisted by inversion in the scaling group. This is a source-derived equality on the half-density scaling carrier.

For \(a\in C_S\), let the unitary scaling action be

$$
(U_S(a)f)(x)=|a|_S^{-1/2}f(a^{-1}x).
$$

A change of variables in the additive Fourier integral gives

$$
F_SU_S(a)F_S^{-1}=U_S(a^{-1}).
$$

For an integrated observer

$$
U_S(h)=\int_{C_S}h(a)U_S(a)\,d^*a,
$$

define reciprocal reflection by

$$
(\iota h)(a)=h(a^{-1}).
$$

Haar invariance then gives

$$
F_SU_S(h)F_S^{-1}=U_S(\iota h).
$$

Writing the source-to-geometric constructor as \(C_{12}(h)=U_S(h)\), the mixed square is

$$
\operatorname{Ad}_{F_S}C_{12}=C_{12}\iota.
$$

Thus the vertical action on the source presentation is reciprocal reflection \(\iota\), while the vertical action on the geometric presentation is Fourier conjugation. They are intertwined by \(C_{12}\); they are not the same endomorphism on one carrier.

## Consequence for six mixed squares

For each presentation \(V_i\), one must first construct its own vertical action \(\rho_i\). The required equations are

$$
\rho_jC_{ij}=C_{ij}\rho_i.
$$

The first action pair is now explicit:

$$
\rho_1=\iota,
\qquad
\rho_2=\operatorname{Ad}_{F_S}.
$$

The remaining independent work is to identify \(\rho_3\) on the canonical-dual spectral pair and \(\rho_4\) on the complete trace observer. Once source-rooted squares for \(C_{13}\) and \(C_{14}\) are proved, the other three squares follow by composition on the observer-generated essential images.

## Disposition

One of the six mixed squares is analytically constructed. Literal commutation by one symbol \(\mathcal F_k\) was incorrectly typed; the correct structure is equivariance among presentation-dependent vertical actions.