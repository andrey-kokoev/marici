# Supplied overlaps and bounded joining routes

## Scope

The added `rules.mjs` APIs classify a supplied pair of applicable matches and
check explicitly supplied continuations. They do not enumerate matches, enumerate
critical pairs up to isomorphism, prove minimality, search for joins, or establish
global confluence. Visualization is unchanged.

## 1. Classify the actual peak

`analyzeOverlap(store,a,b)` requires two checked plans at the same exact revision.
It records:

- shared matched occurrences, with each rule's deletion/preservation flags;
- directional delete-versus-match conflicts;
- fresh-allocation collisions, separately from structural deletion conflicts;
- whether the two match images jointly cover the host incidence object, and the
  host records they leave uncovered;
- whether the previously implemented sufficient independence criterion is met.

Shared preserved vertices are not deletion conflicts. Joint coverage is a useful
condition for investigating a critical overlap, but the API does not promote it
to an exhaustive critical-pair classification. Model context and provenance are
still retained at the source revision.

## 2. Supplied finite continuations

`checkSuppliedJoin(store,a,b,leftSteps,rightSteps,options)` executes each initial
rule application, then only the supplied branch continuations. A continuation
step contains a checked rule, explicit match components at the current branch
object, and any fresh allocation. Every step is planned through the existing
two-pushout checker and applied at its exact revision boundary.

The default bound is 16 continuation steps per branch; callers may choose a bound
from 0 through 64. Initial peak applications are additional to that count. This
is a route-length bound, not a graph-size, memory, or general execution quota.

Execution takes place in an isolated replay store. The caller's history and heads
are unchanged. The returned dependency-complete bundle contains both actual
branches; the witness binds their applications, supplied programs, engine digest,
source peak, terminal revisions, and full-state IDs.

Results have deliberately narrow meanings:

- `joined`: the supplied continuations reach exactly equal full states, checked
  by both normalized data and digest;
- `notJoined`: these supplied continuations have unequal endpoints;
- an execution refusal: one of these continuations is not a valid checked route.

Neither of the latter two proves that another rule, match, or longer route cannot
join the peak. An empty continuation is allowed: the initial branch endpoints
may already have equal states despite different derivation histories.

`verifyJoinWitness(store,witness)` reconstructs the peak and both programs in a
fresh store and compares the complete recomputed witness. Changing a status to
`joined` and recomputing its content digest does not pass replay.

## 3. Distinguish independence from joinability

A test peak starts with two directed edges u and v. Rule A matches both but deletes
u; rule B matches both but deletes v. Each deletes a record in the other's match,
so the sufficient parallel-independence criterion fails.

The immediate endpoints each contain one edge but are not equal states. Supplying
a residual single-edge deletion on each branch joins them at the same three
vertices with no edges. Both routes are checked; neither history is erased.

A second test uses distinct derivations of the same deletion. Independence still
fails, but the peak joins with zero continuation steps. A third test separates
fresh-ID collision from deletion overlap: identical allocated IDs block sequential
independence without establishing that the peak endpoints are unjoinable.

These examples refute the inference from failed independence to nonjoinability.
They do not prove confluence of the rule system.

## 4. Categorical interpretation

A joining witness compares two paths after projection to complete construction
states. The terminal revision IDs generally differ because their parent chains
and rule declarations differ. The witness does not identify these histories or
supply a literal 2-cell between parallel arrows in the revision category.

Higher composition of comparison witnesses requires its own boundaries and laws.
It is not inferred merely because several finite joins have been checked.

## 5. Verification and remaining boundary

```
node --test tests/isotope-wiring-overlaps.test.mjs
```

Eight tests cover shared preserved records, conflicting overlaps, host coverage,
count-equal but unequal endpoints, supplied residual joins, zero-continuation
joins, allocation conflicts, route bounds, invalid matches, and forged witnesses.

[CENSUS.md](CENSUS.md) now adds bounded enumeration with explicit fixed-pattern
host-isomorphism conventions and partial-coverage reporting.
[JOIN-SEARCH.md](JOIN-SEARCH.md) now explores bounded continuations with explicit
allocation-policy limits. Stronger criticality and global confluence remain open. Predicate-result
transport is addressed in [SELECTIVE.md](SELECTIVE.md), with cross-process replay
in [VERIFICATION-BUNDLES.md](VERIFICATION-BUNDLES.md).
