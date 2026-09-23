# An observation-refinement calculus for certified filling interfaces

## Semantic types

Fix a source presentation P with declared source identity. A schema is an observation map O_A:P->Y_A and a declared query language. Evidence E is a predicate on Y_A, together with its retained syntax and admission context. A state denotes

    C(A,E)={x in P : E(O_A(x))}.

Keep four types distinct:

- State: a presentation of all admitted possibilities, bound to source, schema and evidence.
- Witness(C): one source point together with a proof of membership in C.
- Query(C): a declared question about C, with exact quantifier/accuracy semantics.
- Certificate(expected state, expected query, answer): checkable evidence for that statement.

A solver output is not a State. A Witness is not an observation of the actual source. An externally expected statement must not be reconstructed solely from the response being checked.

## Five typed operations

### 1. Add evidence

    add : State(A,E) x AdmittedFrame(A) -> State(A,E and f)

The source and schema are fixed. C_new subset C_old. Feasible witnesses for the new state remain valid for the old one; old witnesses may fail the new frame. Universal claims valid on the old set remain true on the subset, but if the API's FORCED statuses require nonemptiness, the old feasible witness cannot establish that additional obligation. Old inconsistency remains inconsistency.

For maximization over nonempty carriers, refinement cannot increase the maximum. A previously certified upper bound remains a bound; its old optimizer need not remain feasible. A state-bound old packet is not automatically accepted as a new packet even when a semantic consequence persists.

### 2. Extend schema

Suppose O_A=p O_B, where p forgets newly exposed coordinates. Define

    expose : State(A,E) -> State(B,E composed with p).

The source carrier is exactly unchanged. Queries expressed in the old language translate through p and retain their answers. Additional audit values are not supplied by expose. They require a separate evidence-addition operation.

The square involving add and expose commutes for an old-language frame f:

    expose(add(E,f)) = add(expose(E), f composed with p)

at the level of denotation, and under a canonical translation at the level of frame tuples. This law does not assert commutation of selected witness contractions: the owning selectors satisfy R_A R_B=R_A, but the reverse composite need not equal R_B.

### 3. Replace backend or encoding

    implement : Presentation(C) -> AnotherPresentation(C)

The obligation is equality of denotation and preservation of declared query semantics, not equality of returned witnesses. Each solver may return a different optimizer when optima are tied. Independent verification against the same expected statement supplies a common acceptance boundary.

Finite workloads compare implementations; they do not establish denotational equivalence of arbitrary encodings. The source-space translation used here has an exact linear pullback proof. The exhaustive and simplex solvers then propose certificates for the same translated problem.

### 4. Select a representative

    select : NonemptyState(C) -> Witness(C)

There is deliberately no generic coercion Witness(C)->EquivalentState(C). Replacing C by the singleton of the selected witness is evidence strengthening without an admission warrant. Evaluating a new atom audit on that witness is not a measurement of the actual source.

A continuous section can additionally supply a contraction under a specified homotopy identity. This still does not preserve every declared query. Query-preserving contraction requires invariance of those queries along its paths; raw atom audits can prohibit it.

### 5. Forget through an observation

Let p:Y_B->Y_A and O_A=p O_B. For a refined carrier C define its coarse saturation

    forget_A(C)=P intersect O_A^-1(O_A(C)).

Then C subset forget_A(C), and both have exactly the same O_A image. Hence every query determined solely by that image has the same answer: coarse point membership, optimization of functions of O_A, and possible/forced predicates of O_A (with the same nonemptiness convention).

This is a semantic preservation theorem, not a claim that O_A(C) is cheap to compute or represent. It also does not preserve queries inspecting discarded witness coordinates, multiplicities or identity structure. If C was already A-saturated, forgetting changes nothing.

Dropping selected frame rows is generally NOT this operation. To preserve coarse queries one must retain the exact projected relation, including consequences of the forgotten-coordinate constraints. For example, from U=h and h<=1 one must retain U<=1 after forgetting h; deleting the second row and existentially dropping h admits every U.

## Composition laws and deliberate nonlaws

- Evidence conjunction is associative and commutative denotationally; ordered history bindings need not be equal.
- Successive schema extensions compose by composition of projections.
- Schema extension and old-language evidence pullback commute.
- Backend change is semantically invisible when its translation theorem and certificate obligations hold.
- Saturation is extensive and idempotent for a fixed observer; saturations for different observers need not commute.
- Selection is not an inverse of forgetting, nor a way to reconstruct discarded audit observations.
- Forcing a coarse query commutes with exact coarse projection; reconstructing all fine witnesses does not follow.

These laws are source-relative. Changing P is another operation requiring an explicit relation between source models; it must not be disguised as frame addition or coordinate renaming.

## Executable instances already available

| Operation | Existing evidence |
| --- | --- |
| add | Nima's retained-halfspace and two-free measurement histories; stale packets rejected |
| expose | Schema-relative source-space reference inserts zero coefficients for new audits, preserving every old source row |
| implement | Exact simplex packets independently verified and compared with exhaustive reference values |
| select | Symbolic and audit-aware greedy sections, with explicit source witnesses and identity scope |
| forget | Saturation results prove preservation limits; no general projection API implemented here |

The attached small finite semantic checker tests the operation laws on the bounded integer grid of the three-atom tail source. This grid is an auxiliary test domain, not a new analytical admission claim or proof of the continuum laws. It also checks that coarse-query preservation under forgetting can coexist with loss of a fine audit. The continuum statements follow directly from the displayed preimage/image identities.

## Implementation direction

A future unified API should give add, expose, select and projected forget distinct names and return types. Backend choice belongs behind a common certificate interface. Each certificate binds an independently expected source, schema, evidence history, query and accuracy convention. Operation-specific proof objects may justify translated queries or projected relations; a generic 'refine' method should not silently perform all these operations.

This document is a semantic contract, not an API refactor. It identifies a substantive next gate: exact projected forgetting with proof that all retained coarse queries are preserved, or an explicit refusal when the chosen representation class cannot express the projection. That gate is stronger than deleting history or returning one lift.

## Reproduction

    python research/voevodsky/checkers/check_observation_refinement_laws.py

Artifact: `results/observation-refinement-laws.json`.
