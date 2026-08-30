# Angular moments and hidden scatter model order

## A rank-two fit can hide a third channel

Freeze three possible angular bins at `-1`, `0`, and `+1`, with true weights

```text
(1/100, 2/100, 2/100).
```

The total and left-right contrast are `1/20` and `1/100`. If the central bin is
omitted from the model, the endpoint-only fit

```text
(2/100, 0, 3/100)
```

reproduces both records exactly. The two-port inversion is unique inside its
two-endpoint model and nevertheless physically wrong.

This is the model-order trap: injectivity conditional on a support library does
not establish that the library is complete.

## Minimal repair on the declared grid

Add the second angular moment. The loading rows on the three bins are

```text
total:          ( 1, 1, 1)
first moment:   (-1, 0, 1)
second moment:  ( 1, 0, 1).
```

Their determinant is `2`. The three records recover the true weights exactly.
A three-segment Fourier-plane detector or calibrated spatial-mode projection
can implement these moment ports.

The second moment does more than improve precision: it catches the central
channel because the central bin contributes to total power but not to either
nonzero angular moment.

## The deeper hostile

Full rank on the three-point grid still does not prove that scatter lives on
that grid. A two-atom off-grid distribution at symmetric positions whose
squared coordinate is `3/5`, with a suitable weight imbalance, reproduces the
same first three moments.

Therefore finite moment data identify a measure only relative to a declared
support or sparsity law. Certifying continuous-angle model order needs further
moments, a flat-extension or positivity certificate, or a source-derived
scattering support theorem. A camera with many pixels is not by itself such a
theorem; diffraction and calibration determine its independent mode count.

## Claim boundary

The positive result is exact only on the declared grid `{-1,0,+1}`. The
off-grid construction is retained as a falsifier of global model-order claims.

## Verification

```text
python research/aspect/checkers/check_scatter_model_order_moments.py
```
