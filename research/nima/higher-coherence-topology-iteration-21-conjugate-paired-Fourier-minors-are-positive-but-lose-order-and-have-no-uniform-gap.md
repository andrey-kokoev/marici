# Higher-coherence topology iteration 21: conjugate-paired Fourier minors are positive, but lose order and have no uniform gap

## Candidate topology

Retain the Fourier sector and its conjugate simultaneously. Instead of asking a
complex Fourier minor to have a fixed phase, use its Hermitian square as the
oriented two-polarization coordinate.

For ordered samples `q_1<q_2`, `xi_1<xi_2`, put

\[
\Delta_F
=e^{-i(\xi_1q_1+\xi_2q_2)}
-e^{-i(\xi_2q_1+\xi_1q_2)}.
\]

Let

\[
\theta=(\xi_2-\xi_1)(q_2-q_1).
\]

Then

\[
\boxed{
\Delta_F\overline{\Delta_F}
=4\sin^2(\theta/2)\ge0.
}
\]

Thus conjugate pairing removes the oscillating complex phase and produces a
canonical nonnegative Hermitian minor.

## What this achieves

The paired minor is source-independent in sign, Fourier-covariant, and stable
under conjugation. It detects whether the two sampled Fourier columns are
linearly independent. Hence it gives a valid positive exterior-square topology
for the two-polarization carrier.

This is a real gain over the single Fourier chart, where no fixed orientation
exists.

## Loss of variation orientation

Variation diminution requires more than nonnegative squared volume. It must
remember which side of an ordered flag a transported sign change occupies.
The map

\[
\Delta_F\longmapsto|\Delta_F|^2
\]

identifies `Delta_F` and `-Delta_F` and discards their phase. Therefore it cannot
distinguish an ordered `+,-` signature from a reversed or interlaced transport
solely through the paired minor.

The Hermitian square proves noncollapse, not one-transition preservation.

## No strict completed margin

The paired minor vanishes whenever

\[
(\xi_2-\xi_1)(q_2-q_1)\in2\pi\mathbb Z.
\]

Under dense spectral sampling or expanding windows, rectangles approach these
resonant areas arbitrarily closely. Consequently there is no cutoff-independent
strict lower bound

\[
|\Delta_F|^2\ge\varepsilon>0
\]

on the unrestricted completed carrier.

A restricted sampling lattice could avoid exact resonances at one cutoff, but
would need a source-derived Diophantine separation law stable under prime and
jet refinement. No such law is presently declared.

## Higher-cone consequence

Repeated Hermitian pairing can keep exterior volumes positive at every rung,
but positivity of squared volumes does not prevent the underlying oriented
signatures from alternating. A higher cone may rotate through phase while its
Hermitian Plücker norm remains unchanged.

To preserve ordered signature one must retain an additional phase or Maslov
index coordinate, not only the conjugate square.

## Verdict for topology 21

Two-polarization Hermitian-minor topology repairs positivity and noncollapse of
Fourier minors but does not transport variation diminution. It also loses a
uniform strict margin at resonant rectangles.

The next nonredundant topology to test is a phase-lifted/Maslov topology on the
Fourier Plücker line, which retains winding and orientation rather than passing
to the squared norm.