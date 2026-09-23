# A later owner claim cannot overwrite an earlier denial by graph order

A FICTIONAL row-owner response at event 7 declines proof use; another fictional event at 8 says allow. A later graph sequence alone cannot supersede the denial. Fresh `check_revised_owner_response.py` requires an EXPLICIT `supersedes` edge naming the prior event, the exact same action/request/row manifest, matching live source generation and atomic policy epoch, and nonrevocation. Missing revision edge, changed scope, stale epoch and revocation all fail. A fully matching synthetic chain returns only `TEST_ONLY_REVISION_CHAIN_NOT_AUTHORIZED`, while the denial record is retained.

There has been NO real denial or later owner response: actual Farkas recipient and source event are still unset. A legitimate change of policy would require signed independently admitted issuer events and current revocation evidence, not temporal ordering of epistemic graph mutations. Even a valid origin attestation does not resolve a separately declined proof-use action.

Next test FORKED REVISIONS: two hypothetical successor events both explicitly supersede one denial but grant incompatible scopes. They cannot both be linearized solely by graph sequence; require source-owned conflict resolution before any publication action. Analytic S,A,R,C,G mapping remains deferred.
