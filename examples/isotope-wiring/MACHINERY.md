# Isotope wiring: categorical machinery, draft 0

## Question, boundary, disposition

**Question:** What machinery would make constructions, edits, composition,
comparisons, and verification reproducible in the isotope-wiring workbench?

**Boundary:** This is a proposed software semantics for finite, explicitly
presented wiring records. EP and neutron labels retain their present grammar
meaning; this document does not identify them with physical particles or derive
isotope stability. A finite presentation is not a claim that the physical source
is finite. An edit sequence is workflow order, not physical time.

**Disposition:** Adopt the distinctions and acceptance obligations below as the
implementation target. The existing app is not an implementation of the proposed
categories. No composition or coherence theorem for its code is asserted here.
The operator requested this development after the core audit; this is a design
instruction, not evidence for the model.

**Structural implementation milestone:** the independent kernel in
[`core/finite-diagrams.mjs`](core/finite-diagrams.mjs) now implements finite
incidence diagrams, natural transformations, finite (co)limit primitives, and
open-component composition. See [`core/CLOSURE.md`](core/CLOSURE.md) for the
closure argument, API, fourteen passing bounded tests, and residuals. It now also
has [model labels, support-interface gluing, and a retained-source legacy
adapter](core/ADAPTER.md), plus [versioned model predicates and policy-composition
closure checks](core/MODEL.md). [Immutable revisions and exact ground
rewrites](core/REVISIONS.md) provide atomic edits, undo, and replay. [Linear typed
rules](core/RULES.md) now construct checked two-pushout applications, explicit
match transport, and bounded independence witnesses. [Supplied overlap/join
checks](core/OVERLAPS.md) and [selective read-projection verification](core/SELECTIVE.md)
are implemented, now extended by a [bounded labelled overlap census](core/CENSUS.md)
and [cross-process verification-bundle replay](core/VERIFICATION-BUNDLES.md).
[Bounded automatic matching](core/MATCHING.md) now discovers exact-label monic
occurrences in fixed hosts, including residual matches for supplied joins.
[Bounded join search](core/JOIN-SEARCH.md) explores multi-step routes with explicit
coverage and fresh-allocation limits. [Supplied isomorphic joins](core/ISOMORPHIC-JOINS.md)
now carry checked endpoint maps fixing common surviving source occurrences;
[automatic search can now opt into that comparison](core/ISOMORPHIC-SEARCH.md)
with separate budgets, while exact equality remains the default.
[Persistent-occurrence checking](core/PERSISTENT-JOINS.md) optionally requires all
common post-peak source occurrences to survive both continuations and be fixed
by the comparison. [Context lifting](core/CONTEXT-LIFTING.md) checks the extension
of such a join through one supplied monic source embedding, without promoting
that concrete witness to a universal theorem. [Context-lift composition](core/CONTEXT-COMPOSITION.md)
now checks concrete two-stage lifts and their commuting triangles/squares, with
identity and associativity cases tested. Global criticality/confluence analysis and mechanically certified read contracts
remain open. The visualization remains untouched.

Primary SCC obligation: **route/coherencer compatibility**. Forward realization
must first specify how construction syntax becomes an incidence object;
attachment transport concerns explicit interface maps; readout descent is a
separate, later obligation. SCC guidance was inspected. Registry discovery
currently reports pre-existing manifest errors; this design has not received an
SCC categorical certificate.

## 1. Governing conjecture and its test

- **Problem:** The present app conflates record identity, geometric coincidence,
  delta replay, and verification in a single HTML implementation.
- **Conjecture:** Explicit incidence, pinned operation boundaries, and witnessed
  comparisons can make composition and replay independent of presentation while
  preserving provenance and exposing invalid exploratory states.
- **Rivals:** Strengthen JSON patches alone; identify structures by rendered
  coordinates; or identify them by counts. The first may suffice for storage
  but does not itself specify assembly; the latter two forget distinctions.
- **Risky consequences:** Layout changes cannot change topology checks; independent
  edits admit a checked commuting square; stale bases are refused; same counts
  cannot certify structural equality; incompatible interfaces cannot be glued.
- **Strongest current falsifier:** A legacy delta roundtrip passes `sameGraph`
  while inheriting metadata absent from the target. The advertised graph check
  therefore does not establish full-definition roundtrip. A generated cell ID
  also conflates `(row=1,col=10)` with `(row=11,col=0)`. The new characterization
  suite additionally shows that `compile(diff(A,A), {A})` rejects the identity
  delta as cyclic: logical definition IDs are not revision identities.
