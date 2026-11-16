# Model predicates and policy-composition closure

## Scope

`model-predicates.mjs` adds a versioned, headless checker for the declared
shell-lattice grammar. `attributed-diagrams.mjs` now provides policy-restricted
open components, identities, composition, and attributed isomorphism inverses.
Neither module is connected to the visual application.

The obligation is route/coherencer compatibility for structural composition,
followed by checking explicit model predicates. Model validity is not assumed
preserved by composition. A passing grammar check is not evidence that the grammar
is physically adequate, that targets are derived, or that a placement is resolved.

## 1. Explicit predicate family

`verifyModel(object, context)` accepts a checked attributed diagram. The
supported schema is the full `isotope-wiring.support-incidence.v1` presentation,
not merely a string matching its name. Its model is
`isotope-wiring.shell-lattice-model.v1`.

| Predicate | Tested property |
|---|---|
| `attribute-types` | Exact label fields, safe integer coordinates, shell sizes 1–20, port roles, witness axes, named boundary kind, support endpoint-label types |
| `lattice-incidence` | Unique shell order, in-range and nonoverlapping cells per shell, exactly four labelled ports per cell, exact port/lattice agreement, consistent frame within each shell |
| `support-incidence` | Edge endpoints lie in one frame and agree with the referenced undirected support labels |
| `pair-grammar` | Local diagonal routes, shell-parity color rule, duplicate-occupancy rejection, at most two pair records per cell |
| `witness-grammar` | Axis/route agreement and no duplicated cell/axis or shell-boundary witness slot |
| `color-disjointness` | No referenced support occurrence bears both red and blue pair routes |
| `inventory-targets` | Owned pair/witness totals and per-shell counts agree with supplied targets; no target entries refer to absent shell orders |

The target-without-shell check is an explicit strengthening over the legacy
checker's behavior. Targets Z, N, and expectedByShell remain supplied data. The
checker does not infer them from an isotope name or accept them as predicted
values. Extra unreferenced support objects are not automatically deleted.

The predicate family is not claimed complete for all intended isotope semantics.
It does not certify boundary cycles, physical geometry, measured inventory,
energies, or uniqueness of source placement. The old borrowed-contour advisory
and the source fixture's unresolved-status annotation are not converted into
these predicates. They remain retained source information. In particular, V51
satisfies these named predicates while its source placement remains unresolved.

## 2. Status, dependency, and receipt contract

Each predicate reports `verified`, `refuted`, `unknown`, or `notApplicable`, with
its dependencies and localized issues. Invalid attribute data blocks dependent
checks as `unknown`; it does not trigger undefined computations or vacuous passes.
Absent required targets are `unknown`; malformed or mismatching supplied targets
are `refuted`. A different schema is `notApplicable`.

Aggregate status is `refuted` if any applicable predicate is refuted, otherwise
`unknown` if a prerequisite/input is missing, otherwise `verified`. For an
unsupported schema it is `notApplicable`. This aggregation never promotes the
physical-interpretation field, which remains `not-checked`.

The frozen report contains model/checker versions and a deterministic SHA-256
digest of the entire normalized incidence diagram, model labels, and supplied
context. This identifies the exact checked input, not an isomorphism class.
A renaming can preserve predicate statuses while changing the digest.

The standalone report is not a durable evidence-transport certificate. The
subsequent [revision layer](REVISIONS.md) binds it to a revision, full state, and
local engine-source digest. Edits still attach no verification automatically.
[SELECTIVE.md](SELECTIVE.md) now permits explicit reuse only when the declared
predicate read projection and current prerequisite statuses agree exactly.
This mechanism is not a general rewrite-preservation theorem. The separate
[verification-bundle protocol](VERIFICATION-BUNDLES.md) persists claims and replays
their dependency closures, recomputing baselines before permitting reuse.

## 3. Policy-restricted open components

The added APIs are:

- `checkSupportLeg(f)`: check the monic, occurrence-free, support-complete policy;
- `supportComponent(left,right)`: two eligible boundary legs into one attributed apex;
- `supportIdentity(boundary)`: identity cospan on an eligible boundary;
- `composeSupport(g,f)`: glue the internal boundary and recheck both resulting external legs;
- `inverseAttributed(f)`: inverse of an attributed isomorphism.

