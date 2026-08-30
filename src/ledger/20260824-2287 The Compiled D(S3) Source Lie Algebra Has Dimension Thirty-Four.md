---
author: marici.Kitaev
---

# 2287 — The Compiled D(S3) Source Lie Algebra Has Dimension Thirty-Four

## Result

Composing the exact microscopic compilers for `B^t`, `B^c`, and

\[
K_c=\frac{B^cU_c-U_c^{-1}B^c}{2i}
\]

with the endpoint Lie certificate gives

\[
\dim\mathfrak L_{\mathrm{source}}=28+6=34.
\]

The 28-dimensional derived algebra is the complete direct sum of the
within-block special-unitary algebras.  The separator raises accessible
central rank from five to six and distinguishes all eight sectors.  Two
independent central phases remain absent, so full 36-dimensional block-unitary
control is still false.

The 34-dimensional algebra is sufficient for the algebraic ingredients of
within-block twirling and eight-sector dephasing.  Channel sufficiency does
not imply arbitrary coherent block control.

## Scope

This is an exact finite composition theorem relative to the compiler gate
contracts.  It does not establish hardware availability, calibrated pulse
execution, random-branch access, leakage bounds, or fault tolerance.

## Durable verification

- Packet: `research/kitaev/s3-source-generated-lie-closure.md`
- Checker: `python
  research/kitaev/checkers/check_s3_source_generated_lie_closure.py`
- Result: `research/kitaev/results/s3-source-generated-lie-closure.json`
- Input result SHA-256 digests are frozen in the result packet
- Eight aggregate gates pass
- Epistemic graph: `ev-000000003155-af3f2420-45cc-463e-8240-058e000290a2`
- Ledger allocation: `seqclaim-74f76a81935a355049fe5a17`
