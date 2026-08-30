# Retaining the primitive term does not create a cross-grade map

## Question

For an exact lift

\[
f=r+\sum_i q_i g_i,
\]

Entry 2648 used the corrected representative

\[
\nabla r=\nabla f-\sum_i q_i\,\partial g_i.
\]

The filtered totalization might instead retain the source-derived term

\[
\sum_i q_i\,\partial g_i
\]

as a map between the visible and exact-generator grades.

## Result

The retained and corrected dual matrix packets were compared at A, B, and
HOMA and at two primes. Their difference has support only in:

- the visible (4\times4) diagonal block;
- one diagonal entry of the three-dimensional coherence block.

There is no off-diagonal visible--coherence component. Mixed curvature remains
nonzero under both conventions. In addition, (F_{12}) and (F_{13}) acquire
one extra coherence-block defect at entry ((5,5)).

## Conclusion

The primitive multiplication term is not the missing cross-grade
differential. Retaining it changes the two diagonal-grade connections but does
not couple them.

The next admissible object must come from a higher syzygy or mapping-cone
differential in the exact complex. It cannot be obtained merely by deciding
whether to subtract or retain the first primitive term.

## Artifacts

- `research/benincasa/checkers/check_cm_rank_seven_dual_flatness.py`
- `research/benincasa/results/cm-rank-seven-dual-cross-grade.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

