# Retained fibration diagram debugger

## Run

From the repository root:

```sh
node scripts/audit-fibration-diagram.mjs
node --test tests/retained-diagram-audit.test.mjs tests/fibration-evidence.test.mjs tests/marked-table-diagram.test.mjs tests/belt-fibration-diagram.test.mjs tests/native-marked-table-bridge.test.mjs tests/native-window-star-binding.test.mjs tests/native-window-transport.test.mjs
```

Node and Python are required (`PYTHON` can override the interpreter). All generated evidence is isolated under `results/fibration-diagram-audit/`; historical receipts are not overwritten. The current regression suite has 31 passing tests.

## Architecture

Native payloads stay with their owning implementations. A small evidence envelope records adapter identity, exact input/output boundary fingerprints, claim, checks, explicit premises and evidence dependencies. It does not translate every packet into one scalar or universal schema.

Registered carrier signatures currently cover:

- `native-channel`: retained channel → native retained diagram;
- `native-field-sewing`: native diagram → full44 sewn section;
- `marked-table`: marked table ↔ marked source fibers;
- `native-table-bridge`: native diagram ↔ marked table, with a separately checked retained-context port;
- `native-window-stars`: native diagram → source-bound ordered-window/star annotations (not a field transport operator);
- `native-window-transport`: native diagram → exact five-coefficient window/complement transport audit, referencing the prior full44 sewing.

Evidence dependencies form a checked DAG. Explicit boundary links separately state which outputs feed which inputs; array order does not turn the diagram into a single route. Composing linked outputs requires both carrier agreement and exact state fingerprint agreement. A genuinely equivalent but differently represented boundary needs an explicit comparison adapter rather than a silent coercion.

Premises propagate through composition. Remaining assumptions yield `verified-conditionally`; missing premises yield `incomplete`; failed checks, incompatible boundaries, missing/cyclic evidence, unsupported adapters and conflicting premise definitions yield `rejected`. An empty collection cannot obtain a vacuous success.

**Trust boundary:** evidence envelopes are outputs of the registered executable adapters/checkers, not proof certificates accepted from arbitrary JSON. A content hash identifies a boundary; it is not a mathematical proof. Registering new adapter names alone cannot verify their claims.

## Positive diagram 1: actual native assembly and exact field sewing

The runner checks source-fixture freshness, encodes its 23-record stream, and reconstructs the whole with the existing native decoder. The decoder receives records, not completed charts, carriers or readout tables. An independent semantic comparison checks the reconstructed assembly against the existing fixture.

All 14 packets and 18 interfaces are checked, including four incidental interfaces outside both generating histories. Native fixture validation now reports nested malformed records by field path rather than letting them fall through to ordinary exceptions. Checks retain native root, charts, carriers, packet records, histories, comparisons and reconstruction metadata.

The unchanged field mathematics is replayed through the exact multiradical sewing checker: native coefficient composition, full44 field/readout squares, full-five recovery, distinct histories, metric factors and rank2/rank3 exits. Its existing scope assumptions are structured premises of the resulting evidence composition. Only assertion messages were added to the source checker, naming the affected interface and equation.

A hostile test swaps two slots on an incidental interface while preserving both generating histories and their operations. The adapter diagnoses the exact failed coefficient square; the independent exact checker rejects the same interface. Missing an interface is separately classified as a missing witness, not an equation failure.

## Positive diagram 2: marked-table regrouping and retained context

`marked-table-diagram.mjs` implements the prior source-group/reversed-unpack cycle with explicit carriers, selector, complete row payloads and history:

`table → marked source fibers → transposed table → marked source fibers → original table data`.

The final table data recover, while the operation history grows by four records. Repeated row labels do not merge rows; empty fibers remain represented. Endpoint uniqueness is a declared finite-adapter premise, not a restriction claimed for the generic HoTT recovery theorem.

