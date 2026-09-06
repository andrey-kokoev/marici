---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 4178 — The Soft Gaussian Score Has an Invariant Square-Root Nearby Limit

## Scaled field coordinate

As the Gaussian coefficient \(a=\operatorname{Re}\psi_2(y)\) approaches zero,
the unscaled normalized measure spreads and has no finite weak limit in
\(\Phi\). The source-normalized coordinate is

\[
\xi=\sqrt a\,\Phi.
\]

Then

\[
P_a(\Phi)d\Phi
=\pi^{-1/2}e^{-\xi^2}d\xi,
\]

and the score becomes

\[
S_K=\xi^2-\frac12.
\]

The square-root deck transformation acts by \(\xi\mapsto-\xi\). Therefore

\[
\boxed{
\chi_{\rm deck}(\xi)=-1,
\qquad
\chi_{\rm deck}(S_K)=+1.
}
\]

Its Fisher norm remains \(1/2\).

## Consequence

The field coordinate carries the expected Kummer square-root line, but the
quadratic score descends to its invariant part. The observable needed for the
contact packet has a canonical soft nearby limit without choosing a sheet.

This is coefficient/readout structure over the existing soft carrier, not a
new soft incidence stratum.

## Evidence

- Entries 126, 128, 2214, and 2220
- `research/benincasa/checkers/soft_gaussian_score_rescaling.rs`