# The Laguerre buffer has macroscopic transition occupancy

## Question

Can transition occupancy reduce interface pair counts under an admissible degree-overlap scaling?

Take

\[
n=X^{\beta/8}.
\]

This satisfies \(n=o(X^{\beta/4})\). The buffered cuts become

\[
z_-=n,
\qquad z_+=n^3.
\]

For the local Laguerre projection kernel, exact integer incomplete-gamma integration computes

\[
\mathbb E[N_C]
=
\int_n^{n^3}K_n(z,z)e^{-z}dz.
\]

For \(n=3,4,6,8,10,12\), the occupancy fraction stays between \(0.3858\) and \(0.3928\). It does not decrease on this grid; transition occupancy is proportional to \(n\), not negligible.

## Disposition

Reject negligible transition occupancy as the mechanism for relaxing interface pair counts. The buffer contains a macroscopic part of the local Laguerre ensemble under a valid joint scaling.

The next leaf is `nonperturbative-interface-determinant`: retain transition interactions at leading order rather than treating them as a sparse correction.

## Claim boundary

The computation is exact for finite Laguerre kernels, not for the full shifted Weibull ensemble. It is a counterexample to assuming that scalar overlap plus admissible degree scaling forces negligible occupancy; it is not a universal occupancy theorem.
