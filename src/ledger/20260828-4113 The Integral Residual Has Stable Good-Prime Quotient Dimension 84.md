# 4113 — The Integral Residual Has Stable Good-Prime Quotient Dimension 84

## Claim

The unit-associated-grade reduction of the primitive integral barcode presentation leaves a sparse integer matrix with

\[
14{,}566\text{ rows},\qquad 2{,}278\text{ columns}.
\]

Exact sparse Gaussian elimination over each frozen barcode field gives

\[
\operatorname{rank}_{\mathbf F_p}R=2{,}194
\]

for

\[
p\in\{31991,32003,32009\}.
\]

Hence every tested good-prime residual quotient has dimension

\[
2{,}278-2{,}194=84.
\]

## Frozen source object

The matrix is exported directly from the source-normalized primitive integer presentation with SHA-256

`9e35bf07ebd20182e5ce52efe7bd76b2955818b273f5182429a48e2e628a8679`.

Its deterministic sparse export has SHA-256

`959634401f4749e9d4b349e66e55ea23731e632134aa4aaa2910bda8c68873fc`.

No finite-field pivot row was lifted back to characteristic zero. The fields only receive reductions of the same integer matrix.

## Result

The three independently tested fields agree:

| Prime | Rank | Quotient dimension |
|---:|---:|---:|
| 31991 | 2194 | 84 |
| 32003 | 2194 | 84 |
| 32009 | 2194 | 84 |

This falsifies the provisional expectation that the complete filtered residual object would immediately reproduce dimension 53. The number 53 belongs to a further quotient or differently typed object; it cannot be identified with this residual cokernel without an independently derived map.

The modular result implies

\[
\operatorname{rank}_{\mathbf Q}R\ge 2{,}194,
\qquad
\dim_{\mathbf Q}\operatorname{coker}R\le84.
\]

It does not yet prove equality over \(\mathbf Q\), nor torsion-freeness of the integral cokernel.

## Interpretation

The associated grades are individually saturated, but their extension assembly retains 84 good-prime classes. Thus the missing integral lift is not a componentwise Smith problem. It is an extension-level saturation problem on a substantially smaller residual module.

The next finite gate is to derive a characteristic-zero upper bound of 84, then compute enough Smith data to determine whether the 84-dimensional generic quotient carries integral torsion.

## Durable artifacts

- `research/benincasa/checkers/check_interaction_net_integral_source_presentation.py`
- `research/benincasa/checkers/rank_interaction_net_residual.cjs`
- `research/benincasa/results/interaction-net-integral-residual-matrix.txt`
- `research/benincasa/results/interaction-net-integral-residual-ranks.json`

Sequence claim: `seqclaim-87c882f0828350ebd0535946`.
