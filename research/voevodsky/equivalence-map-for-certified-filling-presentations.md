# Equivalence map for certified filling presentations

## Fixed parameters before comparison

Fix the source, public observer, state class, admitted queries, allowed continuations, witness identity and cost model. Let X,Y be nonempty compact public possibility sets in R^d unless emptiness is explicitly allowed. Distinguish mathematical answers from full response packets; a packet may expose source witnesses invisible to the public query language.

## The implication map

    equal public sets
        => equal answers to every extensional public query
        => equal answers to any restricted public query language

    equal public sets
        <=> equal feasibility after every exact public-point refinement

    equal public sets
        <=> equal linear support functions       [compact CONVEX sets]

    equal linear support functions
        <=> equal closed convex hulls            [compact sets]

    current public-set equality
        => equivalence under public-only evidence continuations
        -/-> equivalence under arbitrary audit re-exposure

    source-relative audited witness equivalence
        => equal audit ranges
        -/<- equal audit ranges alone

    checked certificate translation both ways
        => answer transfer for queries covered by those translations
        -/-> efficient translation under an unspecified cost budget

The extensional-query arrow only has a converse if the declared queries separate states. Bidirectional certificate translation also needs matching statement translations and preservation of query/answer semantics; translating arbitrary bytes is not enough.

## 1. Query and refinement equivalence

For membership queries at every point, query equivalence is simply set equality. Refinement by the exact point y followed by feasibility is the same test. For compact rational polytopes, rational point tests suffice: rational points are dense in each such polytope, including lower-dimensional ones, and a closed unequal counterpart misses a relative neighborhood of some rational point. This conclusion need not hold for arbitrary sets or arbitrary restricted test languages.

Linear support answers determine the closed convex hull by separating hyperplanes. Thus for compact convex states they already determine membership semantics, even though obtaining membership from an optimization oracle with a finite certified procedure requires additional algorithmic assumptions. Semantic determination is not an algorithm or complexity bound.

For nonconvex states this implication fails. The sets {0,2} and [0,2] have identical support in every scalar direction. Refining by 1/2<=x<=3/2 leaves the former empty and the latter nonempty. Current support equivalence is therefore not generally a congruence for even closed linear refinements. This counterexample does not contradict the owning convex-polytope interface, whose carriers' linear images remain convex under retained linear frames.

Restricted refinements may fail to detect geometry. With only upper-threshold refinements x<=r followed by feasibility, the intervals [0,1] and [0,2] are indistinguishable: every finite history reduces to a tightest upper threshold, and both survive exactly when it is at least zero. A maximization query distinguishes them. The continuation language and terminal query must both be specified.

## 2. Continuation equivalence

For a public map L and public predicate f,

    L(C intersect L^-1(f))=L(C) intersect f.

Hence equal public images are a congruence under all public predicate additions. Adaptive choices based only on equal public answers follow equal branches. The owning parallel-segment example in `sufficient-state-is-relative-to-permitted-continuations.md` proves failure after a hidden audit is re-exposed. This arrow is already settled; no new fixture is needed.

Schema extension without new evidence preserves source carriers, but it enlarges the query language. It can therefore distinguish states previously equivalent only at the coarse observation. Merely saying 'the update preserves possibilities' does not prove that a previous coarse quotient supports that update.

## 3. Audited witness equivalence

An equivalence of fibers commuting with an audit map necessarily preserves attainable audit values. Equality of those values is insufficient: a discrete two-point fiber and a singleton can both carry the same constant audit but admit no bijection or discrete homotopy equivalence. Additional structure within audit fibers matters.

Owning analytical examples already exhibit both outcomes: disjoint raw-audit ranges block every audit-preserving map, while a source-certified product trivialization with a complete audit coordinate supplies unique coherent transport. Ordinary contractibility and selected feasible witnesses do not supply audit-preserving identity automatically. This branch needs no additional experimental program unless an API promises witness transport.

## 4. Certificate equivalence and resource-sensitive translation

Specify a presentation-specific proof relation Verify_P(statement,packet). A translation P->Q needs:

1. a statement map preserving the intended source/query semantics;
2. a packet map taking every admitted P proof in its stated domain to a Q proof;
3. independently checkable preservation of the answer;
4. a declared operational domain, including what happens on unsupported requests.

Two opposite maps need not be inverses on packet syntax or selected witnesses. They also need not be cheap. Without restrictions, a purported translator could simply invoke a complete target solver; this is much weaker operationally than algebraic proof transport.

Nima's precision-to-full-schema bridge provides a substantive direction: insert pins in primal witnesses, translate row weights and cancel pinned-coordinate coefficients with pin equalities. It does not re-solve. The source-set translation has an inverse, but that alone does not certify an implemented inverse translator for every general packet: the reverse domain must restrict target states to the translated pinned subfamily, and all proof forms must be accounted for.

Resource assertions must separate:

- state/schema/history expansion;
- number of nonzero multipliers;
- total encoded packet bits, including repeated statements;
- translation arithmetic and bit complexity;
- verification work;
- any solver calls required by translation.

A polynomial bound may still be unsuitable for a promised constant-size interface. Conversely a larger one-time migration proof may permit a smaller long-lived state under a different retention policy. No universal resource equivalence follows merely from semantic equivalence.

## Settled and unresolved arrows

| Arrow | Status | Evidence |
| --- | --- | --- |
| Convex public set equality <=> support equality | Mathematical theorem | Compact separation argument |
| Public set equality <=> unrestricted exact-point feasibility tests | Definition/theorem | Point refinement is membership |
| Support equality => refined feasibility for nonconvex states | False | {0,2} versus [0,2] |
| Public-image equality => public-only continuation equivalence | Proved | Image/intersection identity |
| Public-image equality => fine-audit continuation equivalence | False on owning source | Parallel tail segments |
| Equal audit ranges => audited witness equivalence | False generally | Constant-audit fibers with different discrete cardinalities |
| Specialized precision proof => full-schema proof without re-solving | Implemented and independently checked | Nima bridge |
| Every general proof on translated pinned states => specialized proof without re-solving | Target for a precise proof-domain theorem and implementation | Must handle equality corrections, source rows and proof normalization |
| Bidirectional proof translation => comparable costs | Unresolved until costs are specified | Measure and bound both translations, not just solver workloads |

## Next gate

Do not test all equivalences independently. The outstanding useful task is to define the reverse domain of the existing bridge, construct reverse certificate translation without optimization, and account for growth in both directions. A successful result would show when the specialized and general backends are operationally interchangeable while preserving expected-history binding. A failed proof form would identify a real interface mismatch rather than another geometric example.

This document is an implication/proof map, not a new executable run. It distinguishes established mathematical arrows, owning implementation evidence and remaining obligations.
