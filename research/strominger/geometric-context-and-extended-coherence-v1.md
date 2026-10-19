# Geometric context selection and extended field-frame coherence

## Context selection tightened by geometry and symmetry

The N reader has incoming face buv and outgoing face cuv. Each has a unique
centroid-edge patch incident to their common edge uv. These two patches now
supply the two context modes, instead of the earlier arbitrary choice of two
patches on one face.

On each selected patch take the complex line orthogonal to its native cyclic
mode in the derived plane metric. Replicate this context line coherently over
the three rotated sectors. This is necessary for the tested C3 coupling:
the two outside coefficients are fixed while the active triple cycles.
A context supported only in one sector would fail that equivariance test.

With the inherited corner/axis phases and the explicit assignment of the two
faces to the two context slots, all five columns are orthonormal. The full
binding intertwines the C3 action and reduces all three N projectors.

On the five coefficients their induced actions are:

- L: retain the active triple; reject the two contexts.
- G: average the active triple; retain the two contexts.
- Return: average the active triple; reject the contexts.

These are derived actions inside this chosen window-to-sector binding, not
an independent proof that the supplied native coefficient grammar selected
that binding. The PN pullback, joint NE exchange, five-coefficient norm checks
and explicit accounting ledger all still pass.

## Extended native-path test

Explored all native packet paths through 28 transitions from each of 24 seed
markings, tracking the candidate's field frame independently of its five-slot
coefficient permutation:

- 250,040 packet/frame states;
- 458,912 checked transitions;
- zero packets reached with conflicting candidate field parities;
- zero marked charts reached with conflicting field parities, even before
  retaining origin or coefficient permutation.

These counts sum across seeds; no claim of global distinctness across seeds
is made. The candidate uses a fixed global PN map and inverse, geometric
P-reader transport, and identity co-moving ordered-corner N-reader/NN transport.
In a common reference fiber its field map is determined by the P-reader count
modulo two. This reduction is why a bounded parity test checks the relevant
candidate frame rather than repeatedly multiplying dense 36-component matrices.

In this explored region, the parity is already determined by the marked
geometric chart. The observed order-five coefficient comparison does not force
an additional independent physical field mode: its differing coefficient frame
is handled by the propagated binding.

## Limits

This is a positive bounded coherence result for the declared candidate edge
maps. It does not prove the result at arbitrary depth or select those edge maps
uniquely. The fixed PN factor rotations and window-to-sector interpretation are
still hypotheses; the ledger term still lacks a physical energy interpretation.

The search tracks native paths, not a quantum tensor product of all packet
states. It does not by itself settle field values at every incidental contact
of every simultaneous assembly, electron boundary closure, or physical dynamics.
No torus/vortex topology is inferred from the frame result.

```sh
python research/strominger/checkers/check_full_five_channel_candidate.py
node research/strominger/checkers/check_extended_field_frames.mjs
```

Evidence: `results/full-five-channel-candidate/verification.json` and
`results/extended-field-frames/verification.json`.
Production/viewer unchanged.
