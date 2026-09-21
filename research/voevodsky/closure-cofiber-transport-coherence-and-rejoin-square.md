# Cofiber transport coherence and the remaining rejoin square

## Result

For A -> B -> C -> D, the model now compares direct transport B/A -> D/A with transport through C/A. This is the shared-boundary homotopy required before comparing the full quotient-rejoining assemblies.

The new modules are `agda/ClosureCofiberTransportCoherence.agda` and `agda/ClosureCofiberTransportRegression.agda`.

The full rejoin-naturality comparison is NOT proved in this increment. Its two maps are now constructed with exactly matching source and target, and its required homotopy is named `RejoinSquare`. That name defines a type, not an inhabitant or an assumption.

## Actual maps and proofs

`Transport.direct` defines fixed-source cofiber transport by higher-inductive elimination, with an explicit action on every attachment path. `Transport.normalize` gives a homotopy from the existing 3-by-3-induced map to this map. Its attachment square is the previously proved unit-concatenation comparison, not an imposed equality.

`normalizedCofiberComposition` transports the existing cut/rejoin equivalence along that map identification. Thus the older theorem is connected to the new maps rather than silently replaced by an unrelated equivalence.

`Triple.directComposition` compares the two normalized transport routes, and `Triple.originalComposition` compares the ORIGINAL 3-by-3 transport routes using normalization, composition, and the reverse normalization. Both homotopies are defined on the complete cofiber.

For four composable maps, `Quadruple.left` and `Quadruple.right` assemble the normalized composition witnesses in the two possible ways. `comparisonOfComparisons` proves these paths equal. This is a genuine higher equality in the path-retaining model. It is simple because the normalized transports have strict constructor behavior, not because the cofibers were truncated to sets.

## Exact remaining square

For f:A->B, g:B->C, h:C->D, let P be normalized transport B/A->C/A, Q be normalized transport C/A->D/A, and R be normalized transport B/A->D/A.

The shared-boundary proof compares QP and R and hence supplies a comparison between their cofibers.

The two constructed parallel maps have source cofib(P), namely (C/A)/(B/A), and target cofib(hg), namely D/B:

- `transportThenRejoin`: use induced transport into cofib(QP), apply the boundary adjustment to cofib(R), then the normalized rejoin equivalence for f and hg;
- `rejoinThenTransport`: rejoin via the normalized equivalence for f and g into C/B, then transport to D/B using g and h.

`RejoinSquare` asks for a homotopy between precisely these two functions. This is naturality of the specific constructed rejoin equivalence. It is not supplied merely by the fact that its source and target types are equivalent, or by constructor-level composition of the lower transport maps.

Proving it requires tracking the 3-by-3 equivalence and span-contraction equivalences under h, or establishing a fully boundary-compatible canonical characterization of the rejoin map and comparing the previous construction to it.

## Nontruncated regression

For Bool->Unit, the cofiber is equivalent to the circle. The regression proves that normalized identity transport preserves the loop obtained from the two attachment paths. It also checks the higher compatibility as a family over the entire circle, not only at its base point.

This is a regression of the cofiber transport model, not a claim concerning an analytical circle obstruction or physical realization.

## Verification

Ran a fresh dependency-closure check:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureCofiberTransportRegression.agda`

Agda 2.8.0.1 / Cubical 0.9: exit 0. Both modules use `--safe --cubical --guardedness`. No holes, postulates, or assumed inhabitants of `RejoinSquare` were added. Existing modules were left unchanged.

## Disposition

Established: fixed-source transport composition, its comparison with the prior maps, and a higher compatibility of normalized composition witnesses.

Still required: the constructed rejoin maps' naturality square, followed by compatibility of the full cut/rejoin assemblies. This increment does not close the latter by relabelling the lower transport coherence as that theorem.