The runner independently executes the actual finite reference functions from `research/nima/checkers/check_table_fibration.py` on all 147 cases. It extracts their unchanged function definitions via Python AST, avoiding the historical checker's report-writing top level. The JS adapter must agree on source fibers, two-step transposition and four-step recovery. Source hashes identify the executed reference. **This is fresh finite reference execution, not a fresh Agda compiler closure.**

The noninvertible-key-projection control uses two tables with the same displayed keys but different retained payloads. Keys alone cannot recover the input; the retained fiber context does. This keeps the architecture from assuming every displayed projection must have an inverse. No claim is made that ordinary regrouping derives the chosen reversed wiring convention.

## Connected positive example: native → table → native → full-field sewing

`native-marked-table-bridge.mjs` now connects the two previously separate positive adapters. All 18 actual native interfaces become table rows; all 14 packet identities are retained endpoint carriers. Operation kinds are nonunique row labels, while operation identities and original ordering remain explicit. Packet, chart, carrier, history and comparison data travel in an attached native-context record; there is no hidden duplicate operation list in that record.

After the four-step marked cycle, reconstruction recovers the complete native fixture exactly, including all incidental interfaces. Presentation history grows separately from the unchanged native execution histories. The existing exact sewing checker is freshly rerun on the recovered fixture; all interface results, packet bindings and exit splits agree with the original exact run.

The composed evidence diagram connects native assembly, table encoding, four presentation steps, native recovery and full-field sewing. It also checks an explicit side-context edge between encoding and recovery. Changing or deleting that context cannot be hidden by matching the visible table boundary.

A hostile test attempts to read the two-step transposed table as executed native transport. It fails native carrier typing: table endpoint reversal is NOT automatically a physical inverse operation. Other controls preserve table shape while corrupting an incidental coefficient map, erase histories, inject hidden endpoint fields, or duplicate operation-order metadata.

Boundary fingerprints now sort object keys recursively while preserving array order. Non-JSON values are rejected instead of being silently dropped by serialization.

This bridge presents the bounded native diagram; it does not generate it from an unprovided source and does not identify its 14 packet-source fibers with the four L1 stars. That specific four-context/window and geometric attachment remains open. No 18-to-12 or 14-to-4 reduction is imposed by counting.

## Native three-plus-context window binding

`native-window-star-binding.mjs` now reads the existing species-specific `windowProtocol`, actual chart aliases and carrier faces for every reconstructed packet. The four source vertices are no longer anonymous four-element labels: they are the packet's actual marked native vertices. Its twelve directed relations receive candidate satellite addresses on either L1 layout, and the protocol's continuation mark identifies the selected centre/context. The selected satellites retain the actual ordered three-mark window; their displayed arm order is not silently substituted for native window orientation.

All 14 packets pass this annotation on both layouts. Each supplies exactly one selected native window and three alternative geometric context faces. The alternatives are not promoted to certified operations or full-field readouts. The same carrier is also compared in fixed geometric coordinates: in the bounded root-carrier histories, the selected context visits two vertices (indices 1 and 3 of the initial frame), not all four. This is a property of the inspected fixture, not a no-go theorem for other native histories.

All five coefficient slots, packet origin, chart and history positions remain referenced. Electron context M2 remains a geometric context; it is not invented as an additional coefficient slot. Equal-looking packet views do not merge the two retained histories. All 24 local mark orders preserve the selected actual face/context when the mapping and native order travel with them.

This is a concrete source-bound window annotation, not yet a full four-star field adapter. A common four-context interpretation across changing carriers, native readouts for the other contexts, and attachment to the actual ESD7 parents remain explicit obligations. No parent links or viewer geometry were changed.

## Carrier changes require retained data beyond the displayed window

`native-window-transport.mjs` now reuses the actual `activePhaseSlots`, `phaseFrame` and `applyPhasePermutation` from the prior native phase-advance implementation. It encodes three active complex coefficients plus both complementary coefficients, the actual occurrence/context frame and a reference to the sewn full44 root/frame. This is not a new field law or a materialization of all 44 field coordinates.

All 18 interfaces pass transport/recovery, root-coefficient readout squares and inverse recovery on the five-slot basis plus a complex-valued probe (108 cases). Projection-only controls expose specific dependencies:

