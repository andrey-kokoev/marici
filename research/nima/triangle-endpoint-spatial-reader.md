# A covariant spatial reader for retained cross-component counts

## Reuse the existing geometry

The native/rung bridge retains endpoint counts

    LR=(1,0,0,1), RL=(0,1,1,0)

on the actual A,B,C,D vertices. Use their existing tetrahedral coordinates
from `check_twelve_triangle_positive_geometry.py`:

    A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1).

Let X have these columns. Define the count centroid `q(c)=Xc/sum(c)` for
nonzero total count. This is a declared observer of structural occurrences,
not a Born rule, mass density or particle-position identification.

## Exact outcome

    q(LR)=(0,0,1), q(RL)=(0,0,-1).

These are the midpoints of opposite tetrahedral edges AD and BC. Their
combined equal-count centroid is zero and their separation is two in the
fixture's coordinate units. No meters or dynamical time are derived.

For every vertex permutation P, the induced matrix O=X P X^T/4 satisfies

    O^T O=I, O X=X P, q(Pc)=O q(c).

Thus the result is covariant, not a fixed camera-axis assignment. The
common count mode is annihilated by X; the contrast modes carry the vector
reading.

Solving all linear intertwiner equations for this declared S4 action gives
ONLY scalar multiples of X. This supplies a representation-theoretic reason
for the first-moment map, conditional on choosing the standard spatial
representation. It leaves the length scale free and does not classify
nonlinear readers or force a physical spatial interpretation.

## Distinguish orientation from charge

The actual seed symmetry exchanging the two triangle roles is (AB)(CD).
In this spatial realization it acts by diag(1,-1,-1), with determinant +1.
It maps q(LR) to q(RL).

Therefore the opposite signed coordinates describe a spatial direction
reversed by a proper rotation. They do NOT by themselves supply positive
and negative electric charge. A rotation-invariant scalar charge reader
cannot use that signed coordinate as its charge value under the same
physical symmetry interpretation. An additional internal charge sector
would require its own transformation and coupling laws.

## Distinguish construction from motion

Each primitive triangle contains three occurrences, whereas a cross product
contains two endpoint-compatible words. A change of their normalized count
centroids is not already the displacement of conserved physical matter.
No velocity, momentum, inertial mass, interaction work or elapsed time
has been inferred from this construction.

The old aggregate J4 remains blind to the role contrast. This finer reader
is available because the rung presentations retain their leaves. Availability
and covariance do not prove it is the source-selected physical measurement.

## Verification

    uv run --with sympy python research/nima/checkers/check_triangle_endpoint_spatial_reader.py

85 exact checks pass. Includes all 24 spatial frame actions, the full linear
intertwiner classification, actual role-exchange action and the occurrence-
count control. The preceding native/rung reader integration reruns.
Receipt: `results/triangle-endpoint-spatial-reader.json`.
