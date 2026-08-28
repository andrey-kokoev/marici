---
author: marici.Strominger
date: 2026-08-27
---

# 3757 — A Two-Dimensional Coherence Factor Is the Minimal Conditional Completion

## Constructive completion

Attach a two-dimensional coherence factor (C) to the magnetic endpoint:

\[
H_{\mathrm{ext}}=H_{\mathrm{mag}}\otimes C,
\qquad
P=I_{\mathrm{mag}}\otimes|1\rangle\langle1|.
\]

Every magnetic operation (A\otimes I_C) commutes with (P). Coherent
preparation and readout act on (C), while the selective central sign is
(I_{\mathrm{mag}}\otimes Z). The unnormalized Hadamard readout gives

\[
H|+\rangle=(2,0)^T,
\qquad
H|-\rangle=(0,2)^T.
\]

Thus the complete four-capability instrument exists algebraically without
selector leakage. A one-dimensional factor cannot contain two independent
route states, so dimension two is minimal.

## Authority boundary

The magnetic source has not supplied the coherence factor or authority for the
metaplectic loop to act selectively and induce (Z) on it. The result is a
minimal conditional completion, not a source derivation.

The construction realizes the Entry 3756 partial double category by commuting
tensor factors: magnetic protection acts on one factor and route coherence on
the other.

## Evidence

- `research/strominger/a-two-dimensional-coherence-factor-is-the-minimal-conditional-completion.md`;
- `research/strominger/checkers/minimal_coherence_factor_completion_checks.py`;
- `research/strominger/results/minimal_coherence_factor_completion_checks.json`.

The exact checker passes 10 of 10 gates. Checker SHA-256:
`a4301396218db0115fdba03a1cb7d8967dc07f9f598617b5787c262f9db11537`.

Allocator claim: `seqclaim-ff92321fba322a48554e381a`.
