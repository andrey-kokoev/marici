# Gamma erfc series reconciles with an explicit omitted tail

## Question

Does the accelerated gamma series reproduce the integral at sufficient accuracy for the rank-two test, with an analytic truncation budget?

## Execution

The checker evaluated the first 200 erfc-series terms and six asymptotic correction terms after the leading harmonic tail. It compared the result against 80-digit direct quadrature for

\[
t=0.001,0.004,0.01,0.025,0.05,0.08.
\]

For each value it also computed the first omitted asymptotic tail

\[
B_K(t,M)=
\frac{(2K-1)!!}{(8t)^K}
\zeta(2K+1,M+1/4),
\]

with `K=7`, and verified the successive-term ratio bound is below one.

## Results

The largest reconciliation residual occurred at `t=0.001`:

\[
|I_{\rm series}-I_{\rm integral}|
\approx2.7461\times10^{-14},
\]

while the first omitted-tail bound was

\[
B_7\approx2.8583\times10^{-14}.
\]

At `t=0.08`, the residual was approximately

\[
1.3623\times10^{-27}
\]

against bound

\[
1.3630\times10^{-27}.
\]

Every observed residual lay below its analytic omitted-term bound. The worst decreasing-term ratio was approximately `0.0468`, at the smallest heat argument.

## Consequence

The erfc representation is numerically stable enough for the displayed rank-two boxes. Its analytic truncation budget is many orders below the `7.55e-8` determinant residual. The remaining obstacle to a formal certificate is outward rounding of:

- the first 200 scaled-erfc terms;
- digamma and Hurwitz-zeta evaluations;
- constants and the final determinant operations.

Direct improper quadrature is no longer needed in the certification path.

## Boundary

The checker uses high-precision `mpmath`, not directed interval arithmetic. Agreement with direct quadrature and satisfaction of the analytic tail bound are reconciliation evidence, not a rigorous enclosure of finite-term rounding.

## Artifacts

- `research/grothendieck/checkers/gamma_erfc_series_reconciliation.py`
- `research/grothendieck/results/gamma-erfc-series-reconciliation.json`

## Disposition

Use the accelerated series as the gamma backend for a future outward-rounded `D_2` certificate. The analytic tail has been isolated; only finite special-function rounding remains.