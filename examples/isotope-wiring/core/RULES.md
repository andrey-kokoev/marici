# Linear typed rules, match transport, and independence witnesses

## Implemented fragment

`rules.mjs` implements explicitly matched linear attributed rules over the checked
finite-diagram kernel. It constructs both double-pushout squares for an application,
compiles their result into a revision-bound ground edit, and checks bounded
parallel-independence witnesses by replaying both routes.

The visualization remains disconnected. [MATCHING.md](MATCHING.md) now adds
bounded exact-label automatic matching, and [CENSUS.md](CENSUS.md) enumerates
bounded fixed-pattern overlaps. Attribute-variable unification, negative
application conditions, global model guards, termination proofs, and general
confluence remain outside the implemented fragment.

## 1. Rules and matches

A rule is an attributed span

\[
L\xleftarrow{l}K\xrightarrow{r}R
\]

with both legs monic. K is the retained interface, L is the required pattern,
and R is its replacement. All incidence maps and labels are checked; names alone
do not identify records. IDs on K, L, and R may differ because the legs are
explicit maps.

`defineRule(name,left,right)` returns a frozen content-addressed rule. `exportRule`
and `importRule` retain/check the full schema, objects, labels, and both maps.
Import does not infer a rule from a matching name or count.

An application supplies a monic attributed match `m:L -> X`. The match must target
the exact checked object at the specified revision. Reuse means supplying another
valid explicit match, not assuming that a similar drawing carries the same rule.
Fixed model labels constrain reuse: this fragment has no schematic label variables
or inferred frame transport.

`subdiagram` accepts an explicitly closed selection. `generatedSubdiagram` closes
chosen records under outgoing schema arrows. Neither deletes incoming references
from an ambient object. Those references matter to rule applicability.

## 2. Constructing and checking the two pushouts

For each sort, remove `m(L minus l(K))` from X to form a candidate D. Since m and l
are injective, the deleted and preserved occurrences have unambiguous images.

If a remaining record points to a deleted record, the candidate is not a
subdiagram. The planner returns `rule-dangling-condition` with the offending
incidences; it does not cascade-delete those records. With a closed complement,
retain the maps `K -> D` and `D -> X`.

Construct the attributed pushout of `L <- K -> D`. Its canonical factor to X is
built from m and the inclusion `D -> X`. The kernel checks that this factor is
an attributed isomorphism. Thus the first square is checked through its universal
comparison, not through equal cardinalities.

Construct the second attributed pushout of `D <- K -> R`. Its apex is the
replacement object. For readable persistent occurrence identity:

- every D record retains its host ID;
- every record in R outside r(K) receives an explicitly supplied fresh ID;
- allocation must be injective within each sort and disjoint from all original
  host IDs, including deleted ones;
- an explicit attributed isomorphism renames the pushout-generated IDs to these
  chosen IDs.

This produces maps `D -> Y` and `R -> Y`. The result is a checked two-pushout
application in this monic attributed fragment, not a claim that an arbitrary
JSON patch has DPO semantics. The categorical interpretation rests on the
pointwise universal constructions described in `CLOSURE.md` and `ADAPTER.md`;
the code is tested, not theorem-prover certified.

## 3. Compilation, provenance, and application

`planRewrite(store, inputRevision, rule, match, allocation)` constructs the above
objects without changing the caller's store. It compiles deletion/addition lists,
then replays that ground operation in a separate store to check agreement with Y.
The operation does not alter context or metadata; model constraints remain
separate predicates.

`applyRewrite(store, currentRevision, plan)` requires the checked plan to belong
to that store and to the exact current revision. It applies the compiled edit and
returns its ground receipt plus a typed-rule application witness. Callers advance
branch heads explicitly using the existing compare-and-swap API.

A ground operation now has an optional `provenance` field, separate from state
metadata. Rule compilation uses it to retain the complete declared rule, match,
and allocation. Consequently two different declared derivations of the same
ground effect produce different operation/revision IDs while their state IDs
may agree. Ordinary ground operations retain `provenance: null` unless supplied.

Provenance is a declaration, not automatic evidence. The ground revision engine
checks the ground operation but does not certify every statement in its
provenance. `verifyRuleHistory(store)` reconstructs each declared typed-rule
application and compares its compiled operation and receipt with stored history.
A deliberate test uses a valid deletion carrying a false addition-rule claim:
ground replay succeeds and the rule-history audit refuses the claim.

The engine-source digest now includes `rules.mjs`. Existing same-engine bundle
requirements remain in force; cross-engine migration is still explicit future work.

## 4. Explicit match transport

Given an application with `D -> X` and `D -> Y`, another match `n:L2 -> X` can be
transported through the retained context when its image avoids the deleted set.
`transportMatch(plan,n)`:

1. checks the original target boundary;
2. refuses any matched record that was deleted;
3. constructs `n_D:L2 -> D` and checks that its composite into X equals n;
4. returns the transported match through `D -> Y`.

