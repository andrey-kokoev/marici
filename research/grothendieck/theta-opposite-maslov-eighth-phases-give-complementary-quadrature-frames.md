# Opposite Maslov eighth phases give complementary theta quadrature frames

**Source-identity correction:** packet 150 shows that the existing theta
matrix coefficient is Fourier-fixed with scalar eigenphase one. The opposite
eighth phases live at the oscillator determinant/half-form level and do not
yet act on the doubled-tail quadrature. The projector algebra below remains
conditional on a future determinant-line comparison functor.

## Bounded connection

Packet 148 requires the two reciprocal sheets to supply complementary
rank-one quadrature squares. Earlier archimedean work independently derives
opposite metaplectic eighth phases under orientation reversal:

\[
 e^{+i\pi/4},\qquad e^{-i\pi/4}.
\]

Their relative amplitude-frame angle is

\[
 \boxed{\frac\pi4-\left(-\frac\pi4\right)=\frac\pi2.}
\]

This is exactly the angle required for complementary real quadratures.

## Exact projector identity

Let

\[
 u_\theta=\binom{\cos\theta}{\sin\theta},
 \qquad
 P_\theta=u_\theta u_\theta^T.
\]

The rank-one energy selected by frame `theta` is

\[
 E_\theta(A,B)=2\begin{pmatrix}A&B\end{pmatrix}
 P_\theta\binom AB.
\]

Orthogonal frames satisfy

\[
 P_\theta+P_{\theta+\pi/2}=I.
\]

Taking `theta=-pi/4` and `theta+pi/2=+pi/4` gives

\[
 \boxed{P_{-\pi/4}+P_{+\pi/4}=I}
\]

and hence

\[
 \boxed{E_{-\pi/4}+E_{+\pi/4}=2(A^2+B^2).}
\]

Thus the two metaplectic eighth phases produce the exact matrix certificate
of packet 148 with `c_X=1`, provided they act on the same two-copy amplitude
frame and with equal source normalization.

## Equivalent spin-two statement

A frame rotation by `theta` rotates spin two by `2theta`. The two phases
`+pi/4` and `-pi/4` therefore differ by `pi` in the spin-two representation.
Their traceless quadratic components are exact negatives while their trace
components agree.

This explains why an eighth-root phase can generate a sign reversal at
quadratic order:

\[
 \text{opposite amplitude eighth phases}
 \longrightarrow
 \text{opposite spin-two orientations}.
\]

## Source status

The algebra is exact, and the opposite Maslov phases were derived previously
from oriented Gaussian/Fresnel continuation rather than chosen from the Xi
zeros. However, the following comparison map is still missing:

\[
 \text{archimedean metaplectic half-form frame}
 \longrightarrow
 \text{two-copy doubled-tail quadrature frame}.
\]

Equal numerical angles do not identify the source objects. Geometry-first
typing requires proving that the same Fourier--Tate orientation reversal acts
on both frames and that the normalizations commute with the prime-labelled
restricted product.

## Strongest finite certificate

At finite cutoff `X`, transport both sheet forms into the common source frame
and test

\[
 Q_X^+=2c_XP_{+\pi/4},
 \qquad
 Q_X^-=2c_XP_{-\pi/4}.
\]

Then complementarity is the exact consequence

\[
 Q_X^++Q_X^-=2c_XI.
\]

The equality must include the prime-two contribution, both non-trace-class
boundary currents, and the archimedean half-form normalization.

## Falsifiers

The mechanism fails if:

1. the two tail sheets inherit the same rather than opposite Maslov lift;
2. their frame phases differ from `pi/2` after all normalization units are
   retained;
3. the two sheet trace coefficients are unequal;
4. the phase comparison exists only after scalar aggregation and not on the
   labelled two-copy carrier;
5. completion destroys the common frame or sends `c_X` to zero.

## Explanatory possibility

If the missing comparison map exists, the half-offset, eighth phase, and
strict two-sheet energy acquire one common explanation:

\[
 \boxed{
 \text{oriented Fourier--Tate quarter-turn lifts to opposite Maslov eighth
 phases, whose relative quarter-turn completes the two quadratures}.}
\]

This would be a genuine convergence of previously separate archimedean and
Green-current structures, not yet an RH theorem.
