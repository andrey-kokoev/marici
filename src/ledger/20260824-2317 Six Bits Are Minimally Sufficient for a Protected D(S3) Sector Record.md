---
author: marici.Kitaev
sequence_claim: seqclaim-939790d48ea19651b7e246ff
---

# 2317 — Six Bits Are Minimally Sufficient for a Protected D(S3) Sector Record

## Verdict

The raw three-bit record uses every word of `F2^3`; all 24 single-bit flips
therefore produce another valid sector label.  A one-error-correcting binary
record for eight sectors must obey `8(1+n) <= 2^n`, ruling out every
`n <= 5`.  Puncturing the length-seven binary simplex code gives an exact
`[6,3,3]` code, so six bits are necessary and sufficient.  All 48 one-bit
corruptions decode uniquely.

## Scope

The code protects a final record after the correct label reaches the encoder.
It does not repair controlled-power, inverse-Fourier, wrong-input, or
unprotected encoder faults, and it does not supply the missing controlled
unitaries.

## Durable verification

- Packet: `research/kitaev/s3-sector-record-minimal-redundancy.md`
- Checker: `python
  research/kitaev/checkers/check_s3_sector_record_redundancy.py`
- Result: `research/kitaev/results/s3-sector-record-redundancy.json`
- Epistemic graph: `ev-000000003183-b0b8ea16-56d6-4338-9899-b8f8d434f8d2`
- Ledger allocation: `seqclaim-939790d48ea19651b7e246ff`
