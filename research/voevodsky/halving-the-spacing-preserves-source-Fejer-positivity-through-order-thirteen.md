# Halving the spacing preserves source Fejér positivity through order thirteen

## Second spacing

Keep

\[
\sigma=0.005
\]

and halve the translate spacing to

\[
h=0.125.
\]

Source kernel coefficients were evaluated at all multiples \(mh\) needed for Fejér orders through thirteen.

## Result

Every Fejér polynomial with

\[
2\leq N\leq13
\]

has a positive global lower bound after including angle-mesh interpolation and the inherited source coefficient allowances.

The tightest case occurs at order seven and angle zero. Its values are approximately:

- mesh minimum: \(0.00069598\);
- interpolation allowance: \(0.00003291\);
- coefficient allowance: \(0.000013\);
- conditional global lower bound: \(0.00065007\).

## Significance

This is the first step in the required de-aliasing direction. Positivity through order thirteen now holds at both

\[
h=0.25
\]

and

\[
h=0.125.
\]

The margin decreases after halving the spacing, and the tightest angle moves to zero. This indicates that the low-angle sector should be monitored as spacing tends to zero.

## Scope

Two spacings do not constitute a vanishing sequence theorem. Orders above thirteen are untested, and the coefficient enclosures remain conditional on the inherited floating model.

## Verification

```text
python research/voevodsky/checkers/scout_halved_spacing_fejer_hierarchy.py
```

Artifacts:

- `research/voevodsky/checkers/scout_halved_spacing_fejer_hierarchy.py`
- `research/voevodsky/results/halved_spacing_fejer_hierarchy.json`
