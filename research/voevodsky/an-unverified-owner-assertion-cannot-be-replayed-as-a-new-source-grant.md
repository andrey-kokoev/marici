# An unverified owner assertion cannot be replayed as a new source grant

Fresh `check_unverified_authority_scope_replay.py` uses a token explicitly marked UNVERIFIED, scoped to a fictional old row digest, generation 1 and `validate-local-math`. A changed row digest or generation returns `ASSERTION_SOURCE_SCOPE_MISMATCH`; asking to `publish-source` returns `ASSERTION_ACTION_SCOPE_MISMATCH`. Even exact old-scope matching returns only `SCOPE_MATCH_ONLY_NOT_AUTHENTICATED`, never authority. These are negative scope predicates, NOT a signature-verification procedure.

A verified owner recipient and signed source contract are still absent in the inspected branch evidence; no message should be sent to an invented identity. Analytic S,A,R,C,G map remains deferred.

This bounded path-edge branch now distinguishes typed rule, exact target, row source, composition and grant scope. Open a separate research successor for CATALOGUE CLOSURE on a candidate source migration: all endpoint proof packets and typed comparison/weakening edges must revalidate against the same new generation. No actual owner/source edit or publication.
