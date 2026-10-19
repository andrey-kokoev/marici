# Full nine-position tower atlas v2

## Scope: complete candidate atlas, not a completed physical identification

This version populates all positions **12 through 4 in the clarified diagram**, including the three transport roles. It extends v1 without rewriting its historical claims. It records an executable, lossless **candidate field-slot tower**, alongside the existing numerical/DG tower as a separate layer.

```
12 --G9--> 6
 |         |
11 --G8--> 5
 |         |
10 --G7--> 4
```

The six state presentations retain the same **36 complex field components**. The horizontal maps introduce **137 structured comparison leaves**, not 137 independent modes. No state object called rung9, rung8 or rung7 is introduced by this diagram; those numbers name maps. No extension below rung4 or identification with a different ladder is assumed.

Machine-readable atlas: `rung-symmetry-atlas-v2.json`.

## Complete object and map inventory

| Position | Candidate object / operation | Outer entries | Comparison leaves | Independent field components |
|---|---|---:|---:|---:|
| 12 | Twelve endpoint-labelled vector triples | 12 | Not generated | 36 |
| 11 | Same triples grouped by source vertex | 4 | Not generated | 36 |
| 10 | Same triples grouped by target vertex | 4 | Not generated | 36 |
| 9 | G9: raw field → raw comparison leaves | Map | Generates 121 + 16 | Retains 36 |
| 8 | G8: source-indexed field → source-indexed leaves | Map | Generates 121 + 16 | Retains 36 |
| 7 | G7: target-indexed field → target-indexed leaves | Map | Generates 121 + 16 | Retains 36 |
| 6 | Raw paired field occurrences | 137 | 137 | 36 |
| 5 | Leaves grouped by branch and source pair | 32 | 137 | 36 |
| 4 | Leaves grouped by branch and target pair | 32 | 137 | 36 |

Every row in the JSON also specifies its role, phase, recovery map, outgoing maps, action types, numerical-layer counterpart and remaining gap. Zero `comparison_leaves` on the left means comparisons have not been generated there, not that the field has no internal relationships.

### Payload policies

The marked directed reference arrow is supplied. Eleven other arrows constitute the counted arrow branch. The four state payloads are defined as full outgoing source-vertex fibers, three triples per vertex. The owner generator forms ordered same-kind pairs, including self-pairs: 11² + 4² = 137. No arrow/state cross pairs are inserted.

Arrow-pair payloads retain two labelled triples. State-pair payloads retain two full source fibers. All repeated values must agree. Recovery collects those occurrences and requires exact regeneration of the full slot structure. It does not consult a hidden copy of the original field. The marked arrow remains recoverable through the state branch.

These source-fiber and reference policies are explicit hypotheses. They are not selected by the group order or by a desired numerical coupling.

## The entire candidate diagram commutes

The new constructor defines actual nodes for all six presentations, along with vertical and horizontal maps. It checks:

```
G8 V12-11 = V6-5 G9
G7 V11-10 = V5-4 G8
V5-4 V6-5 G9 = G7 V11-10 V12-11.
```

Equalities concern rung, reference and full field-bearing view. Construction histories remain different and are retained as distinct traces. This is a retained-history candidate, not a claim equating the full history-bearing objects.

The checks run through all six states and both routes for all 36 basis fields and all twelve possible reference arrows. State presentations are validated, so substituting a source-indexed view for a target-indexed one fails. Horizontal maps on output states, a state at rung9, and vertical descent after rung4 are rejected rather than silently reinterpreted.

## Symmetry inventory at every candidate state

Four kinds of action must remain separate:

| Action | Order | Meaning and verification |
|---|---:|---|
| Support relabelling | 24 | S4 moves vertices, endpoints and the reference. Component coordinates stay unchanged; this is not a claim of 24 proper spatial rotations. Inherited from the checked field-decoration map. |
| Proper geometric action | 12 | A4 permutes patches and rotates their three-component vectors. Independently realized on each slot occurrence and checked against the native field matrices at all six states. |
| Induced internal action | 4 | V4 from the source projector reflections. Recover the field, apply the source reflection, encode into the same presentation. All 16 internal composition pairs are checked at every state. |
| Induced generated action | 48 | A4 × V4 on the family of consistently encoded fields with transported references. All seven diagram maps intertwine each of the 48 actions. |

