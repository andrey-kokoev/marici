# Complete Strict Hankel Positivity Does Not Confine the Evans Character Orbit

Let the source measure have density `1` on `[0,1]` and density `2` on
`[1,2]`. Its bilateral Laplace transform factors as

\[
F(z)=\frac{e^z-1}{z}(1+2e^z).
\]

It therefore vanishes at

\[
z=-\log 2+(2k+1)\pi i,
\]

an exact off-seam family.

Nevertheless its moments are

\[
m_j=\frac{2^{j+2}-1}{j+1},
\]

and every ordinary and shifted Hankel moment matrix is strictly positive
definite. Indeed, their quadratic forms are respectively the integrals of
`p(x)^2` and `x p(x)^2` against a positive density on intervals. Thus even
the complete strict Stieltjes moment tower of a positive continuous carrier
does not confine zeros of its exponential-character readout.

This strengthens Ledger 3352. The missing RH law cannot be a stronger
carrier positivity condition alone. It must couple the positive carrier, the
distinguished exponential character orbit, and theta/modular sewing.

Research packet:
`research/grothendieck/complete-strict-hankel-positivity-does-not-confine-the-evans-character-orbit.md`

Exact checker:
`research/grothendieck/checkers/check_complete_strict_hankel_evans_hostile.py`

The checker passes 6/6 gates and verifies exact strict ordinary and shifted
Hankel determinants through order eight. The all-orders theorem follows from
the positive-density integral representation.
