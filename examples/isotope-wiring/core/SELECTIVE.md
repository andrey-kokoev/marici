# Selective verification through exact read projections

## Scope and APIs

`model-predicates.mjs` now publishes `predicateReadContract` and provides
`verifyModelSelectively(object,context,previousReport)`. The previous report must
be a checked, immutable result created by this loaded checker instance; a parsed
JSON report is not a trusted baseline.

The revision-store entrypoint is:

```
store.verifyAt(sourceRevision)
// Apply an edit; the target still has no verification report automatically.
const transported = store.verifyAt(targetRevision, { reuseFrom: sourceRevision })
```

A fresh, revision-bound report records the baseline verification ID, current
state and input digests, engine digest, and each predicate's reused/computed mode.
`verificationById` retains access to historical baseline reports even when a newer
report becomes the latest for the same revision. The archive remains in-memory.

The baseline can be on another branch: the justification is exact agreement of
predicate reads, not an assumed preservation property of ancestry. No UI or
visualization changes are involved.

## 1. The factoring obligation

For each versioned predicate p, the declared projection must contain every input
read by the checker body, plus the current statuses of its prerequisites. With
schema and checker constants fixed, the intended factoring law is

\[
\operatorname{Check}_p(X,C;\sigma)
=\overline{\operatorname{Check}}_p(\pi_p(X,C),\sigma).
\]

The implementation compares the complete canonical projection strings, not just
their hashes. If they agree, it reuses the old predicate result, including any
localized residual. Otherwise it recomputes that predicate. Current prerequisites
are evaluated first, and their statuses enter the comparison.

This transports the result of this checker on these inputs. It is not a claim
that arbitrary rewrites preserve the underlying mathematical predicate, nor a
physical evidence-promotion rule. Completeness of the manually declared read
contract is an implementation obligation: source inspection and differential
hostiles support it; no theorem prover or automatic read tracer certifies it.

## 2. Read domains and global/negative information

Every projection includes the full schema presentation and predicate/read-contract
identity. The additional data is:

| Predicate | Whole record sets | Label collections | Incidence maps |
|---|---|---|---|
| Attribute types | All | All | None |
| Lattice incidence | Shell, cell, port | Shell, cell, port, vertex | Cell→shell, port→cell, port→vertex |
| Support incidence | Edge | Vertex, support | Source, target, edge→support |
| Pair grammar | Pair | Port, shell | Pair→cell, cell→shell, four route-port maps |
| Witness grammar | Line and boundary witnesses | Line witness, port | Line→cell/start/end, boundary-witness→shell |
| Color disjointness | Pair | None | Pair→red/blue edge, edge→support |
| Inventory targets | Shell, pair, both witness sorts | Shell | Cell→shell, pair→cell |

Inventory additionally includes the complete supplied target object and whether
it is present. Other context annotations are not read by these predicate bodies.
A root context must still be a valid JSON object before selective evaluation.

Whole relevant collections are included, not merely IDs visited on the previous
run. Adding a new witness therefore changes the witness projection and invalidates
a previous no-duplicate conclusion. Count-equal changes do not automatically
preserve route, support, or occupancy checks.

Some projections intentionally include more data than the body needs. This may
cause unnecessary recomputation but cannot justify omission of a necessary read.
Future predicate changes require a read-contract audit; a fresh process/source
digest is required when changing engine code. Hot-reloading code against an old
baseline cache is not a supported evidence workflow.

## 3. Dependency statuses are part of the boundary

Suppose an edge's supporting label becomes inconsistent. The pair incidence used
by the color checker may be unchanged, but its support prerequisite becomes
refuted. The dependency-status projection changes, so the old color result is
not reused; it becomes unknown under the existing prerequisite rule.

Conversely, a label change can require rerunning the attribute check while leaving
its verified status unchanged. A downstream predicate whose own reads are equal
may then reuse its result. It depends on that prerequisite status, not on every
input of the prerequisite's checker.

Verified, refuted, unknown, and inapplicable results retain their meanings during
reuse. A repeated negative result stays negative; an unchanged missing-target
condition stays unknown. Reuse is not a status promotion.

## 4. Concrete boundaries exercised

- A metadata-only revision reuses all seven predicates: metadata is outside the
  model checker. The new receipt still binds the changed full state and revision.
- Changing Z recomputes inventory and reuses the six unchanged structural checks.
- Deleting one owned pair reuses lattice, support, and witness checks while
  recomputing attributes, pair grammar, color disjointness, and inventory.
- Adding a duplicate witness recomputes duplicate/absence-sensitive checks despite
  all previously known witness records remaining unchanged.
- Corrupt support labels change prerequisite status and prevent stale downstream
  color verification.

These are observed results for the named cases, not a universal optimization rate.
The implementation still serializes/hashes the complete input for its binding;
no performance or asymptotic improvement claim is made by these tests.

## 5. Persistence and evidence limits

Every edit still begins without an attached target verification. Selective reuse
is an explicit verification operation that produces a new bound report. The
source result remains accessible under its original verification ID.

Revision bundles continue to omit verification reports. After importing a bundle,
recompute a baseline before requesting selective reuse. Arbitrary serialized
reports, even with plausible digests, are rejected as baselines. [VERIFICATION-BUNDLES.md](VERIFICATION-BUNDLES.md) now supplies a separate
transport-bundle protocol: it reconstructs the baseline dependency closure in a
fresh store, recomputing reports before trusting them for reuse. Ordinary revision
bundle import alone still provides no baseline.

## 6. Executed checks

```
node --test tests/isotope-wiring-selective.test.mjs
```

Eight tests compare selective results to fresh evaluation for all 81 ordered
pairs of the nine fixtures, malformed-label hostiles, global duplicate insertion,
prerequisite failure, context/metadata edits, and pair deletion. They also check
that imported reports are not trusted and that archived baseline IDs remain
resolvable.

The selective suite remains eight tests. With the later census, verification-bundle,
matching, join-search, isomorphic-join/search, persistent-join, and
[context-lifting](CONTEXT-LIFTING.md) and [context-composition](CONTEXT-COMPOSITION.md)
suites, the sixteen structural suites contain 162 tests. Legacy-engine TODO failures remain separate. Mechanically
auditing read contracts, broader criticality/confluence analysis, and higher
composition of witnesses remain open.
