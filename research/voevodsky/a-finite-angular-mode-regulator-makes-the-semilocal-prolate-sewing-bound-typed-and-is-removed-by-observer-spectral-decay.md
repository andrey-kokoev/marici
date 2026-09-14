# A finite angular-mode regulator makes the semilocal prolate sewing bound typed and is removed by observer spectral decay

## Radial and angular directions

Let

\[
C_S^1
=
\ker
\left(
|\cdot|_S:C_S\to\mathbb R_+^*
\right)
\]

be the norm-one subgroup. After quotienting by `O_S*`, it is compact in the semilocal setting used by Connes. Its dual

\[
\widehat{C_S^1}
\]

is discrete.

The module cutoff `P_Lambda` acts only on the radial coordinate. It does not suppress arbitrarily high angular characters.

## Finite angular projection

Choose an increasing finite family

\[
\Gamma_N
\subset
\widehat{C_S^1}
\]

closed under inversion, and let

\[
K_N
=
\sum_{\chi\in\Gamma_N}
K_\chi
\]

be the orthogonal projection onto those angular isotypic components.

Because the physical cutoff depends only on total module,

\[
[K_N,P_\Lambda]=0.
\]

Fourier transform exchanges an angular character with its inverse/dual. Inversion stability of `Gamma_N` gives, on the declared decomposition,

\[
[K_N,F_S]=0,
\qquad
[K_N,Q_\Lambda]=0.
\]

The second identity is conditional on the Fourier transform preserving precisely this angular decomposition; this must be checked for the chosen basic character and quotient model.

## Regulated prolate transition

Define

\[
B_{\Lambda,N}
=K_NP_\Lambda Q_\Lambda P_\Lambda K_N.
\]

Only finitely many angular sectors remain. If each radial sector has the standard local prolate trace property, then

\[
B_{\Lambda,N}-B_{\Lambda,N}^2
\]

is trace class and

\[
\boxed{
\operatorname{Tr}
(B_{\Lambda,N}-B_{\Lambda,N}^2)
=
\sum_{\chi\in\Gamma_N}
\mathfrak p_{\Lambda,S}(\chi),
}
\]

where

\[
\mathfrak p_{\Lambda,S}(\chi)
=
\operatorname{Tr}_{\chi}
(B_{\Lambda,\chi}-B_{\Lambda,\chi}^2)
\ge0.
\]

For fixed `N`, a bound

\[
\mathfrak p_{\Lambda,S}(\chi)
=O_{S,\chi}(\log\Lambda)
\]

makes the regulated transition trace finite and logarithmic.

## Regulated observer

Set

\[
A_N
=K_NU_S(g)K_N,
\qquad
H_N=A_NA_N^*.
\]

The finite-mode sewing term is

\[
\mathcal E_{\Lambda,N}(g)
=
\operatorname{Tr}
\left(
P Q(I-P)H_N
\right).
\]

Now both off-diagonal factors are Hilbert--Schmidt on the finite angular sum. The earlier Cauchy estimate is legitimate:

\[
\boxed{
|\mathcal E_{\Lambda,N}(g)|
\le
\left[
\sum_{\chi\in\Gamma_N}
\mathfrak p_{\Lambda,S}(\chi)
\right]^{1/2}
\|[P_\Lambda,H_N]\|_{HS}.
}
\]

This is a fully typed finite-mode inequality.

## Why taking `N -> infinity` naively fails

If

\[
\mathfrak p_{\Lambda,S}(\chi)
\asymp
\log\Lambda
\]

uniformly in `chi`, then

\[
\sum_{\chi\in\Gamma_N}
\mathfrak p_{\Lambda,S}(\chi)
\asymp
|\Gamma_N|\log\Lambda.
\]

The unweighted estimate diverges as `N -> infinity`. Thus finite-mode regularization alone does not prove a bare semilocal transition trace.

Observer smoothness must be retained in the angular sum.

## Angular observer coefficients

Decompose the observer action into angular blocks

\[
A_{\chi,\psi}
=K_\chi U_S(g)K_\psi.
\]

For smooth `g` on the compact angular group, Peter--Weyl/Fourier coefficients decay faster than any polynomial:

