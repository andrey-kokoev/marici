# Experimental terminal P→E support contraction

Implements Strominger handoff event16172 as a **separate experimental mode**. Native generators, families, atlas and receipts are unchanged.

## Rule and guard

`experimental-terminal-pe.mjs` builds shortcut schemas only from actual native P→N→E factors, validating both with the original full transfer checks. All three packets have equal absolute origin and distinct body sites. P/E share exactly the marked C1/M1 edge, E is a native sink, and the composed five-coordinate map is `[3,4,2,0,1]` in the native convention and reproduces the target packet map.

Each shortcut retains the native factor IDs, intermediate neutron packet/cell, all three reference chart IDs, marked edge and full coefficient permutation. Occupied support is P/E; reference support remains P/N/E. The reference neutron is not inserted, and no origin or context index is reset.

On the **complete selected set**, eligibility additionally requires:

- selected endpoints;
- no occupied body at the intermediate N site, regardless of which packet would occupy it;
- no native outgoing edge from that particular selected P reader to any selected packet, including a same-body reader advance.

The guard is recomputed after additions. It is not cached as an unconditional operation, does not test whole-P-body terminality, and imposes no arbitrary electron-last ordering.

Original occupancy, global C/M, root/exit reachability and triangular-face witnesses remain required. Only native face operations can witness actual occupied triangular contacts: PE edge support cannot substitute for one. Cross-branch equality and full global field sewing remain separate obligations.

## Complete small-family verification

| Maximum origin | Experimental configurations | Experimental local exit certificates | Native configurations | Native local exit certificates |
|---|---:|---:|---:|---:|
|0|4|2|3|1|
|1|136|24|108|14|

Three representations agree:

1. Explicit rooted construction graph, recomputing eligibility/rootedness on each complete target selection.
2. Exhaustive inspection of all 8 and 4096 packet subsets.
3. An independent guarded Boolean formulation using conditional edges and bounded transitive reachability.

The Boolean condition for a PE edge includes selected endpoints, negated occupancy of the intermediate N body, and negated selection of every native successor of its P source. Rootedness and exit reachability are computed by Boolean path closure rather than reusing the native monotone component support proof. Face-witness clauses refer only to native operations.

The complete construction graphs retain labelled revisits/self-loops: 10 edges at D0 and 1368 at D1. Every retained edge is replay-audited. The arbitrary small configuration resource limit returns incomplete, not saturation.

Every new zero-grade schema ends at a native E sink; therefore it introduces no new return cycle or strongly connected component. The native finite packet universe still contains every endpoint because each shortcut is factored through native PN/NE at the same origin. Conditional guards do not create new packets. The complete subset check independently verifies explicit-prefix completeness at the tested depths. No larger experimental family count is claimed.

The unchanged native Boolean compiler was freshly rerun at D2 and still gives **198,356 configurations / 459 local exit certificates**. Native D0/D1 counts were also checked against exhaustive selected-set inspection.

## Saved controls

All 24 hydrogen markings pass as H1 with the shortcut. Their corresponding native H2 paths pass without shortcuts.

All **20** saved isotope-deletion outcomes agree with Strominger's probe. Four pass:

| Source witness | Deleted N cell (source-local ID) | Counts | Eligible shortcuts |
|---|---:|---|---:|
|N15|16|7P/7N/7e|1|
|N15|17|7P/7N/7e|2|
|Ne22|16|10P/11N/10e|2|
|Ne22|29|10P/11N/10e|1|

Every positive reconstruction prefix is compatible and rooted after recomputing the experimental guard. These cell IDs belong to Strominger's regenerated source universe, not the separate Nima gallery.

Eight negative/resource controls cover occupied N, a different packet occupying the same N body, selected same-body native successor, wrong origin, wrong full map, wrong marked reference edge, wrong geometric edge and a resource-limited incomplete construction graph.

The checker reads Strominger's saved probe as a comparison oracle; it does not rerun his writing commands or alter his outputs. His independent Python evidence is supporting provenance, not falsely presented as a fresh Nima execution.

## Boundaries

These are **experimental reference-support certificates**, not native certificates or physical atom/binding results. The added occupancy permission is explicit and not derived from invertibility. No inverse operations or dual reversal grammar were added. No existing atlas entry was silently promoted. General generation is not filtered by isotope or electron neutrality; isotope cases are validation controls only.

## API and reproduction

- `contractionUniverse({maxOrigin, seedBindings})`: unchanged native universe plus validated conditional PE schemas.
- `inspectContraction(universe, ids, {mode})`: `experimental-terminal-PE` (default) or `native`; complete-set guard/contact/reachability audit.
- `guardedFamily(universe)`: exact guarded Boolean family subject to explicit diagram resource bound.
- `enumerateContractions(universe)`: explicit labelled configuration graph with revisit edges and completeness status.

```sh
node research/nima/checkers/check_experimental_terminal_pe.mjs
```

[Module](experimental-terminal-pe.mjs) · [Checker](checkers/check_experimental_terminal_pe.mjs) · [Verification](results/experimental-terminal-pe/verification.json) · [Complete D0/D1 graphs and provenance registries](results/experimental-terminal-pe/complete-small-graphs.json)
