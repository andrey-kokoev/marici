# An exact row-owner handoff payload can be prepared without sending

A local payload at `results/unsent-owner-handoff-payload.json` contains exact Farkas source ID, canonical ordered-row manifest digest, both separately requested actions, a digest of the frozen row-attestation request and three bounded local evidence file hashes. It has NO recipient, owner event or source generation and is explicitly `LOCAL_PREPARED_UNSENDABLE`. Fresh `check_unsent_owner_payload.py` refuses send as `OWNER_ROUTE_UNASSIGNED`; even filling fictional recipient/event/generation fields refuses a missing admitted source-scoped channel.

The payload is an intent/evidence reference, not a source event, publication or actual owner request. It deliberately omits unrelated project data and does not claim that the evidence hashes attest the row issuer. If a genuine admitted recipient and source endpoint later appear, the payload, current evidence, live generation and requested capabilities must be rechecked under the owning communication surface before any send. No such recipient is available now.

Next test EVIDENCE DRIFT: if one referenced local evidence file changes after the payload is frozen, detect the changed digest and require payload regeneration rather than sending stale claims. The analytic S,A,R,C,G map remains deferred.
