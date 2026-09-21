# Boolean-indexed arity: sum/product interpretation and cofiber bridge

## What is formalized

The chosen reading is "for every input index, a function", not "a function consuming all input values jointly".

`agda/ClosureBooleanArity.agda` defines the single Boolean-indexed family

`F s t = (i : K s) (j : L t) -> X s i -> Y t j`.

A false flag selects a Unit index and the unindexed type; a true flag selects the supplied index family. The three corners containing Unit indices have explicit isomorphisms to the requested ordinary signatures. The fully indexed corner already has exactly the requested type.

For all four cases simultaneously, `sumProductEquiv` proves

`F s t ≃ (Sigma (K s) (X s) -> ((j : L t) -> Y t j))`.

`assemble` and `disassemble` are actual inverse functions. Input indices assemble as a dependent sum, output indices as a dependent product. This corrects any attempted identification of these independent-input signatures with the earlier joint-input product signatures.

## A square is additional data, not a Boolean path

The flags alone are discrete labels. `Indexing` takes two concrete maps:

- input assembly: Sigma I Ai -> A;
- output observation: B -> Pi J Bj.

It constructs the input-indexing and output-indexing operations on the function types. `square` proves that applying these in either order gives the same function family. The equality follows from the actual formulas, not from an assumed square witness.

If those two supplied maps are equivalences, `Reversible` constructs inverse operations with both inverse laws. `cycleLaw` checks the cycle

unindexed -> output-indexed -> both-indexed -> input-indexed -> unindexed.

The cycle uses the inverse of output indexing and the inverse of input indexing on its return edges. No path false=true and no automatic equivalence between arbitrary corners is asserted.

## Connection to the existing cofiber construction

`agda/ClosureBooleanArityCofiberBridge.agda` uses the already checked filtration-ladder map and its four HoTT presentations.

The required extra realization data are stated explicitly:

- a sum frame, Sigma I Ai equivalent to the source double cofiber;
- a product frame, the target double cofiber equivalent to Pi J Bj.

Composing those frames with the canonical rejoin/cut equivalences gives the assembly and observation equivalences needed by the selector square.

The bridge then compares two constructions of the fully indexed operation:

1. start with the unindexed cofiber map and apply the two indexing operations;
2. take the independently constructed map between double cofibers and express it in the supplied sum/product frames.

`operationComparison` proves these agree, using the previous higher comparison of the independently constructed map with transported rejoin data. `roundTrip` exports the cycle law for that particular operation.

The bridge does not manufacture the frames from the flags. Unlike the earlier product-boundary example, its input frame is a SUM frame.

## Tests

`agda/ClosureBooleanArityRegression.agda` includes three cases.

### Actual cofiber instance

The pointed target is Bool × Bool with point (false,false), in the existing Bool -> Unit -> X construction. Both index sets are Bool. The input sum has two Bool components; the output family has two Bool-valued coordinates.

The frames are constructed from the checked pointed-target cofiber equivalence and the explicit equivalence between pairs of Booleans and Bool-indexed Boolean functions. The vertical source map is Boolean negation and the target map swaps the pair coordinates. Both square witnesses are supplied and typechecked.

The regression checks agreement with the existing independently constructed cofiber map and the full four-corner round trip. It does not supply either desired comparison as an assumption.

### Higher-path case

Circle-valued input/output families verify that assembly retains the selected input tag and its loop, while a different output component can be constant. The full assemble/disassemble round trip is checked. No hom-set restriction is needed.

### No automatic cycle

Both index sets are nonempty Bool. The unindexed target is empty, whereas each indexed target is Unit. An indexed operation exists, but an unindexed one cannot. This proves there is no reverse output-indexing function, hence no equivalence of those two corners in general.

Thus a cycle requires the extra assembly/observation structure; it is not a consequence of the shape of the label square.

## Verification

Fresh check:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureBooleanArityRegression.agda`

Exit 0. All three new modules use `--safe --cubical --guardedness`, with no holes or postulates. Existing source modules were not modified.

An initial incremental check found a termination-checking issue in the copattern-defined sum/product isomorphism with a nested pattern lambda. Separating the two maps into named `assemble` and `disassemble` definitions with projection-based evaluation resolved it; both inverse laws then check by reflexivity. No termination pragma or unsafe bypass was used.

## Scope

This is the standard sum/product mapping law and its contravariant-input/covariant-output square, made explicit and connected to an actual instance of our cofiber model. It is not a new general mathematical theorem.

Still separate are intrinsic analytical choices of the input/output frames, compatibility with changes of those frames, and comparison of this indexing square with the full filtration cut pentagon. The earlier joint-input product model has not been silently relabelled as this independent-input model.
