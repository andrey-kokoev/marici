# Request-ID namespace authority

`QualifiedRequestId` pairs an issuer namespace with a local request number.
`NamespaceGrant` carries source authority for exactly one issuer, and `MayIssue`
requires the identifier to name that issuer.

Positive result: issuer A's local `7` and issuer B's local `7` remain distinct.
Erasing the issuer collapses them, demonstrating that an unqualified natural
number is not a globally faithful request identity.

Hostile result: two disconnected allocators both acting as issuer A can still
allocate the identical qualified ID `(A, 7)`. Issuer qualification prevents
cross-issuer collisions; it does not manufacture shared linearization inside a
namespace.

Transport preserves the original namespace grant and cannot authorize issuance
inside another issuer's namespace.

Missing convention-fixed inputs:

- canonical issuer identity and authentication;
- one shared allocator or prior subnamespace partition per issuer;
- durable allocation/reuse policy;
- namespace retirement and request-ID retention bounds.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/RequestNamespace.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the aggregate build later
reported `Build completed successfully (8719 jobs).` The site build was not run.
