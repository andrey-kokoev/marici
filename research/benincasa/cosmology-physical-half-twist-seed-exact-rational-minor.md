# Physical half-twist canonical seeds replay exactly over the rationals

The source-derived dependency closures were rebuilt independently with physical
gamma `-1/2` at four primes. Every sparse row entry was reconstructed as a
rational number under the standard four-prime unique-height bound. Exact
Gaussian elimination over `Fraction` then gave:

- pole 0: nonsingular `27 × 27` minor and full target reconstruction;
- pole 1: nonsingular `45 × 45` minor and full target reconstruction.

The solved q coefficients equal the negatives of the previously reconstructed
provenance coefficients, as required by the identity convention

`target + provenance q combination in T + S_K`.

The full sparse target dictionaries, not only retained minor columns, match the
exact source combinations. The source-coefficient hashes equal the generic
integer-gamma run, establishing gamma independence on these two bounded
closures rather than assuming it.

This is an exact degree-14 rational theorem on modularly selected dependency
minors. It does not prove pivot-independent uniqueness, ambient induction, an
unbounded cofinal vanishing theorem, or a primitive tau map.
