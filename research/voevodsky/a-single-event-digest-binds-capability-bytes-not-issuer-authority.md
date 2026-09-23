# A single event digest binds capability bytes, not issuer authority

A FICTIONAL complete row-source event contains issuer string, event ID, generation 7, ordered-row manifest digest and the SORTED set of origin/proof-use capabilities. Fresh `check_single_event_capability_binding.py` binds the full canonical event bytes by SHA-256 and refuses an undisclosed or partially disclosed event. Editing action set, generation or row manifest without updating the commitment fails `EVENT_COMMITMENT_MISMATCH`. One full event digest can therefore make capability-set BYTES unambiguous without the separate-event coexistence problem.

Even a correctly opened digest yields only `TEST_ONLY_EVENT_BYTES_BOUND_NOT_AUTHORIZED`. It proves neither a real signer, event existence, live revocation status nor an admissible root of trust. The actual Farkas owner and event remain unassigned. A self-authored synthetic event cannot be elevated into source publication by its digest or its order in the epistemic graph.

Next test EVENT CANONICALIZATION: action-set ordering, duplicate action names and JSON normalization can change digests or silently widen meaning. Define a strict schema that refuses duplicate capabilities and ambiguous encodings before hashing, but still never claims real issuer authority. Analytic S,A,R,C,G mapping remains deferred.
