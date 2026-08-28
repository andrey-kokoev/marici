---
id: marici-ledger-20260827-3625
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP824
---

# Spectral Completion Repairs the Mass Fiber but Does Not Select the Scale

For the finite acyclic Dirac sector

\[
D_m=
\begin{pmatrix}
0&m\\
m&0
\end{pmatrix},
\]

the calibrated heat trace is

\[
\operatorname{Tr}e^{-\tau D_m^2}=2e^{-\tau m^2}.
\]

It is strictly sensitive to \(m>0\), so full spectral data distinguishes
threshold masses erased by charge homology.

The normalized heat action \(2e^{-m^2/\Lambda^2}\) has no positive finite mass
stationary point and is invariant under
\((m,\Lambda)\mapsto(\lambda m,\lambda\Lambda)\). A polynomial spectral action
selects \(m^2/\Lambda^2=-\alpha/(2\beta)\), leaving its coefficients and the
absolute cutoff free. Spectral multiplicity, heat-time calibration, detector
gain, threshold/RG parallelization, and physical16 descent also remain open.

## Evidence

- Packet: research/flavor/flavor-finite-spectral-completion-scale-selection-audit.md
- Checker: research/flavor/checkers/wp824_finite_spectral_completion_scale_selection_audit.py
- Generated result: research/flavor/results/wp824_finite_spectral_completion_scale_selection_audit.json
- Exact result: 19 of 19 checks passed.
- Ledger-sequence claim: seqclaim-d1d275ea8c1ed80ed271f93d, value 3625.
- Graph admission: ev-000000007784-4d5bbaf5-8324-4d5a-acd4-ab78b13842fb.

## Claim boundary

The result concerns a finite two-state spectral sector and exact heat/polynomial
actions. It proves fiber repair and scale nonselection in this domain, not a
general no-go for every possible dynamical spectral theory.
