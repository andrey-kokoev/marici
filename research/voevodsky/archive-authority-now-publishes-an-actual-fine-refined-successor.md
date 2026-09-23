# Archive authority now publishes an actual fine-refined successor

## Across-lane connection

The fixed-family restoration adapter now consumes the ambiguity returned by Nima's `CapabilitySession.request_fine`. The underlying request service remains unchanged and authority-free. A separate, explicitly trusted owner archive is admitted BEFORE retirement and binds the event, expected initial contract/section and original history.

Unlike the earlier query-only resolution prototype, successful restoration replaces the live operational state. The old coarse service is removed from the wrapper, the ambiguity is cleared, and a fresh head exposes exact point admission and exact fine lifting against the reconstructed history plus new fine evidence.

## What is archived and authorized

The vault retains the original A/B selector AND its complete fixed-family fine rows, public polygon and source-chart identity. It does not store merely a selected source witness. Owner-supplied identity is trusted at retirement; physical observation authentication is outside this prototype.

For restoration, a vault reference must match the retirement event and initial context. The service also requires the current head, independently expected predecessor and exact digest of the currently verified Nima ambiguity. Its internal authorization result binds that request digest. A reference is not accepted merely because candidate metadata claims a matching issuer or history.

The archive verifier reconstructs the original fine family from n and history, compares it with the authorized archived relation, and requires the successor to contain exactly those original rows plus the requested upper bound. It also checks event/request bindings and the precise new capability set. This verifier imports neither session implementation; it shares the established envelope arithmetic. Candidate construction in the test uses the same archive-schema helper, so this is not a separately implemented geometric kernel.

## Atomic publication

All authority, statement and fine-successor checks occur under the wrapper lock before publication. Failure leaves the predecessor state, head and bound ambiguity unchanged. The test calls Nima's ambiguity path again after failed restores to show the predecessor is still usable.

After success:

- old handles fail;
- the old common request path is unavailable;
- exact point queries compute the interval from ALL successor fine rows;
- an empty interval yields refusal, not a stale common lift;
- a nonempty interval produces a source witness obeying the new evidence;
- archival re-exposure remains a separate denied capability.

This service exposes point admission and lifting, not general LP optimization, arbitrary further fine updates or an imported archive protocol. The linear successor here is one fine-upper refinement of the fixed family.

## Distinguishing workload

Both histories receive h<=1/2 at the same retirement stage. At public point (1,1), restored A has an empty fine interval and restored B returns a valid source witness. At the first public vertex both histories return witnesses obeying h<=1/2. The old shared section can no longer serve as an unrestricted lifting path after restoration.

The test directly rechecks returned atoms against caps, exact public moments, t1=51, every original fine row and the new bound. It also freshly replays each successor against its authorized archive and Nima ambiguity.

Eighteen refusal controls include missing successor evidence, capability escalation, foreign/self-asserted archive references, stale request digests, stale coarse handles, use of the old request path, re-exposure, authority-free selection and a revoked archive. Failed calls preserve receipt equality. Concurrency is serialized by locks but concurrent scheduling was not tested.

## Information and accounting

The vault's encoded records are charged separately and include selector, full fine rows, event, context and reference keys. Receipts record live state, ambiguity and fine-successor encodings; after restoration the live state and fine-successor accounts describe overlapping data and must not be summed as disjoint heap allocations. The underlying coarse service retains its section before restoration, but that initial section storage is not yet included in the wrapper receipt's byte fields. External result logs and source code are likewise separate.

Thus live coarse equality is not total forgetting: reversible sessions preserve actual history in the vault. An authority-free control still returns ambiguity and refuses restoration. Neither a family archive listing alternatives nor a chosen common witness can supply the missing actual-history authority.

## Scope

This completes an actual state-replacement transition for the declared fixed-family contract across the Nima ambiguity boundary and Voevodsky archive boundary. It does NOT authenticate external provenance, add authority to Nima's service itself, or compile an arbitrary owning projection migration into a fine archive. The owner-admission assumption remains explicit.

## Reproduction

    python research/voevodsky/checkers/check_atomic_fine_restoration.py

Implementation: `checkers/atomic_fine_restoration.py`.

Successor verifier: `checkers/verify_fine_successor.py`.

Artifact: `results/atomic-fine-restoration.json`.
