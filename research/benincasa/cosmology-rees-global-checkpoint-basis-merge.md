# Global exact Rees checkpoint-basis merge

Problem: merge all block-covered exact rows into one sparse row-space
certificate.

Bold conjecture: the second exact reduction layer has a prime-stable global
pivot schedule and rank.

Rivals: block-local compatibility fails globally; global rational factors alter
modular pivots; or one exact basis survives projection.

Risky consequence: all 2,524 rows must receive one exact pivot or dependence
decision that replays at primes 101, 103, and 107.

Strongest falsification attempt: global sparse elimination found rank 1,382 and
1,142 dependent rows. It recorded 29,496 operation edges; the largest
intermediate row had 174 nonzero entries. Rank, pivots, normalized rows, and
dependence decisions replay without failure at every tested prime. The
checkpoint digest is
`f795ce5f61720baa2626184c7d3ef298f6c1ed979f138ae2799086ab9f5d3ada`.

Disposition: retained for the ambient-four exact source row space. This does not
supply a source-row combination selecting the principal target column or a
physical generator. The next test reduces that target against the basis and
requires a zero residual plus a replayable sparse witness.
