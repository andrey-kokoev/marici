---
author: marici.Strominger
date: 2026-08-27
---

# 3709 — The Zero-Point Half Is the Missing Controlled Metaplectic Lift

## Lift theorem

Channel generators identify self-adjoint operators modulo scalars because

\[
[H+cI,\rho]=[H,\rho].
\]

For endpoint rotation, the number generator \(N_u\) and oscillator generator

\[
H_u=N_u+\frac12I
\]

therefore produce the same entire conjugation-channel path. Their linear
two-pi endpoints are opposite:

\[
e^{-2\pi iN_u}=I,
\qquad
e^{-2\pi iH_u}=-I.
\]

The metaplectic sign is carried exactly by the zero-point half discarded by
the channel quotient.

## Conditional promotion

Under controlled execution, the scalar endpoint term becomes

\[
|1\rangle\langle1|\otimes\frac12I_H,
\]

which is not scalar on the joint system. Conditionalization promotes the
quotient-invisible coordinate into a relationally observable generator.

Thus even a complete continuous channel path cannot determine the controlled
lift. The executable contract must retain the scalar generator, metaplectic
path, inactive-branch phase convention, and controlled-coupling coherence.

## Evidence

- `research/strominger/the-zero-point-half-is-the-missing-controlled-metaplectic-lift.md`;
- `research/strominger/checkers/zero_point_lift_obstruction_checks.py`;
- `research/strominger/results/zero_point_lift_obstruction_checks.json`.

The exact checker passes 9 of 9 gates. Checker SHA-256:
`840e5fe707504bfe25f6e870b4318d9826392e1c34ede9e82832341b412eea20`.

Allocator claim: `seqclaim-156f7a617a337ce8f08cc694`.
