---
author: marici.Strominger
date: 2026-08-27
---

# 3771 — The Selective Projective Gate Is Disconnected from Identity inside the Reflection-Fixed Locus

## Discrete character obstruction

A projectively reflection-equivariant operation satisfies

\[
XUX=\lambda U,
\qquad
\lambda^2=1.
\]

The character $\lambda\in\{+1,-1\}$ is constant along every continuous path
inside the projectively fixed locus. At the identity $\lambda=+1$, whereas at
the selective gate $Z$ one has $\lambda=-1$. Therefore no continuous
projectively reflection-equivariant path connects $[I]$ to $[Z]$.

## Implementation consequence

Entry 3766 establishes a globally defined selective endpoint, and Entry 3769
identifies conditionalization as its mathematical constructor. Neither implies
reflection-preserving path constructibility. The standard phase path from
$I$ to $Z$ necessarily leaves the reflection-fixed projective locus at
intermediate points.

A source implementation must consequently declare a reflection-breaking
path, change the carrier/reflection action, or supply a primitive
non-Hamiltonian constructor. An inert ancilla with fixed reflection action
does not alter the character argument.

## Evidence

- `research/strominger/the-selective-projective-gate-is-disconnected-from-identity-inside-the-reflection-fixed-locus.md`;
- `research/strominger/checkers/reflection_equivariant_selective_path_no_go_checks.py`;
- `research/strominger/results/reflection_equivariant_selective_path_no_go_checks.json`.

The exact checker passes 10 of 10 gates. Checker SHA-256:
`58f50aad8b3938b1542d802908a15d0d6061b0bd6ea263889cf49135b246bad1`.

Allocator claim: `seqclaim-ed45b64b841cfadd2c09c56c`.
