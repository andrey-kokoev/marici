# A digest-correct row migration without an issuer is not a provenance edge

Fresh `check_issuerless_source_migration.py` stages a synthetic y-upper 1->2 row edit with correct old/new ordered-row digests and incremented generation. Its result is `LOCAL_DIGEST_SCOPE_ONLY_NO_ISSUER`, not an admissible source migration: no owner-issued grant is attached. A wrong digest fails structural scope; arbitrary strings in issuer/grant fields yield `UNVERIFIED_GRANT_NEEDS_OWNER_CONTRACT`, NOT authorization. The checker makes no actual source mutation and no signed owner verification claim.

Thus locally revalidated math and consistent path shape cannot launder changed rows into observed/provenance-bearing history. No known authorized recipient can be identified from this branch's evidence, so do not fabricate a handoff address. Analytic S,A,R,C,G remains deferred.

Next test AUTHORITY-TOKEN REPLAY: even a structurally plausible owner assertion tied to old digest must not be reused for a distinct new digest or generation. This is a negative local scope test only; it does not validate signatures or confer authority.
