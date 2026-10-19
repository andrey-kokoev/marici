# Assembly generation from a marked seed

> Historical **operation-count** experiment. The phase-bounded implementation is [Origin-bounded branching assemblies](origin-bounded-assemblies-v1.md); the numbers below do not answer the phase-budget request.

This implements the operator's corrected request: **generate compatible assemblies, not paths inside selected isotope layouts**. The earlier [path atlas](bounded-phase-path-atlas-v1.md) is a different instrument and is not an input here.

[Open the generated-assembly explorer](results/generative-phase-assembly/index.html). It is self-contained and opens directly in a browser.

## Inputs and stage convention

The [frozen contract](inputs/generative-phase-assembly-v1.json) supplies:

- One origin regular tetrahedron with the inherited ordered C0,M0,C1,M1 seed marking.
- The common PN, inverse-PN, NE, reader-phase-advance and NN-phase-advance laws, preserving all five reference coefficient slots and absolute realization origins.
- Nine **individual source operations**, including re-reading or transfer into an existing construction record. An operation introduces at most one new primitive body.
- The existing tetrahedral/octahedral honeycomb primitives and octahedral subdivision, generated locally through their actual faces.

There is no isotope selector, target proton/neutron/electron count, retained element prefix, predefined nucleus, preassembled transition graph, finite343-cell domain or C-exit-index4 filter in the search. The seed and local laws are input; geometry, attachments, configurations and composition profiles are output. The nine-operation claim is conditional on this fixed marked seed and these reference laws, not on every possible seed or physical interaction law.

Entry means the root window's C0. Every E packet provides a marked C-exit at its last window occurrence, C_(origin+2). These are declared marked boundaries, not derived physical ports.

## Search construction

A packet is a geometric reader chart, an absolute origin and a full five-slot coefficient permutation from the root input. All possible operations are generated from **every retained packet**, not only the most recently attached body. An E record has no outgoing rule but does not terminate other construction branches.

For each operation:

1. Obtain the unique neighboring primitive through its actual face, or the actual same-cell next reader.
2. Bind the target chart and its complementary reference marks.
3. Check the inherited occurrence witness and full coefficient map.
4. Reject cell-species conflicts, global C/M role disagreements and unsupported full-face contacts.
5. Retain the new construction record and every compatible continuation, with no composition filter.

P uses the native regular reference. N's complementary C0 is obtained from its actual neighboring regular-P geometry; that reference P need not be occupied. The reference does **not** count as a constructed proton. This is an explicit frame-provenance convention, not particle insertion or a physical binding law.

The common NE protocol admits either regular or split target primitives when its ordered window and distinct new context fit. A split-only E restriction would import an isotope-search ansatz. All24 ordered seed embeddings are checked against the native P/N/E constructor, including8 with a regular E target. Main nine-operation results below still use the one declared seed.

Packets are retained symbolic construction maps, not a claim that a physical quantum state was cloned. Reusing a record is part of the declared construction algebra. A physical coupled-field realization of that algebra is not supplied.

## Completed nine-operation result

| Quantity | Count |
|---|---:|
| Compatible retained-packet configurations |136,979|
| Generated labelled construction edges |754,479|
| Distinct occupied geometry/C–M-role candidates |2,784|
| Derived P/N/e composition profiles |65|
| Configurations containing E exits |49,207|
| Exit-certified coefficient/phase configurations |2,550|
| Geometry/role candidates with an exit-certified realization |360|
| Maximum occupied primitive bodies found |9|

New configurations at minimum operation counts0 through9:

`1, 2, 6, 21, 82, 333, 1381, 5804, 24593, 104756`.

Geometry/role grouping uses only occupied cells and their vertex roles. Unoccupied reference marks, alternative phases and different coefficient maps remain distinguished in the realizations; grouping shapes does not erase their effect on future construction.

The150 local cells examined include reference/lookahead geometry across all branches. They are not150 bodies in one configuration and are not an ambient-domain cutoff.

## What an exit certificate requires

A geometric neighbor is not silently promoted to a transfer. Structurally permitted additional contacts are recorded as **pending** until available packets provide their typed full-map witnesses.

An exit-certified configuration has:

- at least one E exit;
- a witnessed transfer on every occupied full-face contact;
- every retained packet able to reach an E within the available-packet graph.

