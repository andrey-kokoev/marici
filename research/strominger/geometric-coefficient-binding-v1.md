# Geometric five-coefficient candidates and the PN filter

## Replacing arbitrary P slots

Constructed two embeddings directly from the twelve oriented surface patches.
For each patch, sample the coefficient at either its first outer corner or its
second outer corner, and multiply by its native cyclic eigenvector. Each
vertex occurs three times as either chosen endpoint, so division by sqrt(20)
makes the four vertex columns orthonormal.

The fifth, outside-context coefficient is placed in a transported vector
orthogonal to the local selected line. In the reference frame, with native
mode v0, choose `w=(conjugate(v0_y),-conjugate(v0_x),0)`, normalized across the
twelve patches by `8 sqrt(6)/3`. This context direction is a stated choice,
not something determined uniquely by the four vertices.

Both resulting 36-by-5 maps are exact complex-linear isometries. Both intertwine
all twelve proper tetrahedral rotations, not just the native order-two reader
advance. Both also define reducing subspaces of L,G,N.

## Induced five-dimensional operators

For either embedding the exact compressed operators are:

- L retains the four vertex coefficients and rejects outside context.
- G averages the four vertex coefficients and retains outside context.
- N averages the four vertex coefficients and rejects outside context.

These are candidate field-induced operators. They are not claimed to be the
native active-three-slot Fourier readout, which is a different specified
construction. This distinction prevents replacing the existing five-slot
protocol with an inferred projector rule without checking it.

Two distinct endpoint choices produce the same reduced operators. Geometry,
proper-rotation covariance, norm and these projector constraints therefore do
not select a unique binding. In fact the unconstrained A4-equivariant linear
map space from four vertex scalars plus one context scalar into the 36-field
has complex dimension 15, from the representation character count.

## PN supplies a nontrivial additional filter

Suppose a full metric-unitary PN field map S exchanges P/N projection roles,
and carries the embedded five coefficients by the native PN permutation Pi.
It must preserve their compressed projector matrices:

```
Bp* Mp Lp Bp = Pi* Bn* Mn Gn Bn Pi
Bp* Mp Gp Bp = Pi* Bn* Mn Ln Bn Pi
Bp* Mp Np Bp = Pi* Bn* Mn Nn Bn Pi.
```

Both previously constructed arbitrary N embeddings fail this necessary test.
Thus their phase/norm compatibility alone was insufficient for the proposed
role-exchanging PN attachment. This rejects those seeds under that hypothesis,
not all possible N embeddings or all PN field transports.

## Disposition

P now has two explicit geometry-based, norm-preserving candidate couplings,
with exact projector reduction. PN has become a substantive selection test,
and it rules out the earlier arbitrary N slot choices. The next construction
must derive N's binding from its reader patches while meeting these induced
projector conditions—or explain why a different PN transport hypothesis is
appropriate. E and global sewing remain open.

```sh
python research/strominger/checkers/check_geometric_coefficient_binding.py
```

Evidence: `results/geometric-coefficient-binding/verification.json`.
Production/viewer unchanged.
