# Fixed coarse Green sewing is obstructed before completion

## Definitive finite-cutoff no-go

Let V be the ordinary common source cell, and F_L:V->Y_L and F_R:V->Y_R its source-derived coarse observations with prescribed forms q_L,q_R. Under the raw derivative assembly with orthogonal coarse-cut labels, there is no carrier Z and maps i_L,i_R satisfying all three conditions:

1. i_L preserves q_L on F_L(V);
2. i_R preserves q_R on F_R(V);
3. i_L F_L = i_R F_R.

This remains impossible with an arbitrarily large indefinite or degenerate Z. If such data existed, pairing the common images of any u,v would give

    q_L(F_L u,F_L v) = q_Z(i_L F_L u,i_L F_L v)
                       = q_Z(i_R F_R u,i_R F_R v)
                       = q_R(F_R u,F_R v).

The exact forgotten two-vector witness in `ordinary-raw-coarse-green-forms-disagree-between-groupings.md` instead gives

    Q_L = [[16,4],[4,16]],  Q_R = [[16,0],[0,16]].

The cross entry would have to be both four and zero. This is a contradiction in exact finite source data, not an unresolved analytical estimate.

## Why the evident repairs do not meet the fixed task

- Adding the same counterterm to both source pullbacks leaves Q_L-Q_R unchanged.
- Adding radical directions changes no pairings.
- Changing only the shifted-product observation does not affect these ordinary vectors.
- A suspension sign or common unit phase on both arguments leaves a self-form unchanged.
- More spectral samples, theta-tail bounds, or completion cannot repair the unit-vacuum witness while preserving its finite restriction.
- A distinct correction on each side can cancel the difference only by changing at least one prescribed ordinary form. That is a new assembly to justify, not an isometric sewing of the fixed ones.

The full 90-channel forgotten defect has rank 52 and inertia (26,26,38), as recorded in `the-forgotten-ordinary-cut-defect-has-rank-52.md`. The two-vector obstruction alone already proves the no-go.

## Independent spectral obstruction and provenance

`../grothendieck/the-ordinary-middle-block-has-a-nonzero-cut-dependent-green-anomaly.md` identifies the actual coarse multiplication maps and proves a within-partition residual 4 w_memory K(g,h) is not identically zero. It also distinguishes the normalized two-sheet signature from the singular raw four-port coefficient. Its exact checker passes. Thus moving to a single partition does not remove the full spectral problem.

## What remains valid and can be retained without fitting a metric

There is still a canonical relative graph record

    T(v) = (F_L(v), F_R(v)) in Y_L direct_sum Y_R,

with the already determined difference form q_rel=q_L direct_sum (-q_R). Its pullback is exactly Delta=Q_L-Q_R, including every spectral pair when interpreted at the packet level. This uses existing source maps and existing forms; no eigenbasis of Delta defines the carrier. At fixed finite envelope it is an ordinary well-defined linear construction.

This graph record is not an isotropic sewing relation: its pullback is nonzero. Calling it a relative packet must not be promoted to a repaired Green equality. Likewise the existing surjective correspondence of ambient linear observations is not an isometry of the source self-forms.

The shifted 720-channel paired square and the 2160-channel uncompressed ordinary injection survive. The no-go concerns simultaneous preservation of the two coarse ordinary forms under source-identifying sewing, not source faithfulness or all possible future relative constructions.

## Disposition

The fixed-form equality branch has an insurmountable mathematical blocker. Further work must explicitly change the target claim to a relative, nonisometric comparison retaining Delta, or derive an independently justified new coarse assembly. It cannot continue as an attempted proof that the two given forms agree.

Verification: `uv run --with sympy python research/voevodsky/checkers/check_fixed_coarse_green_sewing_no_go.py`.

Artifact: `results/fixed-coarse-green-sewing-no-go.json`. It reruns the source witness, verifies inconsistency of the common Hermitian pullback equations, and checks common-counterterm, radical-extension, and shifted-only nonrepairs. The general arbitrary-carrier no-go is the argument above, not an extrapolation from a sampled matrix.
