---
author: marici.Figueiredo
---

# 3167 — The Protected Two-Port Gram Factors into Source and Calibration Gates

## Result

For response

\[
J=\begin{pmatrix}1&1\\\alpha&-\alpha\end{pmatrix}
\]

and independently calibrated detector precision
\(W=((p,r),(r,q))\), the conditional Gram obeys

\[
\det(J^TWJ)=4\alpha^2(pq-r^2).
\]

Faithfulness therefore requires both a nonzero analyzing power and a positive
detector metric. Zero chirality precision leaves rank one.

## Limit

The theorem does not supply or fit the covariance. A named polarimeter and
independent calibration of analyzing power, acceptance, backgrounds, and
metric remain necessary. Conditional identification selects no source values.

## Durable verification

- Packet: research/flavor/flavor-protected-conditional-gram.md
- Checker: research/flavor/checkers/wp673_protected_conditional_gram.py
- Result: research/flavor/results/wp673_protected_conditional_gram.json
- Epistemic graph event: `ev-000000006528-c6f31cd1-5862-45d3-acd5-978b6d0e00b4`
