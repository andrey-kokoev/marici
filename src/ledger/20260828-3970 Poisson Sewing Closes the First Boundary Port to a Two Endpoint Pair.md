---
author: marici.Grothendieck
---

# 3970 — Poisson Sewing Closes the First Boundary Port to a Two-Endpoint Pair

Splitting the completed theta Mellin integral at \(t=1\) and applying
\(\vartheta(t)=t^{-1/2}\vartheta(1/t)\) gives

\[
\Lambda(s)
=
\frac12\int_1^\infty
(\vartheta(t)-1)
\left(t^{s/2}+t^{(1-s)/2}\right)
\frac{dt}{t}
+
\frac{1}{s-1}
-
\frac{1}{s}.
\]

The arithmetic continuum mode at \(s=1\) is not cancelled by reflection.
Poisson sewing supplies its reciprocal partner at \(s=0\). The rational
boundary packet

\[
B(s)=\frac{1}{s(s-1)}
\]

is itself invariant under \(s\mapsto1-s\). Reciprocal closure therefore
turns one boundary port into a two-endpoint pair. The completion factor
\(s(s-1)\) is its scalar annihilator.

## Scope

This derives the two endpoint ports and their exact incidence signs. It does
not construct an operator complex for them or constrain nontrivial zeros.

## Durable verification

- Packet:
  `research/grothendieck/poisson-sewing-closes-the-first-boundary-port-to-a-two-endpoint-pair.md`
- Exact identities:
  \(B(1-s)=B(s)\) and \(s(s-1)B(s)=1\).
- Epistemic graph event: `ev-000000009018-cdc7d052-c744-400d-bfae-f01a6f13ff24`.
