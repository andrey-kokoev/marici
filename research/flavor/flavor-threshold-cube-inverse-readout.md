# The threshold cube explains amplification but does not select its ratio: WP1025

## Question

Can the small observed Jarlskog invariant be the cubic image of a moderate
finite-threshold ratio (r=f/M), and does that determine (r) as a source
prediction?

## Exact physical response

For the fixed WP90 coefficient packet, the normalized invariant is

\[
J^2(r)=
\frac{400r^6}{3P(r)},
\]

where

\[
\begin{aligned}
P(r)={}&12878670000r^8+16583280000r^7+10789212400r^6\\
&+4331604000r^5+1454241747r^4+398819200r^3\\
&+90718200r^2+10800000r+1687500.
\end{aligned}
\]

This is computed from the commutator determinant and both exact spectral
discriminants, so it is a physical quotient readout rather than an
unnormalized chart response.

## Perturbative branch

On

\[
0<r\le1/4,
\]

an exact Sturm count proves (dJ^2/dr>0). At the endpoint,

\[
J^2(1/4)=\frac{400}{369161163681}.
\]

Every one of the 1,210 fitted (J)-magnitudes lies strictly between zero and
this endpoint. Exact rational bisection therefore reconstructs one and only
one (r) for every fitted sheet on this declared branch.

The complete reconstructed interval is recorded in the generated JSON with
per-sheet bracket width (2^{-42}). It is a moderate finite threshold, not an
exponentially tiny parameter.

## Selector versus inverse readout

This is a hierarchy amplifier: near decoupling, (J^2=O(r^6)), so a moderate
threshold ratio produces a much smaller CP invariant. It is also a faithful
inverse readout on the chosen branch.

It is not a selector. The source grammar admits every (r) in the interval.
Using the measured (J) to reconstruct (r) reverses the readout arrow; it
does not derive (r) before observation. A singleton inverse fiber on a
declared branch is not source authority.

## Instrument and smallest falsifier

The CKM/Jarlskog instrument realizes the inverse readout conditional on the
WP90 coefficient packet. Two distinct positive (r) values preserve the
same field, charge, CP, and mediator grammar but produce different (J).
That is the smallest exact falsifier of selection.

## Claim boundary

The result does not identify (r) outside (0<r\le1/4), validate the WP90
coefficients, or establish the mediator experimentally. It assigns no
implicit time or causal interpretation.

## Disposition

Retain the cubic threshold mechanism as a viable explanation of hierarchy
amplification, but not of numerical selection. The next required arrow is an
independent source equation selecting (r) inside the reconstructed interval
before CKM readout.

Verification: uv run --with sympy python
research/flavor/checkers/wp1025_threshold_cube_inverse_readout.py.
