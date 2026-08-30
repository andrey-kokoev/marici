# Provisional CP-even kaon likelihood: WP460

## Question

Can the real current direction erased by WP459's `eps_K` likelihood be measured by a source-independent CP-even neutral-kaon likelihood without inventing a no-overshoot rule?

## Frozen inputs

The [RBC/UKQCD lattice calculation](https://arxiv.org/abs/2301.01387) reports, in units of (10^{-12} MeV),

\[
\Delta m_K^{\rm SM}=5.8\pm0.6_{\rm stat}\pm2.3_{\rm sys}.
\]

The same paper quotes the experimental value

\[
\Delta m_K^{\rm exp}=3.484\pm0.006.
\]

The current [2025 PDG conservation-laws review](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-conservation-laws.pdf) reports the equivalent frequency-domain measurement, (0.5293 plus or minus 0.0009) times (10^{10} inverse seconds). The packet uses the lattice paper's energy-domain transcription so the prediction and measurement share units without a new conversion convention.

The lattice authors call their result preliminary and estimate a roughly 40 percent discretization systematic. WP460 therefore declares, rather than hides, the additional statistical model:

- the experimental, lattice-statistical, and lattice-systematic errors are independent;
- all three are represented as Gaussian;
- no correlation or non-Gaussian systematic tail is supplied;
- the new-physics contribution is additive in the real mixing amplitude.

These assumptions define a provisional likelihood. They are not asserted to be the collaboration's likelihood.

## Common-frame response coordinate

Let

\[
x=\frac{\Delta m_K^{\rm BSM}}{\Delta m_K^{\rm exp}}.
\]

For a real CP-conserving amplitude, this is WP455's normalized response coordinate (Sigma_K). The normalized residual estimator is

\[
\hat x=1-\frac{5.8}{3.484}=-\frac{579}{871}.
\]

Under the declared independent-Gaussian completion, its exact standard deviation is

\[
\sigma_x=rac{\sqrt{0.006^2+0.6^2+2.3^2}}{3.484}
=\frac{\sqrt{1{,}412{,}509}}{1742}.
\]

The likelihood is

\[
-2\log\frac{L(x)}{L(\hat x)}=\frac{(x-\hat x)^2}{\sigma_x^2}.
\]

Its response Jacobian with respect to the real BSM coordinate is one, so it removes WP459's real-ray kernel at the formal likelihood level. The symmetric 1.96-sigma working interval is approximately

\[
-2.002<x<0.673.
\]

Zero is inside the interval. The current central lattice value actually prefers a negative BSM contribution, but the large systematic uncertainty prevents evidence for one.

## Authority boundary

WP460 is an executable, explicitly assumed CP-even likelihood constructor on the normalized real mixing-amplitude coordinate. It is not yet an admitted numerical constraint on WP447 because:

- the lattice systematic distribution and covariance were not published as the Gaussian used here;
- the result is preliminary and lacks a continuum extrapolation;
- WP447's two pole thresholds still require matching and running into the same low-energy convention.

It supplies the missing instrument direction conditionally. It neither selects (g_F f/v) nor rigidifies a flavor presentation, and it adds no reference port.

## Smallest exact falsifiers

- The normalized response derivative with respect to (x) vanishes.
- The exact combined variance is nonpositive.
- The experimental value lies outside the declared common unit system.
- Replacing the Gaussian systematic by an allowed hostile distribution removes every finite interval.

The successor must perform WP447's pole-by-pole matching and then test the bound under non-Gaussian and enlarged lattice-systematic completions.
