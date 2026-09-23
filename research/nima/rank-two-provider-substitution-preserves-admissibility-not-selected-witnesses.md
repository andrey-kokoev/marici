# Rank-two provider substitution preserves admissibility, not selected witnesses

## Delivered distinction

Two live providers now realize DIFFERENT continuous exact sections of the same real retired rank-two domain. Both satisfy the complete original fine evidence, but they return different source vectors at an interior point.

A substitution gate accepts replacement under the contract

    return some exact admissible fine lift,

and refuses the same replacement under

    preserve the selected source vector.

A separate live provider of the same selected map passes the stronger gate. Thus the difference is in the promised task, not a blanket refusal to replace implementations.

This is contract-preserving substitutability, NOT unrestricted observational equivalence. A caller inspecting the numerical returned vectors can distinguish the providers. Their vectors are not being quotiented away or declared equal.

## One owning migration, two sections

Use the existing `one-sided-audit-evidence` retirement: m=3, retired audit 0, public coordinates

    U=t0+t1+t2,
    V=t0+t1/128+t2/16384,

with original fine bounds 0<=t0<=10, 0<=t1<=102, 0<=t2<=104. Its complete retired public domain is the already certified hexagon.

The first section is the four-triangle boundary fan from the previous rank-two attachment. The second adds the hexagon center and uses six triangles joining that center to successive boundary vertices.

The first section returns (5,51,52) at the center. The second assigns

    (5,51,52) + (1,-129,128)/1000.

The displacement has zero sum and zero weighted moment:

    1-129+128=0,
    1-129/128+128/16384=0.

Both source vectors obey every original cap and fine frame. Their original-atom infinity distance is 129/1000. This is a witnessed center displacement, not a claimed uniform distance bound between the sections.

Each section independently passes full polygon coverage, original fine vertex admission and shared-face source continuity. Convex interpolation then proves admissibility at every public point, not just at the center or sampled boundary points.

## Relational substitution versus map equality

For the admissible-lift contract, the proof obligation is that both providers satisfy the same fine-lift relation on the same full public scope. Equality of their chosen witnesses is unnecessary.

For the selected-vector contract, the checker examines every vertex of every intersection between a source triangle and a target triangle. On each such intersection the difference of the two source maps is affine. Equality at all intersection vertices therefore proves equality throughout that intersection, and hence throughout the covered polygon.

The six-cell replacement fails this stronger test. The refusal contains a rational point and two differing source lifts, and leaves the router's head unchanged. Its old selected map remains available.

The positive stronger-contract control uses an independent live session with the original four-cell map. Whole-domain map equality is verified despite the different live provider generation.

No closeness budget, optimization guarantee, actual-source identity or temporal continuity across substitution is inferred from the weaker contract. Each provider is continuous in its public argument, but replacing the selector can change a repeated query's returned vector.

## Verifier-observed provider premises

The gate accepts actual verifier-owned `FullPolygonSession` objects, not imported descriptors. Under locks it checks:

- the current provider handle and retained section identifier;
- the independently expected live state;
- the same owning migration and immutable fine context;
- full coverage of exactly the same declared current polygon;
- lift capability without archival re-exposure;
- the complete section certificate and retained encoding.

This implementation deliberately uses the same full-domain scope for both providers. Arbitrary partial-scope substitutions are not implemented.

The contract is fixed at router bootstrap. A caller cannot weaken it by editing a receipt. Successful substitution publishes a fresh router head only after all checks; a selected-map mismatch publishes nothing.

Queries check the current provider generation, retained section and fine context before delegating. The original provider may remain live in another session; replacement does not imply its data was erased or its storage reclaimed.

## Hostile controls

Eight additional refusal controls cover a stale router head, archival escalation, a forged provider descriptor, foreign migration metadata, an altered scope, a caller-edited contract, a stale active provider and a stale replacement candidate.

The stale-provider controls use a REAL subsequent public refinement U<=162. Although the center still belongs to the smaller domain and the old section encoding still exists, the old provider generation cannot serve as authority for the router's admitted full-domain scope. A new live comparison is required.

Fine-history identity is never selected by this gate. The common migration/fine-context binding establishes which constraints the witnesses must satisfy; neither witness is claimed to be the actual hidden source.

## Replay and costs

`verify_rank_two_provider_substitution.py` imports no router. It freshly verifies the owning migration, both full-domain sections, the common-refinement comparison, reported source answers and the genuine public refinement used by the stale-handle control.

It shares the established exact geometric and owning-source kernels. It does not authenticate historical live handles from JSON; generation validity and atomic refusal behavior are exercised in process.

The source and replacement have four and six cells respectively. The router currently retains a serialized copy of its admitted section in addition to the live provider's copy. Receipts account separately for that router record, provider polygon encodings and provider fine context. Comparison constructs triangle intersections, and queries still scan the selected provider's cells. This is not a compression benchmark or an optimal point-location algorithm.

## Structural consequence

The previous rank-one provider cone compared different encodings of one affine source map. This example separates two notions that coincided there: satisfying the same scoped lifting relation and preserving the selected lifting function.

It supplies a rank-two operational comparison under an explicit task contract. It does not yet decorate a full rank-two nine-vertex cone, identify analytic presentation roles or prove higher coherence for witness-changing substitutions.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_rank_two_provider_substitution.py
    uv run --with sympy python research/nima/checkers/verify_rank_two_provider_substitution.py

Implementation: `research/nima/checkers/rank_two_provider_substitution.py`.

Artifacts: `research/nima/results/rank-two-provider-substitution*.json`.

The earlier full-polygon attachment replay also passes.
