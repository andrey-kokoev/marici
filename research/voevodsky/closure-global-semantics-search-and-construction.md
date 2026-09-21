# Boundary-sensitive native semantics: prior-work audit and first construction

## Search before construction — 2026-09-21

The search concerned today's **local research streams**, not new historical publications by Voevodsky or Grothendieck. Modification dates were used to locate current notes; claims were checked against their stated scope and, for the directly reused formal result, its Agda source.

### Grothendieck: complete constructor data already determine maps

Read:

- `../grothendieck/closure-operator-generated-comparison-and-the-arithmetic-attachment-obligation.md`
- `../grothendieck/agda/ClosureGeneratedMapNecessity.agda`
- `../grothendieck/agda/ClosurePolarizedMapNecessity.agda`
- `../grothendieck/necessity-before-realization-for-the-single-closure-operator.md`

The corrected finding is important: global finite-chain normalization frames are already constructed upstream, not merely assumed by the reference-frame facade.

The checked one-node equivalence is

`Map(Pushout(f,g), X) ≃ Σ(l:A→X) Σ(r:B→X) ((s:S) → l(f s)=r(g s))`.

The attachment path is part of the data. The two-slot version retains the mixed attachment cells. This is the right construction to extend recursively, rather than introducing another interface that assumes the desired global comparison.

### Grothendieck: an actual arithmetic attachment is now constructed

Read `../grothendieck/arithmetic-theta-attachment-cocone-and-two-prime-polarized-gluing.md`.

For an admitted square-integrable forcing, the window/tail decomposition supplies explicit restriction, zero-extension, and translation maps. It derives the bounded cone contraction and the full polarized identity

`G(c,d) = Q_p(c,d) + G(A_p c,A_p d)`.

It also constructs the two-prime common-refinement comparison. The seam-window energy is retained, not erased. Identification with the independent Green form, the reciprocal/Xi extension, and its norm-domain requirements remain separate. Its numerical fixtures were reported in that packet, not rerun here.

### Voevodsky: analytical presentation semantics are not wholly absent

Read:

- `theta-packet-graph-realization-and-comparison-with-the-prior-analytic-tower.md`
- `theta-packet-is-a-tensorized-localized-common-history-observation.md`
- `the-joint-source-graph-makes-the-chamber-twistor-tower-analytically-equivariant.md`
- `the-analytic-realization-of-the-prior-two-segal-baseline-is-the-waldhausen-s-construction-of-closed-cone-packages.md`

The admitted source-retaining graph systems already have coherent analytical comparisons and transported successors. Today's finite theta construction additionally gives explicit interval-source maps `A`, an observation `O`, and `OA=F`, with distinct source and output pairings.

Still separate are comparison with independently specified successors, completed catalogue inclusion, and restriction of the earlier signed Green form. The closed-cone S-construction realization and its completion seam have their own explicit scope. It would be incorrect to describe all analytical realization as unconstructed.

Also read `../nima/nested-closure-system-full-categorical-construction-sketch.md`: the abstract stable/2-Segal framework and finite nested S-constructions already exist at the mathematical-model level. They do not identify independently specified native or analytical operations automatically.

## Construction delivered

Five new safe Cubical Agda modules build a **finite-chain, directed native-calculus foundation**. This is not yet a claim of a completed all-dimensional realization functor for every intended constructor.

### 1. Recursive complete boundary semantics

`agda/ClosureTreeBoundarySemantics.agda` imports Grothendieck's actual one-node theorem.

For each finite bracket tree `t` and target type `X`, it constructs `Local t X` recursively:

- a leaf contributes its actual piece map;
- a fork contributes both children's complete local data and the path matching their assembled maps on every attachment.

Simultaneous structural recursion constructs

`realization t X : Local t X ≃ (Realize t → X)`.

Both reconstruction round trips are proved. Consequently equality of complete recursive local data forces equality of global maps. An equivalence on their path spaces is also provided; attachment paths are not discarded while comparing maps.

