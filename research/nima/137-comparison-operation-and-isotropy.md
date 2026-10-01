# An operation-level test of equal 137-slot contribution

## Geometry and features

Take four probes from the fixed S12 stabilizer Gram, normalized once by10!:
G4=10I4+J4. A state feature e_i has squared norm11; an arrow e_j-e_i has
squared norm20. In the tensor comparison space K=G4 tensor G4, use one
feature v per slot:121 arrow tensors and16 state tensors.

This is an explicit comparison response realization, not a derived particle
or electromagnetic operator. It also differs from the earlier trial with
state norm12 and arrow norm22; here the fixed-carrier Gram supplies the metric.
All137 features inhabit one16-dimensional tensor space; labels distinguish
operations even when their feature vectors are linearly dependent.

## Raw feature storage

Arrow-slot squared norm is400; state-slot squared norm is121. Their total is
121*400+16*121=50336. Normalizing by that total gives arrow-slot weight25/3146
and state-slot weight1/416. The corresponding arrow block mass is3025/3146.
Raw Gram-feature storage therefore assigns different weights to the two blocks.

## Normalized comparison removal

For any nonzero comparison feature v, define the metric-orthogonal removal

    Q_v x = v*(v^T K x)/(v^T K v),
    P_v x = x-Q_v x.

The removed quadratic budget is (v^T K x)^2/(v^T K v). For second moment C,
its expectation is

    (v^T K C K v)/(v^T K v).

If excitation is isotropic in the comparison metric, C=sigma^2 K^-1, this
becomes sigma^2 for every slot. It is also invariant under rescaling v.
Thus a specified normalized comparison operation supplies an explicit mechanism
for equal expected contribution, conditional on isotropic preparation.
A coherent non-isotropic control produces five different slot responses.

## Preparation and schedule matter

The identity applies to each comparison evaluated on the same fresh isotropic
ensemble. It does not remain valid after an arbitrary sequence of projections.
The initial total expected budget is tr(KC)=16 sigma^2. A passive closed sweep
cannot remove more than that amount. Repeating one identical comparison
immediately removes zero additional budget.

Executing137 separately prepared comparisons gives137 sigma^2 expected removed
units, with preparation/reset resources to be accounted for. Sampling labels
uniformly gives probability1/137 by the chosen schedule. Neither statement
identifies that probability or a normalized mean with electromagnetic coupling.

This separates three quantities: primitive comparison response, operation
selection probability, and physical interaction strength. The isotropic
projection calculation establishes the first. A physical programme must fix
the preparation law, sequencing/back-action, and measured response.

## Structural gain

There is now a concrete sufficient condition for the proposed equal-slot
normalization: equal-rank metric projections on a common isotropic ensemble.
Symmetry and counting alone had left the weights undetermined. The next test
is whether actual carrier evolution supplies this isotropy or a stationary
replacement, including its source and reset costs, and whether the resulting
observable is the electromagnetic response.

## Verification

    python research/nima/checkers/check_137_comparison_operation.py

Exact rational arithmetic verifies the inverse metric, all137 feature norms,
all137 expected projection losses, rescaling invariance, initial ensemble
budget, and a non-isotropic control. No measured constants are used.
