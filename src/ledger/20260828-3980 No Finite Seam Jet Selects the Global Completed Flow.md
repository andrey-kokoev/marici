---
author: marici.Grothendieck
---

# 3980 — No Finite Seam Jet Selects the Global Completed Flow

For any finite seam-jet order \(m\), set

\[
K=\left\lfloor\frac m2\right\rfloor+1
\]

and define

\[
h_K(q)=q^{2K}e^{-q^2}.
\]

This hostile is positive, even, entire, and rapidly decreasing. Since
\(2K>m\),

\[
h_K^{(j)}(0)=0
\qquad
(0\le j\le m).
\]

It therefore preserves every declared seam derivative through order \(m\).
Nevertheless,

\[
h_K'(q)
=
2q^{2K-1}(K-q^2)e^{-q^2}>0
\]

for \(0<q<\sqrt K\). Adding a sufficiently large positive multiple to any
positive even completed kernel preserves its finite seam germ while creating
an increasing off-seam direction.

Thus no finite seam jet, even together with positivity, modular evenness, and
rapid decay, selects global monotonicity. Increasing the finite jet order only
relocates the same failure.

## Scope

The hostile need not preserve the integer-winding heat expansion or the full
theta modular identity away from the seam. Those global source structures
remain viable. The theorem closes only finite-germ explanations.

## Durable verification

- Packet:
  `research/grothendieck/no-finite-seam-jet-selects-the-global-completed-flow.md`
- SCC manifest:
  `research/grothendieck/scc-models/finite-seam-jet-nonselection.json`
- Checker:
  `research/grothendieck/checkers/check_finite_seam_jet_nonselection.py`
- Result:
  `research/grothendieck/results/finite_seam_jet_nonselection.json`
- The exact bounded census passed every order from \(0\) through \(64\);
  the displayed family proves arbitrary finite order.
- SCC validation and model check passed.
- Epistemic graph event:
  `ev-000000009098-acbb669a-3b75-415a-8fbc-70bbee15395d`.
