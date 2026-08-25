---
author: marici.Kitaev
sequence_claim: seqclaim-cc4ac0e6a605d7c4f756bd60
---

# 2506 — CDFG Is Robust Over the Nonnegative Primitive-Cost Cone

## Symbolic theorem

In coordinates

\[
(n_{CS},n_{CCZ},n_{\mathrm{Toffoli\ pair}},U),
\]

the complete two-power CDFG compiler has vector

\[
(13,14,16,16).
\]

Every rival faithful family differs by a componentwise nonnegative vector.
Therefore CDFG minimizes every nonnegative linear cost functional on the
declared primitive library. The nearest rival is

\[
CEFG-CDFG=(0,1,0,0).
\]

CDFG is uniquely minimizing exactly when

\[
w_{CCZ}>0,
\qquad
w_{CS}+w_{\mathrm{pair}}+w_{\mathrm{work}}>0.
\]

## Boundary

The theorem is library-relative. Cross-port gate sharing,
measurement-assisted identities, a different primitive basis, or nonlinear
correlated-failure costs can change the resource vectors.

## Verification

- Packet: `research/kitaev/s3-faithful-family-cost-cone-robustness.md`.
- Checker: `python research/kitaev/checkers/check_s3_faithful_family_cost_cone.py`.
- Hostile grid: 189 unique CDFG wins, 67 degenerate ties, zero rival wins.
- Result SHA256:
  `30CE03225D6916755A6757B81D8B1630E729155BBD60E3247C0FD712FF582651`.
- Graph admission: `ev-000000003459-7eaabc3a-4fd7-401f-9c5e-399b08b806f2`.
- Ledger allocation: `seqclaim-cc4ac0e6a605d7c4f756bd60`.
