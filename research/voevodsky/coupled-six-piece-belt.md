# Coupled six-piece belt: 5346 retained coefficient transfers

## Result and scope

The actual six-piece belt now has a coupled, rank-one-return implementation with **5346 distinct nonzero typed coefficient transfers**, under the explicit inter-orbit rule below.

```text
local selection L:       162
alignment G:            2268
collective return N:    2916
TOTAL:                  5346
```

There are 162 typed ports. The return satisfies GL=LG=N and NGL=N. All arrows occur in strictly positive closed three-step traces, giving the same kind of fixed-weight deletion certificate as the original proton.

This is a completed calculation for a declared extension of the original construction. It is not a theorem that the bare belt geometry uniquely selects this extension. In particular, the multi-orbit alignment stage below is a positive contraction, not an orthogonal projector as in the one-orbit case. That change is explicit and tested.

## Coupling rule

The original geometry supplies eighteen oriented small triangles, grouped into three six-placement rotation orbits. Their source-generated vectors are v_i; put n_i=||v_i||² and S=sum_i n_i.

Keep the original spatial rotation transport wherever two triangles belong to the same orbit. Where they do not, use only their already selected cyclic modes:

```text
tau_ij = v_i v_j* / n_j.
```

This sends v_j to v_i and is zero on the source mode's orthogonal complement. It adds no invented spatial rotation between noncongruent triangles.

The eighteen-triangle shared-edge graph is connected. Put these line maps on its seams. Their composition is flat on the selected modes:

```text
tau_ik tau_kj = tau_ij,
tau_ii = P_i.
```

Thus the selected amplitude comparison is independent of which shared-edge path connects the triangles. The generator retains the original architecture's direct all-pair alignment blocks; path compression is not counted as extra transfers, just as the original alignment was materialized as direct blocks.

Using the original monomial Cartesian frame, define

```text
L_i = v_i v_i* / n_i,
N_ij = v_i v_j* / S,

G_ij = (n_j/S) R_i R_j*      if i,j share a rotation orbit,
G_ij = N_ij                 otherwise.
```

The weights n_j/S are fixed by the requirement that selecting a source local mode and then aligning produces the stated normalized collective projector. Indeed G_ij L_j=N_ij in both cases. No measured mass or desired total is used.

This line-only convention for cross-orbit transport is the added rule. It uses the source modes as interface data; it is not claimed to follow from geometric intersection alone or to be the only possible extension.

## Original-proton regression

For a single orbit all local norms agree, so n_j/S=1/g and there are no cross-orbit blocks. The rule reduces exactly to the old construction.

The checker reconstructs the actual proton packet and compares **every original L/G/N coefficient and typed endpoint**, not just its total. All match. Its support remains 108+432+1296=1836.

## Why the count is 5346

All 54 belt spatial coordinates are nonzero.

- L: eighteen dense 3-by-3 local projectors: 18×9=162.
- G within orbits: three sets of 6×6 monomial blocks, three entries each: 324.
- G across orbits: 216 dense 3-by-3 blocks: 1944.
- N: dense 54-by-54 collective projector: 2916.

Hence 162+(324+1944)+2916=5346.

Relative to three independently closed 486-arrow components, coupling adds 1944 G transfers and 1944 N transfers. Existing within-orbit weights are renormalized to the joint mode, but their support is unchanged.

Grouping by the actual six face-to-center pieces gives

```text
within each piece:        171
between each pair:        288  (both directions)
5346 = 6×171 + 15×288.
```

The numbers 135 and 216 from the proton cannot be reused: the belt's three small triangles within a single piece lie in different rotation orbits, so their alignment blocks are now dense line bridges rather than monomial spatial rotations.

## The alignment distinction

Let G_r and N_r be the original normalized alignment and collective projectors for orbit r, embedded in the full port space, and let alpha_r=(sum of n_i in r)/S. Then

```text
G = N + sum_r alpha_r (G_r-N_r).
```

The summands act on mutually orthogonal subspaces. Consequently G is self-adjoint and positive, its norm is one, and GL=LG=N. For this belt the orbit weights are 1193/4485, 2099/4485, 1193/4485.

G has one eigenvalue 1, each alpha_r with multiplicity two, and the rest zero. It is not idempotent. A requirement that the multi-orbit G remain an orthogonal projector would be a different implementation and must not silently inherit this count.

## Deletion certificate

Every closed three-stage cycle has weight

```text
N[j,i] G[i,k] L[k,j]
```

with k and j belonging to the same local triangle. Within an orbit, the monomial rotation identifies the relevant vector coordinates up to their real sign, which cancels. Across orbits, the line bridge supplies the conjugate factor directly. In both cases the cycle weight is strictly positive real.

The checker covers every arrow with such a cycle. All 6804 cycles together have trace 1. Deleting any nonempty set of arrows, without changing other weights, removes at least one strictly positive contribution and cannot restore it through cancellation. The complete return therefore changes. This is stronger than testing single deletions; it is still not unrestricted circuit minimality.

## Verification and artifacts

```text
python research/voevodsky/checkers/check_coupled_six_piece_belt.py
```

The fresh run verifies exact GL=N, coherent return, the positive-cycle certificate, connected shared-edge mode transport, complete original-proton coefficient regression, serialization/reconstruction of all 5346 arrows, and missing-arrow rejection for each stage.

- `results/coupled_six_piece_belt.json`
- `results/coupled_six_piece_belt_store.json`

Historical geometry and proton sources remain unchanged. This gives a count for the coupled belt candidate, not an identification with the physical neutron or its mass.
