---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2232 — Energy Collisions Quotient Boolean Routes by Deletion Counts

## Collision partition

Partition the labelled edge set into equal-energy blocks

\[
E=B_1\sqcup\cdots\sqcup B_d,
\qquad |B_a|=m_a.
\]

A momentum-only Gaussian deformation assigns one multiplier \(g_a\) to all
edges in \(B_a\). The route polynomial becomes

\[
F(g)=\sum_{S\subseteq E}v_S
\prod_{a=1}^dg_a^{|S\cap B_a|}.
\]

Thus physical responses determine only the grouped coefficients

\[
V_{k_1,\ldots,k_d}
=\sum_{|S\cap B_a|=k_a}v_S,
\qquad 0\le k_a\le m_a.
\]

The faithful momentum-score quotient has dimension

\[
\boxed{
\prod_{a=1}^d(m_a+1),
}
\]

instead of \(2^{|E|}\).

## Consequence

Arbitrarily high momentum-only score order reconstructs every deletion-count
aggregate but cannot distinguish subsets with the same count vector inside
an equal-energy block. This is a structural quotient, not a finite-order
failure that more derivatives can repair.

## Evidence

- Entries 2228 and 2231
- `research/benincasa/checkers/energy_collision_route_quotient.rs`
