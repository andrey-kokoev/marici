# P/N/E interface catalog — first synthesis-net test

The registered `interface-path-catalog-D012-L234` test is complete. All simple directed native paths of lengths2–4 were enumerated from every packet in each complete origin-bounded universe. Parallel operation labels and all factor provenance are retained.

| D | Paths | Whole-support compatible | N-internal P→E paths | Same-origin PN→NE interfaces | Geometric endpoint groups with different maps |
|---|---:|---:|---:|---:|---:|
|0|1|1|1|1|0|
|1|19|19|6|4|1|
|2|115|113|24|12|23|

Counts are per depth, so smaller-depth paths can recur in larger universes.

## Findings

**1. The grade-zero classification is exact in this domain.** Every same-origin P→E path with only internal neutron packets is PN→NE. The catalog yields1/4/12 such interfaces at D0/1/2. Each carries the experimental contraction's explicit occupied P/E, vacant N, retained P/N/E reference support and selected-reader terminality guard.

**2. Shape alone loses transport information.** At D2,23 endpoint-body/species groups contain paths with different five-coordinate maps. For example, endpoint group `0:proton:3:electron` contains both `[3,4,2,0,1]` and `[1,4,0,2,3]`. These are records0,20,31,67,89 in the D2 catalog. Marked packets and occurrences must survive interface identification.

**3. Matching the PE permutation is also insufficient.** D2 record7, PN→NN→NN→NE, gives the same `[3,4,2,0,1]` permutation, shares an endpoint edge and has compatible occupied support, but advances origin by2 and retains five body sites. It is a different interface from the same-origin contraction. Six compatible N-internal P→E paths at D2 share an endpoint edge while advancing origin; eleven pass endpoint compatibility and terminality while advancing origin.

**4. Valid factors need not coexist as occupied support.** Two D2 paths fail the whole-path occupancy guard even though every native factor individually validates:

- record10: PN→NN-phase-advance→reader-phase-advance→NE;
- record48: NN-phase-advance→reader-phase-advance→NE.

Both require incompatible species at one occupied cell. The catalog retains them as rejected support configurations rather than discarding their valid transport derivations.

## Independent verification

The Python checker imports neither the JS generator nor its search. It independently breadth-first enumerates paths over the serialized source registry, reconstructs native permutations from a separate operation table, checks their five-coordinate compositions on ten real/imaginary basis inputs, verifies absolute occurrences/reference support, and reconstructs whole-support species/role/contact compatibility.

All135 depth-indexed path records agree;1350 basis checks pass. Wrong-map, lost-context-index, dropped-reference-support and incomplete-path-list mutations reject. This independently checks the catalog over the supplied native universe; universe generation remains the shared source.

## Next frontier: guarded composition

The next registered test is `guarded-interface-critical-pairs-D01`: compare interface-record predictions against direct source audits for every one- and two-packet addition to the complete D0/D1 experimental families, examining both insertion orders and extracting minimal stale-guard/support-conflict witnesses.

This follows from the catalog: transport is composable as a map, while occupied support and reader guards can obstruct the corresponding assembly. The next step is to make those obstructions explicit composition data.

[Catalog and registry](results/pne-interface-catalog/verification.json) · [Independent receipt](results/pne-interface-catalog/independent-verification.json) · [Net revision2](contracts/pne-structural-synthesis-net.v2.json)

```sh
node research/nima/checkers/check_pne_interface_catalog.mjs
python research/nima/checkers/check_pne_interface_catalog_independent.py
node research/nima/checkers/check_pne_structural_synthesis_net.mjs research/nima/contracts/pne-structural-synthesis-net.v2.json
```
