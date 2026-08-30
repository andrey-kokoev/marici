# 2648 — The Direct Rank-Seven Exact-Generator Completion Is Not Flat

## Candidate under test

Entry 2629 found that three source exact-generator derivatives fill the
fiberwise rank gap between the four visible classes and the rank-seven
localized quotient. Entry 2643 made their local derivatives exact over dual
numbers. The simplest candidate was therefore the direct seven-class frame
with primitive correction

\[
\nabla r=\nabla f-\sum_i q_i\,\partial g_i.
\]

## Acceptance contract

The checker retains termwise ordinary-basis identity and source traces, solves
the seven coordinates over dual numbers, and exports separately:

- derivative differences;
- frame commutators;
- both commutator signs;
- pivot packets.

It runs at A, B, and HOMA with a second-prime replication at A.

## Result

For all three mixed pairs in every run:

\[
\#\operatorname{supp}(\partial_iA_j-\partial_jA_i)=16,
\]

\[
\#\operatorname{supp}([A_i,A_j])=16.
\]

Both signed curvature candidates also have support size sixteen. The support
is exactly the upper-left (4\times4) block. The three added coherence
directions remain in a sparse decoupled block and supply no cancellation.

Value matrices and pivot packets agree across all three dual variations, so
the defect is not a variation-dependent pivot artifact.

## Narrow conclusion

The inference

\[
\text{rank-four packet}+\text{three exact-generator directions}
\Longrightarrow\text{flat rank-seven transport}
\]

is falsified for the direct-sum constructor.

Entry 2629's fiberwise span theorem remains valid. What fails is promotion of
that span to transport without a source-derived cross-grade differential or
homotopy. The next search must derive such a map from the filtered exact
complex; it may not add another fitted coefficient class.

## Artifacts

- `research/benincasa/cm-rank-seven-dual-curvature-falsifier.md`
- `research/benincasa/checkers/check_cm_rank_seven_dual_flatness.py`
- `research/benincasa/results/cm-rank-seven-dual-flatness.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

Ledger sequence claim: `seqclaim-4ece1b02ff5dab835eed0a83`.

Epistemic event: `ev-000000004009-5239dcc5-f2ef-40c9-b9de-1bf73c03c5df`.
