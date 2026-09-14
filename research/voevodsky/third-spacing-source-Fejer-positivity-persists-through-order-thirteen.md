# Third-spacing source Fejér positivity persists through order thirteen

## Third de-aliasing scale

Keep

\[
\sigma=0.005
\]

and halve the spacing again:

\[
h=0.0625.
\]

The source kernel was evaluated at the twelve spacing multiples required for Fejér orders through thirteen.

## Result

Every order from two through thirteen remains globally positive after angle interpolation and coefficient allowances.

The tightest case is now order eleven at angle \(\pi\). Its values are approximately:

- mesh minimum: \(0.00108980\);
- interpolation allowance: \(0.00007736\);
- coefficient allowance: \(0.000021\);
- conditional global lower bound: \(0.00099144\).

## Comparison across spacings

The tested spacing sequence is

\[
0.25,
\qquad0.125,
\qquad0.0625.
\]

Positivity through order thirteen persists at all three scales. The tightest angle does not move monotonically toward zero: at the third scale it occurs at \(\pi\), and the lower margin increases relative to the second scale.

This falsifies the tentative interpretation that the low-angle margin was already collapsing monotonically under spacing refinement.

## Scope

Three spacings are finite evidence, not a vanishing-spacing theorem. The order remains capped at thirteen, while the RH-equivalent statement quantifies over every order at every spacing in an infinite refining sequence. Moreover, fixed-rank nonconstant margins generally shrink on the \(h^2\) scale, so a valid refinement must shrink coefficient errors or grow rank; see `research/voevodsky/vanishing-spacing-requires-shrinking-error-or-growing-rank.md`.

## Verification

```text
python research/voevodsky/checkers/scout_quarter_spacing_fejer_hierarchy.py
```

Artifacts:

- `research/voevodsky/checkers/scout_quarter_spacing_fejer_hierarchy.py`
- `research/voevodsky/results/quarter_spacing_fejer_hierarchy.json`
