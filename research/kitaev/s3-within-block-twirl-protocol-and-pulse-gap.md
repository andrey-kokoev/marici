# Explicit within-block twirl protocol and the primitive-pulse gap

Owner: `marici.Kitaev`

Status: exact finite channel-target protocol; primitive timed pulse words are
not yet derived.

## Bounded question

What does the 28-dimensional projective controllability theorem actually
compile for within-block depolarization?

For the six nontrivial blocks in order `(C,D,E,F,G,H)`, independently draw

\[
(p,q)\in\mathbf Z_{d_a}^2
\]

uniformly and conjugate block `a` by its Weyl operator `W_{pq}`, acting as the
identity on every other block.  The branch counts are

\[
(4,9,9,4,4,4).
\]

The six stages exactly implement

\[
X_a\longmapsto\frac{\operatorname{Tr}X_a}{d_a}I_{d_a}
\]

on every nontrivial block.  There are 34 branch choices across the sequential
stages and 20,736 unitaries in the flattened ensemble.  The ideal independent
randomness cost is

\[
8+4\log_2 3\ \text{bits}.
\]

## Reachability strength

The compiled source Lie algebra contains
`direct_sum_a su(d_a)`.  Therefore every listed Weyl conjugation target is in
the reachable projective group; any determinant phase is irrelevant to the
channel.  This proves exact group-level reachability of the target protocol.

It does **not** provide a constructive word in the primitive gauge, flux, and
orbit-current pulses.  The Lie-rank algorithm certifies the connected group
but does not return amplitudes, durations, or a bounded word for each target.
Accordingly this packet is an explicit finite randomized target protocol, not
yet an explicit timed microscopic pulse protocol.

## Verification, assumptions, and falsifiers

Run

```text
uv run --with sympy python research/kitaev/checkers/check_s3_within_block_twirl_protocol.py
```

The checker lists every branch and exact probability, verifies unitarity and
the twirl on all 34 nontrivial-block matrix units, and records the digest of
the source Lie result.  Eight aggregate gates are declared.  Saved result:
`research/kitaev/results/s3-within-block-twirl-protocol.json`.

The finite protocol is falsified by a nonunitary branch, a surviving
traceless matrix unit, an ensemble size other than 20,736, or failure of
projective reachability.  Primitive compilation remains falsified as a
completed claim until actual finite pulse words with amplitudes and durations
are supplied.
