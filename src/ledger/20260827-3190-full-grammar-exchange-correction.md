---
author: marici.Figueiredo
---

# 3190 — Full-Route Endpoints Falsify the Exchange Selector

## Correction

WP676 established exchange invariance only for the internal two-messenger mass
block. The independently typed entrance and exit currents couple to different
bare fields, so holding those physical sources fixed breaks
(A\leftrightarrow B). Exchange balance is therefore an internal-block
rigidifier and erosion minimizer, not a source-authorized selector of the full
flavor constructor.

## Pole-basis result

On the balanced block, the frame fluctuation transforms as

\[
H^T
\begin{pmatrix}0&1\\1&0\end{pmatrix}
H=
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

It is pole diagonal. Hence the cross-pole (P_+\leftrightarrow P_-+n)
transition vanishes and the WP674 bare-species cascade cannot be combined with
the exact exchange explanation.

## Durable verification

- Packet: research/flavor/flavor-full-grammar-exchange-audit.md
- Checker: research/flavor/checkers/wp681_full_grammar_exchange_audit.py
- Result: research/flavor/results/wp681_full_grammar_exchange_audit.json
- Corrects ledger 3177 and WP676
- Epistemic graph event: `ev-000000006633-f5008d24-4430-4520-b29a-50974efa0fd0`