The full action is **on the constrained image** of the encoding, not on arbitrary independently varied slot values. Corrupted or inconsistent slot packages are rejected.

The 48 source matrices and their group laws come from the freshly replayed simplex-operation checker. Injective encoding and exact recovery transport this faithful representation. Therefore the full induced symmetry is the **same at every candidate state**, not a different group invented for each rung. This is a mathematical consequence of the candidate encoding, not independent evidence selecting the physical rung interpretation.

Only the proper geometric subgroup has an independently checked, occurrence-wise output action here. The internal reflections use global decode/apply/encode; no local transport-edge or fiberwise implementation is claimed. Their existence under conjugation should not be confused with a newly derived local mechanism.

### Marked domains versus point stabilizers

For a fixed directed reference arrow:

- The label S4 stabilizer has order 2: it may swap the two spectators.
- The proper A4 stabilizer has order 1: no nonidentity proper rotation fixes an ordered edge.
- The full generated A4 × V4 action has a fixed-reference **domain** stabilizer of order 4, supplied by the internal involutions.

These are domain-preserving transformations, not necessarily transformations fixing a particular field value. A chosen field, C/M marking, history or observer can have a smaller stabilizer. The atlas leaves such point/observer stabilizers unassigned until the data are specified.

## Numerical/DG layer: preserve the distinction

The existing generating schedule starts with bare twelve-arrow records plus a supplied Context. Its horizontal maps generate 137 support slots, bind numerical/DG legs and witnesses, then perform two retained incoming-family promotions. The pinned inherited-key output has **32 promoted outer rows at rung6**, retaining 137 leaves.

The new candidate has **137 raw pair-valued outer rows at its rung6**. Its 32 source/target families are groupings of those raw slots, not automatically the old promoted row objects. Equal leaf support or equal counts do not identify these two layers. This distinction is stored explicitly in each atlas entry.

The inherited prior suites verify the numerical diagram and its source fixtures. The new checker verifies the field-slot diagram. It does not claim that both are now the same typed construction.

## Evidence and checks

Run:

```
python research/strominger/checkers/check_field_tower_atlas.py
```

The checker replays the existing generating schedule, the geometric rotation square, the earlier field-decoration checks and the simplex-operation group suite. New checks cover:

- All nine atlas positions and all six reconstruction maps.
- Both commuting squares and complete routes, with different histories retained.
- All 36 basis fields and all twelve reference choices.
- 48 actions × seven diagram maps = **336 induced-action map squares**.
- Twelve proper rotations × six states = **72 independent occurrence-action comparisons**.
- Six states × sixteen V4 composition pairs = **96 internal composition checks**.
- Reference-domain stabilizers and explicit malformed-state/unsupported-map controls.

The receipt is the ignored runtime file `research/strominger/results/field-tower-atlas/verification.json`. It includes direct source hashes and prerequisite replay logs. No physical normalization or new formal proof-assistant certification is inferred from these finite exact checks.

## Remaining obligations, by layer

1. **Source policy:** justify the marked reference, outgoing-state fiber interpretation and same-kind comparison rule without selecting them to fit 137.
2. **Numerical adapter:** connect pair-valued field leaves to the actual numerical/DG legs, witnesses and d, preserving the required information and operations.
3. **Promotion:** transport the field action through the actual inherited-key family constructor, including fresh labels and provenance; do not identify raw-slot indexing with that promotion.
4. **Local implementation:** determine whether the globally induced internal actions have independently admitted local or fiberwise realizations.
5. **Observation:** specify a fixed rung4 reference/reader and its stabilizer, metric and physical calibration.

The atlas is now populated at every diagram position with executable candidate data and explicit gaps. Filling an entry means recording its actual status, not replacing an unknown physical identification with a guessed group name. No viewer, website, production dynamics or deployment is changed.
