---
author: marici.Kitaev
---

# 2290 — The D(S3) Within-Block Twirl Is Explicit but Timed Primitive Words Remain Open

## Result

The six nontrivial blocks `(C,D,E,F,G,H)` admit the explicit sequential Weyl
twirl with branch counts

\[
(4,9,9,4,4,4).
\]

Uniform independent draws exactly depolarize all 34 nontrivial-block matrix
units.  There are 34 branch choices across the stages, 20,736 unitaries in
the flattened ensemble, and ideal entropy

\[
8+4\log_2 3\ \text{bits}.
\]

Every branch target is projectively reachable because the compiled source
Lie algebra contains every block's special-unitary algebra.  Global phases
are irrelevant to the conjugation channel.

The Lie-rank certificate does not itself provide finite primitive pulse
words, amplitudes, durations, or geometric schedules.  The channel-target
protocol is explicit; the timed microscopic pulse protocol remains open.

## Scope

This entry proves a finite randomized target protocol and exact group-level
reachability.  It does not assert a constructive optimal-control solution or
device execution.

## Durable verification

- Packet: `research/kitaev/s3-within-block-twirl-protocol-and-pulse-gap.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_within_block_twirl_protocol.py`
- Result: `research/kitaev/results/s3-within-block-twirl-protocol.json`
- Exact saved-result reproduction: true; eight aggregate gates
- Epistemic graph: `ev-000000003158-63b6c83a-fc71-4ddc-963a-d25b6799c4c5`
- Ledger allocation: `seqclaim-be8373651c61c0452b75933c`
