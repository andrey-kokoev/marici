# Pasting canonical rejoin squares

## Checked result

For A -> B -> C -> D -> E, two successive canonical rejoin-naturality squares (for h:C->D and k:D->E) agree with the single square for their composite kh, after explicit comparison of their upper and lower boundary maps.

The theorem compares the path witnesses, not merely their endpoints. The inverse-cut squares satisfy the corresponding comparison.

Implementation: `agda/ClosureRejoinSquarePasting.agda`.
Regressions: `agda/ClosureRejoinSquarePastingRegression.agda`.

## The compared assemblies

Write R for the canonical rejoin equivalence, U for induced transport of double cofibers, and L for transport of single cofibers. Subscripts indicate the target transport.

Both compared paths start at R(U_k(U_h(x))) and end at L_k(L_h(R(x))).

- `pastedRejoin` first applies the square for k at U_h(x), then the square for h transported by L_k.
- `compositeRejoin` first compares U_k U_h with U_kh, applies the independently instantiated square for kh, then reverses the comparison L_k L_h with L_kh.

The upper comparison is proved by elimination on the entire double cofiber. The lower comparison uses the previously proved normalized cofiber transport composition. Thus the two assemblies have the same endpoints by explicit boundary homotopies, not by an assumed strict law.

`rejoinPasting` proves equality between those two paths. It includes the nested attachment-square constructor. The proof uses the path unit law to compare the resulting concatenations; reflexivity concatenations are not silently treated as strict.

`pastedCut`, `compositeCut`, and `cutPasting` give the inverse-direction construction and proof.

## Verification coverage

One fixture has nonempty A=Bool, B=Unit, C=D=E=Bool, and h=k=Boolean negation. It checks the nested attachment family, the inverse pasting family, and the transported point after both nonidentity maps.

A second fixture has a circle as the rejoined output. It checks the higher-comparison family along an entire lifted circle loop. This is a dependent path through the family of comparisons, not only a check at the base point.

Fresh closure check:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureRejoinSquarePastingRegression.agda`

Exit 0. Both new modules use `--safe --cubical --guardedness`, with no holes or postulates. Existing modules were not modified.

## Scope and next gate

This closes compatibility under successive **target postcomposition** for the chosen canonical rejoin and cut squares. It is not yet the pentagon for arbitrary rebracketings of filtration decompositions. It also does not identify the canonical implementation with the earlier opaque 3-by-3/univalence-transported choice.

The remaining filtration-level task is to encode changes of the intermediate cut itself, rather than only postcomposition of the final target, and compare the resulting rebracketing routes. Naturality-square pasting is now proved data available to that construction, not a placeholder for its pentagon.