Precomposition by an actual realization map induces `pull` on complete local data, with checked identity, composition, and realization laws. A universal identity-valued packet reflects equality of realized maps. This does **not** imply faithfulness on free route words or identification of independently selected higher witnesses.

### 2. Polarized reconstruction for arbitrary trees

`agda/ClosureTreePolarizedSemantics.agda` constructs

`Local t (Local t X) ≃ (Realize t → Realize t → X)`.

Both round trips and the full local-to-global comparison follow. The nested dependent data include the mixed attachment cells. No bilinearity, Hermitian structure, positivity, or independent Green identification is inferred from this type equivalence.

### 3. Sequential composition retains the entire endpoint package

`agda/ClosureCoherentComposition.agda` composes two complete `Coherent` changes.

Its equivalence is the actual composite. Each external port is the mapped first port followed by the second port. Distribution/associativity corrections and a path through the paired-port state construct the composite normalization path and both higher endpoint cells.

This avoids falling back to unpointed admission when a program contains several moves.

### 4. Explicit native source syntax and its evaluation

`agda/ClosureNativeDecompositionCalculus.agda` defines:

- native arbitrary-subtree rotation generators;
- left and right contextual constructors;
- typed directed routes with identity and sequential composition;
- source unit and associativity paths;
- evaluation of every route into a complete `Coherent` comparison.

The underlying actions retain the supplied native equivalences, including word-index transport. Their composition law is checked.

Complete observations act contravariantly along routes. Identity and composition laws are proved, together with first/last endpoint preservation and naturality of normalized observations.

Arbitrary finite contexts act on both move syntax and route syntax. Move evaluation agrees with the previously proved contextual lift as a **complete Coherent value**. Contextualizing route syntax preserves concatenation.

The source is not quotiented by pentagons or by equality of observed outputs. There is no claim that distinct physical source histories become the same syntax.

### 5. Regression

`agda/ClosureNativeDecompositionCalculusRegression.agda` checks two successive contextual native rotations on a six-piece circle-valued tree. It verifies action on both whole rotating subrealizations, retention of both higher endpoint fields after composition, compositional observations, and the full compatible presentation comparison.

A separate two-attachment fixture has identical leaf readouts and a circle-generator seam. Assembly retains that seam exactly and cannot replace it by reflexivity. Its complete local packet round trip is checked, as is two-slot reconstruction.

The seam test does not assert that agreement on leaf values makes arbitrary global maps unequal or equal; it specifically tests the retained attachment path.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i research/grothendieck/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureNativeDecompositionCalculusRegression.agda`

Exit 0, no warnings, **7 minutes 59.873 seconds**, under a 1200-second bound. The final incremental run took about 47 seconds.

All five new modules use `--safe --cubical --guardedness`, without holes or postulates. This closure freshly rechecks the imported Grothendieck one-node theorem, both append inductions, native subtree/context admission, and the new recursive semantics. It does not rerun Grothendieck's separate two-slot entrypoint, the analytical fixtures, or every historical regression.

## Precise remaining global structure

This is now an explicit source syntax, a boundary-complete reconstruction theorem, and route evaluation with retained coherence—not only a proposal for a future interface. However:

1. Full higher functor laws comparing independently parenthesized **Coherent compositions**, and interchange between composing whole routes and lifting their completed Coherent values, are not asserted by the underlying-map composition theorem. Move-level contextual correctness and syntax-level concatenation compatibility are proved.
2. Independently specified pentagon and higher source generators still require their selected compatible cells. The earlier higher-admission obstruction remains relevant; they cannot simply be inserted as automatic equalities.
3. Formal inverse-move syntax and empty-chain/gluing-unit syntax have not been added. Identity routes do not supply empty-chain objects.
4. General graph constructors, infinite completions, and the analytical comparisons identified by today's search remain separate extensions.

The next global step is therefore higher compositional compatibility of the retained endpoint packages, followed by a specified native pentagon—not another assumption of global frames, nor an unrelated finite observer.
