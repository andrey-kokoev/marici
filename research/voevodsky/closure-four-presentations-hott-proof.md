# Four HoTT presentations of the checked filtration map

## Model-level realization

`agda/ClosureFourPresentations.agda` instantiates the four-presentation formulation using the already constructed arbitrary filtration-ladder maps. Nothing is assumed about products of endpoint families.

Write Q and Q' for the source and target double cofibers, C and C' for the corresponding single cofibers. Let e:Q≃C and r:Q'≃C' be the canonical rejoin equivalences. The existing ladder construction gives L:C->C' and U:Q->Q', together with a proved naturality square rU ~ Le.

The four operation types and their selected functions are:

- V1 = C->C', with F1=L;
- V2 = C->Q', with F2=cut' composed with L;
- V3 = Q->C', with F3=L composed with e;
- V4 = Q->Q', with F4=U.

Crucially, F4 remains the independently constructed ladder map. It is not redefined to make the square commute.

## Checked comparisons

`outputReassembly`, `inputReassembly`, and `independentSquare` give the first three compatibility witnesses. `F4-as-transport` compares F4 with F2 composed with e.

The module also exports equivalences of the ambient function types, including `operationEquivalence : V4 ≃ V1`. `chosenOperationComparison` proves that this particular equivalence sends the independently constructed F4 to F1 up to equality of functions.

This does not assert that F1 through F4 themselves are invertible functions. The original vertical maps and the resulting operation can be noninvertible. The equivalences are between presentations and their function spaces.

## Comparison including the square witness

For fixed F3, define

`CompatibleLift = Σ (F : Q->Q'), (r composed with F = F3)`.

Postcomposition by r is an equivalence from (Q->Q') to (Q->C'). Therefore `CompatibleLift`, its homotopy fiber over F3, is contractible. This is the standard HoTT equivalence-fiber theorem, applied to the actual model.

Two concrete inhabitants are constructed:

- `independentLift`: the existing F4 together with its proved ladder-naturality square;
- `transportedLift`: F2 composed with e, together with the target rejoin/cut inverse law.

`liftIdentification` compares these pairs. Its first projection is `functionIdentification`; its second projection is the dependent higher path `squareCoherence`. Thus the proof identifies not only the maps but also their square witnesses along that map identification.

Contractibility is asserted only for compatible map-and-square pairs with the rest of the square fixed. Neither the cofibers nor the full operation spaces are asserted to be sets or contractible.

## Regression

`agda/ClosureFourPresentationsRegression.agda` uses the previous ladder fixture with circle-loop witnesses for both commuting squares. It verifies:

- the identification of the actual and transported compatible pairs;
- the two faces of the higher square comparison, retaining the original naturality witness at one end and the reassembly witness at the other;
- the comparison family along a whole retained circle loop lifted into the double cofiber.

## Verification

Fresh check of the final sources:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureFourPresentationsRegression.agda`

Exit 0. Both new modules use `--safe --cubical --guardedness`, with no holes or postulates. Existing source modules were not modified.

## What this does not identify

The labels V1 through V4 denote these four function-type presentations. Identification with particular unary/many analytical operations, or with proposed endpoint-family products and residual boundary types, still requires explicit realization equivalences and compatibility proofs. A dependent-product factorization of a cofiber is not implied by the arity label.

This increment does not prove composition coherence for arbitrary filtration ladders, naturality of the complete pentagon under them, or coherence for arbitrary finite towers. It makes the user's four-presentation HoTT formulation precise for the already checked cofiber model.
