# One-row proof support does not shrink a full-source grant

The local x<=2 proof can use only the x-upper source row with multiplier 1 and surplus 1. A one-row support-subset manifest, however, has a different canonical SHA-256 than the frozen COMPLETE four-row square source. Fresh `check_support_vs_source_scope.py` refuses substituting that support digest for a FICTIONAL grant scoped to the complete source as `FULL_SOURCE_SCOPE_MISMATCH`. Even an exact full-manifest match is explicitly TEST-ONLY, not a real owner grant.

Selected proof support answers which row coefficients a mathematical verifier consumes; source publication scope answers which ordered row source an issuer authorized. They cannot be conflated. An owner might explicitly issue a separate subset-scoped grant later, but none is presently authenticated and source-generation/analytic role mapping remain unknown.

The standalone math-without-owner branch is complete: endpoint algebra is independently checkable, proof-history retention can be stronger than endpoint truth, and minimal proof support cannot launder a full-manifest grant. A nonredundant successor should test INCREMENTAL LOCAL ROW-CHECKING under one source bound edit: identify which saved proof packets require recomputation using a row-dependency index while all authority conclusions stay unchanged. Analytic S,A,R,C,G correspondence deferred.
