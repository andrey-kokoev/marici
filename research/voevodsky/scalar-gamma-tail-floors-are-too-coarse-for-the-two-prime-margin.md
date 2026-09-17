# Scalar gamma-tail floors are too coarse for the two-prime margin

Two positive lower-form constructions were tested after evaluating the prime
translations in physical coordinates.

First, the gamma tail beyond a radius `R` was replaced by the constant lower
multiplier at `R` times the out-of-band concentration operator. This remained
indefinite for every tested `R` from 10 through 1000.

Second, the monotone gamma multiplier was bounded by left-endpoint constants
on twelve dyadic bands from its positive crossing to radius about 25763, with
the final outer tail retained. The lower form still had four negative
eigenvalues; its smallest eigenvalue remained near `-0.157`.

The failure is expected quantitatively. A dyadic floor loses roughly a fixed
`log 2` increment of the logarithmic multiplier, while the observed full-form
margin is only about `2.5e-8`. Positivity of the tail as an operator is not
enough; its detailed distribution across the polynomial modes is essential.

Therefore scalar coercive floors cannot certify the second-prime low block.
The viable finite-block calculation must evaluate the gamma matrix accurately
on a long finite range and use an asymptotic matrix remainder that preserves
its Bessel-mode structure. Exact physical translation still removes all prime
frequency tails, so only the positive archimedean matrix requires this
high-accuracy treatment.
