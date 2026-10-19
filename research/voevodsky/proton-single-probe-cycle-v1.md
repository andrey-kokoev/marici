# One fixed probe: a complete source-cycle decoder and a metric obstruction

## Results

For the unchanged tetrahedral coefficient realization:

| Probe access | Independent complex input coordinates resolved |
|---|---:|
| One fixed coordinate, all twelve seed-generated geometric orientations, raw readings only | 12 of 36 |
| The same probe and orientations, retaining all native stage readings | 24 of 36 |
| Two independent coordinate axes, those orientations and native stage readings | 36 of 36 |
| One coordinate, those orientations and the three powers of the existing source slot cycle, read before projection | 36 of 36 |

The final row has an explicit inverse using exactly 36 complex scalar readings.
However, the transported slot cycle is **not unitary in the existing native
metric**. A unit input at AB:y has squared norm 9 after one application. No
positive metric can simultaneously make this exact cycle unitary and keep the
unchanged native L as an orthogonal projector.

Thus there is a complete algebraic one-probe reconstruction, but not an
unqualified native norm-preserving one-probe gate. The two-axis reconstruction
already works without introducing that extra action.

## Source and operation types

This continues `proton-native-task-catalogue-v1.md` and
`proton-seed-rotation-readout-repair-v1.md`. The source frontend is freshly
replayed; all 1,836 typed coefficients equal the archived manifest exactly.

The original geometric rotations ABC and ADB generate A4. Their coefficient
actions U_p transport triangle labels and spatial frames together. The checker
reconstructs all twelve and verifies their composition laws and covariance
with L, G and N. The native prefix records remain x,Lx,Nx,Nx; Gx is not silently
added as another raw-input reading.

A fixed probe means one declared complex coordinate, here (AB,x). Different
source actions are read on retained or reproducible **raw input**. Exact complex
amplitude access and input retention are mathematical permissions, not a
constructed physical apparatus or permission to copy unknown quantum states.

## Why rotating one probe is insufficient

The A4 orbit of one coordinate row has one nonzero coordinate address in each
of the twelve triangles. Raw readings therefore have rank 12. Local-stage
readings add one independent row per triangle, proportional to that triangle's
selected mode covector. The global return supplies no further independent row
once every local amplitude is observed.

The baseline all-mask theorem consequently gives rank 24. There is one hidden
complex direction in every triangle: a direction invisible both to the chosen
raw coordinate and to the selected local eigenline. The receipt retains a
basis of all twelve hidden directions.

A second independent probe axis generates two observed coordinates in every
triangle. Together with one local-stage reading, those determine all three
input coordinates in each triangle. This recovers rank 36 using the earlier
explicit local decoder. One axis fails and two succeed in this operation/readout
language, so the axis count is sharp.

Repeated native returns do not help, since LN=GN=NN=N. Nor do phase controls
built solely from local selection. For example,

    V=(I-L)+omega L,  omega=exp(2 pi i/3),

is unitary, but each row of VU_p is already a linear combination of the observed
rows of U_p and LU_p. Its addition leaves rank 24. Any finite word in geometric
actions and such L-phase controls has the same row-span restriction because
all geometric actions commute with L.

## The source already contains another reversible operation

For the actual centroid-edge triangle t, let X_t have its three ordered spatial
corner vectors as columns. The source's three-slot coefficient permutation is

    C = [[0,1,0],[0,0,1],[1,0,0]].

The original local eigenline construction uses

    A_t=X_t C X_t^-1.

We now make explicit what allowing this source-defined operation would add to
the probe grammar. Let A be the direct sum of its twelve blocks. Exact checks
give

    A^3=I,
    A U_p=U_p A,
    A L=omega L.

The source rotations act on triangle positions and frames; A changes the
coefficient slots at fixed frames. They are different typed operations. This
extension is not an additional arrow stage found in the 1,836 manifest, nor a
passive relabelling of a state and its probe.

The geometric and slot-cycle actions generate A4 x C3, of order 36. Their
intersection is trivial: a nonidentity geometric action permutes triangle
positions, whereas A and A^2 act within every triangle. This is a finite group
of source-derived coefficient operations, not a universal gate set.

## Complete one-probe decoder

