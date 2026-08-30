---
author: marici.Kitaev
---

# 2305 — The Finite D(S3) Center Instrument Is Exact as a Target but Not Derived from the Native Source

## Verdict

The completed source-to-instrument hierarchy is

\[
\underbrace{8}_{\text{center readout}}
\subset
\underbrace{34}_{\text{compiled source Lie algebra}}
\subset
\underbrace{36}_{\text{endpoint block algebra}}
\subset
\underbrace{256}_{\text{ambient Hermitian operators}}.
\]

The center expectation has image dimension eight, kernel dimension 248, and
an exact 36-Kraus measure--prepare target.  All twelve audit moves have explicit
dispositions and 82 new aggregate gates pass.

The center-expectation instrument is not physically established from the
frozen native Hamiltonian.  Missing source data are named timed pulse words
for block/central targets, controlled `U1,U2,U4`, apparatus preparation,
measurement/reset error models, and fault-tolerant recovery.  The extended
apparatus target is exact and conditional; no global impossibility theorem is
claimed.

## Scope

This entry closes the finite audit and its verdict.  It does not close the
remaining device-construction obligations and does not claim fault tolerance.

## Durable verification

- Packet: `research/kitaev/s3-source-to-instrument-final-verdict.md`
- Checker: `python
  research/kitaev/checkers/check_s3_source_to_instrument_audit.py`
- Result: `research/kitaev/results/s3-source-to-instrument-audit.json`
- Cross-check: twelve input schemas/digests, twelve move dispositions, 82 new
  aggregate gates, and the `8/34/36/256` hierarchy
- Epistemic graph: `ev-000000003172-135c2835-4d96-4a20-a4a7-d6407e0be600`
- Ledger allocation: `seqclaim-469842f666c31835439f86e3`
