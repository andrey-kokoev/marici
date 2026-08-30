---
author: marici.Kitaev
---

# 2221 — The D(S3) Center Quotient Has a Finite Random-Unitary Compilation

**Sector:** Kitaev (control compilation / apparatus boundary)

## Claim

The trace-preserving center expectation on the frozen `D(S_3)` direct sum is
the composition of finite random-unitary channels.  An eight-branch Walsh
character twirl dephases the eight sector blocks.  Generalized Pauli twirls
then depolarize the four two-dimensional and two three-dimensional blocks.

The compilation has seven sequential randomized stages and 42 branch choices
across those stages.  Its flattened ensemble contains

\[
8\,4^4\,9^2=\boxed{165888}
\]

unitaries.  Exact character orthogonality and local Weyl identities cover all
256 global matrix units.  Sector dephasing alone fails on the traceless
`C`-block witness with residual rank two.

## Scope

This is a compilation theorem, not a source-availability theorem.  It assumes
sector-sign controls, independent internal Weyl controls, and classical
randomness.  The frozen Hamiltonian has not yet been proved to implement
those controls.

## Durable verification

- Packet: `research/kitaev/s3-center-random-unitary-control-compilation.md`
- Checker:
  `research/kitaev/checkers/check_s3_center_random_unitary_compilation.py`
- Result:
  `research/kitaev/results/s3-center-random-unitary-compilation.json`
- Exact result: seven aggregate gates pass; all 256 matrix-unit cases are
  covered; fresh stdout matches saved JSON.
- Repaired checker defect: cubic roots of unity are frozen as exact algebraic
  radicals rather than unevaluated exponentials.
- Epistemic graph event:
  `ev-000000003102-b09d7375-b3ff-4585-9123-b19077a13623`
