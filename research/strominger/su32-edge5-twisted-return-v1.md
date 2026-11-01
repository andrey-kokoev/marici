# Edge-5 return: duality, retained history, and a reflection-compatible route witness

## Question

Can the dependent-return construction be bound to the retained edge-5 routes without treating reflection as a transport hop or erasing traversal history?

The tested step is a **declared block of four actual face crossings**. This granularity and the earlier arbitrary-cell-turn/multiplexing policy are assumptions of the candidate executor, not derived native laws.

## Reflection audit and constructive revision

The original globally solved routing had only **1 of 80** fibres satisfying reflected-route = inverse-route under its fixed identity. Its whole reflected assignment used **74 faces** absent from the original selected support. Carrier symmetry therefore did not automatically make that route assignment reversal-compatible.

A separate candidate now enforces the additional constraint globally:

1. Keep all eighty upper-half paths, including their middle-layer N occurrences.
2. Define each lower half by reflecting and reversing that complete upper prefix.
3. Verify the entire resulting assignment before interpreting local visits.

Every middle-layer N cell is fixed by reflection, so the two halves attach at their actual common cell. No reflection is inserted as a physical hop, and no independent local reader or endpoint matching generates the continuation.

The new witness passes:

- 80 unchanged fibre identities and upper halves;
- all 245 cells covered;
- reflection = inverse for all 80 labelled routes;
- the original named visits to all eight middle triples and their partner tips retained;
- actual shared-face hops, per-cell conservation and exactly 80 occurrences per layer.

Compared with the original witness, 79 routes change in their lower halves. The new support uses **368 shared faces**: 38 added, 36 removed. It is reflection-closed, with no additional dual-only faces. Neither the original witness nor the failed symmetry audit was overwritten.

Contract: `contracts/su32-edge5-reflection-compatible-routing-v1.json`.
Receipt: `results/su32-edge5-reflection-compatible-routing-v1/verification.json`.

## A witnessed four-block return is twisted

The executor retains the orientation chart and block position. Four blocks traverse the carrier to the opposite N boundary. The supported comparison is

\[
G^4(a)=R(a),
\]

not ordinary equality with the original oriented reference. Here R is the carrier/route duality. It compares references; only actual face crossings execute transport.

A second leg follows the dual route. In the reflection-compatible witness that leg is exactly the original route's inverse. It is a real path along the same supported interfaces, not a seam jump. The resulting declared eight-state controller satisfies

\[
G^8(a)=a.
\]

Every one of its 640 labelled oriented reference states passes the twisted four-return and ordinary eight-return tests. Ordinary four-return fails on all of them. Each of the 80 entrance-rooted certificates retains the three intermediate macro references, the actual terminal reference, all four macrostep histories, and the dual-reference comparison witness.

Eight is the period of this explicitly constructed controller. It is **not an inferred physical period**: changing the macrostep granularity changes that description.

## Formal distinction from ordinary Per4

`agda/TwistedRouteReturn.agda` freshly typechecks in safe Cubical Agda. It proves:

- if R commutes with G and is involutive, a witness `G⁴(a) ≡ R(a)` constructs `G⁸(a) ≡ a`;
- the concrete orientation/block frame obeys four-step duality and eight-step return;
- its ordinary `Per4` type is empty;
- forgetting orientation identifies two distinct frames.

Thus the earlier general coherent-C4 theorem is not a license to assert four-periodicity of these retained oriented states. A four-cycle obtained by forgetting the chart uses a non-injective projection, which is not silently admitted as physical state equality.

## History and operation boundary

After eight blocks the active reference and payload return, but the record contains **32 face crossings**. The original sixteen-crossing prefix remains intact. This is not equality with the initial history-bearing state.

The return certificates implement a geometric comparison with retained history. They do not supply the signed-record-to-fibre map, native junction/payload dynamics, comparison fillers for the 44 cones, or nonintersecting finite-width strands. The global route selection and reflection-compatible completion remain explicit candidates under the corridor policy.

## Reproduction

```sh
pwsh -NoProfile -File research/strominger/checkers/check_dependent_four_return_agda.ps1 -Module TwistedRouteReturn -Fresh
node research/strominger/checkers/check_su32_edge5_twisted_return.mjs
node research/strominger/checkers/check_su32_edge5_reflection_compatible_routing.mjs
```

The first Node checker retains the original symmetry failure, validates all reflected geometry and the full 640-state twisted executor. The second verifies the separate reflection-compatible candidate. Both pin their source receipts and contracts. Formal receipt: `results/su32-edge5-twisted-return-v1/agda.json`.
