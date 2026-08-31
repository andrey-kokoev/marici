# A fourth prime changes the unresolved coefficient set

The canonical degree-14 seed was extracted at verified prime 32029 with the
same 7-row and 11-row typed supports. Four-prime CRT has modulus large enough
for unique-height bound `724846791`.

Reconstruction now succeeds for all seven pole-0 coefficients and nine of
eleven pole-1 coefficients. The coefficient previously unresolved after three
primes reconstructs as `-25/7715736`. However, two pole-1 q-pole-0 descriptors,
at exponents `(0,2)` and `(2,0)`, no longer admit candidates across all four
residues. Their earlier three-prime candidates were therefore not stable
characteristic-zero coefficients.

The complete result is `16/18`, not a rational seed theorem. This demonstrates
why individual finite-modulus reconstructions cannot be promoted before the
entire coefficient vector stabilizes and the characteristic-zero relation is
replayed. Another prime or source-derived coefficient constraints remain
necessary.
