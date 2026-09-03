# Source scans lose the completed sign near the first prime threshold

## Question

What happens numerically when the rank-two source scan crosses the first infinitesimal prime sign threshold near `t=0.2402`?

## Extended scan

The source checker was raised to 100 decimal digits and extended at mesh `h=0.01` to

\[
t=0.20,0.24,0.25,0.30.
\]

The gamma-plus-prime remainder matrices retained positive numerical minimum eigenvalues, from about `1.44e-18` at `t=0.20` down to `4.07e-22` at `t=0.30`. Their rank-two determinants remained positive, from about `7.58e-21` down to `2.20e-24`.

However, after subtracting the exact endpoint rank-one mode, the computed completed minimum eigenvalue became negative at and beyond `t=0.24`:

\[
-1.02\times10^{-21},
-1.59\times10^{-21},
-2.86\times10^{-20}.
\]

These signs conflict with the known low-zero spectral validation and therefore diagnose source-side numerical cancellation error, not evidence of a negative completed cone.

## Error budget collapse

The per-source-value radius needed to preserve half of the remainder `D_2` margin collapses from approximately

\[
1.85\times10^{-6}
\]

at `t=0.05` to

\[
1.80\times10^{-19}
\]

at `t=0.20`, and then to order `10^-22` around `t=0.24` through `0.30`.

Thus the proposed elementary `10^-6` interval backend can certify the earlier finite box but cannot follow the source scan into this regime.

## Interpretation

The loss of completed sign occurs near the first moving prime derivative threshold, but the threshold is not established as its cause. The determinant asymptotic already predicts first-zero-scale conditioning. Gamma quadrature and completion cancellation overwhelm the completed residual long before ordinary high-precision agreement is a certificate.

The remainder matrix appears numerically positive because it retains the large endpoint atom. Endpoint subtraction exposes the exponentially tiny completed eigenvalue and amplifies source error.

## Consequence

There are two distinct computational objectives:

1. certify low/intermediate finite boxes as diagnostics using micro-scale intervals;
2. prove the all-heat theorem symbolically, preserving endpoint--gamma--prime cancellation before numerical evaluation.

No fixed decimal-precision source scan can establish the second objective uniformly.

## Boundary

All extended signs are uncertified. The negative completed eigenvalues are classified as numerical defects because the source evaluation lacks an interval enclosure at the required `10^-22` scale. They must not be reported as mathematical counterexamples.

## Disposition

Stop extending raw source scans toward larger heat. Use the failure point as conditioning evidence. Further progress requires a cancellation-preserving analytic identity, not additional decimal precision.