# The blow-up face leg requires a coupled logarithmic source

## Question

Can the sourced blow-up exceptional simplex with column \((0,1)^T\) be completed to the minimal closed target vector by adjoining a separate logarithmic sphere generator?

## Claim boundary

This tests the exact residue matrix and the sourced column reported by the Benincasa audit. It does not construct the missing logarithmic source object or comparison pairing.

## Calculation

Let

\[
D_{\rm res}=
\begin{pmatrix}
1&-1\\
-1&1\\
1&-1
\end{pmatrix},
\qquad
v=\begin{pmatrix}1\\1\end{pmatrix}.
\]

The sourced blow-up face leg is

\[
b=\begin{pmatrix}0\\1\end{pmatrix},
\]

so the missing coefficient leg is

\[
a=v-b=
\begin{pmatrix}1\\0\end{pmatrix}.
\]

Although

\[
D_{\rm res}v=0,
\]

neither leg is closed:

\[
D_{\rm res}a=
\begin{pmatrix}1\\-1\\1\end{pmatrix},
\qquad
D_{\rm res}b=
\begin{pmatrix}-1\\1\\-1\end{pmatrix}.
\]

Their residues cancel exactly.

## Consequence

The missing \(\Xi_{\log}\) unit leg cannot be supplied as an independent map from another one-generator sphere complex: such a map would fail the chain equation. The source must derive either:

1. one coupled cycle mapping directly to \(a+b=v\); or
2. a two-leg source complex whose internal differential/comparison data maps to the opposite residue vectors and proves their cancellation.

This is why common Cayley--Menger provenance is insufficient. A typed relative homology--de Rham pairing must couple the contour and logarithmic legs before projection to \((\Xi_{\log},-\sigma_{123})\).

## Strongest falsification attempt

Verify the three residue equations integrally and over the two audited finite fields. Require both individual legs to be nonclosed, their sum to be primitive and closed, and the missing-leg residual to be exactly \((1,0)^T\).

## Computed result

Integrally and over both audited fields, the logarithmic leg has residue \((1,-1,1)^T\), the blow-up face leg has residue \((-1,1,-1)^T\), and their sum has zero residue. The total vector is primitive. Neither leg separately defines a sphere-source chain map.

## Disposition

The separate-generator rival is falsified. The source-realization branch remains blocked, but its minimal shape is sharper: it must provide one coupled source cycle, or a two-leg source complex with internal comparison data deriving the opposite residues and their cancellation. The first missing arrow is the source-derived relative homology--de Rham pairing that performs this coupling.
