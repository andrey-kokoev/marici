# A directory contact does not designate a row-source verifier

A FICTIONAL directory entry for the exact Farkas row source containing only a contact and source label is `DESCRIPTIVE_CONTACT_ONLY`. It does not supply an admitted issuer identity, trusted verification endpoint, live source generation, revocation route or usable authorized handoff channel. Fresh `check_typed_owner_directory_candidate.py` refuses missing trust/endpoint and generation/revocation fields, as well as a mismatched manifest. Even a fully populated fictional entry yields only `TEST_ONLY_ENDPOINT_SHAPE_COMPLETE_NOT_AUTHORIZED`.

The actual frozen row request still has no owner/event and no such admitted directory entry. This does not say an external owner can never exist, only that inspected evidence does not designate a recipient. A future contact field may support human discovery, but publication or an exact evidence-bearing owner request must go through a separately admitted channel with source/action scope. No message was sent to the example address.

Next test DIRECTORY SNAPSHOT FRESHNESS: even a formerly admitted endpoint may rotate, revoke or move to another source generation; a cached address/trust root must not be used for owner handoff unless the directory snapshot and endpoint binding remain current at send time. Keep actual request fail-closed and analytic S,A,R,C,G correspondence deferred.
