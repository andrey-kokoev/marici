# One source-bound chart: candidate witness comparison, native release still unbound

## Question

For `reading:0:-1`, incoming `neutron:0,0,2,1`, binding `[0,0]`, do the actual constructors supply two native release orders and a retained comparison?

## Executed construction

The local repository contains the specification and implementations unavailable to the external audits. The checker directly imports:

- `su32-signed-reference-encoder.mjs`;
- `su32-layer4-comparison.mjs`;
- `../realization-tower/five-side-oct-routing-obligations.mjs`;
- `../realization-tower/sulfur-32-wiring.mjs`.

The fixed chart's four pair occurrences are:

| Pair | Actual N occurrence |
|---|---|
| P+, E+ | `neutron:0,1,1,1` |
| P-, E+ | `neutron:0,1,2,0` |
| P+, E- | `neutron:1,0,1,1` |
| P-, E- | `neutron:1,0,2,0` |

`reconcileBothOrders` constructs two trees ending at `neutron:1,1,1,0`. Each has the same four complete channel witnesses as leaves, grouped by shared E or shared P. This common family is verified from the returned objects, not assumed from their support labels.

The checker derives `alpha` by matching each complete leaf with its occurrence in the other tree, and derives `beta` in reverse. Both composites preserve every leaf position and witness. Leaf readers agree; both complete readers recover the original four-record registry. Both intermediate trees remain retained and distinct. A leaf with unchanged occurrence identity but changed payload is rejected.

Thus the external note's conditional comparison formula **does apply to this implemented candidate**, including its retained leaf witnesses. It does not identify the two whole construction histories or supply their native admission.

## The input context cannot be omitted

`compareAt` consumes **two channel operands**; it is not a unary transition from one pair record to another. `reconcileBothOrders` obtains all four channel operands from the complete input registry.

Changing only the P- record leaves the P+, E+ starting operand unchanged but changes the comparison at shared E+. The receipt retains both inputs and both different joins. A deterministic release that returns this particular populated family therefore needs the additional registry context; it cannot be inferred from that pair operand alone. This does not exclude contextual release or a family of unspecified completions.

## Why the proposed port-path test is not yet applicable

The checker separately extracts the two cell-incidence walks from P+, E+ to P-, E-. These are **sign-variation walks**, not the reconciliation trees that retain all four possibilities.

Each walk passes through two charged comparison cells. At every such cell, the entering and exiting faces have different coordinate axes and belong to different native wires. The existing wire graph contains no internal edge between those charged ports. Moreover, the two extracted walks use different initial ports and different final ports, despite sharing the initial and final N cells.

Consequently there are no two supplied parallel native port paths on which to evaluate the proposed deck discrepancy. The result records `deckDiscrepancy: null`, not zero or a fabricated nonzero obstruction. A multiwire or family-valued native release could have a different endpoint type; this test does not exclude it.

## First missing source object and stopping condition

The actual obligation builder returns `comparisonWitness: null` and `outputPairing: null` at all four selected comparison sites. The candidate reconciliation returns `nativeFiller: null`. Its reader agreement is executable; native reader/continuation compatibility is not supplied.

The missing object is a **source-admitted contextual release constructor on the complete signed preparation**, with its complete outputs, histories and occurrence maps. Once supplied, execute its two orders on this chart and derive the appropriate reader- and continuation-compatible comparison. A voltage-graph test is appropriate only if that constructor supplies actual port paths.

This branch stops here rather than inventing release semantics, a charged-cell transfer, or a higher filler. This is a bounded audit of the named source chain, not a repository-wide nonexistence claim.

## Reproduction

```sh
node research/strominger/checkers/check_su32_release_source_audit.mjs
python research/aspect/scc/scc.py check strominger-su32-release-source-audit-v1
```

Receipt: `results/su32-release-source-audit-v1/verification.json`. It retains both complete trees, the witness bijection and inverse, the contextual-input counterexample, native null obligations, actual interface ports and all four missing charged transfers. Source hashes are checked and recorded. `nativeReleaseExecuted` remains false; no source implementation or external audit was modified, and no proof assistant was run.
