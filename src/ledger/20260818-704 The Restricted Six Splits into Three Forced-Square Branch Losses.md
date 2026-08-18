---
authors:
  - marici.Nima
date: 2026-08-18
---
# 704 — The Restricted Six Splits into Three Forced-Square Branch Losses

## Hard-to-vary localization

Entries 596 and 702 compute the same deletion census on the
\(q_{\mathcal G_{12}}\)-residue surface before and after homogeneous
specialization. In the fixed source order

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}}),
\]

the generic and homogeneous rank increments are respectively

\[
(3,4,5,5),\qquad (1,2,3,5).
\]

Their difference is

\[
\boxed{(2,2,2,0).}
\]

Hence Entry 703's restricted Euler defect six is supported linewise as

\[
\boxed{6=2_{g_1}+2_{g_2}+2_{g_3}+0_{g_{23}}.}
\]

## Branch geometry

Generically, each of the four retained lines meets the Cayley--Menger
branch divisor in four distinct points. At \(P_i=X_i\), the first three
lines become forced-square boundary lines with only two distinct branch
points, whereas the occurrence line \(q_{g_{23}}\) remains an ordinary
quartic with four distinct branch points.

The finite line-incidence counts do not change between the two censuses.
Thus each decrement two comes entirely from collision of a pair of branch
punctures, not from disappearance or creation of an intersection between
marked lines.

## Candidate vanishing-cycle decomposition

This identifies the only geometrically admissible support for the
restricted comparison defect. Before hypercohomological cancellations, its
Euler class must decompose into three local packets

\[
\Phi_{g_1}\oplus\Phi_{g_2}\oplus\Phi_{g_3},
\qquad \chi(\Phi_{g_i})=2.
\]

The occurrence line contributes no packet. This is a necessary
Euler-characteristic decomposition, not yet a theorem that the derived cone
is concentrated in one degree or splits as a direct sum.

## Consequence for the comparison map

The restricted base-change map \(\beta_{4|G}\) should be constructed
locally near the three forced-square collisions and then glued through the
marked-line localization complex. Any finite model assigning part of the
six-unit defect to \(q_{g_{23}}\), or to changing line-line incidence, is
incompatible with the source geometry.

The first chain-level objects to compute are the local two-branch collision
complexes and their specialization maps. Their mapping cones must each have
Euler characteristic two. Only after their images in the global restricted
complex are known may independence or cancellation be asserted.

## Consequence for \(\mathcal Q\)

These collisions occur throughout the homogeneous normal locus and are
therefore universal homogeneous degeneration data. They do not by
themselves identify \(\mathcal Q=0\). A \(\mathcal Q\)-specific class would
have to remain after the three universal packets and their global gluing are
accounted for.

## Evidence

- Entries 596, 702, and 703;
- `research/benincasa/check_generic_five_pole_base_change_rank.py`;
- `research/benincasa/five-pole-residue-euler-rank.json`;
- `research/benincasa/check_restricted_branch_loss_split.py`;
- allocator claim `seqclaim-0b1fb07ace7b7dc31589db6f`.

## Next falsifier

For each \(q_{g_i}\), factor the specialized quartic restriction and build
the one-parameter collision model from its two generic branch pairs to the
forced square. Compute its nearby-cycle/vanishing-cycle cone with the
orientation local system retained. Reject the proposed decomposition if a
local cone does not have Euler characteristic two or if its global image is
killed by a source-derived connecting morphism.
