# Universal evaluation and the boundary of completeness

## Checked universal evaluation

`WholePackageUniversalProperty.agda` fixes the whole-package generator signature and a seed family S. An Algebra consists of a type-valued family of interpretations, an interpretation of each seed, and an interpretation of each rule on its interpreted premise family.

The following are checked:

* evaluate: every resolution tree receives an interpretation.
* least-closed: every seed-containing rule-closed family receives all generated resolutions, constructively.
* evaluate-unique / evaluate-unique-function: an interpretation that respects the constructors equals the canonical evaluator, as a function, given its preservation laws.
* fusion: a rule-preserving map after evaluation agrees with direct evaluation into the target algebra.
* rebuild-retains-history: evaluating into the original syntax reconstructs the full history.
* evaluate-path / evaluate-higher: identities and identities between identities of histories map to actual corresponding identities under evaluation.

These establish a free, rule-relative evaluation property. Uniqueness concerns the underlying evaluation function; contractibility of the entire space of homomorphisms including all preservation-law witnesses and higher laws is not asserted.

## What 'complete' currently means

The closure includes exactly its inductively generated derivations. Every rule-closed family containing the seeds receives them. In addition, admit-comparison and admit-higher explicitly show that a supplied well-typed comparison between reachable endpoints produces a reachable comparison package.

The word 'supplied' matters: compare-rule accepts an equivalence and its value-boundary path as arguments; higher-rule accepts the higher filler as an argument. They retain these witnesses rather than deriving all possible such witnesses from distributivity alone. The present signature therefore gives witness-relative admission, not a completeness theorem for synthesizing all semantic equivalences from a smaller structural basis.

## A checked separation

`WholePackageHistorySeparation.agda` starts from one complete package a and constructs two histories with exactly the same resulting complete package:

1. use the identity-comparison rule;
2. use the general comparison rule with the identity equivalence and reflexive boundary.

The resulting endpoint is identity-comparison(a) in both cases. A constructor discriminator proves that the two histories are unequal. No extra seed for the target package is used.

Thus equal results do not automatically identify full histories. This is consistent with the retention requirement. Semantic comparison of distinct histories must be represented by additional comparison data, not silently replaced by equality of raw derivation trees.

## Next precise target

Define comparisons of full resolution histories relative to a specified interpretation, retaining both raw histories and their comparison witness. Then distinguish the comparisons generated structurally from arbitrary externally supplied witnesses. This is the next step toward a meaningful completeness theorem for comparisons rather than the already checked least-closure theorem for derivations.

## Verification

Fresh `--ignore-interfaces` checks succeed for both modules using Agda 2.8.0.1 and Cubical 0.9. They use `--safe --cubical --guardedness`, with no new postulates or holes.

```
agda --ignore-interfaces --transliterate -i research/nima/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/nima/agda/WholePackageUniversalProperty.agda
agda --ignore-interfaces --transliterate -i research/nima/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/nima/agda/WholePackageHistorySeparation.agda
```

Both exit 0. The history-separation proof required explicit case splitting on its two comparison premises; the final fresh check includes that correction.
