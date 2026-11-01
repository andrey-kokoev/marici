# Native edge-five bulk, and a conditional closure-capacity obstruction

## Constructed from the global native graph

`native-axis-port-graph.mjs` builds all physical face ports first, joins actual shared faces, and adds the source model's opposite-face, same-axis continuity at every N octahedron. It then computes components of the complete graph. It adds no boundary seams and no internal P/E mixing.

Each tetrahedron retains one port per coordinate-normal axis; each N octahedron retains two opposite ports per axis. Opposite faces are checked against the actual native vertices. The complete face/owner inventory is checked independently; dropping an incidence is rejected.

This replaces the previous axis-changing comparison paths as the starting point for native transport. It does not discard the earlier information operations, but does not label them as single-wire transport.

## Exact edge-three calibration

The open edge-three graph has 280 physical ports and 100 components. Using the existing global wiring's retained lift maps:

- all 280 physical ports map to its 256 quotient ports;
- every bulk edge maps to an existing quotient edge;
- precisely the source's 24 declared seam edges are missing;
- after adding those seams, the reconstructed components equal the complete port sets of all **64 source wires**, not just their count.

No seam, quotient or local axis rule was fitted to the edge-five result.

## Edge-five bulk result

All 245 whole cells remain. The complete open graph has:

| Item | Count |
|---|---:|
| Physical face ports | 1,320 |
| Native shared faces | 560 |
| N opposite-face continuities | 340 |
| Physical boundary ports | 200 |
| Components | 420 |
| Complete P–N–E passages | 220 |
| Open N halves, each with one charged endpoint | 120 |
| Open charged ports | 80 |

Each of the four axes has 55 complete passages, 30 open N halves and 20 open charged ports. Every component is nonbranching, uses one axis and contains at most one physical N cell. Test contents are constant along every component without merging distinct component identities.

“Complete passage” means a two-ended P–N–E segment inside the carrier, not a closed dynamical return. The 200 open legs have not been sewn by an invented edge-five period lattice.

## Can the old whole-cell closure interface be copied literally?

The tested extension preserves all 80 P and 80 E cell fibres, their four distinct ports, and every native charged-face incidence. It permits identifying whole N cells while retaining their physical lifts, but demands:

- eight face ports per N fibre;
- one charged neighbour at each face port;
- four wires per N fibre, with exactly one N channel per closed wire;
- no new branching, port multiplicity, internal charged-cell operation or N–N seam.

Under this inherited interface, 80 P fibres supply 320 axis-labelled wire slots, so exactly **80 N channel fibres** are required. This is a structural slot count, not a claim of 320 independent physical contents or a replacement for the earlier 80 named bundle inventory.

### The native-incidence lower bound is 82

Count the already-present shared faces incident to each physical N cell:

| Retained native charged-face incidences | N cells |
|---|---:|
| 4 | 6 |
| 6 | 36 |
| 7 | 24 |
| 8 | 19 |

A class of identified N cells has only eight target face ports. Because charged fibres and their ports remain distinct, the retained native incidences in that class must fit injectively into those eight slots.

Every physical N cell contributes at least four incidences. Therefore:

- a cell of degree greater than four cannot share a class with another N cell;
- three N cells cannot share a class;
- only the six degree-four cells can potentially be paired.

Even ignoring further geometric restrictions, this requires at least

\[
36+24+19+\lceil 6/2\rceil=82
\]

N fibres. Equivalently, 85 physical N cells would need five class-count reductions to reach 80, but at most three reductions are possible under the eight-port capacity constraint.

Thus **no literal closure of this specified kind exists**. Searching different seam matchings cannot overcome this necessary bound without changing a hypothesis.

### Calibration of the bound

At edge three, the incidence histogram is six degree-four cells, twelve degree-six cells and one degree-eight cell. The same bound gives

\[
12+1+\lceil6/2\rceil=16,
\]

which the actual source quotient realizes. Its grouped N cells satisfy the capacity condition and all source wires are recovered exactly.

## Scope and next step

The native edge-five bulk exists and is explicitly retained. The obstruction concerns a **literal extension of the old whole-cell, four-axis, one-N-per-wire closure interface**. It is not a theorem excluding every edge-five sibling or every content-bearing fibration.

A richer global interface could change one of those hypotheses, but must state and justify that change. This audit does not choose a replacement, invent boundary matching, delete incidences, or treat the old arbitrary-turn corridor routing as native axis transport.

The productive next question is what the actual larger-carrier fibration supplies at its boundary—not another coherence certificate or seam search under the now-obstructed interface.

## Reproduction

```sh
node research/strominger/checkers/check_su32_edge5_native_bulk.mjs
python research/aspect/scc/scc.py check strominger-su32-edge5-native-bulk-v1
```

Contract: `contracts/su32-edge5-native-bulk-v1.json`.
Receipt: `results/su32-edge5-native-bulk-v1/verification.json`.

The receipt retains every edge-five port, edge, component and boundary occurrence, both incidence histograms, all capacity-admissible N pairs and the exact calibration result. Successful checking verifies the construction and obstruction; `literalClosureNecessaryConditionPassed` is false. Existing source geometry and wiring implementations were not changed. No proof assistant was run.
