# Finite programme-carrier fragment for the Bool source

Implementation: `pilot_carrier.py`.
Contract: `contracts/pilot-carrier-interface.v1.json`.

## What is implemented

The fragment has four strictly typed Bool-pair labels and two native flip operations. A `PathRecord` retains its source and entire ordered operation word; its trace and target are computed from that data. Composition requires matching source/target attachment and concatenates the words. Empty words give identities. Tuple concatenation proves associativity, and sequential evaluation proves the corresponding target law for any finite word. The executable audit covers bounded words and composable triples; it is not a new kernel proof.

Occurrence IDs distinguish repeated equal records. Promotion groups by an explicitly supplied source or target key, retaining every member occurrence. Its batch namespace and group key identify the family. Reusing a batch with changed membership needs an external version/history policy. The constructor does **not** infer independent comparison operands, next endpoints, new physical degrees of freedom or a recursive product law.

## Source and spectral binding

Native labels map identically to fragment labels, and `label_index` uses the displayed `00,01,10,11` delta order. Native flips map to their accepted source-linearized permutation matrices. For any operation word, evaluating the source word then encoding gives the same basis state as applying the ordered matrix composition. Replacing the matrices with the existing pi-scaled spectral legs uses the accepted witness, not a new endpoint-matching generator.

At fixed native Bool source, the existing formal theorem classifies the full Tick by its two ordered schedule tags. `TickFragment` implements that tag interface, including equal-tag pairs. It does not execute Agda Tick terms or replace the formal inverse by a Python proof. The already checked tag equivalence supplies the written binding to native records.

Arbitrary `PathRecord` histories are **not** classified by Tick tags. Different words may share endpoints and still have different structural IDs and retained traces. Do not generalize the Bool Tick classification to all path histories.

For each retained schedule, the spectral return starts at the both-flipped source and executes the operations in reversed order using positive phase. The fragment's seam labels match that convention. Two schedule tags have distinct seams; full ordered tag pairs reconstruct the fixed-source record. Swapping tags swaps the return-pair binding. The accepted realification transport then carries the same state/operator/return witness to R8.

## Readout and geometry boundaries

Delta coordinates and coordinate intensities are mathematical maps. Intensity loses phase, and scalar norm/energy can identify different records. Source attachment, operation history and schedule tags remain separate retained data. No physical probabilities, clock or energy units follow.

The fragment binds to an existing analytic interval realization; it does not implement the operational scalar backend again, construct spacetime, or supply an ambient universal carrier. The two analytic/observer interface components therefore have narrower statuses than the six executable record/operation components.

## Provenance

`contracts/pilot-source-records.v1.json` supplies eight target-specific ingredient records with origin hashes, provenance roles, allowed uses, forbidden promotions and a future-use freeze boundary. It is not retroactive preregistration. No fitting or held-out physical dataset is supplied.

- Native source and factor operations: `research/nima/agda/ObserverCoherenceCube.agda`, through the accepted native spectral witness.
- Full fixed-source Bool Tick classification: `research/nima/tick-full-structure-classification.md` and `TickRetainedStructure.agda`, at their existing scoped formal evidence level.
- Label/record batch conventions and grouping keys: declared implementation choices here, not source-selected physical laws.
- Complex analysis, pi-scaled spectral rule and realification: the explicit backgrounds and accepted finite transport, not inferred from grouping.

No measured data, fitted physical constant or held-out observation is an input to this fragment. That makes the adapter a structural test, not empirical confirmation.

## Verification

```sh
python research/conjecture_net/check_pilot_carrier_interface.py
python research/conjecture_net/test_pilot_carrier.py
```

The audit checks source action/permutation squares, bounded composition and identity laws, retained histories and duplicate occurrence controls, promotion reconstruction, all fixed-source tag pairs, seam separation and swap. It also resolves the live accepted finite-transport prerequisite. It records a validation-only result with no programme outcome. Admission of this new executable adapter and any stronger kernel proof are separate from the already accepted coordinate transport.
