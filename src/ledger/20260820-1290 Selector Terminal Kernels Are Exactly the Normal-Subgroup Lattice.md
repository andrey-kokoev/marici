---
title: "Selector Terminal Kernels Are Exactly the Normal-Subgroup Lattice"
date: 2026-08-20
entry: 1290
status: active-selector-kernel-realization-theorem
author: marici.Grothendieck
---

# 1290 — Selector Terminal Kernels Are Exactly the Normal-Subgroup Lattice

Sequence claim receipt: `seqclaim-b0c6d9ab50360fcae4793f03`.

Sequence claim idempotency key:
`grothendieck-ledger-selector-terminal-kernel-realization`.

## Complete realization theorem

Ledger 1287 assigns every selector (c) the normal terminal kernel

\[
K_c=\operatorname{Core}_G(\operatorname{Stab}_R(c)).
\]

Conversely, every normal subgroup (K\triangleleft G) is realized exactly by
the quotient-label selector

\[
c_K:G\longrightarrow G/K,\qquad g\longmapsto gK.
\]

Its right stabilizer is precisely (K), so (K_{c_K}=K). Consequently the
selector terminal kernels are exactly the normal-subgroup lattice, and

\[
K\longmapsto c_K\longmapsto K_{c_K}
\]

is the identity.

## Arithmetic corollary

Every algebraic finite-surjection spectrum (U(K)) from Ledgers 1281--1282
is coefficient-realizable by the selector (c_K). There is no missing
coefficient selector in the abstract theory; the remaining question is
whether the sector supplies that selector and the required Betti map.

## Exact nonabelian control

For (S_3), exhaustive enumeration finds six subgroups and exactly three
normal subgroups, of orders (1,3,6). Their quotient-label selectors have
stabilizers and terminal kernels of precisely those same orders.

## Scope and verification

Replacing a frozen selector by (c_K) changes the observable. Algebraic
realizability does not authorize a physical readout, relative-chain
pushforward, boundary square, or pairing.

- Proof packet:
  `research/grothendieck/selector-terminal-kernel-realization.md`.
- Checker:
  `research/grothendieck/checkers/selector_terminal_kernel_realization.py`.
- Exact checker result: all six (S_3) subgroups enumerated; normal and realized
  terminal-kernel orders both equal (1,3,6); all assertions pass.
- Epistemic graph theorem, nonabelian census, and source admission: event 1292.
- No site build was run, by operator instruction.
