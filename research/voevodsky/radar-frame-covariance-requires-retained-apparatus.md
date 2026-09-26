# Radar frame covariance requires the actual apparatus

## Result and fresh state

Fresh resume selected `radar-frame-apparatus-comparison:v1`.
The finite radar-shape reading is covariant under passive frame comparison
provided the actual probe vectors are transformed and retained. It is not an
apparatus-independent spacetime tensor. These statements are compatible:
the reading is a symmetric bilinear form associated to a source AND a protocol.

The physical clock records and source enclosures come from
`physical-radar-protocol.json`; its generating-code dependencies were checked
against their recorded hashes before use. No new ray model or measured values
were fitted. The old fixed-probe implementation remains unchanged.

## General probe-dependent reading

Write the three dimensionless transverse probe vectors as v_d=(x_d,y_d),
with physical coordinate baseline epsilon*v_d. Define the design matrix

    L(V)_d=(x_d^2, 2*x_d*y_d, y_d^2).

For invertible L, the three normalized squared radar distances q_d determine
one fitted symmetric matrix G by

    L(V) (G_11,G_12,G_22)^T=q.

For the original (3,0),(0,4),(3,4) probes this is exactly the earlier
polarization formula. This interpolation does not assert that q is quadratic
on OTHER directions or baseline lengths. G need not be the spacetime metric.

With the SAME probe geometry at all three proper-time samples, the finite
reading is

    Y=-[G_+-2G_0+G_-]/(2h^2).

The implementation reads the selected section rows directly, takes their
calibrated squared clock differences, sums temporal weights, and solves L.
It does not decode a source packet. Linearity of L^-1 proves equality with
the original time-first reading. A singular design is refused rather than
silently assigned a pseudoinverse or a different readout.

## Passive comparison: same physical rays

Let Q be a constant orthogonal transverse frame change, with new components

    X'=Q^T X, v'_d=Q^T v_d, gamma'=Q^T gamma Q.

Here the prime on gamma denotes transformed components, not a u derivative.
Clock values, emission events and physical reflectors are unchanged. The
integrated inverse metric transforms as S'=Q^T S Q, hence

    b'^T S'^-1 b'=b^T S^-1 b.

Thus each exact null-leg equation and each scalar radar record are unchanged.
Uniqueness of the fitted quadratic form on three independent probes then gives

    G'=Q^T G Q, Y'=Q^T Y Q.

This is an all-record algebraic proof, including noisy candidate records whose
q values are not restrictions of an actual metric quadratic form. It requires
transforming the probe vectors, not substituting the old fixed numerical
polarization coefficients after changing a frame label.

Composition is coherent: for successive changes Q1,Q2, the composite is
Q1*Q2 and the congruence laws compose accordingly. Inverse changes restore the
reading. Frobenius norm is invariant, so these constant orthogonal comparisons
are also continuous isometries on the output. The scalar-record completion
and direct-section comparison commute with this passive transformation.

The scope is constant orthogonal transverse changes, not arbitrary moving
frames. A time-dependent Q would add derivative terms to temporal comparisons
and generally change the declared observer/frame transport problem.

## Active apparatus change is a different operation

Keep the observer coordinate frame fixed and physically rotate the baseline
set: v_d -> Q v_d. For a generic anisotropic wave the scalar radar distances
will change and must be recomputed from the new rays. Reusing the old records
would not be justified merely because the direction names are the same.

There is an exact control where this distinction can be tested without new
ray integration. In the prior flat moving source gamma=(1+u/4)^2 I, the radar
response depends only on |b|. Active rotation preserves each scalar distance.
Nevertheless fitting those distances to the actively rotated vectors yields

    Y_active=Q Y Q^T

in the unchanged observer coordinates. This need not equal Y. The physically
certified control has unequal diagonal entries and nonzero off-diagonal entry;
its unequal diagonal enclosures are disjoint, so this is not rounding noise.

This does NOT refute tensor covariance. It shows that the full observable
includes the apparatus: rotating that apparatus can rotate its fitted form.
Forgetting the apparatus and demanding a source-only tensor would be invalid.
In particular, a source-only rotation-covariant tensor in the isotropic control
would have to be isotropic; this fitted Y is not. Nor is it the zero curvature
tensor of that flat spacetime.

## Correct comparison interface

Retain in each protocol-indexed record:

- actual vectors paired with direction identifiers, not identifiers alone;
- epsilon, proper-clock grid and units, reflection convention and source witness;
- observer/frame identification and the comparison Q;
- the nondegenerate quadratic-probe design and all clock-pair rows.

The reading type is Sym^2 of the retained transverse coordinate space,
indexed by this observation protocol. Across passive frame changes its
components transform by congruence. Across arbitrary apparatus changes there
is no assertion of equal raw records or equal output in the fixed frame.

The finite display-map section comparison now respects this interface. This
is not an owner-admitted implementation of every recursive constructor or
resolution rule. No owner artifact was changed and adoption is not inferred.

## Verification and next gate

Run:

    python research/voevodsky/check_radar_frame_comparison.py

All 16 checks passed. They include physical receipt freshness, both physical
packets' source/native comparisons, a rational non-axis rotation, passive
roundtrips, the active isotropic control, label-only failure, singular-design
refusal and independent null-leg scalar invariance. Receipt:
`research/voevodsky/radar-frame-comparison.json`.

Universal covariance and coherence are written proofs; exact finite controls
do not constitute a proof-assistant theorem or a new physical realization.

The selected frame/apparatus leaf is resolved. The remaining completion gate
is conditioning when the apparatus itself varies. Invertibility at every
finite stage is insufficient if L(V) approaches singularity, or epsilon/h
approach zero. The next leaf should state a uniform apparatus-domain certificate
and test an explicit near-degenerate probe family, rather than extending the
fixed-protocol continuity theorem without its constants.