Collect the 36 scalar readings

    y_(p,k)=e_(AB,x)^T U_p A^k x,
    p in A4, k=0,1,2.

Their 36-by-36 observation matrix O has full rank. The saved exact inverse D
satisfies DO=I36. This is the minimum possible number of scalar complex-linear
readings for an unrestricted 36-complex-dimensional input.

The mechanism is local, not a lucky large determinant. In each triangle, the
three rows of I,A_t,A_t^2 at any fixed coordinate form an invertible 3-by-3
observation matrix. All 36 triangle/axis cases are checked and retained with
their inverses. The geometric orbit visits every triangle, so these local
inverses assemble into the full decoder.

The stored twelve-dimensional native one-probe kernel supplies a hostile test:
a nonzero vector w satisfies all old readings equal to zero, while a specified
slot-cycle reading is nonzero. Thus the added operation actually distinguishes
inputs the previous apparatus language could not distinguish.

A further exact calculation gives another 36-reading decoder layout: twelve
raw readings, twelve native local readings, and twelve raw readings after one
slot-cycle application. Three separate slot-cycle powers are sufficient but
not necessary if the native local-stage readings are retained.

All these statements concern pre-projection data. Since A acts by the same
scalar omega on im L, applying it only after local selection supplies a common
phase there, not the missing raw-input directions.

## Reversibility is not native unitarity

The existing coefficient inner product is Euclidean in the source axis frame.
The slot frames X_t are not unitary. Consequently similarity to a permutation
does not imply that A_t is unitary in that inner product.

The checker finds A^dagger A != I and an explicit example:

    x=e_(AB,y),  ||x||^2=1,  ||Ax||^2=9.

It also finds

    rank(AL-LA)=12.

A is therefore not interchangeable with the unitary native selection-phase
control V above. The extra observable directions come with a genuine change
of permitted action, not an unnoticed alternative presentation of V.

### Why changing the metric does not preserve both structures

The pullback corner metric

    H_t=X_t^-T X_t^-1

is positive definite and makes A_t unitary. With H the block metric,

    A^dagger H A=H.

But the existing native L is not H-self-adjoint. Simply changing the metric
would change the meaning of its orthogonal selection, even if the printed
coefficient matrix were left untouched.

There is a stronger obstruction independent of that particular choice of H.
Suppose a positive metric M made A unitary and L its orthogonal projection onto
the selected subspace. Since AL=omega L, that subspace is invariant under A.
An invariant subspace of a finite-dimensional unitary operator has an invariant
orthogonal complement, so its orthogonal projector commutes with A. This would
force AL=LA, contradicting the exact nonzero commutator.

No metric alone therefore turns this source slot cycle into a unitary gate
while preserving the same L as orthogonal selection. This does not prohibit a
physical implementation with additional resources, a nonunitary filter or a
different control. None of those mechanisms is derived here.

## Verification and surviving scope

The conjecture, rivals and metric hostile were frozen before execution.
SCC fingerprint:
`13f63b5b855378fce0ba811f7c80581dad11a74ace824511b7594fc80eb79784`.

    python research/voevodsky/checkers/check_proton_single_probe_cycle.py

Seven check groups pass. Independent rational realification verifies ranks
48 and 72 for the native and extended observations and the complete decoder
identity. The result stores source hashes, all local frames, the hidden basis,
36-reading matrix and inverse, every local inverse, the separating witness and
the metric obstruction. Shared sources and stores remain unchanged.

Packet: `results/proton-single-probe-cycle-v1.json`.
Contract: `inputs/proton-single-probe-cycle-v1.json`.

**Survives:** source-operation-resolved reconstruction and a sharp obstruction
to identifying two distinct coefficient actions through a metric change.
**Not established:** physical accessibility of the added slot-cycle action or
of an exact complex-coordinate probe. No mass, energy or time value is assigned.

The continuation `proton-protected-unitary-probe-v1.md` constructs a different
control from Q(A+A^dagger)Q, Q=I-L. Its Cayley transform is native-unitary,
fixes im L pointwise and gives a complete one-probe decoder. This is an explicit
control synthesis extension; it does not make the original A unitary or revoke
the simultaneous-metric obstruction above.
