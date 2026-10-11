# Restart iteration 4: physical transport exists, but does not select the missing coupling

## Fresh source

Read Voevodsky's `two-polarization-shear-selects-area-and-parallel-frame.md` anew. Its actual inputs are a full determinant-one shape history C(u), corner area/expansion, gauge normalization and initial observer frame. Einstein's vacuum equation supplies focusing; metric parallel transport supplies frame evolution. The source explicitly does not select its shape history or derive Einstein dynamics.

## Compare the right metrics first

For gamma=r^2 C, the coordinate frame obeys F'=-(1/2)gamma^-1 gamma' F. This generator is generally not skew in the constant Euclidean metric. It preserves F^T gamma F, not an unchanging coordinate dot product.

Thus inserting its raw coordinate matrices directly into the counting-metric bank law would be an unjustified metric identification. In orthonormal endpoint frames, orientation-preserving comparisons are in SO(2) and the previous bank covariance applies conditionally.

## Continuous physical transport does not constrain this mixer

Both Ad_J and L commute with independent proper orthogonal endpoint frame changes: QJQ^T=J for det(Q)=1. Sewing and exchange intertwine those same changes. Consequently the entire attached update commutes with their whole-state action H:

    U H = H U.

This is an analytic identity for the declared representations, with 27 exact rational endpoint-frame controls. A changing chart gives H_(n+1) U H_n^-1, which here is the inter-time connector times U. It transports the existing update; it does not select a new intrinsic mixer.

## Explicit physical-history ambiguity

For the source's rotating-shape family C=R(u)diag(p^2,p^-2)R(u)^T, set

    c=(p^2+p^-2)/2, s=(p^2-p^-2)/2.

The source equations give r=cos(su) with the stated corner conditions, and moving orthonormal-frame connection cJ. At u=pi its comparison rotation is (1-c)pi. Exact controls give:

| p | frame connection coefficient c | return angle / pi |
|---|---|---|
| 1 | 1 | 0 |
| 6/5 | 1921/1800 | -121/1800 |
| 5/4 | 881/800 | -81/800 |

All satisfy 0<=s<1/2, so the written trigonometric solutions remain before a caustic over this interval. Their focusing and frame histories differ, but their orientation characters and intrinsic attached mixers agree. Therefore those mixer/orientation data alone cannot reconstruct the physical history. No choice among these sources is made by the Boolean constructor inspected so far.

The checker independently verifies local metric compatibility and the cJ connection formula. It does not numerically integrate the all-u solutions or assert a WG-to-Einstein identification.

## Gravitational normalization is absent from this recovered sector

The construction is vacuum: Ric=0. In Einstein's equation with T=0, changing G has no effect on this condition. Recovering a nonzero tidal tensor or frame rotation therefore does not determine G. A matter response and its normalization would be needed; they cannot be recovered by comparing the numerical return angle to an old target coefficient.

This is a specific limitation of the recovered physical source, in addition to the previously established calibration freedoms of the record model. It is not a claim that physical-source research is absent elsewhere.

## Stopping boundary for this selection attempt

The four restarted iterations have now tested the concrete continuations recovered by the broader search:

1. Topological orientations have the wrong transformation under the actual Boolean fiber flip unless a further source identification is supplied.
2. Actual compatible marked Boolean states select a counting frame, but its relative sign is the self-edge determinant; all flat Boolean edge attachments are classified.
3. Retained endpoint signs extend the whole conservative update to nonfactorized banks, but do not select physical transport.
4. The recovered Einstein frame construction supplies conditional physical transport, yet its continuous proper rotations do not constrain the intrinsic mixer, and its vacuum equation cannot fix G.

The objective is still incomplete. We are stuck relative to these currently admitted source laws: no sourced map selects gravitational boundary geometry from WG data, and no matter-to-geometry coupling/readout fixes normalization. Inventing such a map or importing an observed coefficient would be another hypothesis, not selection by this model.

This is not an exhaustive impossibility theorem over the repository or all future models. It is the concrete stopping point for the present attempt, after executing its identified attachment and physical-transport continuations. Repeating frame tests or scalar rescalings will not supply either missing law.

## Verification

`python research/nima/checkers/check_physical_frame_mixer_comparison.py` passes. Results: `results/physical-frame-mixer-comparison.json`. No source-owner artifact, existing dynamics, Agda theorem or historical receipt was modified. No physical completion, ledger publication or commit is claimed.
