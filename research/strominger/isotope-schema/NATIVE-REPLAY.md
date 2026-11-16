# Native reader incidence: iteration 8

## Implemented operation

`NativeReaderIncidenceV1` imports the saved Ne-22 D4 finite-reader witness, not a drawing and not a Ne-20 spatial construction. Its artifact is `research/strominger/results/reference-ne22-search/D4-verification.json`; a second explicitly pinned InputArtifact is the neighboring `verification.json` dependency manifest. The selector is `Neon-22-D4`.

Before projecting, `native_replay.mjs` verifies the fixed set of 11 declared dependency pins and the saved D4 input digest. It regenerates the bounded native universe, checks selected packets/charts, replays each construction prefix, validates retained transfers, compares body geometry/species and inspection data, and separately enumerates occupied-face contacts and reverse exit reachability. Saved solver/pass flags are not evidence. It invokes only a fixed local constructor, not code chosen by input data. Reads are size-bounded; dependency paths resolving outside the repository fail.

The checker shares the original generator and geometry. The declared dependency set is verified; this is not a new independent physical model or a claim of complete transitive runtime attestation. Node.js is required (tested v24.19.0). Python validation reports missing runtime/timeouts as source-stage failures. Native checks run fresh, not from a cached success receipt.

## Exact projection contract

| Native input | RDF output |
|---|---|
| Each `bodies` entry: species and cell ID | One nominal Proton, Neutron or Electron record, with the source cell ID in its generated IRI; nucleus/electronic inventory membership follows the declared species. |
| Each packet: ID, origin, chart | ReaderState with typed native ID/origin and the chart's explicit ID. Numeric chart index `c` resolves the native `chart-c` record. Origin is a native index, not physical time. |
| Chart's occupied cell | ReaderState's `readerBody` link to that declared constituent. |
| Each reader/body assignment | Explicit Interpretation binding that constituent to the reader-state role. All constituents have bindings. |
| Each retained operation: ID, source, target, kind, phaseDelta | ReaderTransition with typed ID/delta, kind string, and explicit fromReader/toReader links. |

The output has **68 states, 94 transitions and 32 bodies**. Constructor replay checks **67 construction steps and 37 occupied-face contacts**. The RDF graph has **1,690 triples**. Inventory readouts are Z=10, N=12, A=22, electrons=10, charge_e=0, computed after full validation.

Permutations, geometry, construction prefixes and inspection payloads remain in the pinned input and are checked by native replay, but are not projected into this incidence view. No reader state is treated as a spatial vertex, no transition is assigned a red/green/blue color, and no shell, boundary or filling declaration is invented.

The root is `PartialStructureProfile` with `TotalBindings`. Reader roles satisfy partial-profile coverage, but **cannot replace spatial roles for CompleteStructureProfile coverage**. Inventory-only profiles reject reader members. Reader endpoints and body links must belong to their root, and reader types participate in the same explicit/exclusive record classification guard as other types.

`build_native` constructs a candidate graph; serialization alone is not verification. The integrated checker verifies pins, repeats native replay, and compares every outgoing triple in the expected/source-owned output, including metadata. The CLI validates before emitting Turtle:

```sh
uv run --python 3.12 --with pyshacl==0.30.1 --with rdflib==7.1.4 python research/strominger/isotope-schema/check.py --import-native-reader
```

## Evidence and limits

- `results/native-constructor-replay.json`: fresh native replay, input/code digests, runtime and counts.
- `results/native-ne22-readers.ttl`: generated typed reader/body incidence.
- `results/native-ne22-source-replay.json`: integrated per-root source evidence and exact projection replay.
- `native_replay_tests.py`: changed native transition refusal, changed RDF payload refusal, dependency-pin failure, membership/type separation, profile-promotion failures, spatial binding protection, roundtrip/readout/CLI checks, and independent direct source-row comparisons for every state and transition. These source-row oracles do not call the projection builder to compute their expected values.

Integral JSON numeric spellings (such as `0` and `0.0`) normalize to the same typed IDs and projection payload, but retain different input artifact pins. A constructor-plus-projection control checks this boundary.

A cross-runtime encoding control also verifies that invalid UTF-8 in ignored metadata cannot crash validation after Node's permissive decoding: the projection rejects it with `invalid-native-json`.

Fresh suite: **212/212 passing**. This repairs the native-source replay/import gap for the explicit finite-reader operation. It does not derive the existing Ne-20 drawing, produce a complete native spatial diagram, certify physical truth, or prove arbitrary witness declarations. The audit and tests are self-authored, not an external reviewer signoff. Native source files, drawings and the pre-existing native replay receipt are not rewritten.
