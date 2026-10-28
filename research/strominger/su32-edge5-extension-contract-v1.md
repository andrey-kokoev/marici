# Edge-5 advance: structural contract and edge-3 regression

## First deliverable completed

A versioned global structural contract now exists at:

`contracts/su32-edge5-structural-extension-v1.json`

Its checker independently inventories the complete edge-5 carrier and verifies an incidence formulation of the chosen edge-3 family. No edge-5 routes have been generated.

## New structural interpretation of {2,2}

For each of the sixteen existing localized edge-3 candidates, let:

- T be the selected occurrence of the paired-tip channel whose two members are active;
- U be the N site carrying the P/P pair;
- V be the N site carrying the E/E pair.

The following predicate selects **exactly the eight working candidates**:

> T shares an actual native edge with U, and T shares an actual native edge with V.

The checker uses intersections of native cell-edge sets. It does not inspect squared distances, orbit membership or the desired candidate IDs when evaluating the predicate. Only afterward does it compare the survivors with the retained working family.

Thus `{2,2}` has an incidence-level description suitable for proposing a larger-carrier constraint. This equivalence is established on the sixteen candidate placements, not for arbitrary configurations. Native edge contact is a placement condition, **not** permission to move a signal directly between the two N cells.

All eight labelled working candidates remain retained. No representative or C5 equivalence is selected.

## Complete edge-5 inventory

For `reading:0:-1`, fresh enumeration verifies:

- 245 whole cells: 80 P, 85 N, 80 E;
- 660 native edges;
- 760 triangular faces, including 560 shared interfaces;
- 17 cell-centre layers;
- 44 residual four-interface comparison cones.

The N-layer populations are

```
1, 4, 9, 16, 25, 16, 9, 4, 1.
```

The P and E populations on alternating layers are each

```
2, 6, 12, 20, 20, 12, 6, 2.
```

Cone starts occur at layers 1,3,5,7,9,11,13 with counts

```
1, 4, 9, 16, 9, 4, 1.
```

The receipt retains every cell, native edge, face, cone, path presentation and enumerated comparison boundary. Unbound comparison maps and witnesses remain unbound.

## Contract scope

The required fibre count is **80**, as previously specified. The contract does not infer eighty fibre identities from the eighty P cells or turn the four directional record labels into an eighty-element wire alphabet.

Before a simultaneous routing problem can be formulated, these remain explicit inputs:

1. Fibre occurrence identities and entry/exit port binding.
2. Their relationship to retained directional record references.
3. The edge-5 instances of the marked placement triple `(T,U,V)`.
4. Permitted internal passages and junction types.
5. Contextual comparison/filling conditions and boundary closure.

In particular, the incidence predicate is not automatically imposed once per cone: the corresponding marked objects and their overlap identifications have not been supplied. The forty-four cones are not independent copies of the entrance construction.

The contract preserves global construction before local verification, disjoint partition of named fibre instances, inverse regrouping, actual attachment support and full provenance. It excludes silent reuse of period-four closure, lexical endpoint matching, or an arbitrary shortest-path selector.

## Verification and stopping point

```sh
node research/strominger/checkers/check_su32_edge5_extension_contract.mjs
```

Fresh headless execution passed the exact eight-versus-eight edge-3 regression and the complete edge-5 inventory checks. Source receipts and hashes are validated.

Receipt: `results/su32-edge5-extension-contract-v1/verification.json`.

The first planned deliverable is complete. Routing search is **not yet formulated**, rather than failed or exhausted. The next step is the concrete fibre/port and marked-instance binding—not another search for a preferred edge-3 family.
