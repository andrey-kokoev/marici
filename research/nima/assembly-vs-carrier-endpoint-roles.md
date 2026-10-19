# Actual assembly endpoints versus carrier-index endpoints

## Fresh result

The strongest prior clue was tested against the ACTUAL shared-leg DG source, not just its note or another numerical prototype.

All137 composites really have assembly endpoints A->B, with intermediate objects U and V. Their numerical values are exactly the corresponding original137 rung-row values. However the original rung-row source/target columns are carrier-index decorations, not those common A,B endpoints.

A retained adapter between these two tables preserves labels, values, original rows, masses and J4. It does NOT preserve all operation domains or endpoint uniqueness.

This clarifies the intended-T9 question substantially: "common target" can refer to the source assembly's genuine B, or to a newly collapsed carrier-index column. Those are different constructions.

## Test actual source leg types and values

The checker reads the signatures from `check_shared_leg_dg_realization.py`:

    ax_i:A->U, ay_j:U->B,
    sx_a:A->V, sy_b:V->B,
    d:A->B.

Every path ay_j ax_i or sy_b sx_a has source A and target B. Every evaluated path matches the unchanged original row value. The direct reference stays d=2I; the other boundary-adapter checker uses separate perturbation controls and is not used to replace those values.

No U<->V primitive is present. Parallel composites having A,B endpoints does not require such an intermediate connector.

## Retained endpoint-role adapter

For each original row, retain a wrapper with:

    same label, value and mass;
    source=(assembly,A), target=(assembly,B);
    original carrier-index row as retained member.

Thus the old carrier endpoints remain available and reconstruct exactly. The map changes the active endpoint columns; it does not claim those columns were already the same.

All137 wrapper labels are distinct, but all137 endpoint pairs are identical. Parallel comparison maps are legitimate if the table allows parallel rows. If the endpoint-uniqueness contract is required, this table fails it.

Refining the source with a unique label restores endpoint uniqueness but changes the endpoint semantics. It cannot be described as literally the original common A->B assembly.

## The tower signature changes immediately

Apply the SAME existing two-round incoming-family former to both input tables:

| Input endpoint role | Inherited policy | Common policy |
|---|---|---|
| carrier-index columns |137->32->32|137->32->1|
| actual common A->B assembly |137->1->1|137->1->1|

All four outputs recover the137 original leaves and identical J4. Their grouping domains differ.

Therefore the existing137->32->1 candidate is NOT obtained merely by recognizing the original common assembly endpoints. Its32 first families come from the carrier-index presentation. It uses a hybrid sequence: first group by carrier target decorations, then group by a newly shared target.

A typed common-endpoint assembly supports a direct parallel-family assembly, but does not establish that this hybrid is intended T9.

## Operation-domain comparison

The carrier-index source has:

-977 admitted common-target reference-return pairs;
-916 literal target-to-source composable pairs.

The common A->B assembly table has:

-18769 common-target reference-return pairs, conditional on the existing invertible reference return B->A;
-ZERO literal forward pairs because B and A are distinct.

The role adapter preserves already-admitted reference-return pairs but adds17792, so it fails reflection. It does not preserve the original literal forward operation domain at all.

The checker records a concrete original cross-target pair that becomes common-target after the role change. No physical interaction or missing carrier connector is silently inferred from that comparison.

## Not a single-object graph functor

The same32 original carrier ports occur as both sources and targets of records. Mapping every source column to A and every target column to B would require a single graph-object map to send the SAME port to both A and B.

Since A and B are distinct assembly objects, that is impossible. The adapter is instead a retained TWO-COLUMN table map: its source-column and target-column maps have different roles.

This is why matrix agreement cannot turn the carrier incidence graph into the shared-leg path category. The original carrier graph loops and assembly Hom(A,B) paths are different typed domains.

## Consequence for the previous connector search

The4112 missing pairs in the record-route graph remain genuinely unsupported by that graph's routes. But this is not automatically an obstruction to assembling137 ALREADY PARALLEL comparison paths A->B.

Conversely, assembling parallel maps does not supply physical routes between the carrier-index ports. The two statements are compatible once their endpoint roles are kept explicit.

Intended T9 must say whether it:

1. transports/regroups carrier-index records;
2. assembles parallel reference-relative paths;
3. creates new physical comparison contexts;
4. performs another native family operation.

Their retained matrices can agree while their operation signatures differ. We should not force the assembly task into the carrier-connector API or infer a carrier interaction from common numerical Hom-space coordinates.

## Next useful source binding

The source has an actual common-endpoint assembly, so the next question is a TABLE WIRING question: do the intended rung source/target columns denote A,B assembly roles or carrier-index columns?

A separate existing arrow->state endpoint-readout law is also worth adapting to the marked137 domain, but it is noninvertible and belongs to a readout interface, not this common-target reference-return composition.

No intended-T9 or physical endpoint selection is declared by this audit.

## Verification

    uv run research/nima/checkers/check_assembly_vs_carrier_endpoint_roles.py

299 exact checks pass. Dependencies freshly rerun the geometric record binding, original rung/shared-leg DG source and typed assembly boundary adapter. No fresh Agda closure or physical correspondence is claimed.

Artifacts:

- `checkers/check_assembly_vs_carrier_endpoint_roles.py`
- `results/assembly-vs-carrier-endpoint-roles.json`
