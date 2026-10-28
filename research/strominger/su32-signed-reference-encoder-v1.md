# Su-32 signed-reference encoder: occurrence and phase tests

## Question and frozen test

Construct a lossless reference representation of the operator's four signed records over the already verified Su-32 comparison fixture. Test whether a single binary direction label on each charged cell can support every cone and reading. Then test whether reference incidence selects a common U(1) action.

SCC obligation: attachment transport before route/coherencer compatibility. This is a representation of restrictions of a prospective global object, not construction of wiring by local execution.

Conjecture under test: the signed input can be retained once, with the four pairings represented as references; signs may be static cell attributes and incidence may select their phase law. Rivals: signs belong to reading occurrences; independent phase actions preserve the same incidence. Discriminators: odd-cycle obstruction to global binary cell labels; exact reconstruction and tamper tests; two distinct phase actions satisfying the same reference equations.

The payload type initially is arbitrary JSON data, not a complex amplitude. A four-amplitude fixture will be used only to discriminate proposed phase laws. No amplitude, twist or physical operation is inferred from a direction sign.

## Implemented encoder

`su32-signed-reference-encoder.mjs` constructs 36 charts (six cones in each of six readings) from actual cone paths. Each chart has two P references, two E references, their four joint N occurrences and the four shared-reference comparison locations. It retains all four possible bijections of the two role-specific references with +/−. Lexical ordering enumerates these alternatives; it does not select an orientation.

`encodeSignedReferences(atlas, chartId, binding, records)` stores one registry with keys `P+`, `P-`, `E+`, `E-`. Each channel stores only the two record references and their native reference-cell IDs. Comparison locations retain their shared-record reference. `decodeSignedReferences` checks the packet against the native chart and recovers the registry. Equal payload values do not merge distinct record identities.

The API accepts arbitrary JSON payloads and does not manufacture independent copies of shared inputs. Serialized JSON necessarily represents the registry, but channels do not contain duplicate payload fields. Consistency validation is not authentication: replacing the entire registry with another valid registry represents another input.

The 144 chart/binding choices are alternatives, not a simultaneous global record assignment. The code supplies no channel continuation, physical coefficient encoding or reconciliation operation.

## Test results

Fresh execution passed:

- 432 serialization/reconstruction round trips: arbitrary structured data, equal-valued distinct records and a declared complex-amplitude fixture, in all 144 chart/binding choices;
- 2,304 exact common-phase composition checks using Gaussian-integer amplitudes and phases 1, i, −1, −i;
- six hostile mutations: missing record, wrong channel reference, missing comparison, invented reconciliation, payload inserted into a channel, and wrong occurrence chart;
- source-hash checks against the prior Su-32 fixture;
- SCC manifest validation and fresh checker execution.

### Static cell signs: local solutions do not combine

Declare the tested extension precisely: apply the two-P/two-E opposite-sign entrance template to **every cone in every reading**, and require a charged cell to keep one binary sign independent of its occurrence. This is a uniform-cone hypothesis, not an extra requirement retroactively attributed to the operator's three-layer entry instruction.

For each star and each role, the six readings select all six pairs of its four same-role cells. A static binary labelling would have to assign opposite signs on every edge of K4. Its triangles forbid this. The checker exhausts all 16 assignments on each four-cell set: zero satisfy the six constraints, for both roles at all six stars.

Two controls localize the obstruction:

1. Restrict to the six actual carrier-entry cones: consistent binary cell assignments exist.
2. Restrict to all six cones in any one reading: consistent assignments exist for both roles, for every reading.

The failure is simultaneous, reading-independent labelling across the uniform-cone extension. The encoder therefore retains chart and binding explicitly. This is a finite sign-consistency obstruction, not a Chern class or proof of a double twist.

### Incidence leaves phase action undetermined

For a record registry R and a channel reference r, lookup satisfies

    lookup_r(map(f, R)) = f_r(lookup_r(R)).

Consequently any separately specified per-record payload maps commute with this reference representation. Taking every f_r to be multiplication by the same phase is allowed; taking different phases on different records is also allowed. Reference incidence alone distinguishes neither choice.

An exact witness uses P+=(1,0) and E+=(2,1) as complex coordinates. The relative product `conj(P+) E+` is `2+i`. Multiplying all records by i preserves it. Multiplying only E+ by i gives `-1+2i`. Both operations preserve all record norms and the same native reference skeleton. This is a discriminating amplitude fixture, not an assertion that the operator's records already carry these complex coordinates.

Even choosing the diagonal action on four independently supplied complex amplitudes does not compress them into a two-component spinor: at fixed nonzero total norm its quotient is CP3, whereas the two-component Hopf quotient is CP1. A source relation, additional retained context, or different payload type is required for that reduction.

## Disposition

The lossless signed-reference representation survives. Static cell signs fail only at the specified simultaneous extension; incidence-selection of the common phase law fails because the independent-phase rival satisfies the same reference equations.

The first missing object is now an **operation on the retained signed records**, with its occurrence domain and comparison law, that selects their coefficient encoding and phase action. Neither the reference square nor the cell-sign obstruction supplies that operation. Reconciliation and global signed-record assignment remain null in the receipt. This branch stops at that missing operation rather than selecting a phase law by convention.

## Replay and artifacts

```sh
node research/strominger/checkers/check_su32_signed_reference_encoder.mjs --record
python research/aspect/scc/scc.py validate research/strominger/scc-models/su32-signed-reference-encoder-v1.json
python research/aspect/scc/scc.py check su32-signed-reference-encoder-v1
```

The Python SCC entrypoint launches the Node checker afresh, without a shell. Receipt: `results/su32-signed-reference-encoder-v1/verification.json`. It includes all 36 charts, per-star K4 witnesses, graph edges with source occurrences, satisfying assignments for both controls, source hashes and explicit null global/phase bindings.

Initial execution: `structured_command_execution:e_29164_1793121547846523100_16`. Final SCC replay includes the added entry-only and single-reading controls: producer output `mcp_output:o_29164_1793121686512366000_19`. Manifest validation: `structured_command_execution:e_29164_1793121685716041200_17`. No existing routing or rendering implementation was changed.

Report to marici.Nima admitted as proposal `ep_5048a7f1-0a6e-48fc-af0c-7ddfe4b3380a`, ledger head `122255d50be4bcb69910ab58d5ae9f1ccf32150d236675a80eccfcf032d40c01`. The five new implementation/checker/manifest/packet files remain untracked; no commit or push was performed.
