# Theta reciprocal anomaly lines have an exact cutoff-invariant pairing

## Setup

For each finite prime cutoff `X`, retain the two anomaly lines

\[
 L_X^+(s),
 \qquad
 L_X^-(1-\bar s).
\]

Their bonding maps from `X` to `Y` are the source-derived local Tate
transitions

\[
 U_{X,Y}^+(s)
 =\prod_{X<p\le Y}\gamma_p(s)
\]

and

\[
 U_{X,Y}^-(1-\bar s)
 =\prod_{X<p\le Y}\gamma_p(1-\bar s).
\]

No infinite Euler product is used.

## Exact reciprocal identity

For

\[
 \gamma_p(s)={1-p^{-s}\over1-p^{s-1}},
\]

direct substitution gives

\[
 \boxed{
 \gamma_p(1-\bar s)
 ={1\over\overline{\gamma_p(s)}}.}
\]

Therefore

\[
 U_{X,Y}^-(1-\bar s)
 ={1\over\overline{U_{X,Y}^+(s)}}.
\]

This identity is finite, exact, and placewise.

## The invariant relative pairing

Define at each cutoff the sesquilinear pairing

\[
 \mathcal P_X:L_X^+(s)\times L_X^-(1-\bar s)\longrightarrow\mathbb C,
 \qquad
 \mathcal P_X(x,y)=x\bar y.
\]

Then

\[
\begin{aligned}
 \mathcal P_Y(U_{X,Y}^+x,U_{X,Y}^-y)
 &=U_{X,Y}^+x\,\overline{U_{X,Y}^-y}\\
 &=U_{X,Y}^+x\,{1\over U_{X,Y}^+}\bar y\\
 &=\mathcal P_X(x,y).
\end{aligned}
\]

Hence:

\[
 \boxed{
 \mathcal P_Y\circ(U_{X,Y}^+\times U_{X,Y}^-)=\mathcal P_X.}
\]

The relative pairing descends to the two directed-limit lines even where
neither line is uniformly comparable with the seam metric.

## Interpretation

Packet 175 found reciprocal metric escape:

\[
 \|U^+\|\to\infty,
 \qquad
 \|U^-\|\to0
\]

on a real off-seam displacement.  The present identity shows that this is not
loss of the relationship.  The individual norms are chart-dependent, while
their cross-sector pairing is exactly conserved.

Thus the correct completed value is not a norm in either sector but a dual
evaluation:

\[
 \boxed{
 L^-(1-\bar s)\simeq L^+(s)^{-*}.}
\]

This is the first exact cutoff-invariant boundary current supplied by the
anomaly-line system.

## Why this does not prove RH

Every finite Tate transition is invertible.  If `x` and `y` are transported
from nonzero initial vectors, then

\[
 \mathcal P_X(x_X,y_X)=\mathcal P_{X_0}(x_{X_0},y_{X_0})\ne0
\]

at every cutoff.  Consequently the bare anomaly-line pairing is a
nowhere-vanishing transition unit.  It cannot itself be the distinguished
section whose zeros are the Riemann zeros.

The zero-bearing object must include an additional source state and boundary
incidence, schematically

\[
 \sigma(s)=\mathcal P(\tau_+(s),C_s\tau_-(1-\bar s)),
\]

where the vectors `tau_+`, `tau_-` or the incidence `C_s` can lose
transversality while the anomaly-line pairing remains perfect.

This separates two structures that had been too close:

\[
 \boxed{
 \text{Tate transitions protect the comparison type;}
 \quad
 \text{source incidence determines the zero divisor}.}
\]

## Archimedean extension gate

If the completed local factor at infinity obeys the same reciprocal identity,
its transition can be tensored into the finite-place lines and the invariant
pairing survives unchanged.  This must be checked using the fixed Tate Haar,
Fourier, and gamma normalization; an inserted scalar completion factor is not
authority.

The next calculation is therefore not another Euler convergence estimate. It
is the source-level construction of the zero-bearing incidence vectors in the
paired line system, followed by their finite-cutoff Green boundary identity.

## Falsifier

For any proposed finite-cutoff incidence `C_X(s)`, define

\[
 \mathfrak A_{X,Y}(s)
 =\mathcal P_Y(U_{X,Y}^+x,
 C_YU_{X,Y}^-y)
 -\mathcal P_X(x,C_Xy).
\]

A nonzero typed anomaly `mathfrak A_(X,Y)` shows that the proposed incidence
does not descend through Tate normalization. Scalar agreement after summing
unrelated channels is insufficient.
