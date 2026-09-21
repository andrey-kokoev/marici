# The actual four-piece gluing pentagon

## Constructed comparison

`agda/ClosureGluingPentagon.agda` treats a chain of four arbitrary small types and three attachment boundaries:

`A <- S -> B <- T -> C <- U -> D`.

The five realizations are the five bracketings of this chain. The two routes from the fully left-associated to the fully right-associated realization are:

- long: rotate the left subtree, rotate the root, rotate the right subtree;
- short: rotate the root through the balanced bracketing, then rotate again.

The root rotations reuse the previously constructed three-piece associator. The two subtree rotations are explicitly defined on the outer pushout, including its attachment paths, and proved equivalences using the earlier associator's inverse laws.

No set-truncation or emptiness condition is imposed on the pieces or attachment boundaries.

## Proof before coherence machinery

`pentagonAt` proves the two actual composites agree on every point inclusion and all three attachment-path families of the starting nested pushout. Function extensionality gives `pentagon`.

`equivalencePentagon` lifts this equality to the composite equivalences, using that being an equivalence is a proposition.

This is an explicit proof about the selected reassociation maps. It is not obtained by assuming the desired pentagon as a field of a comparison record.

## Type paths and residual action

`longTypeRoute` and `shortTypeRoute` are concatenations of the univalence paths of the actual reassociation edges. `typePentagon` compares these concatenated paths, using the checked map/equivalence pentagon and univalence's composition law.

`closedTypePentagon` proves that taking the long type route and returning along the short one gives a loop homotopic to the stationary loop. `residualIsIdentity` consequently proves that transport along this loop fixes every inhabitant of the starting realization.

Thus this pentagon satisfies the strong return condition: not just equal endpoint types or a returning selected value, but a null-homotopic type loop. This does not declare arbitrary other loops in the realization trivial.

## Explicit compatibility lift

At the fixed function type from the starting to the final realization, the long route is the reference operation. The short route's compatibility square is the reverse of the proved pentagon.

`compatiblePentagon` explicitly varies both the operation and that square. Forgetting its square recovers precisely the original pentagon path, as checked by `forgetCompatiblePentagon`.

`agreesWithGenerated` compares this particular lifted path with the generated compatible-presentation comparison, at the same fixed endpoints and witnesses.

This is a bridge from the explicit proof to the generic coherence mechanism. It does not assert that independently prescribed alternative square witnesses are already identical to these choices.

## Three-loop regression

`agda/ClosureGluingPentagonRegression.agda` takes four point pieces and three Bool attachment boundaries. It constructs one loop from each pair of attachment paths.

A circle-valued detector assigns independently chosen circle loops to the three pairs. The regression computes its action after the long route and, using the explicit pentagon, after the short route. Setting one detector to the circle loop and the other two to reflexivity distinguishes the three contributions.

All three images under the long route are proved nontrivial. The computed short-route actions retain the same detections. This is not presented as a full classification of the loop space.

The explicit compatibility lift and its agreement with the generated comparison are instantiated as well. Earlier gluing, reassociation, and dependent-boundary regressions are included in the dependency closure.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureGluingPentagonRegression.agda`

Exit 0. Both added modules use `--safe --cubical --guardedness`, without holes or postulates. Existing source modules were not changed.

## Remaining scope

This closes the four-piece pentagon for the actual three-piece associators constructed in this development. It does not yet construct every higher associahedral relation for arbitrary gluing trees, identify older independently selected cofiber-pentagon witnesses with this one, or supply analytical realization data.

The next structural generalization is a reusable normalization/comparison mechanism for arbitrary finite gluing-chain bracketings, rather than adding another hand-written polygon at each size.
