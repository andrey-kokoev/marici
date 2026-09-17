# Rank-320 scout shows the frequency cutoff must scale with rank

The two-prime Legendre scout was extended to dimensions 160, 240, and 320
while retaining the old frequency cutoff 2000. The smallest values were

\[
\lambda_{160}\approx2.41\times10^{-8},
\qquad
\lambda_{240}\approx1.68\times10^{-10},
\qquad
\lambda_{320}\approx-9.2\times10^{-16}.
\]

The final value is at floating roundoff scale. Lower cutoffs lose positivity
at progressively smaller dimensions. This pattern tracks omitted positive
gamma mass rather than a stable negative direction.

The conclusion for the complement programme is operational: a fixed frequency
cutoff cannot support rank growth. For basis order `N`, directed finite-gamma
integration and the structured asymptotic anchor must move with `N`; otherwise
high Legendre modes appear artificially null. A rank-doubling proof therefore
needs a coupled `(N,R_N)` schedule or a direct pseudodifferential coercivity
bound above the certified rank-160 block.
