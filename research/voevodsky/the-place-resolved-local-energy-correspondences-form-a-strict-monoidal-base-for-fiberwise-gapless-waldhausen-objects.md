# The place-resolved local-energy correspondences form a strict monoidal base for fiberwise gapless Waldhausen objects

## Base category of place packets

Let \(\mathsf{Pl}\) be the poset of finite admitted place packets. An arrow

\[
S\longrightarrow S'
\]

is an inclusion \(S\subseteq S'\).

Write

\[
T=S'\setminus S.
\]

The local increments are

\[
\kappa_T
=
\sum_{v\in T}\kappa_v,
\qquad
w_T
=
\sum_{v\in T}w_v.
\]

## Correspondence attached to an inclusion

The inclusion \(S\subseteq S'\) determines

\[
\mathscr E_S
\xleftarrow{\ I_{S'S}\ }
\mathscr E_{S'}
\xrightarrow{\ D_{S'S}\ }
\mathcal K_S
\oplus
\bigoplus_{v\in T}\mathcal K_v.
\]

The left leg is the contractive identity induced by

\[
e_{S'}=e_S+\kappa_T.
\]

The right leg is strict orthogonal row addition:

\[
D_{S'}^{loc}
=
D_S^{loc}
\oplus
\bigoplus_{v\in T}D_v.
\]

## Composition

For

\[
S\subseteq S'\subseteq S'',
\]

let

\[
T_1=S'\setminus S,
\qquad
T_2=S''\setminus S'.
\]

The domain legs compose strictly:

\[
I_{S''S}
=
I_{S'S}I_{S''S'}.
\]

The feature rows compose by orthogonal associativity:

\[
D_{S''}^{loc}
=
D_S^{loc}
\oplus D_{T_1}^{loc}
\oplus D_{T_2}^{loc}.
\]

The increment law is

\[
(\kappa_{T_1},w_{T_1})
+(\kappa_{T_2},w_{T_2})
=
(\kappa_{T_1\sqcup T_2},w_{T_1\sqcup T_2}).
\]

Hence place correspondences compose strictly after the canonical associativity identification of Hilbert direct sums.

## Boundary readout cocycle

At stage \(S\), write

\[
a_S=rac{w_S}{e_S}.
\]

An increment \((\kappa_T,w_T)\) acts by

\[
\mathfrak u_T(e,w)
=
(e+\kappa_T,w+w_T).
\]

The scalar readout is

\[
\rho(e,w)=\frac{w}{e}.
\]

Sequential updates satisfy

\[
\mathfrak u_{T_2}
\mathfrak u_{T_1}(e,w)
=
\mathfrak u_{T_1\sqcup T_2}(e,w).
\]

Therefore

\[
a_{S''}
=
\frac{
e_Sa_S+w_{T_1}+w_{T_2}
}{
e_S+\kappa_{T_1}+\kappa_{T_2}
}
\]

independently of parenthesization.

## Fiber category

Over each \(S\), retain the fixed-stage gapless stable category

\[
\mathcal W_S
=
S_\bullet
\operatorname{St}
\left(
\mathsf{Real}^{asym}_S
\right)
\]

together with the positive spectral tower of

\[
|\mathcal A_S|.
\]

Fixed-\(S\) convolution successors and character truncations act as exact spectral morphisms inside \(\mathcal W_S\).

Place enlargement acts between fibers through the local-energy correspondence. Its scalar absolute-value tower is obtained after applying the stage readout

\[
\rho_S:
(e_S,w_S,D_S^{loc})
\longmapsto
|w_S/e_S|.
\]

## Total Grothendieck correspondence

The family

\[
S\longmapsto\mathcal W_S
\]

with place correspondences forms a correspondence-valued Grothendieck construction

\[
\int_{S\in\mathsf{Pl}}
\mathcal W_S.
\]

Its arrows consist of:

1. an inclusion of place packets;
2. the contravariant energy-domain leg;
3. the covariant orthogonal feature-row leg;
4. a fixed-fiber stable or spectral morphism.

Composition uses strict place-increment addition and ordinary fixed-fiber composition.

## Reciprocal duality

Local reciprocal duality acts placewise on each feature row. Since orthogonal direct sum commutes with duality,

\[
\mathbb D
\left(
D_S^{loc}
\oplus D_T^{loc}
\right)
=
\mathbb DD_S^{loc}
\oplus
\mathbb DD_T^{loc}.
\]

Thus reciprocal reversal extends over the place correspondence base.

## Resulting categorical picture

The analytic system has:

- a strict monoidal base of finite place increments;
- a gapless stable/Waldhausen fiber at every fixed \(S\);
- exact fixed-fiber successor and truncation maps;
- correspondence transport under place enlargement;
- stagewise scalar absolute-boundary readouts;
- placewise reciprocal duality.

This is the categorical carrier required before adjoining the physical seam and its positive obstruction cells.
