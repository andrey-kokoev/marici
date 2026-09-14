# The conull idele-class orbit and Radon--Nikodym weight identify the semilocal quotient scaling action with the regular carrier

## Quotient carrier and its open orbit

Let

\[
A_S=
\prod_{v\in S}k_v
\]

be the semilocal additive space and

\[
J_S=A_S^*
=
\prod_{v\in S}k_v^*
\]

its idele locus. Let `O_S*` act diagonally. Connes's quotient carrier is

\[
X_S=A_S/O_S^*.
\]

The complement

\[
A_S\setminus J_S
\]

is the union of coordinate hyperplanes `x_v=0`. Each has additive Haar measure zero. Therefore `J_S` is conull in `A_S`, and

\[
\boxed{
J_S/O_S^*
=C_S
}
\]

is a conull open orbit in `X_S`.

Consequently restriction gives a unitary identification of `L2` spaces after the correct measure density is inserted; there is no additional positive-measure spectral-multiplicity sector coming from the zero-coordinate strata.

## Additive versus multiplicative measure

On `J_S`, additive and multiplicative Haar measures satisfy

\[
\boxed{
dx
=c_S|x|_Sd^*x
}
\]

for a normalization constant `c_S>0`. After quotienting by `O_S*`, whose elements have total semilocal module one, the density descends:

\[
d\mu_{X_S}(c)
=c_S|c|_Sd^*c
\qquad
(c\in C_S).
\]

Absorb `c_S` into the unitary normalization and define

\[
\boxed{
(W_S\xi)(c)
=|c|_S^{1/2}\xi(c).
}
\]

Then

\[
W_S:
L^2(X_S,d\mu_{X_S})
\xrightarrow{\sim}
L^2(C_S,d^*c).
\]

Values on the null complement are irrelevant.

## Scaling representation

Connes's normalized scaling representation is

\[
(U_S(a)\xi)(x)
=|a|_S^{-1/2}\xi(a^{-1}x).
\]

Compute on the conull orbit:

\[
\begin{aligned}
(W_SU_S(a)\xi)(c)
&=
|c|_S^{1/2}
|a|_S^{-1/2}
\xi(a^{-1}c)\\
&=
|a^{-1}c|_S^{1/2}
\xi(a^{-1}c)\\
&=
(W_S\xi)(a^{-1}c).
\end{aligned}
\]

Thus

\[
\boxed{
W_SU_S(a)W_S^{-1}
=\lambda_{C_S}(a),
}
\]

where `lambda_(C_S)` is the left regular representation.

After integration,

\[
\boxed{
W_SU_S(g)W_S^{-1}
=\lambda_{C_S}(g).
}
\]

This is an exact unitary intertwiner, not merely an asymptotic direct-integral comparison.

## Physical cutoff transport

The physical cutoff is multiplication by the module ball:

\[
P_\Lambda
=1_{\{|x|_S\le\Lambda\}}.
\]

Since `W_S` is itself multiplication by a function of `|x|_S`, it commutes with every module cutoff:

\[
\boxed{
W_SP_\Lambda W_S^{-1}
=P_\Lambda^{C_S}
=1_{\{|c|_S\le\Lambda\}}.
}
\]

Likewise,

\[
W_S(P_R-P_\Lambda)W_S^{-1}
=P_R^{C_S}-P_\Lambda^{C_S}.
\]

Therefore the cutoff commutators on `L2(X_S)` are unitarily transported to the regular group carrier. However, Connes's one-sided additive ball becomes `\{|c|_S\le\Lambda\}`, which has infinite multiplicative Haar volume toward zero. It is not the finite symmetric Folner window used in the regular boundary estimate.

## Fourier cutoff

The additive Fourier transform `F_S` on `X_S` transports to a unitary

\[
\mathscr F_S
=W_SF_SW_S^{-1}
\]

on `L2(C_S)`. It is not asserted to be the ordinary group Fourier transform on `C_S`.

Nevertheless

\[
Q_\Lambda
=F_SP_\Lambda F_S^{-1}
\]

transports to the orthogonal projection

\[
\mathscr Q_\Lambda
=
\mathscr F_SP_\Lambda^{C_S}
\mathscr F_S^{-1}.
\]

The commutator-density proof uses only

\[
\|Q_\Lambda T\|_{HS}
\le
\|T\|_{HS},
\]

so no identification of `mathscr F_S` with group Fourier transform is needed.

## Transfer of the exact boundary formula

Unitary invariance of Hilbert--Schmidt norm gives

\[
\|Q_\Lambda[P_i,U_S(g)]\|_{HS}
=
\|\mathscr Q_\Lambda
[P_i^{C_S},
\lambda_{C_S}(g)]
\|_{HS}.
\]

Unitary transport alone therefore does **not** imply the finite-volume regular-carrier estimate for Connes's actual cutoff. A symmetric auxiliary lower cutoff, a weighted additive-measure estimate, or a direct estimate for the combined product `P_\Lambda Q_\Lambda` is still required.

## Role of the orbit sum in Connes's proof

Connes's `O_S^*` orbit sum remains necessary for the quotient trace and local Weil terms. It may also be needed to prove the corrected weighted cutoff estimate.

## Revised status of bulk Gate A

The regular intertwiner is exact, but the finite-Haar-volume hypothesis fails for the transformed one-sided cutoff. Hence Bulk Gate A is not complete for Connes's actual cutoff.

## Remaining boundary gate

The unresolved problem is now entirely the relative boundary feature:

1. prove convergence, after two-copy bulk removal, of
   \[
   \mathfrak b_{\Lambda,R,S}(g)
   =
   (I-\Pi_{\Lambda,R,S}^{(2)})
   T_{\Lambda,R,S}(g);
   \]
2. identify its limiting Gram norm with the completed Weil form;
3. include the Sonin sector and endpoint--gamma boundary sewing;
4. prove independence, or controlled dependence, on the ratio
   \[
   \rho=
   \frac{\log R}{\log\Lambda}>1.
   \]

## Disposition

The multiplicity obstruction does not occur: the conull orbit gives `L^2(X_S)\cong L^2(C_S)` and `U_S\cong\lambda_{C_S}`. But the transformed physical cutoff has infinite multiplicative Haar volume. The remaining Gate-A obstruction is this cutoff-volume mismatch, not representation multiplicity.
