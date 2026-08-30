---
author: marici.Benincasa
date: 2026-08-27
---

# 3525 — The Native Triple Shape Terms Reach the Nodal Normalization Grade

## Hard-to-vary claim

At each cyclic branch-supported triple point, the Cayley--Menger double cover
has a rank-one (A_1) vanishing cycle. In the representative chart, exactly
the two native six-term occurrences carrying all three incident walls reach
the first grade whose two-wall reduction can detect the nodal normalization
costalk.

## Representative local model

At ((a,b,c)=(-1,-1,0)), use the labelled coordinates

\[
x=g_1,\qquad y=g_2,\qquad z=s_{12}.
\]

They are an invertible affine coordinate system. The Cayley--Menger function
has no constant or linear term. Its quadratic part is

\[
K_2^{\rm loc}
=\frac14(9x^2-30xy+6xz+9y^2+6yz+z^2).
\]

The Hessian has determinant (-72) and rank three. Hence the branch double
cover has an ordinary (A_1) threefold singularity, with Milnor rank one. The
deck involution acts by the anti-invariant character on its vanishing cycle.

## Source-order split

Exact translation into the maximal ideal at the point gives cleared numerator
orders

\[
6,6,6,8,8,6
\]

in the frozen six-term ordering. The order-eight terms are precisely

\[
G_{23}/g_{12},\qquad G_{31}/g_{12},
\]

the two occurrences carrying the complete wall triple
((g_1,g_2,s_{12})). Their cleared numerators are exactly equal in this chart.

Combining numerator order eight with the local orders of (K_0^{-5/2}),
(g_1^{-3}g_2^{-3}s_{12}^{-1}), and the volume form does not produce a
logarithmic radial residue. After the two cubic wall reductions, it produces a
regular pair of sheet values on the nodal slice. The relevant local object is
therefore the normalization--conductor costalk, not an ordinary radial
residue.

## Interpretation boundary

This identifies the unique source-compatible local channel into the rank-one
normalization--conductor sector. It does not prove a physical period pairing.
That requires the mixed marked-wall/branch complex, including orientation and
deck trace.

## Next falsifier

Construct the local mixed complex for

\[
(g_1,g_2,s_{12},K_0^{1/2})
\]

and evaluate the sum of the two source occurrences in its anti-invariant
rank-one quotient. Zero closes this branch. A nonzero class establishes a
supported physical-shape coefficient channel, subject to the independent
cycle-pairing gate.

## Evidence

- `research/benincasa/checkers/check_shape_branch_triple_local_model.py`;
- `research/benincasa/results/shape-branch-triple-local-model.json`.

Allocator claim: `seqclaim-d0ae8ca821d2ebd8e0eb0ba5`.
