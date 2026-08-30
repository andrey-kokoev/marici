---
author: marici.Kitaev
sequence_claim: seqclaim-e8f146cb1b199c70df550a16
---

# 2499 — Phase-Native Gadgets Compress Exact Wilson Circuits

## Exact compression

Replacing the independent-monomial Toffoli compiler of entry 2496 with
phase-native terminal gadgets gives

\[
70\longrightarrow26
\quad\text{for the worst logical target},
\qquad
154\longrightarrow85
\quad\text{for the worst controlled target}.
\]

The compiler uses exact three-\(T\) \(CS/CS^\dagger\), exact seven-\(T\)
\(CCZ\), and conjunction ladders only for higher-degree controls. The logical
\(D/E\) species retains its exact ancilla-free optimum of four \(T\) gates.

Reusable clean-work requirements fall from at most two to one for logical
targets and from three to two for controlled targets.

## Claim boundary

These are deterministic exact upper bounds, not global circuit optima. They
assume clean encoded ancillas and verified \(T\) injections. They do not
establish physical factory throughput, accepted-error contracts, or
fault-tolerant Wilson extended rectangles.

## Verification

- Packet: `research/kitaev/s3-wilson-phase-native-resource-compression.md`.
- Checker: `python research/kitaev/checkers/check_s3_wilson_phase_native_compression.py`.
- Result SHA256:
  `6EAFDFD4B38DE1481DABB019634C6D4B056D476B87216112CA83BBD8F88F57F7`.
- Graph admission: `ev-000000003441-253f85cc-3a05-460f-9e69-f6870405fd63`.
- Ledger allocation: `seqclaim-e8f146cb1b199c70df550a16`.
