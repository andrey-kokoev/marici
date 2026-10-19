# Arbitrary rigid displacement of the existing P/N field geometry

## Frozen next test

Extend the prior12-direction test in `check_field_translation_covariance.py`
to arbitrary displacement by symbolic identities, retaining full fields.
Freshly replay the P and N geometry-to-operator reconstructions. Translate the
same marked object and its chart, not a reader moving through fixed occupancy.
Do not claim electron transport, a connection through changing readers, a
unique physical phase law, or a graded parent.

For P, reconstruct each actual ordered corner matrix relative to the body
centroid: X_g(t)=[p_j+t-(o+t)]_j. At the source tetrahedron o=0, so this is the
existing X_g, not a changed source matrix. Check all12 matrices coefficientwise
in three independent translation variables and retain invertibility, metric
X_g*X_g and cyclic operation X_g C X_g^-1. This covers arbitrary coefficients
in every3-component patch, not only the cyclic eigenline whose coefficients
sum to zero. Relative vertices also determine the unchanged rotation frames.

For N, apply the ACTUAL source `mode` and `frame` functions to affine-polynomial
coordinates. Verify both mode vectors on all18 patches unchanged. The source
plane basis s, r-<r,s>/<s,s>s, its weights, cyclic coefficients and sector
operators are deterministic functions of those vectors and the retained
marking. The fresh native reconstruction must still match every metric and
L/G/return coefficient. Consequently all36 components retain the same chart,
not just the selected return mode.

## Hostile control

A raw absolute-position P corner matrix transforms as X+t(1,1,1), not X.
Translate by minus a triangle's centroid: its three absolute columns sum to
zero and the matrix becomes singular. The centered matrix stays invertible.
Thus a check restricted to the zero-sum cyclic eigenline can miss destruction
of the full corner-coordinate realization. Recentring must be explicit.

## Meaning and limits

For rigid copies of each same P/N geometry, the geometric formulas extend to
arbitrary real displacements, and identity amplitude transport in the derived
co-moving charts satisfies composition and inverse. This is stronger than a
postulated unrelated trivial bundle and stronger than12 sampled directions.
It does NOT add a native reader move or change the fixed lattice's symmetries.
Attachment to a fixed exterior, P/N conversion, E, path-dependent connections,
sewing and physical dynamics remain separate gates. Covariance does not force
a unique connection: scalar phase transports commute with fiber projectors;
phase-sensitive readouts require a specified reference convention.

No new graded multiplication or Monster/Baby Monster evidence follows.

## Replay

    python research/strominger/checkers/check_arbitrary_rigid_field_transport.py

The checker uses exact rational affine coefficients, not numerical sampling,
and freshly executes the two source geometry/field reconstructions.
Receipt: `results/arbitrary-rigid-field-transport/verification.json`.
