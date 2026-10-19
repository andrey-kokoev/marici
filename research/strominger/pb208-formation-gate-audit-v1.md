# Pb-208: gate audit before an untargeted formation experiment

## Question and decision

Does the current construction select and dynamically form Pb-208 without specifying its counts or a Pb-shaped target?

**The reviewed implementation does not yet supply such an experiment.** Its Pb-labelled layout passes a geometry check, but the formation gate is not met. No dynamics, energy functional, random-growth rule, viewer feature, or target-fitting rule was added in this audit. This is not an impossibility result for a future model.

## What the symmetry statement does—and does not—supply

The source protocol `simplex-interface-algebra-v1.md` discusses the direct product **A4 × C2 × C2**: twelve proper tetrahedral actions combined with two commuting projector-derived involutions, acting on a 36-dimensional field. Those derived reflections are explicitly not automatically authorized native moves. The protocol distinguishes this finite action from spatial translations and from inter-instrument transport.

Consequently, calling the displayed lattice an “A4(C2×C2) space” must not silently identify its geometry, finite operator symmetry, and a particle-formation dynamics. This audit does not freshly certify that operator algebra; it checks the actual packing and window constructors. The symmetry label alone supplies neither an envelope-size selection nor a time-evolution rule.

## Where 82 and 126 come from

`simplex-components.mjs` prescribes four layers and rejects resolutions other than 7. Their whole-item counts are **1, 4, 44, 126**. These are geometrically generated within the chosen envelope, not injected as the proton/neutron counts of a dynamical run. Nevertheless, choosing this envelope is an input, not an outcome.

The composition formulas in the source give:

- Layer 2: 10 upright tetrahedra from positive compositions of 6 into four coordinates, plus 34 inverted tetrahedra from positive compositions of 8 with minimum coordinate 1. Thus **10 + 34 = 44**.
- Layer 3: 74 tetrahedra from nonnegative compositions of 6 with a zero coordinate, plus 52 octahedra from nonnegative compositions of 5 with a zero coordinate. Thus **74 + 52 = 126**.

The Pb construction then applies these additional conventions:

1. Match every layer-2 item to a distinct adjacent layer-3 item: 44 reserved witnesses.
2. Label the unreserved outer items as protons: **126 − 44 = 82**.
3. Label the reserved witnesses as neutrons.
4. Attach one neutron connector and one regular tetrahedral electron endpoint per proton: **44 + 82 = 126 neutrons**, **82 electrons**.

This explains the counts without claiming that particles evolved toward them. A whole octahedron or composite gap counts as one body under this representation, despite containing multiple primitive tetrahedra.

## Fresh replay findings

### Matching is not a unique spatial selection

Reversing both inner-item processing order and neighbor order preserves matching size **44**, but changes both the assignment and the reserved outer-site set. Thus the **count** survives these two traversal conventions; the selected locations do not. This is not an exhaustive matching census, and the alternate matching was not carried through a new full chain packing.

### Packing passes; marked-window compatibility does not

The existing geometric checker freshly passes: **761 primitive components**, with **289,180 pair checks**, positive volumes, no duplicate primitives, and no interior overlaps. These include retained geometric context; they are not 761 particles.

In the legacy 82 chains, incoming PN and outgoing NE attachment faces intersect in:

| Shared vertices | Chains |
|---|---:|
| 0 | 17 |
| 1 | 65 |
| Required retained edge: 2 | 0 |

The native packet requires the retained C1/M1 edge. Therefore none of the **existing legacy chain placements** passes even this necessary condition. This does not exclude a different placement.

Fresh local rebinding reproduces the known distinction:

- **74** tetrahedral proton sites have multiple free native packet embeddings; none is uniquely selected by non-overlap.
- **8** octahedral proton bodies have no supplied four-vertex seed-carrier binding.
- These enumerations do not establish a globally propagated marking or phase-consistent assembly.

### Native transitions terminate instead of assembling Pb

For all **24 supplied seed markings** on the fixed subdivision, the reviewed window constructor performs exactly two commits:

**P → N → E**, then `complete`.

Thirty-two further step attempts per marking commit nothing and leave the placed bodies unchanged. This is a terminal construction protocol, **not evidence that its three-body packet is a dynamically stable attractor**. It supplies no E-to-next-P handoff or autonomous branching rule in this implementation.

### Broader native grammar exists, but is not a formation law

The terminal packet is not the entire research grammar. `research/nima/generative-phase-assembly.mjs` already supplies PN, inverse-PN, NE, NN-phase-advance and reader-phase-advance operations. A fresh depth-4 inventory from its default marked seed reaches **42 packets** (14 P-reader packets, 18 N-reader packets, 10 E-reader packets). These are marked states, **not 42 distinct particles or a compatible assembly**. All inventoried electron packets have no outgoing operation.

Thus it would be incorrect to say that no growth-capable local transitions exist. What remains missing for the proposed formation claim is a justified global evolution/selection rule on admissible assemblies, with occupation/contact coherence and a stability criterion. Enumeration of possible transitions does not select a physical trajectory or an attractor. No need for an E-to-P restart has been established: continuation through the existing P/N grammar is a separate possibility.

The related `four-progression-directions-v1.md` also distinguishes native progression from geometric adjacency: it reports two repeatable spatial directions for mobile markings under the fixed grammar, not arbitrary three-dimensional control. Its longer-path/invariant proof was consulted, not rerun by this audit.

### Domain-size sweep is not currently available

Calls at resolutions 3, 5, 9 and 11 are rejected; only 7 is supported. Those rejections are implementation restrictions, not physical exclusions or negative formation trials. An honest size-dependence experiment requires a separately justified domain family.

## Gate to the next experiment

Before random perturbation trials can answer the formation question, supply:

1. A target-independent domain family or reason for selecting the current envelope.
2. A coherent global assembly update on the existing P/N/reader grammar, carrying marked state rather than restarting independent seed frames. Any additional handoff/branching law needs separate justification.
3. A justified carrier interpretation for the octahedral protons and composite neutron bodies—or a different representation without silently changing particle counts.
4. An explicit update/selection rule and stability observable. Geometry-only resource search with address-order tie breaks is not a physical preference law.

The smallest useful next research task is to examine **untargeted growth under the existing PN/inverse-PN/NN/reader grammar**, while preserving global occupation, marks and contact witnesses. First distinguish reachability from a selected dynamical history; random scheduling or relaxation would be an added hypothesis, not something supplied by symmetry. An E-to-P handoff should not be invented merely to make the legacy layout reachable. Inventing a potential that favors 82/126 would answer a different, circular question.

## Reproduction

```sh
node research/strominger/checkers/check_window_construction.mjs
node research/strominger/checkers/check_pb_window_rebinding.mjs
node research/strominger/checkers/check_lead208_model.mjs
node research/strominger/checkers/check_pb208_formation_gate.mjs
```

The new checker records source hashes, layer inventories, count provenance, matching-order comparison, legacy face intersections, all 24 terminal packet runs, the broader depth-4 grammar inventory and the resolution checks in `research/strominger/results/pb208-formation-gate/verification.json`. Results remain ignored runtime artifacts; the checker and this audit are the durable sources. No website or viewer files are changed.
