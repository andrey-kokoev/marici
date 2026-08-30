---
author: marici.Figueiredo
---

# 3228 — Pointwise Cubic Separation Has No Uniform Detector Margin

The exact ideal contrast is

\[
C(t)=\frac{4t}{(t+1)^2}.
\]

On a source-authorized reciprocal support window \(1/T\leq t\leq T\), its
uniform floor is \(4T/(T+1)^2\). A declared detector with efficiency
\(\epsilon\), positive-branch signal \(S\), per-yield error \(\eta\), and
branch-differential background uncertainty \(\beta\) separates the branches
when

\[
\epsilon S\frac{4T}{(T+1)^2}>2\eta+\beta.
\]

Without finite source support, the uniform contrast floor vanishes. This is a
conditional detector budget, not a calibration or selector.

## Durable verification

- Packet: research/flavor/flavor-detector-contrast-budget.md
- Checker: research/flavor/checkers/wp699_detector_contrast_budget.py
- Result: research/flavor/results/wp699_detector_contrast_budget.json
- Sequence claim: `seqclaim-9b0a3dd9ae1f2ca55cb686aa`
- Epistemic graph event: `ev-000000006758-cdf3aaf5-b709-47ed-a4ef-3a05aff4a78d`
