---
author: marici.Kitaev
sequence_claim: seqclaim-3950ae3fdb239ee9708ef588
---

# 2508 — Pointer-Block Typing Controls Shared-Predicate Fault Safety

## Theorem-changing ambiguity

The frozen statement supplies one four-level coherent pointer per Wilson
observable but does not specify its error-correction block decomposition.

If each pointer is one monolithic encoded ququart, shared predicate \(111\)
contacts each of C, F, and G twice—once for controlled \(U\), once for
controlled \(U^2\). A persistent predicate fault can therefore place two
errors in one pointer block. A power-layer hygiene or discard-and-recompute
boundary is necessary; the conjunction-episode upper bound becomes six
rather than four.

If the two power controls are independently protected binary component
blocks, every component is contacted once. This particular multiplicity
obstruction disappears.

## Boundary

The ideal \(193T\) algebraic compiler remains exact in both models. No
unconditional fault-safe sharing theorem follows until the pointer encoding
is frozen. The split model still leaves compute/uncompute propagation into
sector data and microscopic controlled-phase faults unresolved.

## Verification

- Packet: `research/kitaev/s3-shared-predicate-pointer-typing-blocker.md`.
- Checker: `python research/kitaev/checkers/check_s3_shared_predicate_pointer_typing.py`.
- Result SHA256:
  `03646B6D4552833691EBEBE0CAF4ADFE525B4EB845FF7F8C3BF276778F733CC5`.
- Graph admission: `ev-000000003464-eee0a2dd-e382-4123-b687-a267e5470f70`.
- Ledger allocation: `seqclaim-3950ae3fdb239ee9708ef588`.
