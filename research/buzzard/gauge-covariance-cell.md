# Gauge covariance cell

Owner: `marici.Buzzard`

Source locator: the coordinate-change and distinguished-pairing equations in
the `Theta consequence` section of
`research/strominger/distinction-preserving-completion.md`.

## Formal objects

The Lean increment uses an arbitrary field `K`. `PairingCompatible U lambdaX
lambdaY` means that the target-chart covector transported across the scalar
transition agrees with the source-chart covector:

`lambdaY * U = lambdaX`.

For nonzero coordinate gauges `rX` and `rY`, the transition and covectors are
transported by

`U' = rY * U / rX`, `lambdaX' = lambdaX / rX`, and
`lambdaY' = lambdaY / rY`.

Lean proves that pairing compatibility is preserved. It also proves that the
ratio `lambda ^ 2 / h` is invariant when the metric coefficient transforms as
`h' = h / r ^ 2`.

## Hostile fixture

All exact coefficients are rational. Initially `U = 2`, `lambdaX = 1`, and
`lambdaY = 1/2`, so the pairing is compatible. The gauges `rX = 1` and
`rY = 1/2` normalize the transition to one. If the old covectors are retained,
compatibility becomes the false equation `1/2 = 1`. Contragredient covector
transport changes both chart covectors to one and restores compatibility.

The metric/covector pairs `(h,lambda) = (1,1)` and `(1/4,1/2)` have the same
ratio. This is an algebraic invariant, not source authority for choosing the
metric.

## Assumptions and limits

The reusable theorem is one-dimensional and purely algebraic over a
commutative field. Nonzero gauges are required because the formulas divide by
them. No positivity, norm, topology, Hilbert completion, analytic continuation,
or source authority is inferred. A positive Hermitian version requires an
ordered or star-field interface and conjugation in the metric transformation.

The result generalized the gauge/pairing cell but specialized the metric
statement to a scalar-square model. It does not force other sectors into this
representation.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/GaugeCovariance.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` with no diagnostics. No site build or Git
command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/GaugeCovariance.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/gauge-covariance-cell.md`
