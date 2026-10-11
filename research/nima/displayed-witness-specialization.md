# Witness specialization as a displayed construction

## Literature match and correction

The relevant standard construction is the **total of a displayed structure**, not a new generic object called a composition triple. A WG supplies a graph plus a chosen outgoing witnessed step at each node. Its original witness relation need not have identity witnesses or composition. A refinement therefore first corresponds to a displayed graph with chosen lifts of those steps; its history extension carries the categorical operations.

The local Cubical 0.9 library was inspected at:

- `Cubical/Categories/Displayed/Base.agda`: `Categoryᴰ`, including dependent identity/composition laws and `isSetHomᴰ`.
- `Cubical/Categories/Displayed/Constructions/TotalCategory.agda`: `∫Cᴰ`, the dependent-sum composition of displayed categories, and its associator functors.
- `Cubical/Categories/Constructions/TotalCategory/Base.agda`: `∫C`, the ordinary total category.

These give concrete implementation targets for the terminology in Ahrens–Lumsdaine, *Displayed Categories* (2019). Jacobs, *Categorical Logic and Type Theory* (1999), is background for comprehension/fibration structures, not evidence that the present WG family already satisfies their additional axioms. No new reading or reproduction of those papers/books is claimed here; the formal comparison uses the installed library definitions directly.

## Checked bridge

`agda/DisplayedWitnessSpecialization.agda` constructs the following without truncating witnesses:

1. **Displayed graph.** `display F` has admission fibers at nodes and the refinement's proof-dependent `Extra` over each base edge. `chosen F` supplies lifts of the base generator's selected steps.
2. **Totalization.** `compilation-is-total` identifies `compile F` with the total WG of that displayed graph and chosen lift.
3. **Dependent-sum composition.** `composition-is-displayed-sum` identifies the displayed data of `compose F G` with `sum-display (display F) (display G)`. The second edge witness depends on the first, just as in the library's displayed total construction. Both identifications are reflexivity, not assumed equivalences.
4. **Displayed histories.** `Lifted h p q` retains admissions and extra witnesses over a particular base history `h`. `total-history-iso` gives inverse maps between histories of `compile F` and pairs consisting of a base history and such a displayed lift. `forget-join`, `assemble-join`, and `pack-join` check compatibility with concatenation; displayed unit and associativity laws are dependent paths over the actual base law paths.
5. **Generated lifts.** `generated-lift` constructs lifts of every finite generated base history from an initial admission. A three-step Boolean fixture changes admission flags and verifies recovery of the full lifted history.
6. **Actual library categories, conditionally.** `SetValued` takes explicit sethood witnesses for base-history and displayed-history hom-types and constructs Cubical's `Category` and `Categoryᴰ`. The history isomorphism identifies the library `∫C` homs with histories of the compiled WG. `pack-functor` and `unpack-functor` preserve identity/composition, are identity on objects, and have the already proved inverse laws on homs. No unconditional hom-set assumption is smuggled in; the earlier graph/history results do not require those hypotheses.

Source provenance is retained by the original refinement/composer. `display` deliberately exposes its mathematical admission/witness data, not an isomorphism that reconstructs arbitrary provenance records from a graph.

## Risky consequence and counterexample

Rival: chosen generator lifts automatically make the total-history projection a fibration or opfibration. `NotAutomaticFibration` refutes this. A one-node base has two loop witnesses, `true` and `false`; its generator selects `true`. The refinement certifies that chosen loop but assigns the empty type to every lift of `false`, at every target fiber. `no-false-edge-lift` and `no-false-history-lift` prove the absence of a lift. Thus even existence of arbitrary-arrow lifts, before any cartesian uniqueness condition, does not follow from WG specialization.

This is the boundary on transferring comprehension/fibration theorems. A general comprehension-category account requires additional base/morphism choices, reindexing operations and cartesian structure; those are not established by the displayed graph identification.

## Verification and disposition

Fresh safe Cubical Agda is run through `research/nima/checkers/check_cubical_agda.ps1 -Module DisplayedWitnessSpecialization -Fresh`. The receipt and full log are `results/agda-DisplayedWitnessSpecialization.json` and `.log`. The final source uses a general displayed-history eliminator, avoiding the unsupported indexed-pattern-match warning seen in an intermediate counterexample proof. Only the pre-existing `TypedGeneratorLayers.agda` import warning remains.

The SCC model `composable-witness-specialization` includes this source and receipt alongside the actual-operation pentagon and triangle. Its receipt checker validates all three closures against compiler, library, adapter and owner-source hashes; SCC is not a second mathematical proof engine.

The demonstrated transfer is precise: specialization compilation and composition are displayed graph totalization/dependent sums, and history totalization matches the library category construction under stated hom-set assumptions. The next distinct mathematical obligation is reindexing along non-definitional WG comparisons—not more rebracketing of the same dependent tuples. No general fibration, comprehension category, bicategory, or physical-time semantics is claimed.
