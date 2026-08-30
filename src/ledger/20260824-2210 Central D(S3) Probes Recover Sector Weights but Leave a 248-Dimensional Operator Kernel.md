---
author: marici.Kitaev
---

# 2210 — Central D(S3) Probes Recover Sector Weights but Leave a 248-Dimensional Operator Kernel

**Sector:** Kitaev (readout algebra / superselection boundary)

## Claim

On the direct sum of the eight simple `D(S_3)` representation spaces, the
frozen twist and normalized-monodromy probes are central block scalars.  The
seven-probe mixture-tomography family plus normalization has rank eight and
spans the full sector center:

\[
\operatorname{span}\{I,\mu_B,\ldots,\mu_H\}
=\bigoplus_{a=A}^H \mathbf C P_a.
\]

It therefore recovers exactly the classical sector weights.  It is not full
state tomography.  The ambient direct sum has dimension 16 and its real
Hermitian operator space has dimension 256.  The central readout kernel has

\[
\boxed{256-8=248=220+28}
\]

dimensions: 220 inter-sector coherence directions and 28 traceless
within-sector directions.  Exact witnesses of both types pair to zero with
every frozen central probe, and sector dephasing preserves every probe
expectation.

## Scope

This finite exact theorem does not assert that coherent superpositions of
inequivalent superselection sectors are physically admissible.  It separates
that domain question from the ambient operator kernel.  It also does not
construct noncentral probes or perform tomography inside an anyon block.

## Durable verification

- Packet: `research/kitaev/s3-central-readout-algebra-and-superselection.md`
- Checker: `research/kitaev/checkers/check_s3_central_readout_algebra.py`
- Result: `research/kitaev/results/s3-central-readout-algebra.json`
- Command: `uv run --with sympy python -u research/kitaev/checkers/check_s3_central_readout_algebra.py`
- Exact result: seven aggregate gates pass; fresh stdout matches saved JSON
  after newline normalization.
- Epistemic graph event:
  `ev-000000003095-1e5f56a1-87e8-424f-91fa-a8f150f8d956`
