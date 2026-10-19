# Bounded C-entry / C-exit path atlas

Operator request: construct the bounded path map and increase its limit from eight to **nine source transitions**, retaining bidirectional checks. Active obligations: **attachment transport and route compatibility** on Strominger's existing reference carrier. This pilot binds to the selected He-3, He-4 and Li-6 source graphs; it does not enumerate all possible geometries.

## Executable artifacts

- [Self-contained interactive atlas](results/bounded-phase-path-atlas/index.html): open directly in a browser; no server, imports or network needed. Select assembly, path length or C-exit-index filter. Inspect every coefficient permutation, phase frame and retained prefix. Forward records and formal inverse reconstruction are explicitly separate.
- [Complete machine-readable atlas](results/bounded-phase-path-atlas/atlas.json).
- [Mathematical verification](results/bounded-phase-path-atlas/verification.json), [browser verification](results/bounded-phase-path-atlas/browser-verification.json), [viewer screenshot](results/bounded-phase-path-atlas/viewer.png).
- [Constructor](bounded-phase-path-atlas.mjs), [checker](checkers/check_bounded_phase_path_atlas.mjs), [SCC manifest](scc-models/bounded-phase-path-atlas-v1.json).

## Frozen conventions

The entry mark is the first occurrence of the fixed root proton window, C0. An exit is the last occurrence of a terminal electron window, C_(origin+2). This is a declared use of existing marked boundaries, not a derived physical interface. The coefficient carrier is the five-coordinate complex reference carrier, not one scalar on each spatial vertex.

A transition is one admitted, indexed edge of the selected source graph. All occurrences of an edge count toward the cutoff, including PN / inverse-PN detours. An exit ends a path at its first electron arrival. Distinct edge words are distinct paths even when cells, frames and numerical transformations repeat.

Source-transition counts have no derived conversion to C/M-cycle counts. Some admitted PN transfers have phaseDelta0. The current source has no constructor identifying each graph edge with a single elementary C/M operation; the bound counts all nine allowed source-edge occurrences instead.

## Nine-total-transition enumeration

| Selected reference | Previous ≤8 | Current ≤9 | New, exactly length9 | Retained prefixes | Budget-frontier prefixes |
|---|---:|---:|---:|---:|---:|
| He-3 |33|54|21|197|55|
| He-4 |71|135|64|1158|512|
| Li-6 |23|66|43|412|171|
| Total |127|255|128|1767|738|

Every carrier in each selected complex lies on at least one of these bounded exit routes:5/5,6/6 and9/9. This is coverage by a family of routes, not one route visiting every carrier and not coverage of the ambient lattice.

Counts by lengths0 through9:

- He-3:0,0,1,1,2,3,5,8,13,21.
- He-4:0,0,1,1,3,4,10,16,36,64.
- Li-6:0,0,0,1,0,3,1,11,7,43.

The cutoff frontier is not a proof of no continuation; those nonterminal prefixes simply exhaust the declared transition budget. Among these255 words,72 end at C index≤4:24 He-3,34 He-4 and14 Li-6. This endpoint filter is not itself an elementary-C/M-stage count.

Completeness is by exhaustive traversal of every outgoing source edge at each nonterminal prefix through depth9, checked against an independent layered multiplicity recurrence. All smaller transition cutoffs0–8 agree with restriction of the depth9 atlas. The entire eight-transition subatlas, including every path, frame, coefficient map and inverse certificate, is unchanged. Counts are edge-labelled words in these source graphs, not counts of physically distinct processes.

## Bidirectional traversal separates into two results

**Formal prefix reconstruction:255/255.** Each edge permutation is a bijection of the five coefficient slots. Each path stores its full composition, chart, absolute origin and indexed word. Reconstruction reverses the permutations, subtracts the recorded phase increments and recovers the actual stored prefix; a forged origin, chart, permutation or missing command record is rejected. Real and imaginary coordinate basis tests plus a nontrivial complex-vector control give2805 coefficient-recovery cases.

**Admitted native reverse routes:0/255.** Every exit word ends in NE, which has no admitted E-to-N source edge. Positive phase advances also have no negative-origin inverse command: the opposite reader's positive advance increases origin again, even if it has the inverse coefficient permutation. Consequently numerical invertibility does not supply a native reverse route.

A native PN inverse can invert its chart/coefficient/origin packet. Executing it as a new command appends a provenance record; it does not erase the original command. Formal reconstruction of an earlier prefix is not a claim that a physical process deletes its past. No formal inverse was added to Strominger's native grammar.

## A finite map can represent infinitely many histories

The second construction caps the **exit C index at4**, rather than word length. Since every native phase increment is nonnegative and an electron exit has C index origin+2, all such exit words fit in origins0–2. Chart, origin and full coefficient permutation then give a finite labelled packet graph:

| Reference | Reachable packet nodes | Edges | Nodes able to reach an allowed exit |
|---|---:|---:|---:|
| He-3 |9|11|9|
| He-4 |15|21|11|
| Li-6 |10|13|8|

These graphs are included as `CExitCapGraph` in each atlas model. Node reuse does not identify their complete words: the complete word remains the history. A node's `representativeWord` is a witness for that node, not its sole allowed history.

Each source graph has a PN / inverse-PN loop returning to the root chart with origin0 and identity coefficient map. Inserting this loop n times ahead of a fixed exit suffix gives lengths2n+L with unchanged exit C index. The histories remain distinct for every nonnegative integer n. This exhibits an unbounded word family under the C-index cap, represented by a finite graph. Ten inserted loops are also replayed as a direct implementation check; the unbounded claim follows from the exact repeatable identity packet loop, not that sample alone.

Thus a phase bound alone does not establish a finite path list. A bound on all transitions does. Neither result requires discarding history, banning returns or quotienting repeated cells.

## Verification and ownership

The source bundle's MJS files are hashed before dynamic import and again at completion; a change aborts the run. The receipt pins all source hashes and constructor/checker/template hashes. The imported phase assembly currently includes a Li-7 extension, but this atlas's fixed benchmark scope remains the three explicitly named graphs; no Li-7 completeness result is claimed.

Reproduce from the repository root:

```sh
node research/nima/checkers/check_bounded_phase_path_atlas.mjs
node research/nima/checkers/check_bounded_phase_atlas_browser.mjs
python -S research/aspect/scc/scc.py check bounded-phase-path-atlas-v1
```

The registered SCC checker passes in the stated stratum. Chromium exercised all255 forward and formal-reverse route displays,4303 state records, eight- and nine-transition filters, both finite graph views and empty selections, with no page errors. The mathematical checker also passes21 negative controls. SCC acceptance is not a physical reversibility certificate.

Only `research/nima/` was edited. The source mutation locus, native transition grammar, owner receipts, publication tree and deployment were left unchanged. No commit or push was made.
