# The parity-orbit theorem

The electric and magnetic classifications are two faces of the reflection
representation carried by each exponent-lattice component.

Let `sigma` exchange the two reflected sheet branches.  The transported packet
decomposes as

\[
\mathcal P=\mathcal P_+\oplus\mathcal P_-,
\]

with projectors

\[
\pi_+=\frac{1+\sigma}{2},
\qquad
\pi_-=\frac{1-\sigma}{2}.
\]

Up to normalization,

\[
E=2\pi_+T,
\qquad
M=2\pi_-T.
\]

The one-sheet theorem proves that the transport `T` is injective.  Every
kernel is therefore an intersection of its image with the opposite parity
sector, never a transport kernel.

## Fixed reflection orbits: `q=0`

At the reflection center, each target orbit has one point.  Its representation
is purely trivial:

\[
\mathcal P_{q=0}=\mathcal P_+,
\qquad
\mathcal P_-=0.
\]

Consequently

\[
M_{q=0}=0,
\qquad
E_{q=0}=2A.
\]

This is the complete explanation of the tower asymmetry.  Every admitted
center source is a magnetic zero column, while the electric center is
injective.  Towers are fixed-orbit states, not ordinary collision circuits.

## Free reflection orbits: `q>0`

A free two-point orbit carries the regular representation of `Z_2`:

\[
\mathbf1\oplus\mathrm{sgn}.
\]

Tensoring one reflected source branch by the sign character exchanges the two
parity projections.  In matrices,

\[
[C,\bar C]\longleftrightarrow[C,-\bar C].
\]

Therefore electric and magnetic blocks have identical rank for every `q>0`.
Every exceptional circuit must occur as a parity pair related by the branch
sign gauge:

\[
\begin{array}{c|c|c}
q&\ker M&\ker E\\
\hline
1&1-\bar z^{-2}&1+\bar z^{-2}\\
7&\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}&
\bar z^{-8}+3z^{-4}\bar z^2-2z^{-6}
\end{array}
\]

The grade-two carrier degenerations create the rank defect shared by both
parity projections; the sign character determines which primitive source
combination is invisible to which port.

## Complete orbit classification

The mechanisms are now exhaustive:

\[
\begin{array}{c|c|c}
\text{orbit type}&\text{representation}&\text{kernel mechanism}\\
\hline
q=0\text{ fixed}&\mathbf1&\text{odd projector absent: towers}\\
q>0\text{ free}&\mathbf1\oplus\mathrm{sgn}&
\text{paired parity circuits at }(2,1),(2,7)\\
\text{transport}&\text{faithful}&\text{no kernel}
\end{array}
\]

Because the parity projectors are complementary and `T` is injective,

\[
\ker E\cap\ker M=0.
\]

This is not merely a dimension statement.  It says that every ambiguity of
one readout is a nonzero signal in the other irreducible reflection channel.
