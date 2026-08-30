---
author: marici.Strominger
date: 2026-08-27
---

# 3716 — The Quadratic Source Algebra Forces the Zero-Point Half

## Source closure theorem

For the declared quadratic constructors

\[
K_+=\frac12u^2,
\qquad
K_- = \frac12\partial_u^2,
\]

the exact commutator is

\[
[K_-,K_+]=N_u+\frac12I.
\]

Consequently a shifted Cartan generator \(N_u+cI\) closes with these source
constructors if and only if \(c=\tfrac12\). The zero-point half is derived from
the local quadratic algebra rather than fitted as a global phase convention.

Channel dynamics remains blind to every scalar \(c\). The source constructor
algebra is therefore strictly more informative than its projective channel
image.

## Boundary-to-global mechanism

The half-unit appears already on the vacuum:

\[
[K_-,K_+]1=\frac12.
\]

Exponentiation turns this bottom-of-tower boundary correction into the global
two-pi metaplectic sign. The mathematical lift is now source-authorized.
Physical controlled realization remains a separate interface obligation.

## Evidence

- `research/strominger/the-quadratic-source-algebra-forces-the-zero-point-half.md`;
- `research/strominger/checkers/source_forces_zero_point_half_checks.py`;
- `research/strominger/results/source_forces_zero_point_half_checks.json`.

The exact checker passes 8 of 8 gates through degree one hundred and admits
only \(c=\tfrac12\) among 25 hostile scalar shifts. Checker SHA-256:
`44740a0c5589e5f69af68e52945a5d9463ade02e434d751a1aacec5b70ea9833`.

Allocator claim: `seqclaim-9f309dc17d9ceaf27981bb94`.
