# Reciprocal desmoothed characters have no common Hilbert fiber

## Complementary domains

On the positive half-line, define the two reciprocal characters

\[
e_z(q)=e^{zq},
\qquad
e_{-z}(q)=e^{-zq}.
\]

Their norms are

\[
\|e_z\|_2^2
=\int_0^\infty e^{2\operatorname{Re}z,q},dq,
\]

and

\[
\|e_{-z}\|_2^2
=\int_0^\infty e^{-2\operatorname{Re}z,q},dq.
\]

Therefore

\[
e_z\in L^2(0,\infty)
\quad\Longleftrightarrow\quad
\operatorname{Re}z<0,
\]

while

\[
e_{-z}\in L^2(0,\infty)
\quad\Longleftrightarrow\quad
\operatorname{Re}z>0.
\]

There is no spectral point where both reciprocal desmoothed characters belong
to the same half-line Hilbert space. On the seam, each has constant modulus
and neither is square-integrable.

## The cross-pair is spectrally empty

Their complex-bilinear pointwise product is

\[
e_z(q)e_{-z}(q)=1.
\]

At finite cutoff (L),

\[
\int_0^L e_z(q)e_{-z}(q),dq=L.
\]

The entire divergence is the universal length current. Subtracting that
source-independent cutoff term leaves zero. Hence the most immediate
reciprocal bilinear pairing contains no information about (z).

The sesquilinear cross-product removes the real displacement and retains only
an oscillatory function of (\operatorname{Im}z). It likewise cannot
distinguish the two open half-planes.

## No positive doubled character energy

An expression such as

\[
\|e_z\|^2+\|e_{-z}\|^2
\]

is ill-typed at every (z): one term diverges off the seam and both diverge on
it. Therefore reciprocal desmoothing cannot supply an ordinary positive Gram
form whose vanishing confines zeros.

This is not merely lack of a uniform estimate. The two characters occupy
complementary analytic fibers.

## Consequence for the boundary law

Reciprocal sewing must be formulated in one of two ways:

1. after Hankel/source smoothing, where both history tails may be honest
   states;
2. before Hilbert completion, in a rigged relative category retaining the
   universal length and endpoint currents.

Desmoothing each sector separately and then placing the results in one Hilbert
sum is unauthorized.

The physical obstruction therefore returns to the smoothed two-history
packet. There, the doubled Green identity is well-typed, but its mixed forcing
residual must be supplied by modular boundary data. Character-level
reciprocity alone cannot provide it.

## Falsifier

Any proposed positive doubled-character proof must exhibit a declared common
domain on which both reciprocal characters have finite norm. A regulator that
achieves this must retain its boundary current and prove regulator-independent
reconstruction; silently subtracting the universal divergence is not enough.
