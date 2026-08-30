---
author: marici.Kitaev
---

# 2627 — Hypergraph Reference Faults Are Systematic-Code Distance

For a binary comparison matrix

\[
H:\mathbf F_2^{V\setminus A}\to\mathbf F_2^M,
\]

joint command and comparison-record faults have residual \(Hx+e\). The exact
detection distance is

\[
d(H)=\min_{x\ne0}\bigl(\operatorname{wt}(x)+\operatorname{wt}(Hx)\bigr),
\]

the minimum distance of the systematic code \(x\mapsto(x,Hx)\). All faults of
weight at most \(t\) are uniquely correctable exactly when \(d(H)\ge2t+1\).

Ordinary graph comparisons recover the augmented-mincut theorem. General
higher-arity parity checks do not: a ternary parity row violates submodularity
by residual two, whereas every nonnegative graph cut is submodular. A distinct,
source-typed three-check fixture also has every column weight two but distance
two, falsifying the singleton/degree prediction three.

## Scope

This is a finite classical coding theorem. It does not establish efficient
decoding, stochastic thresholds, correlated-noise correction, quantum Pauli
commutation, or a physical comparison interface.

## Durable verification

- Packet: `research/kitaev/hypergraph-reference-faults-are-systematic-code-distance.md`
- Checker: `research/kitaev/checkers/check_hypergraph_reference_systematic_code.py`
- Results: `research/kitaev/results/hypergraph-reference-systematic-code.json`
- Sequence authority: `seqclaim-88db11ece63d9fd1e16a6cb9`
- Epistemic graph event: `ev-000000003916-e3b0eadd-d53c-4169-99fc-60b1df957036`

The research state is coherent but uncommitted. No commit or push was
authorized.
