# 3622 — The Alternating Endpoint Wall Does Not Globalize; the Prime Polytorus Does

The reciprocal-quartic theorem's `P(-1)>=0` gate is exact on one equally
spaced valuation chain, but it is not a global theta/Tate boundary condition.
For a prime `p`, antiphase means `p^{-it}=-1`. Two distinct primes cannot be in
antiphase at the same `t`, because that would force an equality between odd
powers of distinct primes.

The source-native global coordinates are `w_p=p^{-z}`. The open right
half-plane maps into the prime polydisk, the critical seam maps to the prime
polytorus, and the open left half-plane maps into the reciprocal exterior.
Consequently, the plausible global Lee--Yang target is multivariate polydisk
stability of a prime-labelled source object, not positivity at one alternating
endpoint.

This correction makes mixed-prime incidence indispensable. The hostile
polynomial `1+4uv` has positive coefficients and trivial stable restrictions
on both coordinate axes, yet vanishes at `u=v=i/2` inside the bidisk. Thus
one-prime stability does not control the mixed-prime sector.

The exact checker passes 5/5 gates: no common prime antiphase, multiplicativity
of valuation monomials, correct radial chamber geometry, an interior
mixed-prime hostile zero, and failure of the axis restrictions to detect it.

The next falsifiable theorem is: derive the finite prime-labelled generating
objects before diagonal spectral restriction, and prove or falsify their
polydisk stability while retaining all mixed-prime labels.

Artifacts:

- `research/grothendieck/the-alternating-endpoint-wall-does-not-globalize-the-prime-polytorus-does.md`
- `research/grothendieck/checkers/check_prime_polytorus_no_common_antiphase.py`
