# The rank-two certificate only needs micro-scale source enclosures

## Question

How narrow must each of the four source-value intervals be to certify the observed positive rank-two determinant?

## Error propagation

Let `X_k` denote the total gamma-plus-prime remainder value at the four sampled heat arguments and

\[
a_k=X_k-X_{k+1}.
\]

If every source value is enclosed with absolute radius `epsilon`, then each difference has radius at most `2 epsilon`. For

\[
D_2=a_0a_2-a_1^2,
\]

the four-sample error bound becomes

\[
|D_2-\widehat D_2|
\le
2\epsilon\bigl(|\widehat a_2|+|\widehat a_0|+2|\widehat a_1|\bigr)
+8\epsilon^2.
\]

Solving for an error no larger than half the observed determinant gives an explicit per-sample acceptance radius.

## Computed tolerances

The updated checker found:

- `(t,h)=(0.001,0.001)`: required radius below approximately `1.34e-2`;
- `(t,h)=(0.01,0.005)`: required radius below approximately `1.86e-4`;
- `(t,h)=(0.05,0.01)`: required radius below approximately `1.85e-6`.

The hardest box has

\[
(a_0,a_1,a_2)
\approx
(0.00257427,0.00254634,0.00254805)
\]

and observed determinant about `7.55e-8`.

## Comparison with analytic tails

At the hardest box:

- the prime cutoff exponent is below `-459`;
- the accelerated gamma-series omitted tail is around `10^-26` at the individual larger heat arguments;
- the direct gamma integral tail beyond `R=40` is below about `4.25e-18` across the sample domain.

All analytic tails are far below the required `1.85e-6` source-value radius. The certificate does not require extreme interval precision. A modest validated finite-part enclosure is sufficient.

## Consequence

The absent Arb backend is inconvenient but not a mathematical blocker. A validated elementary quadrature with micro-scale absolute width can certify the displayed rank-two sign without interval special functions. The common-center identity can then be used as an independent algebraic cross-check, but direct polynomial propagation is already stable at the required scale.

## Boundary

The tolerances are computed from uncertified central values. A final checker must use outward-rounded centers and radii, include finite-prime rounding, and decide the determinant interval directly. The present calculation is an acceptance-budget design, not a sign certificate.

## Artifacts

- `research/grothendieck/checkers/gamma_prime_hausdorff_localizer_scan.py`
- `research/grothendieck/results/gamma-prime-hausdorff-localizer-scan.json`

## Disposition

Target absolute source-value enclosures narrower than `1e-6` on the hardest four-sample box. This leaves margin beyond the computed half-determinant threshold and avoids unnecessary special-function precision.