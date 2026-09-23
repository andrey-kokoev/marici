# A source-grant lookup must be atomic with publication use

A FICTIONAL issuer registry at epoch 7 lists a row-manifest/event grant; before purported publication it advances to epoch 8 and revokes it. Reusing the epoch-7 lookup is `ATOMIC_SNAPSHOT_STALE`. A fresh epoch-8 read is `GRANT_REVOKED`; changing fields while presenting the same epoch is `INCONSISTENT_SAME_EPOCH`. Fresh `check_atomic_attestation_snapshot.py` checks each condition. An unchanged fictional snapshot returns only `TEST_ONLY_SINGLE_EPOCH_FIELDS_MATCH_NOT_AUTHORIZED`.

The necessary production invariant is an atomic, monotonically versioned binding of issuer identity, signed source event, row manifest, live generation and revocation state AT USE TIME, not separate stale reads followed by an optimistic mathematical packet check. This script does not implement a real transaction or signature verifier and there is still no designated real Farkas issuer. Neither a test snapshot nor graph admission authorizes publication.

Next test a HOSTILE source event whose signature/grant is valid for a DIFFERENT row subset or different dimension but happens to have a similarly named source ID. Exact source scope must include the complete ordered row manifest and permitted action, not just a label or issuer identity. Analytic S,A,R,C,G map stays deferred.
