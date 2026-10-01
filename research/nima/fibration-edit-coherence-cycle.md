# Read/return coherence around a fibration cycle

## Typed interface

For fixed retained member identities, let X be the leaf-value state space.
A presentation p has a state space X_p and an invertible encoding e_p:X->X_p.
Its edit space is the corresponding tangent/vector space in this linear fixture.
Transport from p to q is T_qp=e_q e_p^-1. A readout a:X->Y is represented by
 a_p=a e_p^-1. Transporting the leaf metric defines the edit cost on X_p.

A compatible requested readout increment dy is returned by the minimum-cost
member change. If put denotes that return, the coherence condition is

    T_qp put_p(x_p,dy) = put_q(T_qp x_p,dy).

A three-presentation cycle satisfies T_0t T_ts T_s0=identity. In a general
nonlinear/dependent setting, edit types depend on the state and this equality
requires a dependent transport law. The present implementation verifies the
fixed-membership linear case, not a general HoTT lens theorem.

## Complete record presentations

For137 slot records, source and target indexing retain every member ID and
value. Flattening each grouped presentation in its chosen order gives a
permutation matrix R_s or R_t. Then

    T_s0=R_s,
    T_ts=R_t R_s^T,
    T_0t=R_t^T.

Their product is identity on both states and edits. Expressing a leaf readout
in each presentation and returning its requested edit with the transported
metric gives the same leaf change. This supplies an exact cycle law for the
retained representation, with finite numerical return checks.

## Why means alone fail the cycle

Let A_s and A_t read only the32 source/target means. Their least-change lifts
are L_s=A_s^+ and L_t=A_t^+. The mean-only source->target->source map is

    A_s L_t A_t L_s.

It differs from identity because the means are incomplete views. In the fixture
its Frobenius distance from identity is3.61600386064. Forward and reverse
orders of partial mean corrections also differ, by norm1.33608625247 on the
seeded input.

Neither observation establishes geometric holonomy: the intermediate maps
are noninvertible projections, and the corrections alter the state. Holonomy
would concern composed invertible transport around a loop in a specified base.
We must distinguish forgetting or interventions from such transport.

## Residuals complete the view

A source presentation can instead retain

    y_s=A_s x,
    r_s=x-L_s y_s, with A_s r_s=0.

Its type is the constrained product of the mean space and ker(A_s). Reconstruct
x=L_s y_s+r_s, then form the target pair (A_t x, x-L_t A_t x). This transition
is invertible. Its complete cycle restores x and every similarly decomposed
edit. Keeping only y_s loses information that the promoted record's retained
members are intended to preserve.

## Explanation gained

Complete reindexing has a flat return cycle in this model. Apparent cycle
failure from mean-only interfaces disappears when residual records are restored.
Thus the retained history has a specific role: it completes the state and edit
representation required for coherent bidirectional access.

The architecture supplies complete records. Editable summaries are extra
interfaces whose missing components and update costs must be tracked. Choosing
actual updates, and resolving incompatible requests, remains dynamical policy.
A nontrivial connection/curvature would need an additional transport law or a
changing family of state spaces; it is not generated merely by grouping.

## Next structural boundary

Membership changes invalidate fixed permutation and kernel spaces. The next
step is a dependent edit type covering record insertion, deletion, and movement
between families, with stable IDs, retained tombstones/history as appropriate,
and a law transporting values and return costs. That will test coherence beyond
fixed tables instead of interpreting projection loss as curvature.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_fibration_edit_cycle.py

Checks the exact permutation cycle, least-change returns in three presentations,
mean-only cycle failure, order-sensitive corrections, and reconstruction of
states and edits from means plus residuals. Numerical pseudoinverse checks use
explicit tolerances and fixed seeds.
