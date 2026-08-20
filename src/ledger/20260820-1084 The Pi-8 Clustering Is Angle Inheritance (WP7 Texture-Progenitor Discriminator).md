---
author: marici.Figueiredo
---

# 1084 — WP7 Texture-Progenitor Discriminator: the π/8 Clustering Survives Orbit Collapse and Prior Changes, and Decomposes as Exact Angle Inheritance at Fixed Physics

## Question

WP7 of the flavor follow-up program: the paper's fitted loop phases
cluster near multiples of \(\pi/8\) (Fig. 3 / Fig. S3).  Is that
clustering a property of the flavor generator, or an artifact of the
scan ensemble — its texture multiplicities, its phase-window device,
its fit-count weighting?  The discriminator: rebuild the ensemble with
full provenance, collapse it by support orbit, change the prior, and
see whether the clustering survives.

## Method (all artifacts in-repo)

The paper's per-class phases are not machine-readable (Fig. 3 is an
image), so the nine-link stratum was rebuilt from scratch:

- **Ensemble**: the 18 support orbits of the exact census
  (`results/orbit_census.json`: nine-link, full-rank sectors,
  connected combined graph, \(b_1=1\), mod \(S_3^3\) and sector
  exchange).  Orbit members enumerated by the \(S_3^3\) action; phase
  placed per the paper's rule (smallest down-type loop edge, else
  smallest up-type — placement is rephasing-gauge).
- **Fits**: 17-observable Gaussian \(\chi^2\) at \(M_Z\) (Tab. S2),
  free phase (no \(\pi/8\) windows — those were the paper's scan
  device), hierarchy-aware multi-start Levenberg-Marquardt
  (mass-only pre-fit, then full fit).  Viability:
  \(\chi^2 \le \chi^2_7(0.9973) = 20.28\) (17 obs − 10 params).
- **Validation**: the orbit of paper Example I (S38) refits to
  \(\chi^2 = 3.36\) with \(\varphi\) near \(\pi/2\), all 17
  observables within 1.4σ — the pipeline recovers the paper's own
  example before any new claim is made.
- Checkers: `checkers/wp7_ensemble.py`,
  `checkers/wp7_phase_histogram.py`,
  `checkers/wp7_stratum_coincidence.py`; results in
  `results/wp7_ensemble.json`, `results/wp7_phase_histogram.json`,
  `results/wp7_stratum_coincidence.json`.

## Findings

### 1. Viability is not generic: 14 of 18 orbits fit, 4 fail structurally

Orbits 1, 3, 8, 12 admit no viable fit anywhere in the search budget
(24 members × 20 starts, plus escalation).  Their best \(\chi^2\) are
\(3.8\mathrm{e}3\)–\(4.9\mathrm{e}3\) — three orders of magnitude above
threshold, dominated by 2–3 structurally mismatched CKM observables,
not near-misses.  Orbit 1 has a candidate exact obstruction: its
up-sector is anti-diagonal, forcing \(U_u\) to a permutation matrix.
Recorded as strong numerical evidence of structural inviability, not
proof (budget-limited search).

### 2. The clustering survives orbit collapse and prior changes (WP7.2/WP7.3)

Best-fit branch per orbit (the Fig.-3 analog, one phase per class,
\(n=14\)):

\[
\{0.378_{\times 2},\ 0.399,\ 0.748,\ 0.818_{\times 6},\ 1.187_{\times 2},\ 1.203,\ 1.208\}
\]

All 14 lie within 0.04 rad of a \(\pi/8\) multiple
\(\{0,\pi/8,\pi/4,3\pi/8,\pi/2\}\): on-lattice fraction \(14/14\) at
\(\Delta=0.05\) vs 0.25 for a uniform null; \(13/14\) at
\(\Delta=0.035\) vs 0.18.  The conclusion is stable under every
reweighting tried: uniform-over-fits (\(n=172\)), orbit-collapsed
branches (\(n=32\)), and \(\chi^2\)-likelihood weighting all give
on-lattice fractions 3–5× the uniform null across
\(\Delta \in [0.01, 0.1]\).  The clustering is not a multiplicity
artifact and not prior-dependent — within this stratum.

### 3. φ is multi-valued over a fixed physical point (WP3 strengthened)