This records a factorization, not an ID-based heuristic for rediscovering a new
match. The factorization uses the retained-ID convention, but its naturality and
label preservation are checked independently. Applicability at the resulting
revision is checked again by planning the next rule application.

## 5. Parallel independence and its actual scope

`proveIndependent(store,a,b)` takes two already-applicable checked plans at the
same exact revision. The sufficient conditions for this rule fragment are:

\[
\operatorname{Delete}(a)\cap\operatorname{Image}(m_b)=\varnothing,
\qquad
\operatorname{Delete}(b)\cap\operatorname{Image}(m_a)=\varnothing.
\]

Additionally, fresh allocations of the two rules must be disjoint within each
sort. Disjoint write sets alone are insufficient: one rule can delete a record
read or retained by the other. An added edge also depends on the endpoints in its
matched interface, even though its own ID is fresh.

These conditions preserve both matches and prevent a new incidence from either
rule becoming an external dangling reference for the other. New incidences can
attach only to that rule's retained interface or its fresh records; the former
are protected by the delete/image condition and the latter by allocation
freshness. No unrepresented negative or global guards are assumed.

The implementation does not merely trust this argument. In an isolated replay
store it executes A, transports B and executes B; it then executes B from the
same source, transports A and executes A. It compares the **entire resulting
state**, including context and metadata, by both its digest and normalized data.
It returns a commuting-state witness and a dependency-complete replay bundle.
The caller's store and heads remain unchanged during this proof construction.

The final revision IDs and receipt paths generally differ. Thus this witness is
a commuting square after projection to full construction states, not an equality
of revision histories or an automatically admitted 2-cell between parallel
arrows in the revision category. No quotient of provenance is performed.

Refusal means these sufficient conditions do not establish independence. It is
not a proof that no sequential application, alternative match, or joining route
exists. Such overlapping cases need critical-pair analysis rather than a stronger
word for the refusal.

## 6. Durable declarations and replayable witnesses

The witness formats bind the engine digest, rule data, input revision, match,
allocation, compiled operation ID, target digest, output revision, and ground
receipt. Application witnesses can be serialized separately; complete rule
declarations also remain in the exported ground history's provenance.

- `verifyRewriteWitness` reconstructs and replays one application in a fresh store.
- `verifyIndependenceWitness` reconstructs both initial plans and replays the two
  routes, comparing the complete recomputed witness.
- `verifyRuleHistory` audits declared rule derivations in a replayable revision
  store; other operations are counted separately. With no declared applications,
  its status is `notApplicable`, not a vacuous certificate of rule coverage.

Recomputing a digest on a false claim is insufficient: replay must reproduce its
state, revision, operation, and receipt boundaries. Missing source revisions are
refused. Neither hashes nor successful replay authenticate an author or supply
physical interpretation. Model validity is not preserved by assumption; new
revisions still have no inherited model-verification report.

## 7. Checks and next boundary

```
node --test tests/isotope-wiring-rules.test.mjs
```

Fifteen new tests cover rule serialization, explicit reuse, both pushout
comparisons, preserved-context match transport, independent deletion/addition
squares, delete/read conflicts, external dangling references, nonmonic matches,
fresh-ID conflicts, renamed interfaces, derivation-sensitive history, identity
rules, forged witness claims, added-edge endpoint dependencies, history audits,
and a real isotope-pair deletion with retained shared support and a refuted
inventory check.

The five structural suites now contain 66 passing tests. This is bounded
verification, not exhaustive critical-pair classification or a formal proof of
global confluence. The live app and its three legacy TODO defects are unchanged.

[OVERLAPS.md](OVERLAPS.md) now records supplied overlaps and checks explicit finite
joining routes without equating failed independence with nonjoinability.
[SELECTIVE.md](SELECTIVE.md) transports predicate results along equal declared
read projections. [CENSUS.md](CENSUS.md) adds bounded labelled overlap enumeration;
[VERIFICATION-BUNDLES.md](VERIFICATION-BUNDLES.md) replays verification transport
across processes. [MATCHING.md](MATCHING.md) enumerates exact-label monic matches
in bounded fixed hosts, and [JOIN-SEARCH.md](JOIN-SEARCH.md) explores bounded
continuations under an explicit allocation policy. [ISOMORPHIC-JOINS.md](ISOMORPHIC-JOINS.md)
compares supplied endpoints while fixing surviving source occurrences;
[ISOMORPHIC-SEARCH.md](ISOMORPHIC-SEARCH.md) integrates this as an optional search
mode with explicit budgets. [PERSISTENT-JOINS.md](PERSISTENT-JOINS.md) adds an
optional persistent-occurrence condition for supplied and searched routes.
[CONTEXT-LIFTING.md](CONTEXT-LIFTING.md) checks extension through one supplied
monic context, including commuting embeddings and the extended endpoint map.
[CONTEXT-COMPOSITION.md](CONTEXT-COMPOSITION.md) checks concrete composition
triangles and endpoint squares, with identity and associativity test cases.
Negative conditions, label variables, global confluence,
higher witness composition, migration, resource quotas, and automatic durable
storage remain open.
