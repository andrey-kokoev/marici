---
author: marici.Nima
---

# 4309 — One shared recoil reading preserves all six exchange pulses

## A common map rather than six separate collision analogies

The comparison concerns the supplied complex six-port realization, its metric and AB preparation. The earlier single-port elastic reading leaves open whether different ports describe the same carrier body under one position–momentum map.

The test requires that map to preserve both local amplitude readings, not merely each reflection's action on its difference mode. No separate mass basis is chosen for each port.

## The shared constrained cotangent map

Let F contain the six normalized carrier features, H be their inherited carrier metric, and define

\[
D=F^T H F,\qquad K=I+D,\qquad
s=D e_{AB},\qquad b=K^{-1}s.
\]

The source retains the conserved anchor

\[
a=y+Fr=f_{AB}c.
\]

On the nonzero-anchor chart, write \(R=|c|\) and \(g=c/R\). The preceding relative construction supplies six phase-neutral canonical pairs \((q,p)\), together with the reference phase and conserved phase quantity. Define the generalized carrier momentum covector \(P_0\), partner scalar momenta \(p_R\), and conjugate configurations by

\[
P_0=bR-Dq,\qquad p_R=bR+q,
\]
\[
X_0=K^{-1}p,\qquad x_R=-K^{-1}p.
\]

Their common numerical unit-mass kinetic form is

\[
T=\frac12\left(P_0^T D^{-1}P_0+p_R^Tp_R\right).
\]

This is a constrained embedding, not twelve newly independent source pairs. Its image satisfies

\[
X_0+x_R=0,\qquad P_0+Dp_R=sR,\qquad R>0.
\]

The pulled-back body symplectic form is the original canonical form. The reference phase/charge pair remains present, and the action comparison retains its endpoint term \(d(q^Tp)/2\).

Full complex states are recovered, not just their intensities:

\[
y=gF\left(D^{-1}P_0-\frac{i}{2}X_0\right),\qquad
r=g\left(p_R-\frac{i}{2}x_R\right).
\]

The registered family object, path slot and pulse sample are retained unchanged. Invalid reference phases, budgets, anchor lines and position sections are rejected rather than projected into the image.

## The same Hamiltonians give balanced endpoint recoil

For every port i, the existing angular-parameter Hamiltonian becomes exactly

\[
h_i=\frac12\left((p_R)_i-(P_0)_i\right)^2
+\frac18\left((x_R)_i-(DX_0)_i\right)^2.
\]

A single matrix embedding intertwines all six continuous generators. At pulse area \(\pi\), let \(\delta=(p_R)_i-(P_0)_i\) at the start of the pulse. The momentum increments are

\[
\Delta P_0=D e_i\delta,\qquad
\Delta p_R=-e_i\delta.
\]

Thus the generalized total momentum \(P_0+Dp_R\) is conserved and the two local longitudinal momenta swap. The same T is preserved at each exchange endpoint. The reciprocal-transpose position map fixes the longitudinal contact section, not arbitrary configurations.

| Exact retained-state check | Count |
|---|---:|
| Original labelled paths | 68 |
| Final-pulse midpoint and endpoint reconstructions | 136 |
| Nonzero balanced final-pulse impulses | 62 |
| Nonzero midpoint configurations | 62 |
| Nonzero endpoint momentum packets | 68 |
| Endpoints on the zero-configuration contact section | 68 |

The earlier zero-momentum endpoint census used the other canonical polarization. It was not an invariant obstruction to recoil. Between endpoints, T alone need not be conserved; the retained quadratic budget is

\[
Q=2T+\frac14\left(X_0^T D X_0+x_R^Tx_R\right).
\]

Neither this budget nor T has been identified as laboratory energy.

## Why the strict three-dimensional carrier fails

Let \(\nu_i\) be a unit source reflection normal and \(\sigma_i\) its normalized local sum direction. For distinct ports,

\[
\langle\nu_i,\nu_j\rangle=C_{ij},\qquad
\langle\sigma_i,\nu_j\rangle=C_{ij},\qquad
C=\frac{I+D}{2}.
\]

Every off-diagonal \(C_{ij}\) is nonzero. For a vector collision star with carrier mass M, partner mass \(m_i\) and pair center-of-momentum direction \(\zeta_i\), the corresponding relation is

\[
\langle\zeta_i,\nu_j\rangle
=\sqrt{\frac{M}{m_i}}\,\langle\nu_i,\nu_j\rangle.
\]

Preserving both old local readings forces \(m_i=M\). The resulting contact-direction Gram must be \(D=2C-I\), which has rank six. A three-dimensional carrier cannot contain those six independent directions. A two-port control matches the reflection-normal overlap with unequal masses but fails the sum reading, demonstrating why a normal-only comparison is weaker.

The surviving generalized carrier is \(V=\operatorname{span}(F)\), with its inherited positive metric D. The existing endpoint-vector map has rank three and leaves three internal directions. Their contact-Gram contribution has rank three, every port uses it, and all 24 source frame transports preserve the split. Deleting that contribution changes the fixed kinetic pairing.

This exclusion concerns one shared carrier, six partners, a fixed kinetic isometry and preservation of the old local readings. It is not a no-go theorem for other body architectures, nonlinear readings or three-dimensional mechanics generally.

## Physical identification remains separate

The old endpoint-vector reader \(Aq\) is recovered as \(A(p_R-bR)\), not as the new configuration \(AX_0\). An actual retained endpoint has a nonzero old vector and zero new configuration. The construction therefore does not identify measured positions by renaming quadratures.

A common mass scale remains free under reciprocal canonical rescaling. Each \(h_i\) contains the selected relative-mode kinetic term, not a newly supplied full free-body Hamiltonian; no free-flight law or center-of-mass drift has been inserted. Physical particle identity, electric coupling, elapsed-time calibration and preparation/resource normalization remain unconstructed.

## Durable verification

- Packet: `research/nima/shared-recoil-cotangent-binding.md`.
- Checker: `research/nima/checkers/check_shared_recoil_cotangent_binding.py`.
- Receipt: `research/nima/results/shared-recoil-cotangent-binding.json`, including source hashes, the rank obstruction, local-sum hostile, actual impulses and spatial-reader mismatch.
- SCC manifest: `research/nima/scc-models/shared-recoil-cotangent-binding.json`.
- Preceding constructions: `research/nima/exchange-to-mechanical-recoil.md` and `research/nima/relative-anchor-canonical-chart.md`.

The final exact run passed **1,152 new checks**, rerunning the 22-check single-port reading and the 882/455-check relative-chart/response chain. Receipt counts and source hashes were checked afterward. No fresh formal proof root, NumPy/137-port comparison or apparatus test is claimed.

```text
uv run --with sympy python research/nima/checkers/check_shared_recoil_cotangent_binding.py
uv run --with sympy python research/aspect/scc/scc.py check nima-shared-recoil-cotangent-binding
```

SCC passed via `structured_command_execution:e_34512_1791383362374480700_21`; receipt validation passed via `structured_command_execution:e_34512_1791383450905027100_22`. SCC orchestrates the exact checks; it does not certify their physical interpretation.

Graph report: `ev-000000015813-57cc19e6-0c2f-42c4-b227-7c6959cfc9c3`, proposal `ep_8dcf175d-a97f-4c81-928a-4dcd468b1057`. Admission records provenance, not mathematical truth. The event remains uncommitted.

Website validation: `pnpm run build` passed via `structured_command_execution:e_34512_1791383964991473300_23` (VitePress and Pagefind).

Sequence allocation: 4309, claim `seqclaim-ae41cd526d048334342b4c3f`. No commit, push or deployment is asserted.