- **Surviving scope:** The existing record grammar is useful input to a new core.
  Universal composition, complete equivalence checking, and automatic merging
  remain unimplemented. Tests below are acceptance criteria, not results.

## 2. Separate the objects before naming the categories

A research state has four separately versioned components:

| Component | Contents | Identity rule |
|---|---|---|
| Construction | Typed incidences, owned occurrences, declared interface maps | Exact records or an explicit typed isomorphism |
| Model context | Grammar version, constraint set, supplied Z/N and shell targets | Exact context version |
| Provenance | Operation receipts, input revisions, author/source annotations | Immutable record identity |
| Presentation | Layout, camera, selected cell, colors/theme | UI state; not construction identity |

Supplied targets are predicates against a construction, not values its drawing
is permitted to force. Descriptive isotope names do not select an algorithm.
A model change changes the context even if the incidence object is unchanged.

Use opaque namespaced occurrence IDs, never concatenated coordinates. Keep
`row` and `col` as separate attributes. An ID names an occurrence; equal labels
or equal screen positions do not merge occurrences.

### Candidate incidence schema

The schema must explicitly supply at least:

- shells; cells with a shell map; ports with a cell map and local port label;
- vertices, directed edges with source/target maps, and port-to-vertex maps;
- EP occurrences with their cell map and ordered red/blue edge references;
- line-witness occurrences with cell and supporting-edge references;
- boundary-witness occurrences with shell and explicit boundary references.

Route endpoints must agree with the vertices designated by their declared ports.
Shared support is represented by edge/vertex references, while occurrences remain
separate. A route shared geometrically by two records does not become two support
edges, and one support edge does not become two owned records by being visible.

This is a schema target, not a finished schema declaration. In particular, the
legacy H/V witness and boundary-frame semantics must be specified before claiming
that an adapter into this schema is lossless. Incidence does not determine a
metric, energy, coefficient operator, or physical readout.

## 3. Structural maps are not edits

Choose a finitely presented schema category S with incidence maps and their
required equations. Finite S-diagrams in sets, with natural transformations,
provide a candidate ambient category G. Typing/attribute preservation must be
made explicit, for example by a slice over a fixed type diagram. The finite
support and allowed attribute domains belong to that declaration.

Objects of G are incidence structures. A morphism maps records of each sort and
commutes with all incidence maps. Injective morphisms represent inclusions;
isomorphisms represent reversible renamings preserving structure and attributes.

Capacity, shell targets, and uniqueness restrictions are additional predicates.
Do not assume that their satisfying objects retain the pushouts available in the
ambient diagram category. Construct in the ambient category, then check the
chosen model's constraints. A rejected construction may remain a typed research
candidate with explicit residuals.

An edit deleting an edge is **not** a total incidence-preserving map from its
old graph to its new graph. Therefore the edit system needs a separate category.

## 4. Assembly: interfaces and pushouts

An open component is a cospan

\[
I \longrightarrow G \longleftarrow O.
\]

I and O are declared input/output interface structures, not necessarily discrete
sets. The first implementation should use injective interface maps. Interfaces
must retain all incidence required by the schema, including ownership context
where necessary; matching port names alone is insufficient.

For components with a common, explicitly identified interface O, compose by

\[
G \mathbin{+_O} H.
\]

Return the pushout object **and** both inclusion maps. An interface isomorphism
is input to gluing, not something inferred from a nearby drawing. Two eligible
matches yield two candidate composites until a selection rule is supplied.

Identity components use identity cospans; disjoint union supplies parallel
composition and the empty interface its unit. Associativity is up to the
canonical isomorphism, not literal allocation of record IDs. Retain that
isomorphism as a comparison witness. This motivates a symmetric monoidal
bicategorical account of open components; taking isomorphism classes can give a
category, but the implementation should retain witnesses rather than erase them.

No theorem is claimed for an arbitrary restricted interface policy. Its closure
under composition, unit compatibility, and comparison maps must be checked.
Constrained or partial assembly must return a typed refusal, not silently repair
the inputs to produce a requested count.

## 5. Editing: a path category of revision-bound operations

Let E have immutable revision states as objects. Generating arrows are successful
operation applications with exact source and target revisions. Paths compose by
concatenation when boundaries match; the empty path is identity. A failed request
is a diagnostic, not an arrow with a fabricated target. Retain distinct paths
with equal endpoints until a specified comparison identifies them.

