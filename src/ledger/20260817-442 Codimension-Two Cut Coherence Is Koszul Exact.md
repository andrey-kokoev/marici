---
id: 442
date: 2026-08-17
title: Codimension-Two Cut Coherence Is Koszul Exact
---

# Codimension-Two Cut Coherence Is Koszul Exact

Entry 441 proves the eight individual six-by-four Cut squares after the
cellular sheet transform. Coherence requires comparing both restriction orders
whenever two physical Cut divisors meet.

Among the 28 unordered pairs of the eight physical octagon cuts, 12 are
compatible and 16 cross. Each compatible pair partitions the octagon into
three quadrilaterals. Its common link is therefore
\[
K_4\times K_4\times K_4.
\]
The link has face counts \((1,6,12,8)\), 125 loaded cells, and loaded chain
ranks
\[
(8,36,54,27)=(2,3)^{*3}.
\]

The two restriction orders are not equal as unoriented operations. Normal
contraction along the first Cut followed by the second differs from the reverse
order by exactly the Koszul sign \(-1\). The audit checks this on all 324
underlying common-link faces, equivalently all 1,500 loaded cells across the
12 compatible pairs.

Entry 87's exact certificate gives zero compatible double residue in every
ordered channel pair. Exact additive transport through the octagon conductor
kernel preserves those zeros. Thus all 24 ordered transformed double residues
vanish, and the required anticommuting square is exact rather than merely
equal after forgetting orientation.

Consequently codimension-two Cut coherence holds in the cellular fs/Kato
sector. The next nontrivial arity test is codimension three: on a complete
quadrangulation of the octagon, compare all six orders of three compatible Cut
restrictions and verify the full alternating \(S_3\) sign representation.

The executable audit is
research/voevodsky/check_n8_codimension_two_cut_coherence.py.
