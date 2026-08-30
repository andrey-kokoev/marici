# The cross-tower Ward cell lives on the dynamical null pullback

## Can the towers be related ambiently?

Let (C_X) be a finite labelled input module, let

\[
L_X:C_X\longrightarrow\mathbb C
\]

be scalar output aggregation, and let

\[
W_X:C_X\longrightarrow
\prod_{p\le X}E_{p,X}
\]

be the finite prime-exclusion Ward packet.

Could the desired cross-tower cell be an ambient factorization

\[
W_X=K_XL_X
\]

or an estimate

\[
\lVert W_Xc\rVert\le C_X|L_Xc|?
\]

## Exact no-go

Both proposals require

\[
\ker L_X\subseteq\ker W_X.
\]

But the two-label packet (c=(1,-1)) lies in (ker L_X) and has nonzero
prime-exclusion curvature. Therefore neither an ambient factorization nor an
ambient domination inequality exists.

This obstruction persists at every larger cutoff containing the two labels
and prime two. Adding more input ports only makes (W_X) more faithful.

## Correct pullback object

The Ward implication must be restricted to the admissible zero-state object

\[
Z_X(z)
=
\{\Psi:
\mathcal D_{X,z}\Psi=0,
\ \Psi\in\mathsf{Dom}_{X,z},
\ L_X\Psi=0\}.
\]

Here (mathcal D_{X,z}) is the source-derived finite dynamics and
(mathsf{Dom}_{X,z}) includes the completed boundary conditions. The desired
cell is

\[
Z_X(z)\longrightarrow\ker W_X.
\]

This formulation uses all three towers:

- input supplies (W_X);
- output supplies (L_X=0);
- control and source dynamics define the pullback and the Ward map.

The two-label hostile is rejected only if it does not satisfy the declared
source dynamics and boundary domain.

## Why the dynamics are not optional

Without (mathcal D_{X,z}\Psi=0), scalar nullity is simply a hyperplane and
contains many curvature-visible states. The control Green identity must use
the dynamical equation to transform boundary cancellation into a portwise
curvature statement.

This also prevents circularity. The pullback domain must be constructed before
the zeros are inspected; it cannot be defined as the set on which the desired
Ward implication happens to hold.

## Naturality requirement

For (X\subset Y), cutoff restriction must carry (Z_Y(z)) into (Z_X(z))
and commute with the Ward cells. Scalar equality only after taking the limit
does not suffice.

The exact theorem sought is therefore a natural transformation from the
pro-system of dynamical scalar-null pullbacks to the pro-system of curvature
kernels.

## Falsifiers

The route fails if:

- a finite admissible zero-state has nonzero exclusion port;
- the boundary domain is chosen after scalar zero inspection;
- cutoff restriction does not preserve the solution locus;
- the Ward identity holds only after summing prime ports;
- a hostile source satisfies the same dynamical pullback and Ward cell.

## Result

The first cross-tower coherence cell cannot live on the ambient coefficient
module. It must live on the source-dynamical scalar-null pullback. This is the
smallest correctly typed target for the next finite calculation.

