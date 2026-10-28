# Su-32: first Hopf correspondence tests

## Question and claim boundary

Can the circle-join construction, retained spinor geometry and simplicial comparison model describe the same Su-32 wiring?

The operator requested execution of the revised test plan. This packet delivers the shared fixture, correspondence table, fresh reference replays and first discriminating incidence test. It does not yet construct the global adapter. SCC obligation: **route/coherencer compatibility**, with unresolved upstream attachment transport. The nonzero-contrast chart and zero-contrast stratum are separate.

The standing global-construction rule changes the earlier plan's order: specify one assignment over the whole carrier, its six overlapping cones and boundary, then test restrictions. One cone may be a diagnostic, not a construction seed from which to grow the object.

## Fixture verified against the recorded Su-32 specification

Source: [Sulfur-32 reversible channel specification](sulfur-32-reversible-channel-specification.md), not a new isotope identification.

`buildPESymmetricSector(1)` yields edge units three, 51 cells (16 P, 19 N, 16 E), 104 shared interfaces and 72 boundary faces. The six incoming tips match the six source cell IDs, and inversion verifies all three specified opposite-tip pairs. Grouping those pairs gives 16 N-channel identities without deleting cells.

Each of six readings has layer populations `1,4,4,12,9,12,4,4,1`. Each contains six 14-cell cones with 16 presentations and 20 moves. Deduplicating their cell identities across all readings gives six stars, not 36 independent objects. The receipt retains every cone path, move, integer sphere sweep, pairwise shared-cell set, entry comparison and outer branch. Missing operation maps remain null.

Four hostile mutations are rejected: duplicate reference-product member, deleted comparison edge, wrong shared reference, and deleted incoming interfaces. The audit additionally rejects stale source hashes and insertion of an unsupported identity operation map.

## Correspondence table

The machine-readable table is [`contracts/su32-hopf-correspondence-v1.json`](contracts/su32-hopf-correspondence-v1.json).

| Su-32 object | Candidate description | Tested result | First missing map |
|---|---|---|---|
| Four layer-3 pairings, four layer-4 comparisons | Circle realization, then two-circle join | Their comparison graph is one C4; the two comparison kinds are disjoint-edge matchings | Native retained data to two torsor coordinates and a join weight, with a diagonal action |
| Five-slot coefficient candidate | Two spinor contrasts plus three context coordinates | Exact NE intertwiner and full NN update replayed; contrast-only NN fails | Operator signed P/E records to the five-slot packet |
| Six cones of presentation comparisons | Free simplicial-group model | Native boundaries retained; reference face/degeneracy and primitive-detector checks replayed | Face-compatible map from native boundaries to that model |
| Native direction spheres / internal state base | Circle bundle over S2 | Sphere sweeps retained, but no native clutching function computed | Base identification and source-derived chart transitions |
| Shared cells, outer branches, entry/exit | One global retained object | Complete incidence retained | Simultaneous transition, operation and boundary assignment |
| Reconciliation | Cofiber attachment or higher comparison | Deferred | Identified primary boundary map and reconciliation target |

### New join constraint

For every entry reading, the four central comparison cells give exactly the four edges of a connected square on the joint N occurrences. Comparisons at fixed E give one matching; comparisons at fixed P give the other. Neither matching is a circle. Their union is a single cycle of rank one.

Therefore the two reference families are not already the two circle factors of `T*T`. The prior torsor construction can start from the square after its specified realization, but the native justification for joining two torsor instances is still needed. Choosing a second reading does not automatically supply an independent factor. This rejects that immediate identification, not a global join construction.

### Reproduced transport constraint

The exact native five-slot NN permutation sends `(0,0,0,0,1)`, whose incoming contrast is zero, to contrast `(-1/sqrt(2),1/sqrt(6))` of norm squared `2/3`. Zero input stays zero. Thus no deterministic contrast-only update can reproduce both inputs on this domain. The full five-coordinate update retains the distinction.