A receipt records:

```
operationKind, operationVersion, inputRevision, modelContext,
parameters, matchMap, readSet, writeSet, retainedBeforeImage,
outputRevision, verificationDependencies
```

Small local edits should eventually be represented by typed rewrite rules
`L <- K -> R`: the interface K is preserved, L-only data is deleted, and R-only
data is added. Double-pushout rewriting is a candidate semantics once the exact
ambient category, matching policy, and gluing conditions have been established.
A dangling-reference deletion is refused. JSON patch replay is an initial
implementation mechanism, not proof that these rewrite conditions hold.

Undo requires a retained before-image and the exact output revision as its
input. It restores construction state but creates a new provenance event;
it does not erase the historical edit. An inverse roundtrip is therefore checked
at the construction projection, not as equality of provenance revisions.

Independent edits need a commuting square with transported matches:

\[
X \xrightarrow{a} X_a \xrightarrow{b_a} Y,
\qquad
X \xrightarrow{b} X_b \xrightarrow{a_b} Y'.
\]

Supply a typed isomorphism `Y -> Y'` and verify the claimed retained incidences.
Disjoint writes alone are insufficient: reads, references, negative application
conditions, and model constraints can interact. A merge is a checked completion
of a branch diagram or a conflict report, never last-writer-wins by default.

These comparisons are candidate 2-cells. Do not call the resulting system a
2-category until their identities, composition, and interchange are specified.

## 6. Syntax, compilation, and the meaning of equality

Separate these five claims in both API names and UI labels:

1. Same serialization bytes.
2. Same normalized records and declared metadata.
3. Isomorphic incidence structures under a supplied renaming.
4. Same result under a named observer, such as counts.
5. Same provenance/revision record.

None of claims 3–4 implies claim 5; claim 4 does not imply claim 3.
Hashes detect exact normalized content identity, not graph isomorphism or truth.

A definition is either a complete absolute snapshot or a delta with an immutable
base revision, schema version, grammar version, and explicit metadata operations.
Missing metadata cannot accidentally mean both inheritance and deletion.

Compilation is initially a partial evaluator producing a typed construction or
a structured error. Calling it a functor requires defining arrows between syntax
objects and proving how those arrows are interpreted. The first implementation
must satisfy the narrower, executable full-state roundtrip law:

\[
\operatorname{apply}(A,\operatorname{diff}(A,B))=B.
\]

Equality here means normalized construction plus declared model metadata,
excluding separately stored provenance and UI state. Test deleted metadata,
renamings, empty collections, nested deltas, and stale or cyclic bases.

A schematic naturality obligation for renaming rho is

\[
\operatorname{apply}(\rho X,\rho a)
\cong \rho\operatorname{apply}(X,a),
\]

where rho transports every reference, interface, and operation match. The
comparison is unavailable if the operation depends on an untransported label.

## 7. Verification: indexed claims and retained witnesses

For a revision X, context M, and predicate P, distinguish:

- `verified`: a replayable witness/check result for P(X,M);
- `refuted`: a counterexample with offending records;
- `unknown`: required input or procedure unavailable;
- `notApplicable`: P's declared domain does not contain (X,M).

Warning severity is a separate UI field, not a truth value. A geometry-producing
candidate can still fail count or occupancy predicates and remain editable.
Distinguish malformed input, well-typed candidate, model-conformant construction,
and externally supported physical interpretation.

Evidence is indexed by `(revision, context, predicate, checkerVersion)`.
There is no automatic evidence transport along arbitrary edits. Reuse requires
a proved preservation rule or rerunning affected checks. Dependency tracking
must include negative/global predicates, not just the IDs mentioned in a message.

Verification receipts include input and engine digests, exact parameters,
status, witnesses/residuals, and declared scope. A receipt is not a formal proof
unless its proof object is independently checked under a specified logic.

## 8. Observers, rendering, and information loss

Counts are object-level readouts. On the revision-path category, for a fixed
context and count vector c, the increment

\[
\Delta c(a:X\to Y)=c(Y)-c(X)
\]

is additive under composition by telescoping. It defines a functor to the
one-object category of the additive group of count vectors. This says nothing
about counts being faithful or about their physical interpretation.

