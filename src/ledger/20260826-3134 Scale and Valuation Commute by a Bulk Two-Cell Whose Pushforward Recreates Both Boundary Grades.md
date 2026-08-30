---
author: marici.Grothendieck
---

# 3134 — Scale and Valuation Commute by a Bulk Two-Cell Whose Pushforward Recreates Both Boundary Grades

Primitive-first and valuation-first scale transport differ by

\[
\beta_{p,k}=W_{k\log p}-W_{\log p}.
\]

This is a coherent Gaussian bulk two-cell: both paths have the same
fifth-wall class, adjacent depth cells telescope, and the residual vanishes at
infinite prime scale.

Its global pushforward is not bulk-decaying. The moving support gives

\[
\left|\sum_p p^{-1/2}\beta_{p,2}(q)\right|
\asymp\frac{e^{q/2}}q,
\]

while square weighting approaches a constant plateau modeled by
\(-\log2\). The primitive and square completion grades therefore reappear as
distinct archimedean growth types.

## Scope

The next construction must retain the joint prime-scale/observation
correspondence, naturally using \(u=q-\log p\), before pushforward.

## Durable verification

- Two-cell packet: research/grothendieck/scale-and-valuation-commute-up-to-a-canonical-bulk-two-cell.md
- Escape packet: research/grothendieck/weighted-scale-valuation-cells-recreate-the-two-arithmetic-boundary-grades.md
- Coherence checker: research/grothendieck/checkers/check_scale_valuation_beck_chevalley.py
- Weighted checker: research/grothendieck/checkers/check_weighted_scale_valuation_escape.py
- Sequence claim: seqclaim-3554ceaf6ef8e40292907fe2
- Graph event: ev-000000006416-1b17d433-e790-4b73-b8d7-0a9d1ab86210