NE does descend to a unitary contrast map with determinant minus one. Its paired-frame determinant correction must be retained; multiplying by i to force SU(2) would alter the supplied phase.

These statements apply to the existing conditional window-to-sector encoding. They do not yet identify that encoding with the signed input wire.

## Fresh replays

| Checker | Result |
|---|---|
| `check_wg_circle_torsor.py` | 53,205 exact assertions passed |
| `check_simplicial_source.py` | 24,246 assertions passed; simplicial generator tests through degree 12 |
| Retained spinor dual-line trial | 56 record round trips, 112 phase checks, 672 binary-action equivariance checks passed; source stores unchanged |
| Native dual-line/context adapter | NE alignment and full-context NN transport passed; fixed two-channel NN rejected |
| Berry domain cut | 14 symbolic fields recovered through four decorated charts; connection, winding and annular twist checks passed |
| New fixture and SCC audit | Passed; manifest validation passed |

The original spinor producer was not run: its source functions were replayed read-only by the existing dual-line checker. The all-degree simplicial and universal-bundle conclusions still use the written proofs; finite checker counts do not replace them. No Agda/Lean replay occurred.

SCC's repository-wide `models` and `dashboard` commands returned exit one while listing other models; the scoped model check and path-based validation passed. An initial validation invocation using the model ID rather than the manifest path failed lookup and was corrected.

## Disposition and next construction

The governing conjecture remains: one globally retained Su-32 object admits compatible join, spinor and comparison-history descriptions. The tested rivals are (1) treating the two reference families as two circles, and (2) discarding context for spinor-only NN transport. Both immediate reductions fail their stated tests. The global conjecture has not been tested by those failures alone.

Next, work on the **signed-record encoder and joint phase action over the full carrier**. Require recovery of independent records, a definition at zero contrast, and simultaneous overlap constraints from the fixture. If this supplies two phase torsors and a weight, test the join adapter; if it supplies a spinor/context packet, test the existing exact native intertwiners. Do not insert a second phase, a chosen transition winding or an identity comparison to make the models agree.

The history adapter is deferred at its first missing typed map. Cofiber and eta-squared tests follow only after that map identifies a primary class.

## Reproduce

Run from the repository root, through the admitted structured-command surface:

```sh
node research/strominger/checkers/check_su32_hopf_fixture.mjs --record
python research/chatgpt/20261019/check_wg_circle_torsor.py --output research/strominger/results/su32-hopf-tests-v1/circle-join.json
python research/chatgpt/20261019/check_simplicial_source.py --output research/strominger/results/su32-hopf-tests-v1/simplicial-source.json
uv run --with sympy python research/strominger/checkers/check_berry_connection_domain_cut.py
python research/aspect/scc/scc.py validate research/strominger/scc-models/su32-hopf-correspondence-v1.json
python research/aspect/scc/scc.py check su32-hopf-correspondence-v1
```

Graph report to marici.Voevodsky admitted as proposal `ep_5c198eba-f76c-4de0-940c-cd1b004e4f46` at ledger head `e15acbd2c91f971decdd25933fca45084d7add03b1101aae88763efc11cdab69`. The five new source/contract/packet files are untracked; no commit or push was requested or performed. Generated receipts reside in the owner results directory and were not listed as untracked by the scoped Git status.

The SCC checker replays both read-only spinor/context adapters and writes their receipts alongside `fixture.json`, `circle-join.json`, `simplicial-source.json`, `berry-reference.json` and `verification.json` in `results/su32-hopf-tests-v1/`.

Structured executions: fixture final `e_29164_1793121024080406800_10`; circle join `e_29164_1793120943174576200_5`; simplicial source `e_29164_1793120943442080800_6`; Berry `e_29164_1793121023728178800_9`; SCC audit producer output `mcp_output:o_29164_1793121134819735300_12`; manifest validation `e_29164_1793121144073882500_14`.
