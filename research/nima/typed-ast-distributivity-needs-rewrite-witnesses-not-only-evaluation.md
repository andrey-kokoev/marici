# Typed AST distributivity needs rewrite witnesses, not only evaluation

The earlier opposite-presentation checker compared evaluations of constructed ASTs. That did not test explicit local rewrite histories. The new checker supplies that missing layer.

## What is checked

The typed AST has labelled P, Q and H leaves, rational scaling, sums, and ordered products. Sum operands must have the same corners; products require adjacent compatible endpoints.

Local rules implement left and right distributivity, right association, scalar extraction, scalar distribution, nested-scale multiplication, and sum flattening. Each rewrite records its rule, subtree address, and before/after trees. The checker verifies the exact local rule, typing, actual marked-source value, and independent interaction-coordinate value.

Four reachable rewrite graphs are enumerated exhaustively:

| Root | States | Rewrite edges |
|---|---:|---:|
| competing left/right distributions | 19 | 24 |
| association versus distribution | 286 | 775 |
| signed rational scalar distributions | 17,157 | 78,204 |
| cancellation | 59 | 114 |

This covers 79,117 edges. The terminal ASTs need not be literally identical: different summand orders survive. They agree after collecting coefficients of **ordered labelled formal monomials**. This comparison does not use H=Q-P, so an accidental equality of source values cannot hide a failed formal distributivity calculation.

The full three-sum rewrite graph exceeded the 30,000-state limit. The checker does not claim exhaustive coverage there. Instead, 32 reproducible seeded schedules complete, checking 606 steps and agreeing on the same collected formal sum.

## Replay and observers

Every saved trace survives JSON serialization, verifies forward, and replays backward to its exact original AST. The backwards replay requires that trace; a collected source value alone does not determine its original construction history.

The saved routes also pass 2,502 comparisons of full ordered Fox records. Thus the checked AST rewrites preserve the actual observations, not merely an invented expression score.

Negative controls reject a dropped summand, a wrong sign, reversed incompatible factors, and an incorrect rewrite-rule label.

## Interpretation

Expansion and regrouping can be oppositely directed presentations of a common retained source. Explicit AST witnesses now connect those directions in the tested cases. This does not exchange addition with multiplication, commute source factors, establish unrestricted rewrite confluence, or identify arbitrary presentation categories with categorical opposites.

## Reproduction

`python research/nima/checkers/check_typed_ast_distributivity.py`

Artifact, including serialized rewrite traces:

`research/nima/results/typed-ast-distributivity.json`
