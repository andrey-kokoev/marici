# A handoff receipt does not attest Farkas row origin

The actual prepared row-owner payload cannot transition from `prepared` to `sent`: there is no authorized source-scoped recipient. In a FICTIONAL state-machine route, separate `sent`, `delivered` and `received_not_attested` states can be reached. A receipt must match the frozen payload digest; a foreign receipt is refused. Even a matching receipt cannot become `owner_attested` without an independently authenticated owner attestation verifier. Fresh `check_handoff_ack_states.py` checks these gates and a separate explicit rejection state.

No actual owner message, delivery or receipt occurred. Transport acknowledgement proves at most an addressed request was received, not that its ordered primitive rows were issued, or that either requested capability was granted. Graph admission of a coordination transition likewise cannot replace a signed source event.

Next test PARTIAL OWNER RESPONSE in a synthetic receipt: a legitimate future issuer might attest row origin but explicitly decline proof-use publication. A response must update only its stated action and leave the other capability unresolved, with a signed exact request/source-generation binding. The real recipient remains absent; analytic S,A,R,C,G deferred.
