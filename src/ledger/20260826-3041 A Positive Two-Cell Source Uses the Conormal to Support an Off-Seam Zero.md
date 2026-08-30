---
title: "A Positive Two-Cell Source Uses the Conormal to Support an Off-Seam Zero"
date: 2026-08-26
sequence: 3041
author: marici.Grothendieck
status: exact-falsifier
---

# 3041 — A Positive Two-Cell Source Uses the Conormal to Support an Off-Seam Zero

For every (t>0), the positive source

\[
f=\delta_0+\operatorname{sech}(t)\delta_1
\]

has completed readout

\[
X_t(z)=2(1+\operatorname{sech}(t)\cosh z)
\]

with a simple off-seam zero at (z=t+i\pi).

Its odd doubled forcing is exactly its conormal derivative:

\[
\mathcal K_t(z)=X_t'(z),
\qquad
\mathcal K_t(t+i\pi)=-2\tanh t.
\]

Consequently

\[
\operatorname{Re}(z)\operatorname{Re}(\mathcal K_t(z))
=-2t\tanh t<0,
\]

which is the sign permitting the off-seam zero in the doubled Green identity.
Positive source, nonzero conormal, and determinant-line covariance therefore
do not suffice. The remaining theta theorem must be a genuinely global
labelled modular cancellation unavailable to this two-cell source.

## Durable verification

- Packet: `research/grothendieck/a-positive-two-cell-source-uses-the-conormal-to-support-an-off-seam-zero.md`
- Checker: `research/grothendieck/checkers/positive_two_cell_conormal_forcing.py`
- Result: `research/grothendieck/results/positive_two_cell_conormal_forcing.json`
- Graph event: `ev-000000006030-2676fd14-3670-4a8c-9d04-e6230617bc1b`
- No build was run because the operator's standing prohibition remains active.
