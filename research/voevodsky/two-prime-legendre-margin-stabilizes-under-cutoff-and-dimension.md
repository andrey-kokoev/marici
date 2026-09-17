# The two-prime Legendre margin stabilizes under cutoff and dimension

The floating `L=0.55` calculation was repeated for dimensions 20, 40, 60,
and 80 and cutoffs 250, 500, 1000, and 2000, preserving the exact parity
block decomposition.

At cutoff 2000 the smallest eigenvalues are respectively

\[
2.7263\times10^{-8},\quad
2.6366\times10^{-8},\quad
2.6076\times10^{-8},\quad
2.5761\times10^{-8}.
\]

The margin increases with cutoff after the poorly resolved cutoff-250 tail and
decreases mildly with dimension. This is consistent with a genuine positive
margin near `2.5e-8`, rather than the earlier value being a quadrature or
finite-rank accident.

The data also identify the certification bottleneck. Entrywise absolute tail
bounds will likely be too coarse relative to `1e-8`; the omitted prime cosine
tails must retain oscillation, while the eventually positive gamma tail
should be separated rather than bounded in absolute value. A directed proof
should therefore use integration by parts or an oscillatory Bessel-product
tail enclosure for each prime phase, followed by interval `LDL*` on the
parity blocks.

This remains reconnaissance: stability under four cutoffs and dimensions is
not a bound on the infinite tail or the complement of the 80-dimensional
space.
