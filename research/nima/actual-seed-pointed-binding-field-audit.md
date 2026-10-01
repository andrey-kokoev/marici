# Actual seed versus pointed binding: field-by-field audit

## Scope and primary definitions

This audit checks the inspected seed implementations, not every possible conceptual interpretation or every file in the repository.

- `checkers/check_seed_packet_rung4_trace.py` defines `seed=('AB','BC','CA','AD','DB','BA')` and `initial=[(e,e[0],e[1]) for e in seed]`. Its retained total recurrence wraps those same rows.
- `checkers/check_triangle_half_phase.py` defines `TwoPacket` with EXACTLY `label`, `source`, `target`. `cycle_from_packets` verifies distinct labels/vertices, endpoint matching and closure, then constructs the cyclic operator on packet slots.
- `checkers/check_two_triangle_half_phase.py` supplies the two triples explicitly. Its signed BA interpretation is a later cochain restriction, not a stored package equivalence.
- `checkers/check_natural_tower_return.py` repeats the six labelled endpoint tuples and constructs an incidence matrix by unit entries. Its operator acts on an explicitly chosen coefficient representation.
- `agda/SeedPointedTriangleBinding.agda` is the target requirements contract; no concrete instance is supplied there.

## Field correspondence

| Contract field | Actual seed evidence | Status |
|---|---|---|
|A,B,C : Complete|Vertex names in the source/target fields|Names supplied; interpreted type, construction and marked value NOT supplied by these records|
|AB : Filler A B|Record ('AB','A','B')|Endpoint incidence supplied; no carrier equivalence or marked-value path|
|BC : Filler B C|Record ('BC','B','C')|Same missing semantic fields|
|CA : Filler C A|Record ('CA','C','A')|Return endpoint supplied; no equivalence or inverse-parent witness|
|Admit : Complete -> Type1|No such field in the seed records|No seed-specific native policy identified by this audit|
|admitted-A/B/C : Resolve Admit ...|Retained row history|Recovery of a row is not a derivation under the required admission predicate|
|id-AB/id-BC/id-CA|Distinct string labels AB,BC,CA|Usable as static primitive identifiers after explicit encoding|
|Pairwise identity inequalities|Distinct labels, checked by cycle constructor|Finite combinatorial evidence exists; no concrete Agda occurrence instantiation supplied|
|Occurrence-to-filler association|Row ties a label to endpoint names|Cannot bind a label to an actual filler until the missing filler is supplied|

The endpoint relation proves the abstract word AB-BC-CA is composable and returns to A. It does not turn each word symbol into an equivalence between independently interpreted Complete packages.

## Existing substitutes do not fill these fields automatically

The formal Boolean triangle has actual interpreted types, flip equivalences and native route derivations, but they are supplied for that fixture. Its direct third edge is AC rather than the seed's CA. Renaming the fixture would not establish the missing semantic identification.

The spectral seed reconstruction recovers incidence and occurrence provenance. Its cyclic projectors and matrix entries do not provide the per-edge package equivalences or admission proofs above.

The finite execution ledger allocates fresh event IDs and retains primitive-label references. This adds execution records under a requested schedule; it does not construct an interpretation of primitive seed edges as native pointed equivalences.

Wrapping a string or tuple in an atomic Complete, choosing a permissive admission predicate, or assigning identical carriers to every vertex would produce an example. It would be a new interpretation, not evidence that this interpretation was supplied by the source.

## Minimal genuinely missing source data

1. A semantic interpretation of the seed vertices as complete packages, including marked values.
2. For each primitive arrow, its actual supplied equivalence and marked-value witness under that interpretation, tied to its primitive identity.
3. The applicable admission policy and endpoint derivations.

These suffice to instantiate the pointed triangle contract. They do NOT yet provide runtime event allocation, a physical execution schedule, costs, reset authority or the calibrated rung4 reader; those are later obligations.

No concrete binding can be recovered from the inspected label/endpoint data alone. The combinatorial occurrence identities and incidence are already available and should not be rebuilt. The missing information is semantic and source-policy information, not another finite scheduling computation.

## Verification and stopping point

Fresh run:

    python research/nima/checkers/check_seed_packet_rung4_trace.py

Passes its six-row endpoint/provenance recovery and imported 147-table/1176-step tests. Its eight-step retained-total fixture explicitly does not identify itself with the confirmed transport diagram. This run verifies what the rows retain, not the absent native binding.

No new checker, contract, filler or physical interpretation was added. Further instantiation should wait for a source definition or explicit operator decision supplying items 1--3 rather than silently choosing them.
