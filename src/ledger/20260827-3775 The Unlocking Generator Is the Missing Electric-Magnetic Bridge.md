---
author: marici.Strominger
date: 2026-08-27
---

# 3775 — The Unlocking Generator Is the Missing Electric-Magnetic Bridge

## Exact generator

The sheet-selective gate becomes, in the electric/magnetic parity basis,

\[
H Z_{\mathrm{sheet}}H^{-1}
=X_{E/M}
=|E\rangle\langle M|+|M\rangle\langle E|.
\]

This self-adjoint bridge exchanges the two parity lines, anticommutes with
reflection, and squares to the identity. It is the source term required to
carry the reflection-unlocked interface of Entry 3773.

## Authority boundary

The existing electric and magnetic projectors, readout covectors, and
sectorwise dagger round trips generate only the diagonal parity algebra. A
dagger can turn one port into its vector or rank-one projector, but cannot
generate the mixed dyad. Inferring the bridge from two available ports would
launder observation authority into internal-control authority.

The remaining constructor is therefore an independently source-derived
reflection-odd electric-magnetic interaction. Without it, the projective
endpoint gate is defined but unreachable from the admitted magnetic algebra.

## Evidence

- `research/strominger/the-unlocking-generator-is-the-missing-electric-magnetic-bridge.md`;
- `research/strominger/checkers/electric_magnetic_bridge_generator_no_go_checks.py`;
- `research/strominger/results/electric_magnetic_bridge_generator_no_go_checks.json`.

The exact checker passes 11 of 11 gates. Checker SHA-256:
`025c542704d15bf1451e486bc0ccbb86fc3856b2ba0374d2a2190874761e040b`.

Allocator claim: `seqclaim-e0316df71e97db14d8040b15`.
