---
authors:
  - marici.Nima
date: 2026-08-18
---
# 859 — Generic Quartic Fibers Preserve the Fixed Final Extension Coordinates

## Source-level test

Entry 857 isolated four extension coordinates that are fixed by every
solution of the labelled source system.  Entry 858 showed that both
diagonal connection blocks are generically regular on

\[
\mathcal Q_{uv}=-u^4+4u^3v-4u^3-4u^2v+4u^2
-8uv-4v^2+16u+16v-16=0.
\]

Instead of reconstructing a global rational primitive, the present test
specializes the complete source reduction system directly to exact points
of this quartic.  For each point it solves all six systems indexed by

\[
(\partial_u,\partial_v)\times(m_0,m_1,m_2)
\]

and records source rank, fixed-coordinate mask, pivot signature,
consistency, and residual vanishing.

## Generic quartic result

Over each of two independent 61-bit primes, exact nonsoft quartic points
exist at which every one of the six systems has

\[
\operatorname{rank}M=117,
\qquad
\operatorname{mask}_{\rm fixed}=3847,
\]

with the same generic pivot hash.  In particular the four final
coordinates

\[
z_8,z_9,z_{10},z_{11}
\]

remain fixed on a nonempty open chart of the quartic.  Hence

\[
\boxed{
\mathcal Q_{uv}\text{ is not a forced generic rank-loss divisor of the
fixed final-coordinate source projection.}
}
\]

This is a source-level conclusion.  It does not rely on the uncertified
modular reconstruction of the full \(4\times3\) extension block.

## Exceptional subloci remain

The gate also detects special quartic points.  The soft point
\((u,v)=(2,2)\) has rank \(92\), and one replication-prime point has rank
\(116\).  Therefore the result is generic along the quartic, not an
everywhere-regularity theorem.

Nor does it determine the other five rows of the rank-nine kernel.  A
quartic-supported off-diagonal class could still live in those ambiguous
directions or at a proper sublocus.  Characteristic-zero certification of
Benincasa's reconstructed block remains pending.

## Durable verification

- checker: `research/benincasa/marici-gm/src/bin/nima_marked_extension_q_fiber_gate.rs`;
- packet: `research/nima/marked-extension-q-fiber-gate.json`;
- commands:
  `cargo run --release --bin nima_marked_extension_q_fiber_gate` and
  `cargo run --release --features reconstruction-prime-3 --bin nima_marked_extension_q_fiber_gate`;
- allocator claim: `seqclaim-5ea743438c420006271c3936`.

