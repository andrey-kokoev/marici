# Direct global-fibration extraction exposes the wrong formal interface

## Independent source and fixed test

This audit starts with `buildSulfur32Wiring`, constructs its complete global port graph, and only then extracts a local cut. No comparison adapter selects the cut's internal wire connections.

The fixed three-cell motif is:

- producer: `electron:0,0,0,0`;
- N cell: `neutron:1,1,0,1`;
- proposed output: `electron:0,1,-1,0`.

Both occurrence charts occur in the actual edge-three fixture, so the existing global wiring is directly applicable. The selected example is an audit fixture, not a preferred physical representative.

The wiring is still the repository's **declared edge-three periodic candidate**, not an established physical dynamics or a licensed edge-five seam construction.

## The axis test fails before higher coherence

The formal path enters the N cell on coordinate axis **2** and exits on axis **1**. These ports belong to different native wire identities.

The actual continuation along the incoming wire exits on the other N port of axis 2. The source wiring determines that continuation; no new transition law is required. Its retained lifts and period data are in the receipt.

All 448 geometrically audited formal motifs change axis. Of these, 32 have both charts in the edge-three source atlas. The old three-vertex construction therefore cannot be interpreted as one native wire passing through its proposed two faces. This does not invalidate it as an information-comparison programme, or forbid every possible multiwire operation.

The discrepancy arose upstream of the coherence tests: the formal motif had been selected from local comparison incidence, not extracted from the global wire components.

## The actual native boundary

Cut the complete global graph at all ports of the three selected cell fibres, retaining every crossing interface. The result has:

- **16 internal port occurrences**;
- **6 internal graph edges**;
- **12 boundary port occurrences**;
- **10 internal connected components**, each belonging to one native wire.

Thus the native boundary relation is parameterized by **10 independent wire values**. Boundary appearances on the same wire must agree. Every component meets the boundary, so compatible boundary data reconstruct all internal port values uniquely. The checker reconstructs them without a hidden copy of the interior, verifies independence of boundary enumeration order, and rejects a corrupted same-wire equality.

This boundary is derived from the existing global object. It is not the previously proposed five-port formal operation interface. The difference in port counts alone is not used as a no-go argument: a formal port could in principle bundle several native ones.

## A stronger nonfactorization witness

To compare actual content, signed reference records are explicitly bound to **entire source-grouped endpoint fibres**, using the existing `groupSulfurPayloads` operations. No coordinate slot is selected and no new numerical meaning is assigned. This is a source-supported whole-fibre restriction, not a claim that every possible physical record interpretation is identical to it.

For the fixed motif, the complete formal external inputs observe **18 native wire values**. The full native output fibre contains four wire values, **all four absent from those formal inputs**.

The receipt gives two complete, admissible 64-wire assignments. They differ on one of those unobserved output wires. For all sixteen source/target sign-binding pairs:

- the full formal external inputs agree, including retained metadata;
- evaluation of the formal composite gives the same result;
- the actual native output fibre differs.

Consequently, the full native output does **not factor through those formal inputs** on the currently admitted global-state domain. This is an explicit information-sufficiency obstruction, not a count comparison or a claim about physical impossibility.

All 32 edge-three-supported motifs have at least one such unobserved native output wire. The detailed two-state counterexample is executed for the fixed motif. The two assignments pass the source grouping/restoration checks in both presentations.

## What is corrected

The previous local and contraction-square tests remain valid for their stated formal information operations. They did not identify those operations with the source global-fibration transport.

We now have an independently extracted boundary relation and a direct refusal of that identification. The correct next source interface is the native cut and its wire fibres. A smaller formal interface must come with an information-sufficient restriction and a verified factorization. More coherence checks of the old interface cannot recover missing inputs.

The edge-three period lattice has not been extended to edge-five. The all-448 axis audit is a geometric test; actual global-wiring claims are restricted to the source-supported edge-three cases.

## Reproduction

```sh
node research/strominger/checkers/check_su32_native_boundary_extraction.mjs
python research/aspect/scc/scc.py check strominger-su32-native-boundary-extraction-v1
```

Contract: `contracts/su32-native-boundary-extraction-v1.json`.
Receipt: `results/su32-native-boundary-extraction-v1/verification.json`.

The receipt retains the cut, all component/wire identities, actual versus proposed continuation, all 32 support audits, both global assignments, and the full nonfactorization witness. `formalNativeIdentificationPassed` is false; successful checking means the extraction and hostile pass. Existing source operators were not modified, and no proof assistant was run.
