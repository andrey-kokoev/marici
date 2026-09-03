# All-family streaming exact elimination

Problem: cover all exact Rees source rows by bounded sparse checkpoints.

Bold conjecture: fixed-size exact blocks cover all 2,524 rows with prime-stable
pivots and no dense provenance expansion.

Rivals: later q-multiplication blocks destabilize pivots; family crossings
obstruct replay; or bounded block certificates cover the stream.

Risky consequence: all 40 block schedules must replay at primes 101, 103, and
107, and the blocks must cover every row exactly once.

Strongest falsification attempt: the exact stream was partitioned into 39
64-row blocks and one 28-row block. Every block, including both family
crossings, replayed at all three primes. The blocks cover 2,524 rows, record 25
elimination edges, and materialize no dense provenance vectors.

Disposition: retained for block-local streaming elimination across the full
source stream. The sum of block ranks is 2,524 but is not a global rank because
each checkpoint resets its basis. No exact target relation follows. The next
test must merge checkpoint bases through a second exact reduction layer and
compare its global rank and pivot schedule across the same primes.