\[
\boxed{
\|A_{\chi,\psi}
\|
\le
C_{g,M}
(1+|\chi|
+|\psi|)^{-M}
}
\]

in an appropriate operator or Hilbert--Schmidt radial norm, after choosing a length function on the discrete dual.

For bounded smooth observer packets, the constants are uniform at each fixed `M`.

## Weighted transition criterion

A sufficient source-typed estimate is not an unweighted sum of `p_chi`. It is

\[
\boxed{
\sum_{\chi,\psi}
(\mathfrak p_{\Lambda,S}(\chi)
\mathfrak p_{\Lambda,S}(\psi))^{1/2}
w_g(\chi,\psi)
<\infty,
}
\]

where `w_g` is a rapidly decreasing bound for the relevant observer blocks.

If the per-character transition growth is polynomial in angular frequency,

\[
\boxed{
\mathfrak p_{\Lambda,S}(\chi)
\le
C_S
(1+|\chi|)^d
(1+\log\Lambda),
}
\]

then choose observer decay order `M` larger than `d` plus the growth dimension of the dual. The weighted angular sum converges and yields an observer-dependent logarithmic sewing bound.

The polynomial exponent `d` is the exact remaining radial--angular estimate.

## Removal of the angular regulator

Assume:

1. `K_N -> I` strongly;
2. `K_N` commutes with `P` and `Q` up to errors negligible in the observer-weighted trace norm;
3. the polynomial per-character transition bound holds;
4. observer blocks have rapid angular decay.

Then dominated summation gives

\[
\boxed{
\mathcal E_{\Lambda,N}(g)
\longrightarrow
\mathcal E_{\Lambda,S}(g)
}
\]

as `N -> infinity`, locally uniformly in `Lambda` after division by the derived logarithmic majorant.

This defines the full semilocal sewing term without assigning a trace to the bare angular identity.

## Interaction with the second physical cutoff

For complete trace-class typing, retain the annular regulator `P_R-P_Lambda` before removing `N`. Define

\[
\mathcal E_{\Lambda,R,N,S}(g)
=
\left\langle
Q_\Lambda P_\Lambda A_N,
Q_\Lambda(P_R-P_\Lambda)A_N
\right\rangle_{HS}.
\]

The safe order of operations is

\[
\boxed{
\text{finite }(\Lambda,R,N)
\longrightarrow
N\to\infty
\longrightarrow
R\to\infty
\longrightarrow
\Lambda\to\infty,
}
\]

unless a joint dominated-convergence theorem permits a correlated limit.

Changing this order without estimates can reintroduce the non-Hilbert--Schmidt outside leg.

## Relation to the `S`-unit orbit sum

Angular characters and `S`-unit orbits are dual descriptions of the norm-one directions. Geometric decay in the `S`-unit word metric corresponds to smooth spectral decay in angular character.

The two proposed estimates should therefore be proved together by a Poisson/Peter--Weyl argument:

\[
\boxed{
\text{geometric orbit decay}
\Longleftrightarrow
\text{angular spectral regularity}.
}
\]

This avoids summing the same multiplicity twice.

## What is unconditional here

The following are formal Hilbert-space facts once the angular decomposition is fixed:

- finite `K_N` makes the angular sum finite;
- the regulated Cauchy--Schwarz sewing bound is typed;
- smooth angular observers have rapidly decreasing Fourier coefficients;
- a polynomial per-mode transition estimate is sufficient for removing `K_N`.

The missing source estimates are:

- exact commutation/intertwining of `F_S` with the chosen angular characters;
- polynomial dependence of `p_(Lambda,S)(chi)` on `chi`;
- uniform trace-ideal bounds needed for the ordered limits.

## Disposition

The semilocal transition must be regularized and summed as an observer-weighted angular family. The decisive estimate is

\[
\boxed{
\mathfrak p_{\Lambda,S}(\chi)
\le
C_S
(1+|\chi|)^d
(1+\log\Lambda).
}
\]

Combined with rapid angular decay of `U_S(g)`, this removes the angular cutoff and yields a well-typed full sewing term. The next analytic step is to compute the characterwise radial prolate kernel and establish this polynomial bound.
