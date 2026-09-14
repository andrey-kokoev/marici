# v115: soft D1 Smith torsion profile

The integral Smith checker now reports complete invariant-factor distributions
at cutoff `D=12`.

Before L2 completion the nonunit factors are `2^8, 14^3, 42^4, 84^3, 420^2`
(as multiplicities, alongside 69 unit factors), and the saturation index has
prime factorization `2^25 3^9 5^2 7^12`. After completion the factors are
`2^9, 14^8, 42^4`, again with 69 units, and the index is
`2^21 3^4 7^12`.

Thus L2 removes all 5-primary torsion and lowers the 2- and 3-primary defects,
but leaves substantial 2-, 3-, and 7-primary nonsaturation. The next
construction must either saturate integrally or explicitly choose coefficients
that invert these primes; that coefficient choice is physical data and cannot
be made silently.

`rzk/143-soft-d1-smith-torsion-profile.rzk.md` passes all eight declarations
without assumptions.
