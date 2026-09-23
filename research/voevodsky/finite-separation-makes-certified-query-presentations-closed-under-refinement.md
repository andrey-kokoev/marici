# Finite separation makes certified query presentations closed under refinement

## Question

When does generator-based certified access remain complete after retained evidence is refined? Base membership alone is insufficient to justify a cutting-plane optimizer. The missing hypothesis is a progress guarantee for the separating cuts, together with exact optimization over the outer approximation.

This theorem isolates sufficient assumptions. It is not a claim that they are necessary or that arbitrary compact generators satisfy them.

## Finite-separation theorem

Fix rational observable coordinates in R^d and a nonempty compact rational polytope Z=L(P). A source presentation supplies:

1. A bounded rational polytope B containing Z, with checkable justification for its bounds.
2. A finite dictionary D of rational inequalities whose intersection with B is exactly Z. D need not be materialized or stored in a runtime state.
3. A total exact oracle on rational points y of B. It returns either a checkable source-admitted lift x with L(x)=y, or a dictionary inequality valid on Z and strictly violated by y. Inequality identity is fixed, for example by canonical rational normalization; arbitrary rescaling does not count as new progress.
4. An exact rational LP procedure for bounded rational polyhedra, including lower-dimensional cases. It returns a primal optimum with a nonnegative dual certificate, or a Farkas emptiness certificate.
5. Independent validators for source admission, lifts, cuts, linear certificates and statement binding. Source rules and expected state/query come from the verifier's declared context, not only from the response.

A state retains a finite tuple E of rational observable halfspaces. Its denotation is

    Q_E=Z intersect intersection(E),
    C_E=P intersect L^-1(Q_E).

For every rational linear objective, the following procedure terminates with a certified optimum over Q_E or a certified proof that Q_E is empty:

    rows := bounds of B plus every retained frame in E
    repeat:
        solve the outer LP exactly
        if empty: return its Farkas proof
        query the source oracle at an outer optimizing point y
        if admitted: return its lift and the outer dual proof
        otherwise: append the separating dictionary inequality

There are at most |D| rejected candidates. Persistent storage need not contain D. Query-local rows and proof packets can nevertheless grow to include all of it.

### Proof: invariant, progress and terminal certificates

Every outer row is valid on Q_E: a source bound, a retained frame, or a validated source cut. Thus Q_E remains contained in the current outer polyhedron.

A rejected candidate satisfies all existing rows and strictly violates its returned cut. That dictionary inequality cannot already occur among the rows. Each rejection therefore adds a new member of finite D. After at most |D| rejections no rejected outer candidate is possible. Boundedness and exact LP ensure every nonempty outer problem supplies an optimum; rational polyhedra supply rational optimizing vertices even when their affine dimension is smaller than d.

If the outer problem is empty, its valid rows and Farkas proof certify Q_E empty. If an outer optimum has a source lift and satisfies E, it belongs to Q_E. Its objective attains the outer upper bound, so the source witness and dual bound certify exact optimality.

### Closure under declared refinements

Appending finitely many rational halfspaces changes E but does not change Z, B, D or the source oracle. The same proof applies to every new state. This is closure under rational observable-halfspace refinement, not closure under arbitrary new predicates or hidden source restrictions.

State-relative point membership is simpler: check E, then call the source oracle. A violated frame or source cut proves point exclusion; neither alone proves the entire state empty.

## Certificate size versus proof existence

An optimum admits a dual supported on at most d rows: its objective lies in the cone of active row normals. An empty system admits a Farkas certificate supported on at most d+1 rows by conic Caratheodory applied to augmented rows. These are bounds on the nonzero arithmetic core, not the complete packet. Binding the full retained history, validating cuts, and encoding exact rational values have additional costs. The theorem gives no polynomial bit-complexity or cheap implementation guarantee.

It is not a finite-cut termination theorem if the separator may return arbitrary valid supporting inequalities outside D. Strict exclusion alone does not give a finite bound. Likewise a membership oracle without a separating certificate does not satisfy hypothesis 3. Approximate separation requires a different precision/completeness statement.

## Owning two-moment instance

For Nima's tail engine:

- Z is the two-moment zonotope of the admitted atom-cap box.
- B is the four-bound source-support rectangle.
- D can be the 2m source facets.
- Greedy-profile membership returns a lift or a violated source facet.
- Planar vertex enumeration plus dual/Farkas routines solves the outer LP.
- Independent replay checks source support, lifts, retained frames and linear identities.
- The new state-bound certificate layer supplies expected-state/query comparison separately from arithmetic verification.

This recovers the existing 2m cut bound. The feasible-global-support fast path terminates earlier without changing the theorem. It does not yield constant worst-case work.

## What happens when atom audits are added?

For a finite fixed audit schema A, let

    L_A(x)=(U,V,(x_j)_(j in A)).

The image of the finite rational source box under this linear map is again a compact rational polytope. Its dimension may be smaller than the number of displayed coordinates. Equalities can be represented by paired inequalities. Therefore a finite inequality description and an exact rational LP formulation exist. Bounds on all coordinates give a bounded B.

This gives two distinct conclusions:

1. **Mathematical closure:** finitely many rational linear frames in L_A define a rational source-space LP. Explicit source-space construction provides exact optimization, inconsistency certificates and admitted witnesses in principle.
2. **Generative implementation closure:** the existing two-observable lazy interface cannot simply inherit that conclusion. It needs a validated separator for the joint image with a declared finite progress dictionary and an outer solver in the enlarged dimension, or a separately verified source-space LP backend. Its current two-dimensional cut and sparse-dual bounds do not transfer unchanged.

The audit-aware conditional section solves joint membership at supplied exact pins, including degenerate residual boxes. That is important but does not by itself establish a fixed finite-dictionary guarantee for all of its pin-dependent separators, or implement optimization over variable pins and arbitrary accumulated linear frames. Those additional obligations must be discharged, not inferred from fiber contractibility.

Nonlinear or discrete predicates, noisy audit semantics not reducible to the declared linear constraints, and additional source constraints are outside this instance. Some can be supported by other backends; the theorem does not decide them.

## Trust and identity boundaries

Finite separation proves mathematical completeness for a specified E. State binding proves that the returned proof addresses the independently expected E and query. Neither authenticates the observations or establishes that the caller retained an unknown earlier history.

No stage requires a canonical actual source, continuous section or audit-preserving witness interchange. Those are independent contracts. Query completeness may hold even where no comparison preserving declared audits exists.

## Disposition and next useful gate

The lane now has a sufficient refinement-closure theorem, its owning implementation instance and a precise audit-extension gap. Do not add another finite obstruction fixture. A substantive next implementation would choose one backend for general finite linear audit schemas and prove its certificate and termination contract—while recording the potentially larger dimension, dictionary and arithmetic costs.

This document is an analytical proof and code-contract synthesis, not a new executable verification run. Relevant owning notes:

- `research/nima/a-symbolic-tail-interface-answers-queries-without-materializing-all-facets.md`
- `research/nima/state-relative-query-certificates-require-an-independent-expected-history.md`
- `research/nima/the-symbolic-tail-section-can-preserve-explicit-atom-audits.md`
