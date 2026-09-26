# Comparison completeness reduces to specified boundary theories

## Question

Do E/Pi introduce independent identity-witness generation obligations, or can their comparisons be reconstructed uniformly from generators at the required source boundaries?

The active SCC obligation is route/coherencer compatibility. The tested conjecture is local: a specified boundary-generator theory that represents all identity witnesses at the boundaries listed by a frozen code suffices to represent every identity witness between values of that code. The risky alternative is that completeness secretly requires injective decoding, deletes duplicate derivations, or imports the desired entire composite witness as one primitive.

## Claim boundary

### Two former residual cases now decompose

`SigmaPiComparisonDecomposition.agda` no longer leaves equivalence-code and comparison-code identities opaque.

* Equality of equivalences reduces to pointwise equality of their functions; the `isEquiv` field is proposition-valued.
* For the comparison graph Sigma(x:A).Sigma(y:B).(e(x)=y), projection to x is an equivalence because each target-and-path fibre is contractible. Its induced path equivalence reduces comparisons of graph records to comparisons in A.

These are reversible comparisons, not deletions of the original records. Certificates retain their endpoints, original witnesses and reconstruction paths. The graph reduction applies with e fixed; comparisons between distinct e parameters are a separate boundary.

### Local witness-sensitive completeness

Fix a source generator family G(A,x,y) with a decoder into x=y. No injectivity, uniqueness, discreteness or completeness is built into G.

A representation of a particular witness p is a pair

(g : G(A,x,y), proof : decode(g)=p).

`Requirements(Q)` recursively lists the required completeness assumptions:

* atom A: the theory for A;
* E(I,F): the theory for index I and the requirements of every fibre F(i);
* Pi(I,F): the requirements of every fibre;
* map and equivalence nodes: the requirements of their codomain;
* retained provenance: the requirements of the interpreted expression;
* comparison graph: the requirements of its source;
* a path node: the theory for its decomposed lower-witness type.

`local-completeness` proves that Requirements(Q) suffices for every p:x=y in El(Q). It constructs recursively decomposed evidence, a source derivation supporting each required boundary witness, and a higher path showing that decoding reconstructs the particular p. `local-family-completeness` does the same with a retained coded index and dependent fibre family.

The higher-boundary requirements are explicit. This theorem does not automatically generate the identities of the lower-witness types from a finite collection of primitive atomic loops. Requirements may also range over infinite dependent index families: the schemas are finite in number, not necessarily their instantiated premises.

### Universal reduction

For this code universe, which contains atom A for every small type A, all-code witness completeness implies all-source witness completeness by the atom case. The converse is the recursive construction. `completeness-reduction` checks both functions.

This is a logical equivalence of obligations, not an equivalence of their proof spaces. The all-source premise quantifies over all small types and is consequently strong; the usable theorem for a fixed expression is the local one above. Neither theorem proves a finite source-generator basis or equates arbitrary raw resolution trees. The earlier `WholeHistoryComparisons.Structural.Generated` relation is not identified with this supported decomposition language.

## Disposition

Fresh Cubical Agda verification passed for `SourceRelativeComparisonCompletenessRegression.agda`, including its imported dependency closure, under safe/cubical/guardedness and without new postulates or holes.

Constructive regressions:

1. A source language that attaches either Bool tag to the same path is complete, yet its two tagged derivations are provably distinct. Completeness does not collapse retained derivations.
2. The identity and negation equivalences of Bool have no pointwise comparison witness. The equivalence-code rule does not identify distinct maps.
3. A circle loop becomes decomposed evidence for a comparison-graph loop; roundtrip reconstruction preserves that evidence. The local theorem for this graph needs only the circle source theory.
4. A source language requiring its underlying type to be a set cannot cover the circle. The converse reduction proves that E/Pi closure cannot repair this source-theory failure.

The redundant-path source language is a test of the transfer theorem, not a proposed finite presentation of all source homotopy types. The next scientific obligation is to specify and test the source comparison theory for the intended complete resolution package; extra E/Pi wrapper laws alone do not discharge it.

### Verification

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SourceRelativeComparisonCompletenessRegression -Fresh
```

Exit 0, Agda 2.8.0-3d04bac / Cubical 0.9. Receipt and log:

* `research/nima/results/agda-SourceRelativeComparisonCompletenessRegression.json`
* `research/nima/results/agda-SourceRelativeComparisonCompletenessRegression.log`

The earlier index regression was also freshly rechecked after changing its imported decomposition. SCC model `nima-source-relative-comparison-completeness` passes its source-digest/receipt audit. SCC does not replace the compiler check or promote this relative theorem into global resolution-order completeness.
