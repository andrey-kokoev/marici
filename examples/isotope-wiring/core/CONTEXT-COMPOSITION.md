# Concrete coherence of composed context lifts

`context-composition.mjs` compares context lifting through `G -> H -> K` with
lifting directly through the composite `G -> K`. It builds on
[CONTEXT-LIFTING.md](CONTEXT-LIFTING.md), retaining the original persistent join,
both context constructions, their applications, and every checked intermediate
embedding. Visualization remains unchanged.

## API

```
const result = checkContextLiftComposition(
  baseStore, persistentWitness,
  middleStore, middleRevision, firstEmbedding,
  outerStore, outerRevision, secondEmbedding,
  { middleAllocations, outerAllocations },
)

verifyContextLiftComposition(
  baseStore, middleStore, outerStore,
  JSON.parse(JSON.stringify(result.certificate)),
)
```

Both supplied embeddings must be checked monic attributed morphisms, with the
exact shared middle object. A nonmonic second embedding is refused even if its
restriction to the base image happens to be monic.

The result contains a composition certificate plus dependency-complete base,
middle, and outer revision bundles. None of the caller stores or branch heads
is changed. Each level may have its own context and metadata; structural
embeddings do not assert a translation between those interpretations.

## What is constructed and checked

First, the existing lifting API constructs the join in H and the direct join in
K. The latter uses the composite source embedding. Then each H application is
reconstructed alongside its corresponding K application. The checker verifies:

1. The K match is the H match followed by the current H-to-K embedding.
2. The next H-to-K embedding is monic, follows retained occurrences and actual
   allocation correspondences, and makes both retained and comatch squares commute.
3. At every step, composing G-to-H with H-to-K equals the independently constructed
   direct G-to-K embedding, as checked morphisms, not merely equal cardinalities.
4. At the endpoints, the extended comparisons commute with the final H-to-K maps:

\[
h_K\circ j_L = j_R\circ h_H.
\]

The checker also records and verifies images of H's persistent source occurrences,
fixes the original K context outside the second embedding, and checks that this
outside context together with the embedded H endpoint covers the K endpoint.
The outside occurrence collection need not be a closed subdiagram.

The shared `extendContextEmbedding` helper requires admitted rule plans, checks
the actual transported match, and constructs the step embedding. It does not by
itself certify a whole history or a model predicate. Whole-history boundaries are
checked by the lifting and composition APIs.

## Allocation programs are part of the comparison

Middle allocation overrides have the same per-application shape as ordinary
context lifting. Outer overrides have the same shape, but their default is the
**resolved middle allocation**, as in an iterated lift. Null outer slots inherit
that middle choice; they do not reset to the original base spelling.

If a middle fresh name already occurs in the outer context, the default staged
allocation is refused. An explicit outer override can resolve the collision.
The normalized programs are retained in the two constituent certificates.
Consequently this is coherence for the declared allocation choices, not a claim
that arbitrary fresh-name policies produce literally equal results.

## Identity and associativity cases

Identity-context tests use the same exact source revision and the same allocation
program. Lifting through that identity recovers the original application receipts
and identity intermediate maps. It does not insert an identity rewrite event or
identify different source histories that happen to have equal objects.

For a concrete triple `G -> H -> K -> L`, tests compare both parenthesizations
with fixed allocations at each level. They check equality of the direct outer
lift certificates and equality of the composed intermediate endpoint maps.
Middle histories and the two composition certificates remain separately recorded;
only the checked comparisons and selected outer effects agree.

These are executed coherence checks for the supplied finite data. They are not
a proof-assistant-certified universal functoriality, associativity, or higher
coherence theorem. There is no quotient of provenance.

## Replay and scope

The certificate binds both constituent lift certificates, the second embedding,
every step embedding, persistent images, context coverage, the endpoint square,
and the engine digest. Replay reconstructs all computations and compares the
complete certificate. Rehashing forged stage maps, false coverage, or a false
comparison square does not pass.

Missing source histories, wrong engines, incompatible embeddings, and allocation
collisions are refusals. Failures do not publish partial histories into caller
stores. Returned histories can be audited separately with `verifyRuleHistory`.
The mechanism does not imply model validity or inherited verification, and it
provides no general resource sandbox or automatic storage/publication protocol.

## Executed checks

Eight tests in `tests/isotope-wiring-context-composition.test.mjs` cover two-stage
creation/deletion, inherited allocation choices, concrete identity and associative
cases, nonmonic second embeddings, unadmitted plan-shaped data, outer collisions,
forged certificates, missing dependencies, and caller-store nonmutation.

The sixteen structural suites contain 162 tests. Universal context/coherence laws,
global critical-pair/confluence results, allocation-policy completeness, and
formal predicate read-contract certification remain open.
