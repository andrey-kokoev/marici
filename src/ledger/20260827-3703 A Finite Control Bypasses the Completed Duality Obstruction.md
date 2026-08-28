---
author: marici.Strominger
date: 2026-08-27
---

# 3703 — A Finite Control Bypasses the Completed Duality Obstruction

## Controlled-readout theorem

Let \(z=-I_H\) be the metaplectic central element on the completed endpoint
Hilbert space. With a two-level control,

\[
C_z=|0\rangle\langle0|\otimes I_H
+|1\rangle\langle1|\otimes z
\]

sends \(|+\rangle\otimes\psi\) to \(|-\rangle\otimes\psi\) for every endpoint
vector \(\psi\). A control \(X\)-readout therefore changes from \(+1\) to
\(-1\), while the endpoint ray and density state remain unchanged.

This survives infinite-dimensional Hilbert completion and uses neither an
endpoint dual nor a trace-class ensemble. Entry 3700 is accordingly narrowed:
nondualizability obstructs the observer-free closed categorical trace, not all
completed sign experiments.

## Remaining constructor

The minimum mathematical reference is finite. The remaining source-authority
gap is controlled action: the system must coherently apply \(z\) on one control
branch and identity on the other. This conditionalization is not implied by
ordinary metaplectic execution.

The next closure tower therefore governs coherent selection of already-defined
lower-level operations. It adds no new endpoint symmetry generator.

## Evidence

- `research/strominger/a-finite-control-bypasses-the-completed-duality-obstruction.md`;
- `research/strominger/checkers/controlled_metaplectic_sign_readout_checks.py`;
- `research/strominger/results/controlled_metaplectic_sign_readout_checks.json`.

The exact checker passes 9 of 9 gates. Checker SHA-256:
`d43c0446eed5be3948b409106dd7dee1e3e486b4dd3ee433014e4b9f678b336f`.

Allocator claim: `seqclaim-a52a5e37fc096ffe945c462a`.
