# Selected higher witnesses: exact admission criterion and obstruction

## Result

Automatic admission of independently chosen higher witnesses is false, even when their endpoint maps are admitted. The missing information is coherence with the endpoint normalization-square witnesses.

`agda/ClosureSelectedHigherAdmission.agda` now expresses the exact existence criterion in every finite globular dimension. `agda/ClosureSelectedHigherAdmissionRegression.agda` checks both a counterexample and integration with unrestricted root-rotation admission.

## All finite dimensions

The source tower consists of cells in a contractible compatible-presentation space. The target tower consists of cells in the underlying space, with **no contraction or truncation assumption**.

The forgetful map is extended recursively to boundaries and cells. For an already lifted boundary and a selected target cell h, a lift consists of:

- a compatible source cell alpha with that boundary;
- an equality identifying its projection with the selected h.

A lift exists exactly when h equals the projection of the generated compatible filler. Both implications are proved for every finite dimension.

This is an existence criterion, not a claim that the space of lifts is contractible: the equality identifying the projection is itself additional higher data.

## The explicit higher normalization square

For presentations `(F, squareF)` and `(G, squareG)` and a selected path `h : F = G`, the required coherence is:

`PathP (lambda i -> post (h i) = target) squareF squareG`.

The module constructs a path of complete presentations from this witness, with judgmentally retained projection h. Conversely, a compatible lift yields the required coherence. Thus the API does not replace a supplied homotopy with another path merely having the same endpoints.

## Circle counterexample

The regression uses an admitted identity edge on a single circle-valued piece. Both endpoint presentations have the identity function and reflexive normalization square.

The selected homotopy `turn = funExt rotLoop` evaluates to the nontrivial circle generator at the basepoint. A compatible lift would be a loop in the contractible compatible-presentation space. Contracting that loop and projecting it would contract `turn`, hence the circle generator: a contradiction.

Consequently, this homotopy has neither a compatible lift nor a higher normalization-square witness for those endpoints. It also cannot equal the projection of the generated filler.

## Endpoint witnesses cannot be discarded

A second admitted identity edge retains the same function but uses `rotLoop` as its normalization square.

From this twisted presentation to the reflexively witnessed identity presentation, the **same** selected `turn` does have a compatible lift. Its higher square is the explicit interval-connection filler `rotLoop x (i or j)`.

Conversely, a stationary underlying function path cannot compare those two presentations: that would erase the nontrivial square witness.

Thus liftability depends on the complete endpoint presentations, not merely on the two functions.

## Root-rotation integration

For arbitrary piece types, attachment maps, and three finite subtrees, the regression instantiates the criterion on the complete comparison already supplied by `ClosureArbitrarySubtreeRotationAdmission`.

Its projected function path has the required higher square, retains its selected projection, and equals the projected generated filler. This tests the existing compatible comparison; it does not automatically certify every independently chosen homotopy between the same underlying maps.

## Verification

Fresh final-source check:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureSelectedHigherAdmissionRegression.agda`

Exit 0, approximately 3 minutes 28 seconds. Both new sources use `--safe --cubical --guardedness`, without holes or postulates.

This closure rechecks the arbitrary-subtree root theorem and its induction dependencies, together with the new regression. It does not rerun the separate fifteen-piece regression; that retains its previously recorded fresh verification.

## Remaining constructive gate

Update: [Coherent context admission](closure-coherent-context-admission.md) proves lifting through arbitrary finite contexts when both port witnesses and their higher normalization coherence are supplied. The remaining native-rotation task is constructing that complete port package for the chosen unrestricted root comparison, and identifying any separately implemented strict contextual maps. Automatic admission of arbitrary selected higher witnesses is not an open conjecture: the regression disproves it.
