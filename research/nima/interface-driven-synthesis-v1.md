# Interface-driven D2 synthesis — net iteration3

The registered `interface-driven-synthesis-D2` test completed within its one-million-configuration and500,000-diagram-node limits.

## Result

| D | Configurations | Local exit certificates | Labelled transitions |
|---|---:|---:|---:|
|0|4|2|10|
|1|136|24|1,368|
|2|243,034|698|7,018,785|

At D2 this extends the native baseline by44,678 selected configurations and239 exit certificates. It is the complete family for the experimental terminal-PE grammar at this budget, with no isotope or electron-count filter.

## How it constructs

`interface-synthesis.mjs` consumes the retained path catalog and compiled native interfaces. It compiles pairwise compatibility obstructions once, then generates from the seed using:

- selected endpoint packets;
- required-vacant body sites and forbidden selected successors encoded in masks;
- an index of interfaces affected by each packet addition;
- incremental connection activity updates;
- rootedness of the updated connection graph.

The search itself calls neither the source configuration inspector nor the Boolean family. It adds target packets from interfaces whose sources are already selected. A later verification pass checks every resulting configuration against the original complete-set source audit and the separate guarded Boolean formulation.

The compilation still uses native operations, source packet geometry and original pair guards. This result concerns generation from those compiled interfaces, not independent derivation of the native grammar.

## Verification

For every generated selection:

1. Direct source auditing confirms compatible geometry/roles and all-selected-record rootedness.
2. Boolean-family membership agrees; exact family cardinalities establish completeness.
3. Direct and Boolean exit flags agree.
4. The entire active interface set agrees with selected native operations plus eligible experimental shortcuts.
5. Each stored construction-parent step reproduces the packet set and incremental activity mask, with an active interface from an existing source to the added target.

All possible interface fanouts are emitted against the complete selection map. Only selected sources and interfaces active in the complete target selection contribute transitions. Labelled revisits remain present.

D2 graph statistics:

- 5,257,991 self-loop/revisit transitions;
- 93,174 PE-labelled transitions;
- 44,875 accepted transitions that disable at least one previously active PE shortcut;
- 153 composition profiles;
- maximum16 occupied bodies and27 retained records.

The search rejects42,544 distinct first-encountered compatible candidate selections for lack of rootedness. This is an implementation traversal count, not the total number of invalid subsets. Likewise, the stored `guardDisablingCandidates` count excludes already-known candidate states; the full transition statistic is the appropriate support-replacement measure.

Each archive was decompressed, parsed and checked for matching configuration/edge counts and a complete footer. The explicit resource-stop control returns incomplete. Input hashes were unchanged across the run.

## What this establishes for synthesis

The interface calculus now constructs the complete small atlas rather than merely describing existing examples. Conditional connection activity is sufficient to drive the generator in the tested family. Disabling a shortcut is a connection-update event, not automatically a rejected construction step: the44,875 rooted replacement transitions make that distinction concrete.

The next registered test is **certificate-directed completion planning at D2**. Use reverse reachability and shortest paths from the698 certified states to classify every partial configuration by whether additions can complete it, retain a shortest completion word when possible, and extract obstructions for the remainder. Operation distance is a planning objective; maximum origin remains2 throughout.

## Artifacts

- [Generator](interface-synthesis.mjs)
- [Checker](checkers/check_interface_driven_synthesis.mjs)
- [Receipt and composition profiles](results/interface-driven-synthesis/verification.json)
- [D0 graph](results/interface-driven-synthesis/D0-graph.jsonl.gz)
- [D1 graph](results/interface-driven-synthesis/D1-graph.jsonl.gz)
- [D2 graph](results/interface-driven-synthesis/D2-graph.jsonl.gz)

```sh
node research/nima/checkers/check_interface_driven_synthesis.mjs
```
