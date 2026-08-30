# The direct rank-seven coherence extension is not flat

## Candidate

Entry 2629 showed that the rank-four associated-grade packet together with
three derivatives of source exact generators spans the complete rank-seven
fiber. The candidate tested here treats those seven classes as one frame and
uses the primitive correction

\[
\nabla r=\nabla f-\sum_i q_i\,\partial g_i.
\]

Entry 2643 supplies exact dual-number differentiation of every reduction and
primitive coefficient.

## Hostile test

For each base direction, solve all seven lifted coordinates over

\[
\mathbb F_p[\epsilon]/(\epsilon^2).
\]

Then export separately:

- the derivative difference;
- the matrix commutator;
- both possible signed sums;
- pivot packets and ordinary value matrices.

The test was repeated at A, B, and HOMA and at two primes.

## Result

For every run and every mixed pair, the derivative term and commutator each
have sixteen nonzero entries. Both signed curvature conventions retain sixteen
nonzero entries.

The defect is confined to the upper-left (4\times4) block. The three
exact-generator directions form a sparse decoupled block and do not cancel
the associated-grade curvature. Value matrices and pivot packets are
identical across the three dual evaluations, excluding variation-dependent
pivot selection as the cause.

## Narrow conclusion

Fiberwise rank completion is not transport completion. The direct sum of the
rank-four packet with the three exact-generator derivative classes is not a
flat rank-seven coefficient object.

This does not refute the existence of a filtered or derived completion. It
shows that any successful completion needs source-derived cross-grade maps or
a coherence differential. Adding the three classes as an uncoupled block is
insufficient.

## Artifacts

- `research/benincasa/checkers/check_cm_rank_seven_dual_flatness.py`
- `research/benincasa/results/cm-rank-seven-dual-flatness.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

