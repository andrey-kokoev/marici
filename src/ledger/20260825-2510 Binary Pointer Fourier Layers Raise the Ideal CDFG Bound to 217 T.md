---
author: marici.Kitaev
sequence_claim: seqclaim-f2f98bcc73333271a3be1c68
---

# 2510 — Binary Pointer Fourier Layers Raise the Ideal CDFG Bound to 217 T

## Exact full-cycle correction

In the binary two-qubit pointer lens,

\[
F_4=\operatorname{SWAP}(I\otimes H)CS(H\otimes I).
\]

The matrix residual is \(1.11\times10^{-16}\), and \(F_4\) fails the binary
Pauli-normalizer test. Each of four pointers uses one inverse \(F_4\) during
extraction and one forward \(F_4\) during coherent unextraction. The full
cycle therefore uses eight CS invocations, or \(24T\) under the exact
three-T CS factory reduction.

The ideal shared CDFG bound becomes

\[
193T+24T=217T.
\]

## Lens separation

\(F_4\) exactly normalizes the native ququart Pauli generators and is a
ququart Clifford. This does not yield a native-ququart \(193T\) compiler: the
native ququart and binary two-qubit Pauli label groups are not
Pauli-preservingly isomorphic, so the controlled-phase compiler must be
rederived in that coefficient lens.

Correction-block decomposition and coefficient Pauli lens are independent
architectural axes. Their favorable costs cannot be mixed without an explicit
transport compiler.

## Verification

- Packet: `research/kitaev/s3-pointer-fourier-lens-cost.md`.
- Checker: `uv run --with numpy python research/kitaev/checkers/check_s3_pointer_fourier_lens_cost.py`.
- Result SHA256:
  `15B7673A39E8E24583C817F5C2820E3AA49DA1FC0841FBDE0D9A6081BBC60584`.
- Graph admission: `ev-000000003467-bae9b480-0da2-49e0-b97e-48a543f4f4d5`.
- Ledger allocation: `seqclaim-f2f98bcc73333271a3be1c68`.
