# A checked path of type-and-value realizations

## New export for the model

`agda/ClosureTypedRealization.agda` treats a realization as a pair (T,v), where T is a small type and v inhabits T. The total type of such pairs is `TypedRealization = Sigma (T:Type), T`, which lives in the next universe.

Given an equivalence e:A≃B and a checked compatibility path e(a)=b, it constructs:

- a type path ua(e):A=B;
- a dependent value path over that type path, from a to b;
- a single path (A,a)=(B,b) in TypedRealization.

The value is not equated with its type. Types are one component of the pair; their inhabitants are the other, dependent component.

## Applied to the actual cofiber operation

`CofiberOperation` uses the previously independently constructed filtration-ladder operation F4 between double cofibers, the corresponding operation F1 between single cofibers, and the already checked equivalence between those function types.

The starting realization is (V4,F4), not a replacement function manufactured to make the endpoint agree. The ending realization is (V1,F1).

`operationAlongTypes` is a dependent path between these functions over the univalence path of `operationEquivalence`. `realizationPath` packages it as a path of typed values.

`preservedOriginalComparison` verifies that extracting the endpoint comparison through univalence gives back the original `chosenOperationComparison`, including its path witness. This is not merely an equality of the two endpoint types.

## Applying a moving operation to a moving input

A second construction changes the input and output types separately along the two rejoin equivalences. Its intermediate operation type is an actual function type from the current input realization to the current output realization.

Exports include:

- `arrowAlongTypes`: the operation across the changing domain and codomain;
- `inputAlongTypes`: a chosen input across its source rejoin path;
- `evaluationAlongTypes`: application of the intermediate operation to that intermediate input;
- `evaluatedRealizationPath`: the resulting path of typed output values.

Thus the model now explicitly supports evaluation while the presenting types change, not only a path between opaque function-type inhabitants.

The whole-function-type univalence path and the separately domain/codomain-shaped type path are two valid constructions with the same endpoints. Their equality is not asserted here; it would be an additional comparison theorem.

## Comparison of compatible realization choices

`ChoiceCoherence` works with the fiber of e over b, whose points are an inhabitant of A and its compatibility witness with b. A path between such choices gives a dependent comparison between their typed-realization paths, with source endpoints varying along that same choice path.

In the cofiber instance, the actual choice is compared with the transported choice. The latter's value is checked to be the previous F2-after-input-rejoin presentation. This retains the map-and-witness perspective rather than erasing the square witness.

`returnLaw` proves that following this particular realization path and then its reverse returns to the original typed realization. It does not identify an arbitrary independent return transition with that reverse.

## Diagnostic: same endpoint type does not imply same endpoint value

The regression constructs Boolean negation as an equivalence Bool≃Bool. Its univalence path begins and ends at Bool, but permits a dependent value path from false to true. Consequently there is a path of typed realizations

(Bool,false) = (Bool,true)

whose type component is the swap path in the universe.

There is no contradiction with false≠true inside the fixed type Bool. The regression also proves that no such dependent value path exists over ua(idEquiv Bool). The selected type path matters, not only its endpoint types.

For the model, this explains why a realization cycle must track transported values and compatibility, rather than declaring closure just because its type label returns. It is consistent with the earlier invertible-transition/holonomy counterexample.

## Regression and verification

`agda/ClosureTypedRealizationRegression.agda` also instantiates the cofiber theorem with circle-loop witnesses for both original ladder squares. It checks both faces, recovery of the original proof, evaluation at the input/output faces, and the dependent family of typed-output paths along an entire circle loop of inputs.

Fresh final-source check:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureTypedRealizationRegression.agda`

Exit 0. Both new modules use `--safe --cubical --guardedness`, without holes or postulates. Existing modules were not modified.

Initial incremental checks caught a module-name collision with the library's `Lift` and insufficient inference of the source inhabitant in a module application. Renaming the helper module and explicitly specifying F4 and F1 resolved these before the successful check.

## Scope

This packages and connects existing model data using standard dependent paths and univalence. It adds no analytical realization equivalence, no new Pi/product factorization, and no identification of a value with its own type. The next integration task is to carry the explicit finite-cut routes and their higher comparisons through this type-and-value presentation, while keeping the chosen return paths and any holonomy visible.
