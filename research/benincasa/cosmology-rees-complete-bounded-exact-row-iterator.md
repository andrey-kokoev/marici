# Complete bounded exact Rees-row iterator

Problem: compare a complete labelled rational raw-row stream with the modular
implementation.

Bold conjecture: one prime-independent exact iterator reproduces every
ambient-four `raw_relations` row in stable order.

Rivals: representative compatibility fails elsewhere; untested rows differ in
order or coefficients; or the complete stream has one rational lift.

Risky consequence: every row position and every projected sparse coefficient
must match at primes 101, 103, and 107.

Strongest falsification attempt: an independent exact iterator produced 2,524
labelled rows at point `(3,6,-3)`: 60 twisted-derivative, 64 K-multiplication,
and 2,400 q-multiplication rows. Its label digest is
`449e682f15c4a00d1405a66bd587b17ebd42690ea6fcc9f3fd4e637e0364295b`.
All 2,524 rows match in order and coefficientwise at each tested prime, with no
length or sparse residual.

Disposition: retained for the complete ambient-four raw source stream.
Multiplication by two clears its only half-twist denominator. This constructs
an exact source-row iterator, not an exact row-reduction certificate or a
physical generator lift. The next test must run labelled exact elimination and
compare its checkpoints with modular certificates.
