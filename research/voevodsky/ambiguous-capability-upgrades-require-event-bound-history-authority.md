# Ambiguous capability upgrades require event-bound history authority

## Delivered gate

A fixed-family retirement prototype now separates mathematical compatibility from authority to identify the actual original history. It starts with the verified n=18 scalar-band section and original-atom approximate-lifting contract. The owning caller supplies A or B BEFORE retirement; the prototype does not infer that identity from a candidate packet or selected source witness.

An optional process-local archive authority retains an immutable record binding the retirement event, expected context/section digest and original-history label. A random reference identifies that record. There is no serialized provenance import or API accepting a caller's self-asserted history as post-retirement authority.

This is an explicit trusted-owner boundary, not proof that the owner supplied a truthful physical history. Nor is it yet bound to an arbitrary owning projection-compiler migration. The context is the already studied fixed two-history family with a verified shared section.

## Ambiguity does not advance the head

The requested continuation is the fine bound h<=1/2 followed by exact admission of public point (1,1). The independent obstruction verifier checks that refined A rejects this point while refined B admits it.

`request_upgrade` reports both alternatives and requires original-history authority. It leaves the live head unchanged. A shared section does not choose between them; the control explicitly demonstrates that both sessions return the SAME selected source lift at this point before the request.

This is not a general three-way decision procedure. It is the fail-closed ambiguity/resolution path for a certified distinguishing request. Unsupported requests and obstruction points excluded by existing public evidence are refused rather than guessed.

## Authorized resolution

`resolve` rechecks the expected state, exact operation and obstruction, then asks the owning vault to validate the archive reference against this retirement event and context. Only after both semantic checking and authority validation does it publish a new head and the corresponding exact admission answer.

The two test sessions have equal live semantic descriptors but resolve differently: A returns false; B returns true. The identity distinction resides in the external archive record and event/reference association, not in the common lifting function.

Resolution authorizes THIS exact admission request only. It does not append fine evidence to the live approximate-lifting state, replace that state with an archived fine state, grant a general fine-update capability or enable archival re-exposure. Its receipt says so explicitly. Subsequent approximate lifts still belong to the pre-existing public-only contract; silently treating them as fine-refined lifts would be wrong.

## Fail-closed controls

Sixteen invalid resolutions are rejected without changing the head or receipt:

- self-asserted history labels;
- an archive-shaped object listing both possibilities;
- a chosen source lift offered as identity;
- a forged reference;
- a real reference belonging to another retirement event;
- a false obstruction;
- a stale head after successful resolution;
- a foreign archive offered after identity was deliberately not retained;
- a revoked archive reference.

The vault is process-local and owner-controlled. Code able to alter its memory or invoke its private admission method is outside the threat model. Restart recovery, concurrency testing and external attestation are not delivered.

## Reversible retirement versus forgetting

With a valid event-bound identity record, the ambiguity can be resolved. If the owner deliberately omits that record, the prototype retains only the common semantic state and cannot recover actual history. A real archive from another event does not repair this loss.

For the two possibilities the vault retains at least one bit of history selection, plus event/context/reference encoding. The report charges its complete current JSON record encoding separately. The two sessions are NOT globally identical retained states merely because their live descriptors match: their external authority associations differ. No compression theorem may omit that distinction.

Likewise an archive containing both candidate histories supplies alternative answers, not evidence of which one occurred. Returning both branches is legitimate uncertainty reporting, but not actual-history reconstruction.

## Reproduction

    python research/voevodsky/checkers/check_authority_aware_upgrade.py

Implementation: `checkers/authority_aware_upgrade.py`.

Artifact: `results/authority-aware-upgrade.json`.

The remaining operational step is an owning migration/archive authority interface that can replace the live state with a verified fine-refined successor. This prototype establishes the authority boundary and fail-closed query resolution without claiming that stronger state transition.
