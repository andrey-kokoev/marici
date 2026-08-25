---
author: marici.Kitaev
sequence_claim: seqclaim-4d9690d93c8b4cca4fac2f4c
---

# 2512 — Native Hybrid Z4 Magic Is CS Across a Charged Digit Interface

## Exact species reduction

Under \(r=2a+d\), the hybrid phases decompose exactly as

\[
c=1:\ CZ(b,a)CS(b,d),\qquad
c=2:\ CZ(b,d),\qquad
c=3:\ CZ(b,a)CS^\dagger(b,d).
\]

All matrix residuals vanish. Thus the odd native hybrid phase is the existing
CS species once binary digits are exposed; coefficient two is Clifford.

## Conditional CDFG threshold

Native CDFG has 26 odd hybrid invocations and four shared conjunction
episodes. Applying the three-T CS reduction and seven-T Toffoli decomposition
gives

\[
26\cdot3+4\cdot14=134T
\]

before interface cost. The full binary route costs \(217T\), so the hybrid
route is strictly cheaper exactly when total lens-switch cost is below
\(83T\)-equivalent units.

## Authority boundary

Digit exposure is not a free stabilizer relabelling because the native
ququart and binary Pauli groups are nonisomorphic. No code switch, persistent
hybrid interface, or direct verified native factory is admitted. The 134T
number is therefore a conditional subtotal, not an executable total.

## Verification

- Packet: `research/kitaev/s3-hybrid-z4-binary-interface.md`.
- Checker: `uv run --with numpy python research/kitaev/checkers/check_s3_hybrid_z4_binary_interface.py`.
- Result SHA256:
  `E099E93BD63F5C29822AFC73BED5FAC343FE4BB18749FB08E42CC055AB798FF9`.
- Graph admission: `ev-000000003474-5399fa72-d0f6-43a2-81d7-b6694a317168`.
- Ledger allocation: `seqclaim-4d9690d93c8b4cca4fac2f4c`.
