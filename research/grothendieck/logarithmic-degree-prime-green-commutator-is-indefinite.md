# The logarithmic-degree prime Green commutator is indefinite

## Bounded question

Can the source-derived identity

\[
L_{\rm inc}=\frac12\log Q
\]

turn the staircase Green current into a positive energy that forces reciprocal
adjunction?

## Smallest prime block

Fix one prime \(p\), put \(a=\log p\), and restrict the integer-label module
to

\[
V_p=\operatorname{span}\{e_1,e_p\}.
\]

On this block the logarithmic degree and the compressed prime transport are

\[
L=\begin{pmatrix}0&0\\0&a\end{pmatrix},
\qquad
T=|e_p\rangle\langle e_1|
=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]

The exact incidence covariance survives compression:

\[
[L,T]=aT.
\]

Thus this is already the smallest faithful block on which a degree--transport
Green term can be tested.

## The self-adjoint current is indefinite

The source-authorized real transport observable is

\[
B=T+T^*.
\]

Its positive-commutator candidate is

\[
i[L,B]
=ia(T-T^*)
=a\begin{pmatrix}0&-i\\i&0\end{pmatrix}.
\]

Its eigenvalues are \(a\) and \(-a\). Hence it is indefinite for every prime.
The conjugate quadrature gives the same obstruction:

\[
A=i(T-T^*),
\qquad
i[L,A]=-a(T+T^*),
\]

again with eigenvalues \(a\) and \(-a\).

Therefore no linear Green current made from one prime transport and the
positive logarithmic degree is itself positive. The obstruction occurs before
Euler completion, archimedean sewing, or any limiting topology.

## Why squaring does not rescue orientation

The square of either commutator is positive on this block:

\[
\bigl(i[L,B]\bigr)^2=a^2I.
\]

But squaring removes the sign and phase that distinguish reciprocal transport
from Hilbert adjunction. It produces a regularity norm, not the linear boundary
current in the staircase Green identity. Replacing the current by its square
would therefore change the theorem rather than prove it.

## Mellin phase covariance exposes the missing datum

For

\[
M_te_n=n^{it}e_n,
\]

we have

\[
[M_t,L]=0,
\qquad
M_tT_pM_t^{-1}=p^{it}T_p.
\]

The positive degree and every divisibility projection are unchanged, while the
prime-transport quadrature rotates. Consequently the arithmetic--heat identity
determines transport magnitude and degree but does not select the star frame.
That missing phase is exactly what a zero-confinement argument must orient.

## Result

The equality \(L_{\rm inc}=\frac12\log Q\) is a genuine theta-specific
arithmetic--archimedean coherence theorem, but it cannot by itself strengthen
the staircase Green identity into a positive energy balance. Its linear
prime-current coupling is already indefinite on \(\{1,p\}\).

Any surviving route must couple reciprocal prime transports in a source-fixed
combination whose off-diagonal terms cancel or become a declared boundary
square. Positivity of the diagonal degree cannot perform that cancellation.

## Sharp next gate

Derive the two-sheet all-prime current before scalar aggregation and test
whether Fourier--Tate sewing pairs each \(p^{it}T_p\) quadrature with its
adjoint using equal source coefficients. A residual phase on the single-prime
block is the smallest falsifier.