For a finite pushout along injective interfaces, cardinality of each incidence
sort obeys inclusion–exclusion. A weighted record count inherits that formula
only when weights and overlap identification are preserved. Do not add total
counts blindly when interface records are shared.

Rendering takes a construction **and** presentation settings to a scene.
It is deliberately lossy. Verification of identity, sharing, and ownership must
not consult screen coordinates. Exact geometric realization, if required, is a
separate typed layer with rational/algebraic data and compatibility conditions;
floating-point display coordinates are its downstream approximation.

Changes of presentation must preserve incidence-check results. Hit testing must
return an occurrence/support ID with its type, not reconstruct identity from
pixel proximity. A collapsed visual edge must expose all of its retained owners.

## 9. Persistence and complete-workbench coverage

Persist immutable construction snapshots, pinned dependency closures, operation
receipts, model contexts, and verification receipts. Branch heads are mutable
pointers updated with compare-and-swap. Autosave, export, import, and migration
must report completion or failure; a UI change does not certify durable storage.
Store unapplied editor buffers separately, mark them as drafts, and offer
recovery. Schema migrations are explicit versioned transformations with loss
reports rather than silent recompilation against the newest grammar.

| Workbench subsystem | Required mechanical contract |
|---|---|
| Core constructors | Deterministic typed outputs or diagnostic; no DOM dependency |
| Isotope catalog | Index immutable definitions; labels/targets do not select a construction law |
| Interface assembly | Declared matches, pushout maps, constraint results |
| Cell edits and undo | Revision-bound operation receipts and recovery scope |
| Absolute/delta editor | Full-state replay, pinned bases, explicit metadata semantics |
| Comparison view | Named equality/readout and retained witnesses; compare selected revisions, not hidden fixture substitutes |
| Counts/validation panel | Predicate, scope, status, offending records, checker revision |
| SVG/3D view | ID-preserving selection; display changes cannot alter incidence checks |
| Project storage/export | Dependency-complete, versioned, deterministic payload and durability status |
| Worker/batch execution | Cancellation and resource limits; results bound to input revisions, stale results not displayed as current |
| Physical/research adapters | Explicit imported carrier, metric/operators, comparison map, and claim boundary |
| Browser/website host | Presentation and commands only; same engine as headless tests |

The app currently has no derived map into the repository's coefficient or energy
assemblers. See `docs/arrow-assembly.md` for their required inputs. A common
picture or matching count does not construct such an adapter.

## 10. Build order and falsification gates

| Stage | Deliverable | Refusal/failure case required |
|---|---|---|
| A | Headless legacy characterization suite; frozen fixtures | Deliberate count failure; metadata-roundtrip and ID-collision regressions |
| B | Versioned incidence schema, exact identity, adapter and migration report | Equal coordinates cannot merge different support records; ambiguous legacy conversion is reported |
| C | Immutable snapshots and full-state deltas | Changed base, omitted metadata, corrupt/missing dependencies |
| D | Typed local operations and scoped inverse receipts | Dangling deletion; undo against wrong revision |
| E | Open-component gluing with explicit maps | Wrong port type; ownership mismatch; multiple possible matches |
| F | Route comparisons and dependency-aware verification | Conflicting edits do not commute; count equality does not certify isomorphism |
| G | UI integration, durable drafts, batch experiments | Stale worker result, storage failure, interrupted import, roundtrip export |

For gluing, test identities, the associator, and its pentagon on bounded generated
examples while also identifying the general categorical argument applicable to
the implemented schema. Tests establish their stated domain, not a universal
coherence theorem. For rewrites, test both independent and deliberately dependent
matches, not only successful editor actions.

### Characterization results

`node --test tests/isotope-wiring-core.test.mjs` runs the actual HTML core without
a DOM. Seven characterization tests pass, including the 72 ordered distinct-ID
fixture roundtrips, deliberate-invalid fixture, cycle/missing-base refusals,
nonmutation, structural/count distinction, equal-count/different-graph control,
and mutable-base sensitivity. Three executable TODO requirements currently fail:
identity replay, full-state metadata deletion, and collision-free cell IDs.
These failures are not implementation passes and must not be omitted from the
research status merely because the test runner permits TODO failures.

**First acceptance milestone:** reproduce every current fixture headlessly;
separate checks from drawing; make full-definition replay exact and base-pinned;
retain all three discovered defects as failing regression requirements until repaired.
Do not replace the live editor with an unverified abstraction in one rewrite.
