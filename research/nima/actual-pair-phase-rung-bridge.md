# Actual pair: source-mode lift through the retained rung bridge

## Result

The existing source-mode processor distinguishes histories that the endpoint
profile alone cannot distinguish. The original pair packet and both rung
transport policies are retained unchanged.

Fresh verification: **4603 exact checks pass**, following a fresh run of the
965-check endpoint bridge.

This is a source-generator phase lift, **not** a coherence-dependent pair
interaction or a newly established native admission law. The earlier proposed
next step was too strong if read as asserting that such an interaction was
already bound to this packet.

## Existing operations reused

`research/voevodsky/checkers/evolve_relative_geometry_modes.py` supplies exact
cyclic-mode encoding, phase advance and decoding. For every supplied generator
A, its step satisfies

    decode(advance(encode(v, A))) = A v.

The checker calls those operations rather than inventing a phase assignment or
Hamiltonian. Every one of the six proton and five electron moving-arrow
correspondences matches a unique supplied affine generator. Applying that
generator to the tracked source point reproduces the recorded target point.
The corresponding centered linear action advances all labelled facet centroids
of that owner; the other owner's frame is held fixed.

Choosing generators along a retained path is an explicit scheduling adapter.
It is not the fixed scheduled word used by the backend's own full-cycle demo,
and it does not introduce a coupling between particles.

All centroid modes, including fixed modes, are retained. Exact inverse steps
and inherited metric norms are checked. Total centroid norms remain 4/3 for
the proton and 1 for the electron; these are not SI energies.

## Concrete predictive collision

Start at joint endpoint (A,E), with the source-generated labelled centroid
frames. Compare two five-arrow histories:

- proton AB, BA, AB, BC, CA;
- electron EA, AB, BC, CD, DE.

Both return to (A,E), have one retained path, primitive count 11, word depth 5,
and three endpoint-compatible next choices. Both also give **1/12** for
coordinate 1 of the labelled proton ABC facet centroid.

Request the same next proton AB operation. Both reach (B,E), but that centroid
coordinate becomes respectively **-1/4** and **1/12**.

Thus even endpoint data enriched by this present scalar reading do not predict
the next value of that same scalar. The full labelled centroid frame does.
The coordinate and facet are explicitly marked mathematical probes, not a
derived physical measurement selection.

## Predictive closure and rung transport

The enriched profile counts pairs

    (joint endpoint, labelled proton/electron centroid frames).

Its successor applies the existing mode step independently to each compatible
source generator and sums multiplicities. This computation does not need the
ordered path once the enriched state is supplied. It agrees with extending the
original paths and then reconstructing their frames.

The original rung packet retains those paths. Decoding either retained transport
policy therefore recovers the same phase profile; both policies satisfy the
source/readout successor square. No phase payload, new reference or matrix
response was inserted into the original rung rows. The original fixed-reference
aggregate is not being claimed to measure this phase profile.

The checker first tests complete word frontiers through depth five, then explores
the entire reachable endpoint/frame graph to closure:

- **60 states**;
- **150 labelled transitions**;
- no unexplored successor state;
- an actual retained word witnessing every state;
- independent profile prediction and both rung-policy squares at every state.

For the output consisting of joint endpoint plus the marked centroid coordinate,
partition refinement by all labelled future requests gives

    35 -> 45 -> 55 -> 60 classes.

The final partition is stable. Consequently every reachable state is
observationally distinguishable by some finite future request sequence for this
chosen output. This minimality statement concerns deterministic states and
labelled requests in this finite graph, not arbitrary aggregated path families,
all possible physical observables, or histories with winding information.

## Important controls and boundaries

A full ABC traversal applies its generator three times, not once. Likewise for
ADB. Both orders of the two complete triangle traversals return the native
centroid frame to its initial value. The earlier one-generator-per-triangle
permutation contrast must not be substituted for this traversal semantics.

The available next requests remain endpoint-admitted. This experiment demonstrates
**phase-sensitive response**, not phase-dependent rejection or admission.
The phase-frame endpoint can forget complete cycles; the original retained word
still records them. Neither this state graph nor word depth supplies a physical
clock, spinor lift, energy calibration or proton/electron interaction law.

## Reusable predictive contract

`predictive-pair-quotient.md` packages this graph as the explicit middle layer
between retained histories and the marked reading. Its checker verifies every
labelled request, both rung policies, distinct histories in each state class,
and explicit distinguishing continuations for all 1770 state pairs.

## Reproduction

    python research/nima/checkers/check_actual_pair_phase_rung_bridge.py

Checker: `checkers/check_actual_pair_phase_rung_bridge.py`.
Receipt: `results/actual-pair-phase-rung-bridge.json`.
The receipt records source hashes, witness, finite graph sizes and partition
refinement. This is exact standard-library Python verification, not an Agda proof.
