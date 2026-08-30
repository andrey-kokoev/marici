# 2651 — Retaining the Primitive Exact Term Does Not Create Cross-Grade Transport

## Candidate

Entry 2648 subtracts the primitive term in

\[
\nabla r=\nabla f-\sum_iq_i\,\partial g_i.
\]

The first remaining possibility was that the filtered total object should
retain

\[
\sum_iq_i\,\partial g_i
\]

as the missing map between the visible rank-four grade and the three
exact-generator directions.

## Hostile comparison

The retained and subtracted dual matrix packets were computed with identical
bases, pivots, points, and primes. The matrix difference is source-derived;
no cross block was fitted.

## Result

The difference is block diagonal:

- a dense (4\times4) visible correction;
- one diagonal coherence entry;
- no visible-to-coherence or coherence-to-visible component.

Both curvature conventions remain nonzero. The retained version additionally
produces one coherence-block curvature entry at ((5,5)) for (F_{12}) and
(F_{13}).

## Narrow conclusion

The first primitive term is not a cross-grade differential. Choosing whether
to subtract or retain it changes diagonal-grade transport but cannot repair
mixed flatness.

The next finite search is in the source syzygies among the four exact
generators and their differentiated relations. A successful completion must
derive an off-diagonal mapping-cone or higher-homotopy cell from that complex;
no additional fitted coefficient class is licensed.

## Artifacts

- `research/benincasa/cm-retained-primitive-cross-grade-falsifier.md`
- `research/benincasa/checkers/check_cm_rank_seven_dual_flatness.py`
- `research/benincasa/results/cm-rank-seven-dual-cross-grade.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

Ledger sequence claim: `seqclaim-9b53738af3b99611e90288f6`.

Epistemic event: `ev-000000004019-e83d8b93-d47f-4eef-b001-af0e9624aca1`.
