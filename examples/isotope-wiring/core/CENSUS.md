# Bounded census of labelled rule overlaps

`overlap-census.mjs` extends the supplied-peak machinery in
[OVERLAPS.md](OVERLAPS.md). It enumerates incidence-closed, label-preserving partial
bijections between the left-hand patterns of two checked monic rules.

## Coverage convention

At each sort, two monic matches identify a partial bijection between their source
records. Naturality forces that relation to be closed under every incidence map;
attribute preservation forces identified labels to agree. These selected records
form an interface, with an inclusion into each left-hand pattern. Their attributed
pushout constructs the overlap host and its two matches.

Conversely, if two monic matches jointly cover a host, their intersection gives
such an interface. Pointwise, the pushout of that intersection is their union, so
joint coverage gives an isomorphism to the original host commuting with both
matches. This is the mathematical coverage argument behind the enumeration;
there is no proof-assistant certificate for its implementation.

**Complete** means all such relations for these two fixed, labelled patterns have
been examined. Host isomorphisms must commute with both match legs. Rule or pattern
automorphisms are not quotiented out. Extra host context is not enumerated: the
constructed host is exactly the union of the two match images. Full-state metadata,
model contexts, and alternative coordinate-frame identifications are not part of
this classification.

This is a finite overlap census with explicit applicability checks, not a general
critical-pair/confluence theorem. In particular, it does not certify minimality,
strong joinability, model preservation, or joinability in arbitrary larger hosts.

## APIs

```
const census = enumerateRuleOverlaps(ruleA, ruleB, {
  maxSearchNodes: 10000,
  maxCandidates: 256,
  maxPatternRecords: 24,
})
verifyOverlapCensus(JSON.parse(JSON.stringify(census)))

const c = census.candidates.find(c => c.classification === 'dependentPeak')
const peak = materializeRuleOverlap(ruleA, ruleB, c.identifications)
// Supply continuations explicitly, using OVERLAPS.md's checked join API:
const join = checkSuppliedJoin(peak.store, ...peak.plans, leftSteps, rightSteps)
```

Each candidate is classified as:

- `independent`: both rules apply and the existing sufficient independence
  criterion passes;
- `dependentPeak`: both apply, but that criterion fails; joinability is unresolved;
- `notCoApplicable`: a structural dangling condition prevents at least one rule
  from applying at this host. This is not a two-branch peak.

Only the expected dangling refusal is classified as non-applicability. Unexpected
engine errors abort rather than being counted as mathematical negative results.
New records receive disjoint deterministic allocations for the two rules, so
arbitrary fresh-name collisions do not manufacture overlap conflicts. Explicit
allocation conflicts remain available in the supplied-peak API.

Materialization returns an isolated store, checked plans when applicable, and the
serialized candidate. It does not mutate any existing construction history.

## Bounds and replay

The default limits are shown above. Hard accepted maxima are 1,000,000 search
nodes, 4,096 materialized candidates, and 128 total left-pattern records.
Exceeding the pattern-size bound refuses the request. Reaching a traversal or
candidate limit returns `partial` with `exhaustedBy`; a partial prefix with zero
dependent peaks is not evidence that there are none.

Search-node count includes partial assignments and leaves. Incidence closure is
checked at leaves; `closedRelationsVisited` can exceed the returned candidate
count by one when the candidate cap stops materialization. There is no resumable
cursor: increase the limits and rerun. These are enumeration bounds, not a general
memory, label-size, or execution sandbox.

The census binds both serialized rules, limits, candidates, counts, and engine
source digest. Replay reconstructs both rules and reruns the exact traversal.
Rehashing a false count or a `partial`→`complete` claim does not pass replay.

## Executed boundaries

Nine tests in `tests/isotope-wiring-census.test.mjs` cover:

- Eight closed overlaps of two directed-edge deletion patterns: seven independent
  and one dependent. All seven independent cases produce replayable commuting
  squares; the dependent case has a checked zero-continuation join.
- Isolated-vertex patterns of sizes zero through two, compared against the
  partial-bijection counting formula `sum_k choose(n,k) choose(m,k) k!`.
- Dangling vertex-deletion overlaps, label mismatch, noninjective relations,
  nonclosed incidence, empty-pattern creation, and distinct fresh allocations.
- Honest partial coverage at node/candidate bounds and refusal of forged census
  claims even when their hashes are recomputed.

[MATCHING.md](MATCHING.md) now enumerates monic exact-label matches in a fixed
host, including discovery of residual occurrences for supplied joining routes.
Next obligations include larger independent enumeration oracles, pattern/rule
symmetry reduction, stronger criticality conventions, and conditions under which
local comparisons extend to larger hosts. [JOIN-SEARCH.md](JOIN-SEARCH.md) now
searches bounded multi-step continuations under an explicit fresh-name policy. A complete
census of one rule pair is not global confluence of a rule system.
