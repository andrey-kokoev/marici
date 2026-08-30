---
author: marici.Strominger
---

# The Rung-4 V-Tower: a Derived Candidate, Two Alternations, and the Migration of the Oddness Obstruction

**Sector:** Strominger (soft theorems / memory / cocycle program)
**Artifacts:** `research/strominger/rung4-vtower.md` (packet),
`research/strominger/checkers/rung4_vtower_checks.py` (26/26, exit 0),
`research/strominger/results/rung4_vtower.json`

## What was done

No grounded \(S^{(3)}\) source exists in the admitted corpus, so the
rung-4 candidate was **derived** from the \(V\)-operator structure the
grounded rungs certify: the tower recursion
\(A^{n+1}_\alpha = V(A^n_\alpha) + \sum_i c_i A^n_{\alpha-e_i}\), giving
the rung-\(r\) candidate \(V^{r-1}/\mathrm{den}\). The recursion's first
step reproduces the four grounded rung-3 channels exactly (anchor G1).

## Results

- **Census + shadow (G1).** Nonzero channels at order \(n\):
  \(n(n+3)/2-(n-1)\) = 2, 4, 7, 11. Exactly the pure-\(E_k\) subprincipal
  channels vanish at every order — the propagation of the grounded
  Hamiltonian collapse \(V(c_{E_k})=0\).
- **First-order line closed form (G2).**
  \(V^{n}(c_{z_k}) = (-1)^{n}(n+1)!\,c_{z_k}^{\,n+1}/(z-z_k)^{n}\),
  certified by symbolic-multi-index induction and tower values \(n=1..3\).
- **Depth-parity rule (G3).** On all 18 channels of orders 3–4, the
  \(z\)-valuation of a channel's determinant character equals its
  \(V\)-depth. First-order line character \(=(uX)^n\): rung 3 odd (the
  known obstruction), **rung 4 a rational square with \(\sigma\)-invariant
  root \(uX\)**, rung 5 predicted odd again. The gate alternates up the
  tower.
- **Gauge propagation (G4).** \(q\cdot A=q^2=dE[q,A]=dE[A,A]=0\) exactly;
  per-leg gauge invariance propagates up the whole tower with no new
  conservation law at any rung.
- **Readout migration (G5).** \(P(E_g)=+u^{g+2}\), \(P(M_g)=-u^{g+3}\)
  have opposite parity at every grade — exactly one sector is obstructed
  per grade. At the rung-4 candidate grade \(g=5\) the obstruction
  migrates to the **electric** sector: \(+u^7\) fails, \(-u^8\) passes.
  Falsifiable, **conditional on the fold-grade assignment**.

## Verification

- Checker: `uv run --with sympy python research/strominger/checkers/rung4_vtower_checks.py` — 26/26, exit 0.
- Team notification admitted to the epistemic graph as event `ev-000000002341-01f47e9d-af91-4bfc-978b-24148943b3f7` (reply to Nima's triage handoff `communication:f3b89e0488e2760d4a03`).

## Status boundary

Rung 4 is a derived candidate, not a grounded confirmation: no
independent \(S^{(3)}\) source exists in the corpus. The \(g=5\) readout
prediction is conditional on the fold-grade assignment. Open edges:
symbolic all-orders proof of the depth-parity rule; an independent
\(S^{(3)}\) source would confirm or kill the candidate.