Grouping all 172 viable minima by physical point (17 observables
agreeing to \(<10^{-4}\sigma\); converged fits agree to
\(\sim 10^{-7}\sigma\)): 61 minima from **all 14 fitted orbits** land
on one and the same physical point — the global best-fit point — and
realize **18 distinct folded loop phases** there.  The multi-valuedness
already occurs inside a single orbit: orbit 4 fits the identical
physical point with \(\varphi = 0.818\) and with
\(\varphi = 1.566\) (observables equal to \(10^{-7}\sigma\)).

So \(\varphi\) is not merely non-invariant under the full \(U(3)^3\)
quotient (1051): it is not even a function of the physical point
within the sparse stratum.  The fiber of (chart, parameters) over a
physical point is discrete and multi-valued in \(\varphi\).  This
closes the loophole left by 1051/1076 — "stratum invariant" fails too.

### 4. The mechanism: exact angle inheritance

The realized fiber phases are not generic numbers near lattice points.
The cluster cores equal the fitted CKM angles themselves:

\[
\begin{aligned}
\varphi &= 0.3983 &&= \beta\ (0.3979) + 4\mathrm{e}{-4},\\
\varphi &= 1.1870 &&= \gamma\ (1.1864) + 6\mathrm{e}{-4},\\
\varphi &= 1.5568 &&= \alpha\ (1.5572) - 5\mathrm{e}{-4},
\end{aligned}
\]

with satellites up to 0.03 rad away, and exclusion gaps between
clusters (nothing in \([0.43, 0.74]\), \([0.83, 1.18]\),
\([1.22, 1.55]\)).  The WP4 leading-order map "loop phase ↦
unitarity-triangle angle combination" therefore holds at full
nonlinear precision at the best-fit point, for the cluster cores.

The decomposition of the \(\pi/8\) phenomenon is then forced:

\[
\underbrace{\varphi \approx \alpha,\beta,\gamma}_{\text{exact chart
mechanics (WP4 map, now verified at best-fit)}}
\quad\times\quad
\underbrace{\alpha \approx \tfrac{\pi}{2},\ \beta \approx
\tfrac{\pi}{8},\ \gamma \approx \tfrac{3\pi}{8}}_{\text{measured
values — experimental input}} .
\]

The texture framework transmits the measured near-lattice angles into
near-lattice loop phases; it does not prefer lattice phases itself.
The clustering is neither UV quantization (never on the table after
1051) nor scan multiplicity (Finding 2) nor a sparse-presentation
selection effect — it is **angle inheritance**.

### 5. Strong-CP channel across the fiber (WP5 consistency)

Over the same fiber, \(\arg\det(Y_uY_d)\) takes values exactly in
\(\{0, \pm\varphi, \pm(\pi-\varphi), \pi\}\) — the
perfect-matching menu of WP5.  Charts with \(\arg\det = 0\) exist at
the best-fit point (e.g. orbit 13), and charts carrying
\(\pm\varphi\) in the determinant coexist in the same fiber.  Whether
the determinant is real is chart choice within the fiber, not physics
— consistent with, and sharpening, the paper's "most viable textures
allow the CP phase to avoid the determinant".

## Prior updates (Benincasa's four, after 1051)

- "π/8 is a direct UV quantization law": stays sharply down.
- "π/8 is a sparse-presentation selection effect": **down** — replaced
  by angle inheritance; the presentation transmits, it does not select.
- "the texture mechanism induces a nontrivial physical invariant
  relation": resolved — the relation is the exact chart-level map
  \(\varphi \mapsto\) UT angles (WP4), not a new physical invariant.
- "flavor shares the carrier/coefficient/readout calculus": unchanged;
  governed by the 1077 verdict (not admitted), which this entry does
  not revise — the π/8 structure lives in the chart atlas and reduces
  to measured-angle input.

## Caveats

- Nine-link stratum only; the paper's 156 classes include ten-link
  textures, and the Fig.-3 comparison is qualitative (their per-class
  phases are not machine-readable).
- The 4 inviable orbits are budget-limited findings, not proofs.
- Branch substructure (0.8179 vs 0.8193 clusters 1.4 mrad apart at the
  same point) is unresolved — likely distinct discrete solutions of
  the (support, physics) → parameters polynomial map.
- The S43/S47 supplement discrepancy recorded in 1076 remains open.

## One-line verdict

The π/8 clustering is real, survives ensemble collapse and prior
changes, and is exactly the measured CKM angles — near \(\pi/8\)
multiples as a matter of experiment — inherited into the loop phase by
the chart mechanics; the loop phase itself is multi-valued over a
fixed physical point and carries no physical information beyond the
standard readout.
