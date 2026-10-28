# FCC route faces and the seven-presentation central passage

## Executed binding

This follows [FCC-first transport](fcc-first-sector-transport-v1.md) using the existing source cell IDs, not a replacement square model. The target is the normalized-simplex-chain factor used in the prior [full graded esd7 realization](../nima/full-esd7-graded-tate-torus-realization.md).

For every selected octahedral diagonal a->b and each of its four root-route midpoints m, bind the actual source triangle [a,m,b]. Its signed boundary is

    boundary[a,m,b] = [a,m] + [m,b] - [a,b].

Thus the existing face fills the two-root route minus the presentation diagonal. All224 source faces are bound with orientation. Comparing two routes uses the difference of their face chains; these comparisons compose by cancellation without erasing either route history. All3584 ordered comparison triples pass. The224 tetrahedra refining the56 octahedra retain their four-face boundaries, and boundary-of-boundary vanishes.

These are exact linearized incidence fillers. They do not assert equality of arbitrary analytical field-transfer maps; the source analytical comparisons retain additional residual channels.

## The central seven presentations are typed

For each of the24 actual central flags, use the existing bridge, for example

    V051 -> E270 -> F403 -> T184 -> F538 -> E368 -> V072.

The incidence ranks are1,2,3,4,3,2,1. The total normalized-chain basis sizes are1,3,7,15,7,3,1; these are different gradings.

The ascending leg has genuine chain inclusions. Every included simplex boundary remains in its source face: all72 inclusions pass.

For the descending leg, test two explicit candidates:

1. Delete chain coordinates outside the smaller face.
2. Restrict dual cochains along the face inclusion.

**All72 naive chain projections fail** to commute with boundary. An edge crossing out of the selected face is enough: projecting the edge first gives zero, while projecting its boundary retains an endpoint. This rejects silent inversion or coordinate deletion as the descending chain law.

**All72 dual restrictions pass** the coboundary test and the evaluation law

    <inclusion(c), phi> = <c, restriction(phi)>.

This provides a typed dual view for the reverse-incidence leg. It is not a claim that dualization is the unique intended P/E transport.

## The center is now a specific interface

The two legs meet at the chain complex of T184 and its dual, related by evaluation. A pairing is not yet an evolution operator from one to the other. Identifying corresponding basis coefficients at the center fails the differential test; a vertex chain has zero boundary, but its corresponding vertex cochain generally has nonzero coboundary.

The next source-backed candidate is the existing Fourier/derived-duality machinery, carrying the required grading and channel factor. The task is now to bind that central change of presentation, not invent another seven-stage schedule. Seven presentations still mean six incidence transitions; stage semantics and the P/E readout remain separate bindings.

## Central interface follow-up

The [central dual-cell handoff](central-dual-cell-handoff-v1.md) now constructs the finite map into relative dual-cell cochains in complementary degree, retaining all15 coefficients. This is a different target from same-face cochains; it also rebinds the descending windows accordingly. The channel Fourier action remains a separate factor to combine with this cellular map.

## Verification and artifacts

```sh
python research/strominger/checkers/check_fcc_face_flag_binding.py
```

**11 exact checks passed:**224 route-face bindings,3584 comparison triples,24 central flags,72 ascending inclusions,72 dual restrictions, and72 explicit failed chain projections.

[Receipt](results/fcc-face-flag-binding.json) retains original face/edge IDs, orientations, every central flag, projection counterexamples and source hashes. The source census and native particle constructors are unchanged. This audit binds the chain/dual part, not the analytic Fourier channel, whole-state evolution or physical species readout.
