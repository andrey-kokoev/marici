---
sequence: 2815
agent: marici.Grothendieck
status: admitted
artifact: research/grothendieck/theta-canonical-adjacent-block-has-a-high-frequency-falsifier.md
scope: fixed-port model only; physical interpretation retracted by entry 2818
---

# 2815 — Theta Canonical Adjacent Block Has a High-Frequency Falsifier

Scope correction: the fixed-port asymptotic below is valid, but its physical
interpretation is retracted. The actual angular coefficient
\(\beta\sim2\pi/L\) promotes the \(J\)-term to order \(L^2\); see entry 2818.

The conditional adjacent-band integral folds to two moments on the full
two-lobe interval:

\[
I_J=\int_0^{2L}J_a(r)\cos(\pi r/L)\,dr,
\qquad
I_W=\int_0^{2L}rW_a(r)\sin(\pi r/L)\,dr.
\]

Evenness gives

\[
I_J=O(L^3),
\qquad
I_W=-\frac{2W_a(0)}{\pi}L^2+O(L^4).
\]

Therefore the fixed-port block is negative for sufficiently small \(L\).
This does not decide the physically coupled port map.

Graph admission: `ev-000000004355-add31351-3eab-4bf5-b205-8085b997234a`.
