# Exact integral boundary replay

Problem: test whether a reconstructed primitive provenance vector survives exact
integer replay.

Bold conjecture: the reconstructed vector has zero boundary over the integers,
while a one-unit corruption has a specified nonzero residual.

Rivals: modular-only validation, support matching without replay, and a
nonprimitive integer scaling.

Risky consequences: the coefficient gcd must be one, the exact boundary must
vanish, and corruption must return the altered source row rather than cancel.

Strongest falsification attempt: primitive coefficients `2,-3,5,7` were applied
to four labelled integer rows. Their exact boundary is zero and their gcd is
one. Incrementing the third coefficient gives residual `(-2,3,-7)`. Reduction
at primes 101, 103, and 107 reproduces zero for the valid certificate and a
nonzero residual for the corrupted one.

Disposition: retained for the bounded exact prototype. The rows are synthetic;
no Rees generator was constructed. The next test audits whether the actual Rees
relation generator preserves prime-independent source labels and exact
integer/rational coefficient provenance, including half-twist denominators.