Composition does not call `verifyModel` as a permission to erase a candidate.
It produces a structural object, maps, and gluing witnesses. Model checking is
a separate explicit operation on that result and its supplied context.

### Closure argument for the policy

Fix the support schema and model-label convention. Both boundary maps are
monomorphisms, and the boundary has no owned pair/neutron occurrences. A boundary
map is support-complete when every directed edge over an included support in the
apex is itself included by the boundary map.

For `I -> A <- K` and `K -> B <- O`, form the attributed pushout P. Pointwise
pushout stability of monomorphisms makes the induced maps from A and B injective.
The composite external legs are therefore monic, label-preserving, and retain
the same occurrence-free source boundaries I and O.

To check support-completeness of `I -> P`, take a support in its image:

1. If it is not in the image of K in A, no B edge can acquire that support in P.
   Completeness follows from `I -> A`.
2. If it is in K's image, every B edge over the matching support comes from K,
   by completeness of `K -> B`. Its K record also maps into A. Completeness of
   `I -> A` then places that A edge in I's image. The pushout identifies the B
   edge with it, so no new edge over this support is missing from I.

The argument for O is symmetric. Injectivity is essential: it prevents distinct
supports on one side from being merged through the other side. Identity legs
are complete, and their source must be occurrence-free. Thus the chosen policy
is preserved by the specified composition and units in this ambient setting.
The implementation rechecks it rather than relying solely on this argument.

### Coherence

The associator is obtained from the universal maps between parenthesized
pushouts. It preserves each original apex leg, all model labels, and both
external boundaries. Its inverse comes from the reverse universal comparison.
Support completeness is invariant under these apex isomorphisms.

The pentagon and unit triangle compare maps with the same original incidence
legs. Uniqueness of the universal factor implies equality. The tests construct
and compare these maps explicitly. A packaged API for general 2-cells or a
symmetric monoidal structure is still absent; no tensor/hexagon implementation
is claimed by these checks.

## 4. A retained counterexample: model validity is not closed

Import two copies of O16. Each satisfies the seven named predicates against its
supplied targets. Glue them along their entire occurrence-free support diagrams.
This gluing satisfies the policy and retains both copies' pair and witness
occurrences: the composite has 16 pair records and 16 neutron-witness records.

Even setting targets to Z=16, N=16, and shell counts [4,12] only makes the
inventory predicate pass. Duplicate pair occupancy, cell capacity, and duplicate
witness slots still fail. No record is removed, and no alternate target can
repair those structural-model residuals by count fitting.

Therefore the model-conformant objects do not form a composition-closed class
under this assembly operation. The working category must retain typed candidates
and attach predicate results, rather than restricting all computations to objects
already passing the model. This is a counterexample inside the supplied finite
grammar, not a conclusion about physical isotope assembly.

## 5. Executed verification and remaining gate

```
node --test tests/isotope-wiring-model.test.mjs tests/isotope-wiring-adapter.test.mjs tests/isotope-wiring-category.test.mjs
```

The combined suite has 36 passing tests. Twelve new checks cover the nine
legacy fixtures, missing/malformed target distinctions, unsupported schemas,
dependency blocking, corrupt support labels, count-equal incidence failures,
wrong route colors and duplicated witnesses, input-digest binding, the closure
counterexample, an attributed policy pentagon, distinct vertex-only interfaces,
and a policy unit triangle.

The coherence tests are bounded examples plus the structural argument above;
there is no theorem-prover certificate or complete search of policy diagrams.
They do not repair the three separately tracked legacy-engine defects.

The [revision milestone](REVISIONS.md) implements immutable identities, exact
ground matches, atomic dangling-reference refusal, retained before-images, undo,
and conservative verification invalidation. [RULES.md](RULES.md) now implements monic rules, preserved-context match transport,
and bounded independence witnesses. [Supplied overlap/join checks](OVERLAPS.md)
and [selective read-projection verification](SELECTIVE.md) are also implemented;
[CENSUS.md](CENSUS.md) adds bounded fixed-pattern enumeration, while
[VERIFICATION-BUNDLES.md](VERIFICATION-BUNDLES.md) replays verification transport.
Global confluence and mechanically certified read contracts remain open.
