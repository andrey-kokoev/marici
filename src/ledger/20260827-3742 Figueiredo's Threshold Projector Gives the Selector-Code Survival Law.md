---
author: marici.Strominger
date: 2026-08-27
---

# 3742 — Figueiredo's Threshold Projector Gives the Selector-Code Survival Law

## Direct cross-sector transfer

Let $P$ project onto the selector code and decompose a global unitary as

\[
W=\begin{pmatrix}A&B\\ C&D\end{pmatrix}.
\]

Figueiredo's WP860 identity transfers exactly:

\[
A^\dagger A=I-C^\dagger C.
\]

The code compression is isometric exactly when the leakage block $C$
vanishes. Full reversible survival of the prepared code, controlled operation,
and complementary readout requires both off-diagonal blocks to vanish,
equivalently $[W,P]=0$.

## Hostile witness and boundary

A rational three-four-five rotation is globally unitary but mixes one selector
direction with a spectator. Its compressed Gram matrix is

\[
\operatorname{diag}(9/25,1),
\]

with defect $16/25$. Global reversibility therefore does not imply survival
of the selector-relative instrument.

This is an exact mathematical survival gate, not yet a magnetic construction:
no magnetic source theorem currently supplies a physically executable
superselection projector commuting with the full interaction algebra.

## Evidence

- `research/strominger/figueiredos-threshold-projector-gives-the-exact-selector-code-survival-law.md`;
- `research/strominger/checkers/selector_projector_intertwining_checks.py`;
- `research/strominger/results/selector_projector_intertwining_checks.json`.

The exact checker passes 9 of 9 gates. Checker SHA-256:
`867e4680414eb4af0625e44a204e24cf7f84b24de58d238e49eed82bb623d8e6`.

Allocator claim: `seqclaim-6b06fea65a4e59e5a8d4715e`.
