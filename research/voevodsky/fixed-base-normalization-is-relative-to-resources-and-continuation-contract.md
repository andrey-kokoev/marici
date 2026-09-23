# Fixed-base normalization is relative to resources and continuation contract

## The missing premise

Our polyhedral based cone required that refinement preserve the base attribute. That is not sufficient for an operational identity: two presentations may retain identical numbers but differ in what continuations their available resources can implement.

Use an enriched base package

    B_C=(semantic base, retained data, resource access, authority root; C),

where C is an explicitly scoped task repertoire. An allocation and an allocation-plus-pricing-backend are different operational objects for a contract promising fresh queries.

## A sufficient fixed-base rule

For the restricted implementation class tested here, base normalization is admitted only when:

1. the same declared semantic base survives;
2. the authority root is unchanged;
3. every task promised in C remains supported;
4. the already checked providers and their required retained dependencies remain available and unchanged.

These conditions are sufficient for reusing those implementations. They are not necessary for every possible realization: a different certified algorithm might implement the same task with different resources. Such provider substitution would require its own simulation/equivalence certificate, not merely matching capability flags.

The executable gate receives verifier-observed live-service facts. It is NOT a public endpoint that authenticates arbitrary caller-supplied resource dictionaries. Copying the fields of a successful snapshot cannot create the underlying checked provider.

## Positive live control: a surviving section base

Bootstrap the real owning forced-zero migration and its full two-cell segment section. Choose the retained base B={(u,u):0<=u<=1/2}. Append the public frame U<=3/4.

Both endpoints of B satisfy the new affine frame, hence the entire base survives. The same checked section, original fine context and source-rule binding remain available. The live service returns exact source lifts at both endpoints and the midpoint before/after restriction as applicable. Thus the unchanged-provider rule accepts fixed-base normalization for exact lifting ON B.

The base is not the entire old public domain: the old endpoint U=1 is excluded. Declaring the original whole domain unchanged would be false. The resource contract and domain scope are both essential.

## Negative live control: identical capsule, reduced repertoire

Bootstrap Nima's allocation-continuation wrapper against the current owning moment-column verifier. A fresh query passes before detachment. Detach the backend, retaining exactly the same allocation-capsule digest.

With the source-verification, pricing, graph-construction and admission entrypoints replaced by traps:

- current allocation replay succeeds unchanged;
- a fresh query is refused before a trap can run;
- the full replay-plus-fresh-query fixed-base gate refuses collapse;
- the replay-only gate accepts collapse;
- setting a fresh-query capability flag without its provider is rejected.

Thus identity is RELATIVE TO C. Detachment can be observationally the identity for saved-allocation replay while not being the identity for a richer continuation contract. It is a capability-losing arrow, not an unconditional base degeneracy.

## Geometric obstruction remains separate

The control freshly verifies all six exposure/pricing certificates against the CURRENT owning kernel. The explicit first-five-column dictionary has support 19 where the full source has support 20. This establishes dictionary incompleteness in the declared column model.

It does not prove that every resource-free computation is physically impossible, that the actual saved allocation capsule is this illustrative dictionary, or that the mathematical source cannot be reconstructed from external code. The live test establishes backend refusal; the exposure proof establishes a separate representation obstruction. Neither is silently strengthened into absolute information erasure.

## Consequence for the cone

A geometric cone filler and a resource-aware cone filler are different assertions. To decorate the earlier based diagram operationally, every face must carry its scoped task implementations and dependency/authority bindings. Identifying a base edge then requires the resource-aware gate in addition to geometric preservation.

The current work supplies that gate and live positive/negative controls. It does NOT yet attach these services to every vertex and face of one complete enriched nine-vertex diagram. The previous geometric cone and today's live-service controls have different underlying bases; they must not be conflated merely because both pass a local criterion. Full decorated-cone composition remains a further obligation.

## Verification status and provenance caveat

    uv run --with sympy python research/voevodsky/checkers/check_resource_aware_base.py

Artifact: `results/resource-aware-base.json`.

The new live-service checker passes, including fresh six-exposure arithmetic. A separate attempt to replay Nima's archived `verify_allocation_continuation_checkpoint.py` stopped at its source-binding check: the current `research/grothendieck/checkers/verify_active_cap_moment_master.py` hash differs from that archived report. This is a provenance mismatch before semantic replay, not an observed arithmetic failure. No upstream artifact or binding was rewritten to hide it.

The direct current-kernel checks here do not repair or validate the stale report's historical bindings. They establish the narrower fresh workload described above.