All packets are rooted by their construction records. The definition checks the generated reference graph, not atomic stability. Partial configurations, uncompleted contacts and non-exitable packets remain in the catalog rather than being presented as completed complexes.

The following neutral composition profiles emerge without being requested:

| P/N/e | Minimum construction cost | Exit-certified realizations within9 |
|---|---:|---:|
|1/1/1|2|179|
|1/2/1|3|389|
|1/3/1|4|212|
|2/1/2|5|123|
|1/4/1|6|11|
|1/5/1|7|1|
|2/2/2|7|8|
|2/3/2|7|71|
|2/4/2|8|19|

Other charged or partial compositions are also retained. A profile's minimum cost is its first appearance, not necessarily the minimum cost of an exit-certified realization. These counts do not establish the existence or stability of corresponding physical isotopes. In particular the old selected Li-6 path fixture does not imply that a whole3/3/3 complex can be constructed within nine individual operations.

## Completeness and ordered construction histories

Configuration nodes are keyed by their entire set of retained packets. The occupied cells, roles, coefficient maps, origins and available future operations are determined by that set, so equal configuration keys have equal continuation rules. Complete ordered construction words remain **paths** in the generated graph; they are not identified by node reuse. Repeated operations on an existing packet are explicit labelled self-loops and still cost one stage.

Every operation adds at most one new packet, so breadth-first exploration reaches a configuration at minimum cost equal to its packet count minus one. All compatible successors of every configuration with minimum cost below9 are expanded. Longer histories with repetitions are represented by the same graph with a separate word-length budget.

Checks include:

- All754,479 generated edges validated against their source/target packet sets.
- A separate complete fanout audit: every compatible operation from every expandable configuration is present.
- Direct unmerged enumeration of83 short construction words, yielding the same30 configurations through cost3.
-11,616 basis/vector coefficient composition and inverse-recovery cases.
-8 negative controls, including conflicting roles/species, forged coefficients/origins and an explicit resource stop.
- Native P/N/E geometry reproduction for all24 seed embeddings.

The250,000-state safety limit was **not** reached. A deliberately limited run returns `complete:false`; such a run cannot pass the nine-operation completeness gate.

## Pb-208: the correct current obstruction

Pb is not excluded for lacking a supplied Pb graph. No Pb graph is required by this generator.

A seed plus nine one-body-at-most operations has at most ten primitive bodies, irrespective of the search strategy. A208-nucleon nucleus alone needs at least207 single-body additions from one seed; the neutral82P/126N/82e composition requires290 bodies and at least289 additions. The present search cannot reach that composition under this **individual-operation** budget.

Nine parallel construction rounds or nine collective stages would be a different cutoff and require an explicit compatible joint-operation constructor. The numerical bound here says nothing about physical impossibility or physical assembly duration.

## Explorer, complete archive and verification

- [Explorer](results/generative-phase-assembly/index.html): all2,784 geometry/role groups and all136,979 phase/coefficient variants. Composition and certification filters are output views, not generation filters. Construction playback displays a minimal representative word; the full graph retains alternative orders.
- [Full graph](results/generative-phase-assembly/assemblies.jsonl.gz): gzip JSON Lines with header, local geometry, charts, full packets, operation tables, every configuration, every construction edge and a checked completion footer.
- [Mathematical receipt](results/generative-phase-assembly/verification.json).
- [Browser receipt](results/generative-phase-assembly/browser-verification.json), [screenshot](results/generative-phase-assembly/viewer.png).

Reproduce from the repository root:

```sh
python -S research/aspect/scc/scc.py check generative-phase-assembly-v1
node research/nima/checkers/check_generative_phase_assembly_browser.mjs
```

The checker fingerprints the exact common-source dependency closure and owner-local constructor/contract/checker/template. An in-progress template edit was caught by this guard on the first full invocation; stable replays passed. No source layout or isotope search module is imported.

SCC checks the declared forward-realization/attachment/route stratum. Chromium validates every catalog variant's metadata, all65 composition filters, both certification/empty-result cases and65 interactive samples containing650 displayed construction records. Those are implementation checks, not physical evidence.

Only Nima-owned files and generated outputs were changed. Strominger's sources and receipts, the previous path atlas, publication and deployment were not modified. No commit or push was made.
