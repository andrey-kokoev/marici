# Place enlargement is a spectral correspondence through the local-energy row, not a threshold-preserving map

## Exact symbol relation

For

\[
S'=S\cup\{v\},
\]

write

\[
e_{S'}=e_S+\kappa_v
\]

and

\[
w_{S'}=w_S+w_v.
\]

The normalized multipliers satisfy

\[
\boxed{
a_{S'}
=
\frac{e_Sa_S+w_v}{e_S+\kappa_v}.
}
\]

This is an affine energy-weighted update. Absolute-value spectral levels can move in both directions because \(w_v\) may reinforce or cancel \(e_Sa_S\).

## Failure of threshold transport

The contractive domain inclusion is

\[
I_{S'S}:
\mathscr E_{S'}
\longrightarrow
\mathscr E_S.
\]

A threshold-preserving spectral map would require a function \(\varphi\) such that

\[
I_{S'S}
1_{[\eta,\infty)}(|\mathcal A_{S'}|)
\mathscr E_{S'}
\subseteq
1_{[\varphi(\eta),\infty)}(|\mathcal A_S|)
\mathscr E_S.
\]

Take a spectral point with

\[
a_S=0
\]

and

\[
w_v\ne0.
\]

Then

\[
|a_{S'}|
=
\frac{|w_v|}{e_S+\kappa_v}>0,
\]

while the old point lies in the radical of \(|\mathcal A_S|\). Therefore every positive choice of \(\varphi(\eta)\) fails on such a point.

Cancellation gives the reverse phenomenon: choose

\[
w_v=-e_Sa_S.
\]

Then

\[
a_{S'}=0
\]

although \(|a_S|\) may be positive.

Thus place enlargement does not define a controlled spectral morphism between the one-variable absolute-value towers.

## Positive feature row

Prior work supplies a strict local-energy feature decomposition

\[
D_{S'}^{loc}
=
D_S^{loc}
\oplus
D_v^{(S)}.
\]

The positive carrier grows covariantly by orthogonal row addition, while the energy domain changes contravariantly:

\[
\mathscr E_{S'}
\hookrightarrow
\mathscr E_S.
\]

This gives a correspondence

\[
\mathscr E_S
\xleftarrow{\ I_{S'S}\ }
\mathscr E_{S'}
\xrightarrow{\ D_S^{loc}\oplus D_v^{(S)}\ }
\mathcal K_S\oplus\mathcal K_v.
\]

The signed boundary multiplier is the readout of this correspondence after combining the local rows.

## Joint spectral replacement

For place functoriality, retain the local coordinates before signed summation. Define the joint positive local-energy operator

\[
\mathbf K_S
=
\bigoplus_{u\in S}K_u
\]

or equivalently the commuting measurable family

\[
\bigl(
\kappa_u,
 w_u
\bigr)_{u\in S}.
\]

Place enlargement is then strict coordinate inclusion:

\[
\mathbf K_S
\longmapsto
\mathbf K_S\oplus K_v.
\]

The scalar absolute boundary

\[
|a_S|
=
\left|
\frac{\sum_{u\in S}w_u}
{1+\sum_{u\in S}\kappa_u}
\right|
\]

is a stage-dependent readout rather than the functorial carrier.

## Categorical form

The gapless completion architecture has two classes of arrows:

1. fixed-\(S\) spectral morphisms, including convolution successors and character truncations;
2. place-enlargement correspondences acting on the joint local-energy feature.

Composition of place enlargements is strict orthogonal row addition. Their scalar boundary readouts compose through the affine update formula for \(a_S\).

## Consequence

The categorical target should be a correspondence category of local-energy features. The one-variable spectral tower of \(|\mathcal A_S|\) is a fiberwise completion attached to each fixed \(S\). It is functorial for operations commuting with the multiplier and connected across different \(S\) by local-energy correspondences.
