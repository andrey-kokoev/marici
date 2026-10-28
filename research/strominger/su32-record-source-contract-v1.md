# Source meaning of the four directional records

## Finding

The supplied source defines **four occurrence-relative record identities and their geometric references**, but not four numerical or physical observables.

Record contents enter as caller-supplied data. No native-state-to-payload assignment was found in the audited producer contracts. Consequently, physical admissibility and physical/statistical independence cannot currently be inferred from these APIs.

This does not block parametric wiring or retention results: those can deliberately treat wire contents as opaque. It blocks promoting those results into a particular numerical encoding or physical dynamics without an additional source-supported state interpretation.

## Fixed occurrence and binding

The audit fixes `reading:0:-1`, the entry at `neutron:0,0,2,1`, the central target `neutron:1,1,1,0`, and binding `[0,0]` before checking values.

The native reference assignment is:

| Record identity | Reference cell |
|---|---|
| P+ | `proton:0,0,1,1` |
| P- | `proton:0,0,2,0` |
| E+ | `electron:-1,0,1,0` |
| E- | `electron:0,-1,1,0` |

These signs are local directional labels under the supplied binding. They are not inferred charges, amplitudes, or global scalar labels attached permanently to cells.

## Producer trace

- **Operator specification:** defines directional pairings and shared-reference incidence. It explicitly does not assign charge/amplitude meanings or wire-content transformations. It also does not identify periodic coordinate-axis wire slots with the four directional pairings by count alone.
- **`buildSu32SignedReferenceAtlas`:** derives reference cells and comparison incidence from the fixture. It does not compute payload values.
- **`encodeSignedReferences`:** requires a caller-provided `records` argument under the exact four labels. It attaches those values to the chosen occurrence references.
- **`channelOperand`:** receives a registry and copies the relevant records. Comparison/reconciliation checks repeated-record agreement and retains histories; it is not a native measurement function.
- **Periodic wire API:** accepts a complete externally supplied 64-wire row assignment and regroups it. No source binding from those coordinate-axis slots to these four signed records is supplied.
- **Earlier amplitude-shaped tests:** their own receipt explicitly calls the numerical pairs test fixtures and leaves the source-selected action null. They do not supply a missing physical interpretation.

The consumer search for the signed encoder found the comparison adapter and its checkers, not a producer deriving these four payloads from a native physical state. This is a bounded source audit, not proof that no possible such producer could be defined.

## Admissibility and independence

For the fixed occurrence and binding, all **16 Boolean assignments** are accepted. All **64 one-record flips** preserve the incidence/reference skeleton and successfully reconstruct both reconciliation routes. Mixed JSON-valued assignments and equal-content records are also accepted.

Each record has two channel appearances, and those appearances retain the same identity, reference cell and value. They are not two independently prepared inputs. Conversely, distinct record identities need not have different values: all four may have equal contents.

The implementation supplies the stronger parametric explanation: its reference lookup does not inspect payload meaning, and the comparison operations require equality on shared appearances rather than a law relating the four independent slots. Arbitrary supplied per-record maps preserve the reference skeleton when the resulting values remain admissible JSON data.

This establishes **independent caller variation in the candidate information API**. It does not establish physical freedom to prepare every assignment, probabilistic independence, a conservation law, or permission to execute arbitrary value transformations.

## Underdetermination witness

The receipt contains distinct accepted registries—including all-zero and all-one assignments—over the exact same complete reference skeleton. Thus these incidence/reference constraints do not determine the payload values.

This is not a pair of different outcomes for a fully specified native physical state. The inspected source does not provide that state domain or its observation map. A richer native state might determine values, but its map has not been supplied.

Choosing cell coordinates, reference-cell names or direction signs as payloads would define a new interpretation. None is installed here as though selected by the source.

## Resulting contract boundary

Two distinct tasks should remain separate:

1. **Parametric retention/wiring:** accept externally supplied opaque contents, preserve record identities and attachments, and check shared-record consistency. The existing candidate operations support this task.
2. **Physical realization:** supply a native state domain, a map to these attached records, and the joint admissibility law before claiming a particular physical receiver encoding or dynamics.

The second task's fields remain explicitly null in the receipt. There is no justification for shrinking the source to a Boolean alphabet merely to fit a numerical receiver, nor for treating arbitrary JSON capacity as a measured physical degree of freedom.

The fixed finite receiver obstruction therefore concerns an unrestricted software-data contract. It is not, by itself, a physical objection to Su-32 geometry or parametric wiring.

## Verification

```sh
node research/strominger/checkers/check_su32_record_source_contract.mjs
```

Fresh execution passed 16 joint assignments, 64 one-record variations and five rejection controls. Signed-reference encoder and layer-4 comparison regressions also passed.

Checker: `checkers/check_su32_record_source_contract.mjs`.

Receipt: `results/su32-record-source-contract-v1/verification.json`, including the fixed reference identities, distinct payload assignments on the same skeleton and source hashes.

No new payload interpretation, numerical encoder, routing extension or transport wrapper was introduced.
