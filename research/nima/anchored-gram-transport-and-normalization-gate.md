# Anchored transport and the remaining normalization choice

## What fixing rung4 supplies

The confirmed diagram fixes the transport roles and the physical-reference
locus. It does not by itself specify a probe realization, an observation metric
or the horizontal generator. The retained-family checker already supplies two
horizontal candidates with different target records and commuting squares.

This test examines a separate, stronger set of metric assumptions: nested
coordinate spaces with a permutation-invariant Gram, orthogonal transport,
complete retained residuals, and a fixed unit-norm reference at rung4. These are
conditional Gram charts, not an asserted identification of rung number with the
dimension of the selected record-family presentation.

## A family of anchored metric models

Let

    G_r=a I_r+b J_r,

with positive eigenvalues at all tested rungs. Fix the rung4 reference vector
q4=(1/2,1/2,1/2,1/2). Divide every rung metric once by a+4b, so q4 has unit norm.
The same normalization is retained throughout the tower.

Orthogonality then uniquely determines the projection from m to n:

    (P_(m->n)x)_i = x_i + b*sum_(j>n)(x_j)/(a+n*b).

Each removed signed coordinate is retained. Direct and staged projection agree,
reconstruction is exact, and the quadratic budget splits into retained and
orthogonal-record contributions. The one-step record weight, before the common
normalization, is a(a+k*b)/(a+(k-1)*b).

Take T9=P_(12->6), T8=P_(11->5), T7=P_(10->4), with adjacent projections as the
vertical chart transitions and all records carried forward. Both squares and
both full routes agree as retained states, not merely as scalar budgets.

## Unit reference and symmetry leave freedom

The checker tests (a,b)=(10,1),(2,1),(1,0). All satisfy the requirements above,
including S4 invariance at the bottom and the same unit reference vector.
For the same bottom contrast vector(1,-1,0,0), their squared norms are

    10/7, 2/3, 2.

They also transport data outside the bottom subspace differently. Thus even
these added orthogonality and budget requirements do not select the metric ratio
or horizontal map without fixing the Gram realization. This is a metric-choice
test; it does not assert that all three constructions implement the intended
label/from/to family operator.

## What the existing Gram construction would supply

The repository's fixed S12 construction uses stabilizer-indicator probes
f_i(sigma)=1 when sigma fixes i, counting measure, and one division by10!.
Those explicit choices give G_r=10I_r+J_r. Under the unit-reference convention
above, the rung4 contrast coefficient is10/14=5/7.

That is a definite conditional geometric normalization, not a coupling
prediction. It depends on the probe and measure choice. Its full Gram eigenvalues
are22 and10 at rung12, and14 and10 at rung4 before reference normalization; the
four numbers12,11,4,10 are not its spectrum.

To use this construction as the physical completion of the clarified diagram,
we need an adapter identifying the retained Gram charts and their observations
with the labelled/from/to family presentations. Rung labels alone do not give
that adapter. A physical energy or gauge-action identification is another step.

## Current conclusion

The remaining input is now explicit: which probe/measure realizes the rung4
reference and its metric, and how that realization attaches to the retained
comparison records. Once that datum is fixed, orthogonal transport is unique
under the stated linear assumptions. Selecting it merely because it yields a
familiar number would substitute a normalization choice for a derivation.

## Verification

    python research/nima/checkers/check_anchored_gram_transport_gate.py

Exact rational tests on all12 basis seeds and additional seeds: both squares,
direct/staged retained states, reconstruction, norm budgets, orthogonality,
all24 bottom relabellings, fixed reference normalization and differing contrast
readouts. Probe-count provenance is in carrier-gram-restriction-tower.md and its
existing checker.
