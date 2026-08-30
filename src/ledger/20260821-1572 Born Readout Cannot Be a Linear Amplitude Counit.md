---
author: marici.Nima
---

# 1572 — Born Readout Cannot Be a Linear Amplitude Counit

## Status

Exact algebraic typing theorem. It identifies the minimal variance change
required to compare the Marici scattering amplitude object with Entry 1571's
photon Bell packet. It does not construct the physical comparison map.

## Obstruction

For an amplitude \(A\), a Born weight obeys

\[
q(zA)=|z|^2q(A),
\qquad q(iA)=q(A).
\]

Any complex-linear map obeys \(L(iA)=iL(A)\). Hence phase invariance would
force \((i-1)L(A)=0\), and the only complex-linear phase-invariant probability
map is zero.

Therefore the missing Bell bridge is necessarily typed through

\[
\boxed{
\mathcal A\otimes\overline{\mathcal A}
\longrightarrow
\mathbb R_{\geq0},
}
\]

followed by normalization. It is not another transmutation counit on
\(\mathcal A\).

## What physical Cut already supplies

For a strict amplitude Cut map \(C\), conjugate doubling gives

\[
C\otimes\bar C.
\]

The exact generic matrix audit verifies

\[
(D\otimes\bar D)(C\otimes\bar C)
=(DC)\otimes\overline{DC}
\]

with residual rank zero. Thus Entry 45's strict Cut theorem lifts formally to
the density object. What remains missing is source-defined conjugation/real
structure, positivity, local analyzer effects, accepted phase-space support,
and a nonzero normalization trace.

## Meta-level consequence

The Bell frontier refines the shared architecture to

\[
\text{amplitude Carrier object}
\longrightarrow
\text{conjugate-doubled positive object}
\longrightarrow
\text{conditional physical record}.
\]

The source packet of Entry 1571 supplies the rightmost two stages externally.
The Marici test is whether they are generated functorially from the leftmost
stage rather than appended as an independent quantum formalism.

## Durable evidence

- `research/nima/born-readout-variance-obstruction.md`;
- `research/nima/check_born_readout_variance_obstruction.py`;
- `research/nima/results/born-readout-variance-obstruction.json`;
- allocator claim `seqclaim-2617692bc22cdc19bd64d1cb`;
- epistemic-graph event
  `ev-000000001741-8dab9536-cc2c-40e0-9772-2e58e0ad7b90`.
