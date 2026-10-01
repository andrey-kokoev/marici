# Self-feeding retained-fiber promotion reaches the first tetrahedron

## Generated successor interface

`SelfFeedingPromotion.agda` wraps the preceding retained relationship adapter in
a reusable finite interface. A graph supplies finite vertex and edge counts and
an endpoint map. Every successor obtains its data from the actual generated
connection list:

- new vertex identifiers: the preceding edge indices;
- new edge identifiers: finite indices into the generated witnessed list;
- new endpoint map: the retained left/right indices of each indexed witness;
- equality: generated finite-index equality, with a soundness proof;
- ordering: finite-index numerical order;
- reciprocal fibers and native Pi compilations: the existing promotion adapter;
- actual shared-endpoint equalities: recovered from its incidence witnesses.

Nothing re-enters a hand-written diamond, wheel or tetrahedral graph between
iterations. The initial paw is the sole explicit endpoint fixture.

`History` retains the actual preceding history and its `RetainedPromotion`
bundle at each step. This keeps every previous source table, reciprocal fiber,
original packet, native grouping history and generated witness accessible.
The generic `origin-run` theorem recovers the initial graph from any finite
iteration. Local finite identifiers are interpreted in that stage's history;
the finite executor makes this explicit with cycle-qualified packet IDs.

## Checked sequence

| Promotions | Records | Undirected relationships | Directed packets | Tetrahedral subgraphs |
|---:|---:|---:|---:|---:|
|0|4|4|8|0|
|1|4|5|10|0|
|2|5|8|16|0|
|3|8|18|36|1|

`SelfFeedingPawRegression.agda` normalizes the generated states to prove the
three count pairs (4,5), (5,8), (8,18). It proves all six adjacency statements
among generated vertex indices0,1,2,3 at the third promotion. Those four indices
therefore form the tetrahedral graph; they are not a separately inserted seed.
The regression also constructs the retained three-step history and proves its
original graph is the paw.

The independent finite executor calls the same earlier packet/fiber adapter
three times. It checks original-ID recovery and incidence witnesses at every
step. That adapter compares each output against an independent pairwise
intersection line-graph calculation. The new test enumerates tetrahedral
subgraphs: none at steps0,1,2 and exactly one at step3. All initial eight packet
objects remain recoverable through the actual predecessor chain.

## Scope

This closes the self-feeding loop for the explicitly supplied relationship
promotion rule. It ties the graph-growth sequence to repeated typed fiber
construction and retained source evidence. It does not select the rule as
physical dynamics, identify a particle, add a metric or clock, or establish
that each promotion is the full proposed nine-rung physical cycle.

A finite list index gives a concrete presentation of the generated witness
population. Invariance under arbitrary reordered input enumerations and a
universal simple-graph preservation theorem have not been added here. The
specific three-step seed and all its generated incidence data are checked.

## Verification

```
python research/nima/checkers/check_self_feeding_paw.py
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SelfFeedingPawRegression -Fresh
```

Both passed; the Agda run freshly rebuilt dependencies in safe Cubical mode.
Agda reports `UnsupportedIndexedMatch` warnings for finite-index pattern
matching in lookup, equality, its soundness proof and the seed endpoint map.
These functions compute on the concrete finite constructors exercised here;
the warning concerns computation on transported indices. No such transport
computation is claimed or used as a regression result. The warnings are kept
visible in the saved log.

- Generic iterator: `agda/SelfFeedingPromotion.agda`
- Formal regression: `agda/SelfFeedingPawRegression.agda`
- Finite executor: `checkers/check_self_feeding_paw.py`
- Finite result: `results/self-feeding-paw.json`
- Fresh receipt/log: `results/agda-SelfFeedingPawRegression.json`, `.log`