- Six reader-phase interfaces cannot transport the active triple alone; a retained complementary coefficient enters the next active window.
- Ten PN/inverse-PN interfaces cannot transport a literal four-mark/four-coefficient subset. PN needs source C2 (slot 4); inverse-PN needs source C0 (slot 0), outside the respective four-node carrier presentation.
- The two NE interfaces introduce geometric context M2, which has no independent slot in the native five-coefficient reference. It is not silently invented as a sixth coefficient.

Every failed projection has an explicit pair of full inputs with identical reduced source views but different reduced target views. These are failures of the proposed truncations, not failures of the retained native transport. Restoring the full five coefficients passes throughout.

Thus a four-arrow star cannot be read as four independent scalar coefficients in this native model. A valid packet view retains the complement behind the display. The three-active-plus-two-complement coordinate split is NOT identified with the separate rank-two electron/rank-three baryon Gram-projector decomposition. Arrow flux weights and coefficient dimensions likewise remain different quantities.

This settles a concrete transport-data requirement; it does not yet establish native readouts for all four alternative star contexts or a fixed global four-star frame across changing carriers. Those remain explicit obligations before parent attachment.

## Full-field observation falsification

The exact sewing checker now exhibits a unit-norm full44 root field (coordinate 36) whose five native observations vanish at every retained packet. `R0 B0 = I5` gives native readout rank five, and `R_h U_h = Pi_h R0` shows that all transported observations have the same 39-dimensional blind complement. This refutes readout-only recovery of arbitrary full44 input under the fixed candidate, not recovery of the prepared five-dimensional subspace or a richer retained interface. The declared restricted target is `inputs/fibration-falsification-target-v1.json`; the broader construction, stage count and existence conjecture remain open.

## Actual belt extraction, not fourteen placeholder edges

`belt-fibration-diagram.mjs` extracts directly from the live model and owner-face inventory:

- 64 actual arrow nodes plus two same-sign N terminal bundles;
- all 106 directed links (74 internal, 32 terminal), retaining endpoint identities and wiring rules;
- two retained parent occurrence fibers, at original +N and clone −N;
- 32 explicit boundary demands, now graph-attached to the terminals.

Each real link lacks a native field adapter; each node lacks a full native packet binding. Parent demands have declared terminal graph connections, while both native terminal-field fibrations remain unbound. The prior 49-face assignment was superseded by the operator's N-sector terminal choice; see `belt-N-terminal-wiring.md`. The diagnosis retains these actual identities and does not collapse a layer gap to one fictitious field operator.

`inputs/parent-belt-fibration-question.json` is kept separately as the authored macro-level question: what retained presentation does each stage mean, and what endpoint change is intended? Its earlier 29-item count was a checklist count, not a discovered structural obstruction. The receipt now separates that question from the extracted atomic graph and its obligations.

Missing bindings are not failed equations or a no-go theorem. Neither geometry nor scalar flux balance supplies an unprovided native interface map. Incidental full-field comparisons for a future belt interpretation must also be extracted and verified once those native bindings exist.

## Results and limits

`verification.json` records fresh stages, structured evidence compositions, source hashes and artifact references. `milestone-passed` means the two bounded positive adapters pass, hostile controls reject, and the unbound belt remains incomplete. It does **not** mean the parent–belt fibration is established.

The exact native result remains conditional on the prior PN completion, joint NE exchange, co-moving ordered-corner N/NN convention and transported bindings. No native map was refitted. Marked-table recovery has a different carrier and uses retained context rather than inheriting those metric assumptions.

This is still a bounded composition tool, not a universal proof checker or automatic route synthesizer. Native fixture cardinalities remain specific inside the historical sewing checker. The next extension should supply one genuine source-backed boundary comparison/adapter, rather than guess maps, reinterpret counts or broaden search before verified interfaces can compose.

The debugger does not change viewer geometry or wiring. The separately requested same-sign N terminal graph attachments are now included in its extracted input; full native maps remain explicit obligations.
