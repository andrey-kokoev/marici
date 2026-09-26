# Admissibility is not an origin record

Fresh safe Cubical Agda --ignore-interfaces check passes for `agda/ObserverAdmissibleImages.agda`; log: `results/agda-admissible-images.log`.

For f:X→Y define:

    Record(f) = Σ(y:Y) Σ(x:X) (f(x)=y)
    Image(f)  = Σ(y:Y) ∥Σ(x:X) (f(x)=y)∥

Record retains the particular origin; Image retains the output plus mere admissibility. The preceding record theorem made Record equivalent to X. Here only fibre MEMBERSHIP is truncated, not Y or its identity witnesses.

The module checks a path-space equivalence between image elements and their underlying outputs. Thus admissibility adds no new identity choices, while any higher paths already present in Y remain. Postprocessing maps admissible images to admissible images of the composite, and commutes with actual source arrival.

## Separation tests

For Bool→Unit, records for true and false remain distinct, while their images are equal. Any decoder that claims to recover both bits from the admissible output contradicts true≠false. The same obstruction holds for an image-level factorization back to the identity Bool observer: restricting to images does NOT secretly undo loss.

For an empty source, the image of its map into Unit is empty. A factor between the two empty admissible images exists vacuously, without requiring an impossible total Unit→Empty function at an unreachable output. This repairs the exact unused-output counterexample; it does not establish that every collision-preserving map has image descent.

`ImageFactors(f,g)` is now defined as the preceding witnessed Factors relation between the arrival maps X→Image(f) and X→Image(g). It is not a temporal relation.

## Foundational boundary

Hiding origin membership is an EXPLICIT observer operation. The underlying source and its witnesses are not globally quotiented. If an observer actually retains an origin record, that observer has more information; calling the record mere admissibility would misdescribe it.

No reconstruction was extracted from a truncated witness into an arbitrary non-propositional type. Such an extraction would require coherence. Next establish a precise constructive descent criterion for SET-valued outputs, where higher output path ambiguities are absent, and retain general higher-valued descent as a separate question.
