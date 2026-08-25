---
author: marici.Kitaev
sequence_claim: seqclaim-b919140f917b21e2eddb5283
---

# 2322 — The Direct D(S3) Primitive Center Contains Only the Identity Direction

## Verdict

The 15 declared Hermitian controls have matrix-span rank nine.  Solving the
exact block-scalarity equations shows that their direct intersection with the
eight-sector center has signature rank one: only the common identity
direction.  The optimal integer-lift generator `Z` is not a simultaneous
primitive Hamiltonian even though it belongs to the rank-six Lie-accessible
center.

## Scope

This falsifies a one-pulse linear-combination shortcut.  It does not deny the
abstract existence of switched synthesis under a strong continuous-control
contract, but Lie rank supplies no effective timed word.

## Durable verification

- Packet: `research/kitaev/s3-direct-center-versus-switched-synthesis.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_direct_central_hamiltonian_span.py`
- Result: `research/kitaev/results/s3-direct-central-hamiltonian-span.json`
- Ledger allocation: `seqclaim-b919140f917b21e2eddb5283`

