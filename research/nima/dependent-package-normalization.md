# Arbitrary dependent indices: checked normalization and route coherence

## Result

Arbitrary dependent index types are now supported by the recursive normalizer. They need not be finite, discrete, inhabited or sets. No event enumeration, choice axiom or truncation is used.

For every expression Q in `WholePackageSigmaPi.Code`, the checked construction supplies types S, P(s), A(s,p), together with an equivalence

    El Q ≃ Σ(s : S). Π(p : P(s)). A(s,p).

Both reconstruction directions are proved. The equivalence also induces equivalences of identity types, so normalization preserves higher witnesses, not just inhabitants.

Active obligation: route/coherencer compatibility. The claim tested is that faithful dependent normal coordinates support coherent comparisons without assuming arbitrary source-witness completeness. Rival failures are finite-index enumeration hidden in the construction, lost index holonomy, fabricated dependent sections, identification of raw histories, and treating arbitrary endpoint automorphisms as normalization-preserving.

## The recursive rules

A container retains Shape, Position and Entry as full types. An atomic type A has unit shape and unit position with entry A.

For a dependent sum over I, child containers C(i) combine as:

* Shape = Σ(i:I). Shape(C(i));
* Position(i,s) = Position(C(i),s);
* Entry(i,s,p) = Entry(C(i),s,p).

For a dependent product over I:

* Shape = Π(i:I). Shape(C(i));
* Position(f) = Σ(i:I). Position(C(i),f(i));
* Entry(f,(i,p)) = Entry(C(i),f(i),p).

These formulas retain all dependencies. In particular, a product's positions depend on its entire choice function. The product equivalence is constructive dependent choice for untruncated Sigma data: it rearranges supplied functions and pairs, rather than selecting witnesses from mere existence.

The implementation recurses through arbitrary well-founded Code syntax. E and Pi indices remain types; `maps` is treated as a dependent product. Path, equivalence and comparison payloads are preserved intact as higher-valued atomic entries. Normalization of these entries is not a presentation of their internal source identity theory.

The normal form is reexpressed in the same Code grammar and can be normalized again, with a checked second reconstruction. `Retained` stores the original expression, original value, normal value, forward agreement and reconstruction. The entire record becomes a subsequent Complete input at the next universe level.

## Coherence theorem and its exact hypothesis

A presentation P consists of its expression and an equivalence cP from its values to the same complete normal value type N. A coherent map from P to R is

    Π(x : El P). Σ(y : El R). cR(y) = cP(x).

This type is contractible: pointwise it is a fibre of the equivalence cR. Consequently any two such maps have a comparison, their comparisons have higher comparisons, and path-space contractibility can be iterated to any specified height.

Finite route records compose these maps and retain every step. Any two routes between the same coordinate-equipped presentations have compared evaluations. Their raw records are not identified.

The common-coordinate condition is substantive. An arbitrary equivalence can transport the coordinates to a new presentation, but this does not make that presentation equal to another presentation with the same carrier and different coordinates. No theorem here equates arbitrary automorphisms or automatically supplies common coordinates for every possible syntactic rule.

## Actual arbitrary-dependent resolution orders

`DependentArbitraryIndexRoutes.agda` checks the full outer-first and inner-first factorizations of

    Π i. Σ j. Π k. Σ l. B(i,j,k,l)

for arbitrary I, J(i), K(i,j), L(i,j,k) and B(i,j,k,l), all at any selected universe level. Both routes include their actual intermediate presentations and three versus four primitive maps. Each map's coordinate compatibility is checked by Agda; the final inner-first step is checked against the outer-first terminal coordinates, not against separately chosen endpoint coordinates.

The retained package includes the original value, the existing full seven-edge value trace, both route records and their comparison. It is reified as a subsequent Q without deleting those fields.

## Fresh checked regressions

`DependentPackageNormalizationRegression.agda` establishes:

* reconstruction for infinitely many indices n:Nat with dependent fibres Fin(n+1);
* reconstruction after normalizing the normal form again;
* correct handling of empty sum and empty product indices;
* a circle-index loop remains nontrivial after normalization;
* normalizing the circle double-cover section type cannot invent a section;
* a direct route and a reconstruction detour have compared evaluations but provably distinct raw records;
* Bool negation cannot satisfy identity normalization coordinates.

Fresh verification passed Agda 2.8.0-3d04bac / Cubical 0.9 under `--safe --cubical --guardedness`:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module DependentPackageNormalizationRegression -Fresh
```

Receipt: `research/nima/results/agda-DependentPackageNormalizationRegression.json`.
Log: `research/nima/results/agda-DependentPackageNormalizationRegression.log`.

## Disposition

The finite-index restriction has been removed from normalization and from the checked common-coordinate route-coherence theorem. The finite binary event-poset enumeration is not being generalized to an infinite event poset; the dependent proof replaces that mechanism.

The remaining comparison-basis obligation is syntactic: prove that every intended generated structural rule admits the required common coordinates, and connect the resulting certificates to `WholeHistoryComparisons.Structural.Generated`. Neither completeness for arbitrary atomic source identities nor a finite complete presentation of all package-level comparisons is claimed.

Proofs:

* `research/nima/agda/DependentPackageNormalization.agda`
* `research/nima/agda/DependentNormalizationCoherence.agda`
* `research/nima/agda/DependentArbitraryIndexRoutes.agda`
* `research/nima/agda/DependentPackageNormalizationRegression.agda`
