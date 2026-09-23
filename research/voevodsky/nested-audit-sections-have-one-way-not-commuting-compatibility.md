# Nested audit sections have one-way, not commuting, compatibility

Let R_A(x)=s_A(L_A(x)) for the owning conditional section and let A subset B. Because the finer contraction preserves L_B and hence L_A, there are exact identities

    R_A R_B = R_A,
    R_A H_B(-,t) = R_A.

These hold for all source points and real times, not just sampled controls. Each R_A is idempotent. But R_B R_A need not equal R_B. The original and coarsened points can have different newly audited coordinates.

## Exact owning counterexample

For m=3, x=(0,1,0), A empty and B={0}, the implementation gives

    R_A(x)=(1/129,0,128/129),
    R_B(x)=(0,1,0),
    R_B(R_A(x))=(1/129,0,128/129).

The last operation pins the coordinate of the changed representative, not the original observation x_0=0. With two remaining coordinates, the moments then uniquely determine that representative. The coarse center violates the original newly supplied audit and must not be accepted as a witness for it.

There is no contradiction with the audit-aware constructor: using the original moments and the independently retained original pin x_0=0 reconstructs R_B(x) correctly. The lost datum is not recoverable by auditing an arbitrary representative instead.

## The commuting object is the observation, not the chosen lift

Dropping the B-minus-A coordinates defines a projection p with L_A=p L_B. This observation square commutes strictly. The selected sections do not commute strictly with this projection: generally s_A p differs from s_B as source-valued maps.

Both resulting witnesses share L_A. Their straight-line interpolation is an admitted comparison in the coarse fiber, continuous in the finer observation. It is not generally a comparison preserving B. Thus schema refinement admits a coarse homotopy comparison without authorizing loss of the newly declared audits.

For a fixed schema, restriction by visible evidence still commutes with the same contraction. Changing the schema is a distinct operation: it changes the equivalence whose fibers may be contracted.

## Implementation consequence

Keep source possibilities and admitted observations separate from a selected certificate witness. On schema extension, use the original observable state plus independently supplied audit values to construct the conditional section. Do not promote a representative's coordinate to newly observed evidence. A contradictory representative can be discarded without discarding a consistent underlying state.

## Checks

    python research/voevodsky/checkers/check_nested_audit_sections.py

216 nested contraction/comparison controls passed for m=3,4,8,16. Among 72 schema/source comparisons, 55 have R_B R_A != R_B. This checker uses the owning section implementation directly; it is not an independent verifier. The general one-way identities follow from preservation of the enlarged observations.

Artifact: `results/nested-audit-sections.json`.
