# Exact checkpointed elimination on Rees rows

Problem: test sparse exact elimination on labelled actual Rees rows without
dense provenance expansion.

Bold conjecture: a bounded exact operation DAG has a stable pivot schedule and
reproduces its normalized checkpoints modulo three primes.

Rivals: exact denominators destabilize modular pivots; dense provenance is
necessary; or sparse checkpoint replay suffices.

Risky consequence: every elimination edge, pivot, normalization, and dependence
decision must replay at primes 101, 103, and 107.

Strongest falsification attempt: exact sparse elimination processed the complete
60-row twisted-derivative block. It produced rank 60 with 20 elimination edges
and no dense provenance vectors. All 60 normalized checkpoints replay at each
prime with no pivot, row, or dependence residual. The checkpoint digest is
`3d73b024a5858d62d1bf5c647ad0e51ad1ed2238b399e6e61d93e25f2f0a15b5`.

Disposition: retained for the twisted-derivative block. This is not elimination
of all 2,524 rows and does not identify a target physical relation. The next
test extends streaming checkpoints through K- and q-multiplication blocks and
checks whether the pivot schedule remains prime-stable.
