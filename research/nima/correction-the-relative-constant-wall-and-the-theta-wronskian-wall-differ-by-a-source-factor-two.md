# Correction: the relative constant wall and the theta Wronskian wall differ by a source factor two

## Two linear wall realizations

The multiplication-window coefficient wall has the linear realization

\[
e_{\mathrm{wall}}
\longmapsto
-\mathbf1.
\]

As a relative endpoint vector, \(-\mathbf1\) has traces

\[
(-1,-1).
\]

The completed theta Lagrange boundary instead supplies the wall column

\[
w_\theta
=
\begin{pmatrix}
\frac12\\[2pt]
\frac12
\end{pmatrix}.
\]

Therefore these are not literally the same endpoint vector. Their source
comparison contains the amplitude factor

\[
(-1,-1)
=
-2w_\theta.
\]

The earlier linear-incidence packet correctly constructed the constant
relative-history wall, but it was too quick to call that vector the completed
theta wall without retaining this factor two.

## Odd Wronskian column

The independent oriented column is

\[
j_\theta
=
\begin{pmatrix}
\frac14\\[2pt]
-\frac14
\end{pmatrix}.
\]

With the ordinary Euclidean endpoint pairing,

\[
\langle w_\theta,j_\theta\rangle=0,
\]

and

\[
\|w_\theta\|^2=\frac12,
\qquad
\|j_\theta\|^2=\frac18.
\]

Thus the theta trace matrix

\[
B_\theta
=
\begin{pmatrix}
\frac12&\frac14\\[2pt]
\frac12&-\frac14
\end{pmatrix}
\]

has Gram

\[
B_\theta^*B_\theta
=
\begin{pmatrix}
\frac12&0\\
0&\frac18
\end{pmatrix}.
\]

The wall and reciprocal-jump coordinates are exactly orthogonal, but they
carry different source scales.

## Unit coefficient-wall calibration

If the coefficient wall Gram is normalized to one and the endpoint metric is
restricted to a scalar multiple \(gI\), then the theta wall column requires

\[
g\|w_\theta\|^2=1.
\]

Hence

\[
g=2.
\]

In that metric,

\[
|w_\theta\|_{2I}^2=1,
\qquad
|j_\theta\|_{2I}^2=\frac14.
\]

This is the canonical scalar endpoint metric compatible with a unit
coefficient wall while preserving equal treatment of the reciprocal sheets.

Equivalently, with the Euclidean endpoint metric the isometric wall incidence
is

\[
e_{\mathrm{wall}}
\mapsto
\sqrt2,w_\theta.
\]

This \(\sqrt2\) is a metric normalization. It must not be confused with the
amplitude factor two relating \(w_\theta\) to the constant endpoint vector.

## Three distinct factors

The audit must keep separate:

1. amplitude conversion:
   \[
   \mathbf1_{\partial}=2w_\theta;
   \]
2. wall isometry in the Euclidean endpoint metric:
   \[
   e_{\mathrm{wall}}\mapsto\sqrt2,w_\theta;
   \]
3. any bilateral doubling in the theta convolution convention.

Conflating them produces factors of two or four at Gram level.

## Theta-history graph

The theta mass transport acts after the completed wall column is chosen:

\[
w_\theta
\longmapsto
M_\Phi w_\theta.
\]

With endpoint metric \(2I\), the graph energy is

\[
1+M_\Phi^2.
\]

Thus the graph coefficient derived previously is recovered exactly without
mapping the unit coefficient wall directly to the unscaled constant vector.

## Orientation scale

The same endpoint metric assigns the odd Wronskian column energy \(1/4\).
Therefore any effective odd coefficient entering the shifted-history square
must include the source incidence scaling that converts this quarter-energy
port into the history odd form.

The sign is already fixed by \(j_\theta\); only the magnitude comparison
remains.

## Corrected wall diagram

The source-authorized chain is

\[
e_{\mathrm{wall}}
\xrightarrow{\ \sqrt2\ }
w_\theta
\xrightarrow{\ M_\Phi\ }
M_\Phi w_\theta
\]

in the Euclidean endpoint frame, or equivalently

\[
e_{\mathrm{wall}}
\longmapsto
w_\theta
\longmapsto
M_\Phi w_\theta
\]

with endpoint metric \(2I\).

The unscaled constant vector belongs to the primitive relative-history frame
and is related by a separate amplitude comparison.

## Frontier

The wall metric calibration is now fixed at the finite two-trace level. The
remaining local comparison is the magnitude map from the quarter-energy odd
Wronskian column into the derivative-tail history, followed by the quadratic
Green identity.
