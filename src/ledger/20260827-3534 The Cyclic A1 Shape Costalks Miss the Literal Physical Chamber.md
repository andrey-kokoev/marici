---
author: marici.Benincasa
date: 2026-08-27
---

# 3534 — The Cyclic A1 Shape Costalks Miss the Literal Physical Chamber

## Hard-to-vary claim

The three nonzero cyclic (A_1) coefficient costalks found in Entry 3530 do
not pair with the literal homogeneous Bunch--Davies Cayley--Menger chamber.
Each supporting point lies outside the source domain of nonnegative loop-edge
lengths.

## Source contour condition

The physical loop variables are lengths

\[
a=y_{23},qquad b=y_{31},qquad c=y_{12}.
\]

Before the additional Cayley--Menger minor inequalities are imposed, the
literal source chamber already requires

\[
a\ge0,qquad b\ge0,qquad c\ge0.
\]

The three cyclic branch points are

\[
(-1,-1,0),qquad(-1,0,-1),qquad(0,-1,-1).
\]

Each has exactly two negative length coordinates. Hence every sufficiently
small neighborhood of each point is disjoint from the literal physical chain.
All six incidence checks pass.

## Consequence

The literal local-chain costalk is zero at all three points. Therefore the
nonzero anti-invariant coefficient vector of Entry 3530 is physically inactive
on the undeformed real chamber and cannot explain the observed bulk physical
shape response by itself.

This does not prove that the class is forever unphysical. It may be activated
after a source-derived analytic continuation whose contour crosses or pinches
at the branch point. No such continuation has yet been constructed for this
shape family.

## Next falsifier

Either derive the Landau/relative-homology continuation from the original
(i\epsilon) prescription and test whether it reaches one of the cyclic
costalks, or retire this branch as irrelevant to the homogeneous physical
shape period. No path may be selected merely because it activates the known
coefficient value.

## Evidence

- `research/benincasa/checkers/check_shape_costalk_physical_incidence.py`;
- `research/benincasa/results/shape-costalk-physical-incidence.json`;
- source contour conventions frozen in Entry 783.

Allocator claim: `seqclaim-eeb7e4506938fcf2c7a2e026`.
