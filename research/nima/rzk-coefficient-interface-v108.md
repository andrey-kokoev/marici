# v108: soft D1 Cartier nearby model

The existing Rust implementation of the remaining soft-axis nearby model was
freshly replayed.

`rzk/136-soft-d1-cartier-nearby-model.rzk.md` records the translated section
`z=0`, its physical pushforward relation, and generic locus `b^2 != 1`. The
nearby module has rank two, semisimple eigenvalues `(1,-1)`, and zero nilpotent
logarithm. The even and odd degree characters are respectively `+1` and `-1`;
the odd class has boundary divisor `(3,4)`.

Carrier monodromy is trivial. Nontrivial monodromy lies in the Cartier
pushforward support framing, away from the excluded loci `b=+/-1`.

This constructs the local D1 nearby model but does not identify it with the
full exact physical chain complex. Consequently it does not yet close the
road-Cech witness required by module 132.

The Rzk module passes all ten declarations with no assumptions.
