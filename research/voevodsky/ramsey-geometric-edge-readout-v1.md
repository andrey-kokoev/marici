# Geometric paired edge readouts exist; their PN pullbacks are nonlocal

## Source geometry recovered

The existing tetrahedral field attachment identifies each of12 directed outer edges with a distinct centroid-edge face patch carrying three vector components. The two directions AB and BA are on different adjacent faces. The source itself leaves common-edge restriction maps open; its separate six-component face map does not extend as a closed block of the global PN transport.

This attempt constructs a precise linear observation from those actual coordinates. It is a geometric candidate, not a source-selected physical detector or an assertion that two patch values already agree.

For canonical endpoints a<b, let d=x_b-x_a. Retain both

    h_(ab)(field) = d dot field_(ab),
    h_(ba)(field) = d dot field_(ba).

Both use the same tangent orientation; the patch labels remain distinct. The source tetrahedron has |d|^2=8, and no unmentioned unit normalization is applied.

## Full marking covariance

Stack the12 occurrence readouts into H_P. Exact calculation gives `H_P H_P*=8 I12`, so they have rank12. The complementary marking permutes the occurrences and changes canonical tangent signs, giving an explicit signed permutation W with

    H_P Q_P = W H_P,
    W^2=I12.

Thus there is a nontrivial geometric edge observation compatible with the proton world-frame marking, without confusing its two face occurrences.

## Equality of occurrences is an additional constraint

The six rows h_(ab)-h_(ba) have pairwise disjoint supports and Gram matrix16 I6. Requiring equality imposes six independent linear constraints on the36-coordinate field; it is not automatic continuity.

A unit raw field in coordinate `AB:y` gives readings -2 and0 at the AB edge. Even the stored native proton return column fails the chosen strict equality: each of its six occurrence differences is `i sqrt(3)/15` in the retained source normalization and phase convention. This does not exclude a context-dependent phase comparison, a different state restriction or a physical continuity law. It excludes declaring these literal readings equal from incidence alone.

## Exact PN locality test

Use the existing invertible metric-unitary global PN candidate T. The uniquely required full-field transported observation is

    H_N = H_P T^-1.

The inverse is obtained from the source metric adjoint. The identity H_N T=H_P follows from the imported exact inverse theorem; the checker does not claim a new dense inverse proof. It computes H_N itself exactly and checks every entry for zero.

Every one of its12 rows has36 nonzero entries, distributed over all18 neutron triangles. Therefore no readout supported on a proper subset of those neutron coordinates can equal the same H_N on **all** neutron inputs. Since T is invertible, no other linear readout can satisfy the same full-field intertwining equation while changing that support.

This is a concrete locality obstruction for this particular source-derived tangent readout and this PN candidate. It is not a theorem against all localized interfaces, all PN completions, or the broader context-retaining descent conjecture. The native coordinate support test must also not be misreported as a statement about measured physical propagation.

## Next narrowed gate

The whole-field locality obstruction does not decide the prepared five-dimensional image. Two distinct readouts may agree there while differing elsewhere. The next executable test is to use actual neutron edge/patch support from the source geometry and solve the exact factorization

    L_local B_N = H_P B_P Pi_PN^-1

on that prepared domain, with support and rank constraints declared before solving. A positive result must retain its restricted-domain status; a negative result must give the lost prepared direction rather than merely a dimension count. The same distinction applies to later edge-to-vertex restrictions.

Native retained incidence packages from the preceding turn remain valid. They have not thereby gained a local field observable or resolved the parent.

## Verification

Contract: `contracts/ramsey-geometric-edge-readout-attempt.v1.json`.
Checker: `checkers/check_ramsey_geometric_edge_readout.py`.
Receipt: `results/ramsey-geometric-edge-readout-v1.json`.
Passing freeze: `scc-freezes/ramsey-geometric-edge-readout-v1.f6ec9623ea0912f6.json`.

The frozen SCC challenge passes. Source geometry/PN direct hashes and the world-action pins were checked. All readout and support computations use exact multiradical arithmetic. No kernel interpretation, apparatus, net revision, graph verdict or Git checkpoint is claimed.
