# Dependency-aware partial-repair compiler

The compiler replaces the free finite-repair permutohedron by the legal path
space of a typed dependency poset. A repair constructor carries its local
defect transition, domain and graph-norm requirements, complete boundary and
support deltas, authority root, prerequisites, residual certificate type, and
capability consumption/production signatures.

For a finite repair poset `(R,<)`, the compiler enumerates precisely its linear
extensions. A listed order may still fail dynamically: every leg is checked
against the actual intermediate defect signature, graph domain, graph norm,
and residual capabilities. An unresolved prefix is retained only as an
`unsafe_repair_in_progress` state with its unresolved defects, next admissible
repairs, and residual capability packet.

## First three exact models

Three independent repairs produce all `3! = 6` paths. Authorized adjacent
swaps connect them into one component and all paths yield one typed endpoint.
This recovers the ordinary permutohedron exactly when the dependency poset is
discrete and all swap gates pass.

Adding `A < B` leaves the three linear extensions

```text
A B C
A C B
C A B
```

Adjacent swaps of incomparable repairs connect these paths. The missing
orders are absent because they are illegal, not because a coherence cell was
forgotten.

The third model has two legal orders and identical scalar endpoint bytes, but
the two composites produce inequivalent graph norms. Its swap gate reports
`repair_swap_domain_failure`; the legal path graph has two components and two
typed endpoints. Scalar equality therefore supplies neither a swap cell nor
endpoint coherence.

The current increment deliberately stops before braid/anomaly classification.
Those cells will be generated only after their residual representation and
source-authority types are present. Likewise, the theta/Tate stages
`{S,P,Q,A,L,C,D}` are not assigned dependencies by this compiler: their
`precedes`, `commutes_with`, `domain_after`, `boundary_delta`, and
`completion_scope` declarations remain source-owner obligations.
