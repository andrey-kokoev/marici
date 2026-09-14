# Both rank-two eigenchannels are positive at the selected source sample

## Missing check

For a real even two-translate kernel, positivity requires both

\[
K_\sigma(0)-K_\sigma(d)>0
\]

and

\[
K_\sigma(0)+K_\sigma(d)>0.
\]

The previous enclosure treated only the first inequality.

## Source-side evaluation

At

\[
\sigma=0.005,
\qquad d=0.25,
\]

the diagonal source value decomposes numerically as

\[
K_\sigma(0)
=
1.0025031
-0.8527967
-0.0000084
=
0.1496980.
\]

Using the previously computed antisymmetric value gives

\[
K_\sigma(0)+K_\sigma(d)
=
2K_\sigma(0)-
\left(K_\sigma(0)-K_\sigma(d)\right)
\approx0.0325291.
\]

Thus both eigenvalues are positive numerically at the selected point.

## Scope

The antisymmetric eigenvalue has the coarse positive analytic budget recorded separately. The symmetric value in this packet is still a floating scout, not an enclosure. Its smaller margin requires a tailored lower bound using the nonnegative multiplier \(1+\cos(du)\).

The elementary digamma correction-series method applies because that multiplier is nonnegative. Retaining more correction terms will be necessary to preserve the smaller symmetric margin.

## Disposition

No rank-two sign obstruction appears at the selected source sample. Completing a full rank-two certificate now requires enclosing the symmetric eigenvalue; it does not require changing the source formula or introducing another geometric structure.

## Verification

```text
python research/voevodsky/checkers/scout_two_translate_symmetric_eigenvalue.py
```

Artifacts:

- `research/voevodsky/checkers/scout_two_translate_symmetric_eigenvalue.py`
- `research/voevodsky/results/two_translate_symmetric_eigenvalue_scout.json`
