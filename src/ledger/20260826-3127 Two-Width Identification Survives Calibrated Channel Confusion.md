---
author: marici.Figueiredo
---

# 3127 — Two-Width Identification Survives Calibrated Channel Confusion

## Result

For symmetric labelled-channel confusion probability \(e\), the WP652
detector response is

\[
J_{\mathrm{det}}=2
\begin{pmatrix}
1-e&e\\
e&1-e
\end{pmatrix}.
\]

Its Gram determinant is \(16(1-2e)^2\). The response retains rank two unless
\(e=1/2\), where the reconstructed channels coincide.

For uncertainty \(e\in[e_0-\delta_e,e_0+\delta_e]\), robust identification
holds when \(|1-2e_0|>2\delta_e\).

## Scope

This is a conditional robustness theorem, not a detector calibration. No
experimentally measured confusion matrix or uncertainty set is attached.

## Durable verification

- Packet: `research/flavor/flavor-two-width-confusion-robustness.md`
- Checker: `research/flavor/checkers/wp653_two_width_confusion_robustness.py`
- Result: `research/flavor/results/wp653_two_width_confusion_robustness.json`
- Epistemic graph event: `ev-000000006391-c1097970-5553-44b8-a236-559d72b9efc3`
