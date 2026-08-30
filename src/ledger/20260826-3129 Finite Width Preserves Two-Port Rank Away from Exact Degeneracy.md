---
author: marici.Figueiredo
---

# 3129 — Finite Width Preserves Two-Port Rank Away from Exact Degeneracy

## Result

Two equal-width normalized Lorentzian templates separated by \(\Delta\) have
exact overlap

\[
\rho=\frac{4\gamma^2}{\Delta^2+4\gamma^2}.
\]

Their matched-filter Gram matrix has smallest eigenvalue

\[
\lambda_{\min}=\frac{\Delta^2}{\Delta^2+4\gamma^2}.
\]

Finite widths therefore preserve rank two for every \(\Delta\ne0\), but the
experiment becomes arbitrarily ill-conditioned near degeneracy.

## Scope

This assumes equal Lorentzian widths and ideal matched filtering. Detector
convolution, unequal widths, backgrounds, efficiencies, and calibrated
uncertainties remain outside the result.

## Durable verification

- Packet: research/flavor/flavor-finite-width-template-overlap.md
- Checker: research/flavor/checkers/wp654_finite_width_template_overlap.py
- Result: research/flavor/results/wp654_finite_width_template_overlap.json
- Epistemic graph event: `ev-000000006397-a542e3ed-bbb8-48f2-9e68-d0be518667a4`
