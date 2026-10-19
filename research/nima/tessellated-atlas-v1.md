# Tessellated, obligation-directed atlas — side-by-side implementation

The new generator is implemented in `tessellated-atlas.mjs`. The existing generator, native rules, path catalog, archived graphs and scientific receipts are unchanged. This is a forward-realization refactor, not adoption of the unproved common-T tiling or a field-sewing rule.

## Architecture

- **Geometry:** native primitive cells, marked vertices, faces and occupied-body contact incidence. No periodic-origin quotient or progression-rank pruning.
- **Readers:** separate packet records retaining body, species chart, full aliases, absolute origin and five-coordinate map. Several readers can share a body.
- **Interfaces:** native factors and terminal-PE factors compiled directly from the source universe. PE guards refer to whole-body vacancy and selected native successors. No saved atlas or catalog membership enters compilation/generation.
- **Obligations:** root reachability, exit reachability and missing native face witnesses are explicit. Missing face/exit obligations prioritize the frontier but do not prune potentially completable states. Exhaustive exploratory additions remain necessary for complete-family generation.
- **Atomic materialization:** a separate audited planner operation adds all active PE intermediate readers for one reference body together. Immediate noncertified results remain pending obligations, not admitted certificate-to-certificate macros.
- **Contact closure:** branch on actual native witness factors for a missing face, then use bounded source search for remaining entry/exit obligations. This replaces fixed D2 packet templates. Required-set search states are not claimed to be rooted execution prefixes. Returned certificates need a separate schedule or explicit atomic interpretation; unsat outcomes do not yet serialize a complete new proof tree.
- **Field boundary:** explicitly unbound and excluded from admission. Strominger's field candidate has not been made an occupancy or contact permission.

The full labelled graph retains alternative routes and revisits; selected-set deduplication does not assert equality of their path histories. Each node also keeps a representative construction parent and interface.

## API

```js
import {
  compileTessellatedAtlas, generateTessellatedAtlas,
  materializeBody, closeContactObligations
} from './tessellated-atlas.mjs';

const model = compileTessellatedAtlas({maxOrigin: 2});
const atlas = generateTessellatedAtlas(model, {maxConfigurations: 1000000});
const obligations = model.obligations(model.mask(selectedPacketIds));
const candidates = materializeBody(model, selectedPacketIds);
const closure = closeContactObligations(model, selectedPacketIds, {
  maxNodes: 5000, maxMilliseconds: 5000
});
```

The compiler also supports `mode: 'native'`. Experimental materialization/closure APIs reject native mode. Configuration and search stops return explicit incomplete outcomes. The source universe remains finite and origin-bounded.

## CLI

```sh
node research/nima/generate-tessellated-atlas.mjs --max-origin 2
node research/nima/generate-tessellated-atlas.mjs --max-origin 1 --graph tmp/tessellated-D1.jsonl.gz
node research/nima/checkers/check_tessellated_atlas.mjs
```

The optional gzip JSONL export includes geometry, complete reader records, interface guards/factors, node obligations, all available singleton-labelled edges and a completeness footer. Atomic macros are separate planner operations, not silently inserted into that singleton graph. A configuration-limited run writes an incomplete footer and exits2; argument/runtime errors exit1.

## Verification

Generation precedes reading the comparison atlas. The fresh regression checks:

| Check | Result |
|---|---|
| D2 selected states | exactly243,034 |
| D2 exit certificates | exactly698 |
| D2 labelled transitions, including revisits | exactly7,018,785 |
| State masks and active interface sets | exact archived-family agreement |
| Materialization candidates |265 |
| Fully certified macro edges | exactly the previous195 |
| Target-specific reachability with those macros | all216,531 pairs reachable;0 blocked |
| Rejected immediate materializations | all70 repaired by interface-driven closure |
| D3 seed generalization | all8 previous repaired-core witnesses rechecked |
| D3 materialization probes |5 body candidates, all yield certified results |
| Controls | native-mode misuse, foreign packet, configuration stop and closure stop rejected/reported |

The D3 result is a targeted probe, not a complete D3 atlas. No field-coherence claim follows. Small native-mode generations are source-audited separately.

CLI smoke checks also round-tripped complete D1 (136 states/1,368 labelled edges) and a configuration-limited D0 archive, checking footer counts and the incomplete exit code.

[Regression receipt](results/tessellated-atlas/verification.json) · [SCC declaration](scc-models/tessellated-obligation-atlas.json)

## Remaining work

Keep the old generator as the regression oracle until broader adoption is requested. Next strengthen closure proof/schedule output, including atomic body operations in an explicit execution plan. Field attachments and incidental-contact sewing remain a separate downstream layer with their own admission tests.
