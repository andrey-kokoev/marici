---
author: marici.Figueiredo
---

# 1092 — WP8 Fiber Classification: the Loop-Phase Fiber over One Physical Point Is Exactly Discrete and Already Two-Valued Inside Single Charts

## Question

Entry 1084 left one structural loose end: the fiber of the chart →
physics map over the global best-fit point carries 18 distinct folded
loop-phase values, and two of them (\(0.817882\) vs \(0.819271\), 1.39
mrad apart) sit inside one cluster at the *same* physics.  Fit
tolerance or genuine discrete branch structure?  More generally: what
is the exact fiber structure of the loop phase at one physical flavor
point — cardinality, branch structure, and the relation of its
elements to the unitarity-triangle angles?

## Method

Pure re-analysis of the WP7 ensemble
(`results/wp7_ensemble.json`; no new fits).  The 61 minima landing on
the best-fit physical point (17 Tab.-S2 observables agreeing to
\(\le 10^{-4}\sigma\), best \(\chi^2 = 3.3628\)) are classified by:
exact phase-value grouping (tol \(10^{-6}\) rad, vs LM noise
\(\le 2.4\times10^{-8}\)); same-chart multiplicity (grouping by orbit
+ \(S_3^3\) member + phase edge); and comparison of each distinct
value against the fitted UT angles of the shared physical point
(\(\alpha = 1.557245\), \(\gamma = 1.186398\), \(\beta = 0.397949\),
sum \(= \pi\) to \(3\times10^{-7}\)) and against \(\pi - 2\gamma\),
the cores motivated by the WP4 leading-order theorem (entry 1073).

Checker: `checkers/wp8_fiber_classification.py`; results:
`results/wp8_fiber_classification.json`.

## Findings

### 1. The 18 phase values are distinct exact fiber elements

Within-group spread \(\le 2.3\times10^{-8}\) rad (LM convergence
noise); minimum between-group gap \(2.9\times10^{-5}\) rad; typical
gap \(10^{-3}\) rad.  Four orders of magnitude separate signal from
noise: each value is an exact element of the fiber, reproducible
across independent charts to \(10^{-8}\).  The values, with orbit
support:

\[
\begin{array}{c|c|c}
\varphi & n & \text{orbits}\\
\hline
0.378225 & 2 & 5, 14\\
0.398309 & 3 & 5, 14\\
0.399089 & 2 & 10\\
0.416964 & 1 & 10\\
0.747547 & 2 & 0\\
0.768414 & 2 & 2\\
0.817882 & 10 & 4, 7, 11, 13, 15, 17\\
0.819271 & 10 & 4, 7, 11, 13, 15, 17\\
1.187033 & 1 & 9\\
1.187204 & 2 & 0\\
1.187233 & 5 & 6, 9, 16\\
1.196024 & 2 & 2\\
1.202923 & 6 & 6, 9, 16\\
1.208072 & 2 & 2\\
1.216891 & 2 & 0\\
1.556769 & 3 & 5, 14\\
1.564019 & 2 & 10\\
1.566129 & 4 & 4, 7, 13, 15
\end{array}
\]

Cardinality statement: **at least** 18 exact values (the multi-start
ensemble is not a certified exhaustion of the fiber).

### 2. Multi-valuedness lives inside single charts

The fiber is 2-valued even with the chart held fixed.  Four charts
each carry two discrete solutions at the same physics:

\[
\begin{array}{c|c|c|c}
\text{chart (orbit, member, edge)} & \varphi_1, \varphi_2 &
\Delta(\text{obs}) & \Delta(\log\text{mags})_{L^2}\\
\hline
(11, (298,412), (d,1,1)) & 0.817882,\ 0.819271 &
1.1\times10^{-7}\sigma & 9.66\\
(0, (140,492), (d,1,0)) & 1.187204,\ 1.216891 &
1.6\times10^{-7}\sigma & \text{distinct}\\
(0, (140,498), (d,1,1)) & 0.747547,\ 1.216891 &
5.1\times10^{-7}\sigma & \text{distinct}\\
(2, (140,374), (d,0,1)) & 1.196024,\ 1.208072 &
1.4\times10^{-7}\sigma & \text{distinct}
\end{array}
\]

The 0.8179/0.8193 substructure is thereby resolved: a **discrete
branch pair of one chart**, not tolerance.  In the flagship chart the
two branches differ by a partial edge-magnitude swap (the two largest
hierarchy entries are exchanged) at identical observables — the
fit equations have two isolated solutions of genuinely different
texture magnitudes.

### 3. Cluster cores: UT angles plus unmatched cores

Each WP4-motivated core is matched by a fiber value to
\(\le 1.2\) mrad:

\[
\varphi = 0.3983 \simeq \beta,\qquad
1.1870 \simeq \gamma,\qquad
1.5568 \simeq \alpha,\qquad
0.7684 \simeq \pi - 2\gamma = \alpha + \beta - \gamma .
\]

Further exact values sit 2–50 mrad from the nearest motivated core;
in particular the \(0.818\) cluster matches none ( \(\ge 22\) mrad
from \(2\beta\) and from \(\gamma - \beta\) ).  Residuals at the
fitted point are **not** exact-relation evidence: the WP4 identity is
leading-order with calculable chart-dependent corrections, and a
\(\sim 10^3\)-candidate integer-combo search matches anything to
\(\sim\) mrad.  The LO identification of the unmatched cores
(0.378, 0.417, 0.748, 0.818, 1.20–1.22) is open and requires the
symbolic per-chart \(\varepsilon\)-analysis.

## Scope

This entry classifies the fiber over the WP7 best-fit physical point
only, within the nine-link stratum, at double precision.  It asserts
discreteness and observed cardinality (a lower bound), not fiber
exhaustion; it does not identify the leading-order object of the
unmatched cores; it does not revise the 1077 admission verdict
(flavor is not a fourth Marici sector) nor the 1084 mechanism
(angle inheritance).  It strengthens 1084's multi-valuedness:
\(\varphi\) is not even a *single-chart* function of the physics.

## Verification

- `research/flavor/checkers/wp8_fiber_classification.py` — reproduces
  every number above from `results/wp7_ensemble.json`;
  output `results/wp8_fiber_classification.json`.
- Flagship doublet independently re-verified by direct rebuild:
  chart (11, (298,412), (d,1,1)), observable separation
  \(1.1\times10^{-7}\sigma\), magnitude L2 distance 9.66.
- Epistemic graph: claim/test/source entities and relations at
  ev-000000000787; test outcome at ev-000000000789 (corrects the
  evidence provenance of ev-000000000788); refines the WP7 claim
  (`claim:b89e01b0ebff68ade45b`).
