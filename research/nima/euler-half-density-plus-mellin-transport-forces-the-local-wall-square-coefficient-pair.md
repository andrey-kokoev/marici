# Euler half-density plus Mellin transport forces the local wall-square coefficient pair

The correction in event 10303 places the primitive incidence on the doubled
signal port. The existing Mellin transport law then fixes its two
half-density coefficients.

Let

\[
L=\log p,
\qquad
a_p=p^{-1/2}.
\]

On the bilateral trace coordinates, translation acts by

\[
T_L=
\begin{pmatrix}
e^{L/2}&0\\
0&e^{-L/2}
\end{pmatrix}.
\]

Multiplying by the primitive Euler signal coefficient gives

\[
a_pT_L
=
p^{-1/2}
\begin{pmatrix}
p^{1/2}&0\\
0&p^{-1/2}
\end{pmatrix}
=
\begin{pmatrix}
1&0\\
0&p^{-1}
\end{pmatrix}.
\]

Thus the primitive signal does not enter the two transported history
coordinates with equal coefficient \(p^{-1/2}\). In the comoving
half-density frame, it becomes the exact pair

\[
(1,p^{-1}),
\]

up to the frozen convention assigning \(M_-\) and \(M_+\) to the two rows.

## Interpretation

The two entries have the expected source types:

- coefficient \(1\): constant-wall channel;
- coefficient \(p^{-1}\): reciprocal/square-decay channel.

The constant wall is therefore not an added renormalization. It is what the
primitive Euler half-density becomes in the expanding half-density trace
coordinate.

The second coordinate acquires a full extra factor \(p^{-1}\), explaining
why it is Hilbert-summable while the raw primitive signal is not trace class.

## Parity coordinates

Passing to even and odd wall coordinates gives

\[
w_p
=
\frac{1+p^{-1}}{\sqrt2},
\qquad
j_p
=
\frac{1-p^{-1}}{\sqrt2},
\]

again up to the source-fixed orientation sign.

For every prime,

\[
w_p>0,
\qquad
j_p>0.
\]

Hence neither parity channel is algebraically dark. The smallest-prime lower
bounds are

\[
w_p\ge\frac1{\sqrt2},
\qquad
j_p\ge\frac1{2\sqrt2}.
\]

So the coefficient geometry has a uniform two-channel lower margin before
the base theta incidences are applied.

## Remaining source qualification

This calculation transports coefficients; it does not prove that the frozen
theta source has nonzero base moments in both history channels.

If the base trace vector is

\[
(M_-^0,M_+^0),
\]

then the actual translated primitive trace is

\[
(M_-^0,p^{-1}M_+^0).
\]

A vanishing base moment remains vanishing for every prime. Therefore the
source incidence theorem still needs

\[
M_-^0\ne0,
\qquad
M_+^0\ne0,
\]

or an authorized second source precursor supplying the missing direction.

## Reciprocal typing

Reflection exchanges the two half-density characters and reverses the
translation orientation. The full reciprocal packet must therefore include
the \(L\) and \(-L\) sectors before asserting equivariance. The single
matrix \(\operatorname{diag}(1,p^{-1})\) is one oriented chart, not by itself
a reflection-invariant endomorphism.

## Consequence

The first local meeting has contracted to one base-source test:

\[
\text{Are both seam-fiber half-density moments of the admitted theta
precursor nonzero?}
\]

If yes, Euler weighting and Mellin transport automatically produce a
uniformly non-dark wall/odd coefficient pair at every prime. If no, no choice
of passive dilation can repair the missing history channel.

This result derives the coefficient pair from source transport rather than
from scalar Euler or determinant agreement. The boundary pencil remains
downstream.
