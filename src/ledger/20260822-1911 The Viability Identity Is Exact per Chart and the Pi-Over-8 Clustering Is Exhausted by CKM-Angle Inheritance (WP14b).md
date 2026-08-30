---
author: marici.Figueiredo
---

# 1911 — The Viability Identity Is Exact per Chart and the π/8 Clustering Is Exhausted by CKM-Angle Inheritance (WP14b)

## Question

The brief's fourth work package separates three claims: (1) fitted loop
phases cluster near multiples of \(\pi/8\); (2) a Yukawa-triangle angle
equals a CKM angle at leading order; (3) a UV symmetry dynamically
selects the simple phase.  WP7 established numerically that the
clustering is angle inheritance; WP9's LO atlas classified the phase
cores by carrier with clean and nonperturbative regimes.  What remained
is the groupoid-level closure: an *exact* per-chart viability identity
connecting loop data to the invariant ring, and a decisive audit of
whether the \(\pi/8\) lattice carries any explanatory power beyond the
CKM angles themselves.

## Method

Per chart of the WP9 atlas (61 charts, all over one physical flavor
point per WP10), rebuilt at 40-digit arithmetic from the stored fitted
\(\log\)-magnitudes and \(\phi\):

- extract \(K_v=\det[H_u,H_d]/(2i\sin\phi_v)\) — must be real (WP12/13);
- compute \(J\) two independent ways: the CKM quartet
  \(\operatorname{Im}(V_{us}V_{cb}V_{ub}^\ast V_{cs}^\ast)\) and the
  commutator identity \(\det[H_u,H_d]=-2iJ\prod\Delta_u\prod\Delta_d\);
- verify the **viability identity**
  \[
  J^2=\rho_v\sin^2\phi_v,\qquad
  \rho_v=\frac{K_v^2}{\operatorname{disc}(H_u)\operatorname{disc}(H_d)},
  \]
  where the discriminants are polynomials in the char coefficients —
  CP-even chart data, \(\phi\)-free in the 49 mass-flat charts of WP12;
- re-verify the one-physical-point premise: constancy of \(|J|\), the
  six masses and the CKM moduli across all 61 charts;
- the image audit: per chart, residual of the folded fitted phase to the
  chart's **own** unitarity-triangle angles \(\{\alpha,\beta,\gamma\}\)
  (carrier hypothesis) versus the \(\pi/8\) lattice
  \(\{0,\pi/8,\pi/4,3\pi/8,\pi/2\}\), grouped by phase core and by WP9's
  clean/nonperturbative regime.

Precision honesty: atlas inputs are IEEE doubles, so results are
input-precision limited (\(\sim10^{-13}\) relative); the 40-digit
arithmetic stays well below that.  Checker:
`research/flavor/checkers/wp14b_viability_image_audit.py`; results:
`research/flavor/results/wp14b_viability_image_audit.json`.

## Result

**T1 — the viability identity holds exactly per chart.**  Max relative
error of \(J^2=\rho_v\sin^2\phi_v\) over all 61 charts:
\(4.2\times10^{-41}\) (working precision).  \(K_v\) is real to
\(6\times10^{-60}\).  The two independent \(J\) computations agree in
absolute value to \(1.9\times10^{-40}\); their *signs* differ by the
eigenvector-gauge convention — a numerical re-encounter with the WP11/12
statement that only the unoriented pair \(\{J,-J\}\) is stable data.
The split \(J^2=\rho_v\sin^2\phi_v\) is therefore exact, and
\(\rho_v\) is CP-even chart data: the physical readout sees only the
product, never the factors separately.

**T2 — one physical point, independently re-verified.**  \(|J|\) is
constant across the groupoid at \(3.17875587\times10^{-5}\) with spread
\(5.7\times10^{-13}\); masses and CKM moduli constant to
\(\lesssim4\times10^{-10}\).  (This also repairs a first-run artifact:
a wrong `im` vs `re` extraction made \(J_{\rm comm}\) vanish and
produced a spurious \(10^{+291}\) identity error — caught because the
quartet/commutator cross-check disagreed; disclosed here per policy.)

**T3 — the image audit: the lattice is not the attractor.**  The
spectrum decomposes by regime:

| regime | charts | median carrier residual | median lattice residual |
|---|---|---|---|
| clean (carrier res \(<2\) mrad) | 16 (8\(\gamma\), 5\(\beta\), 3\(\alpha\)) | 0.81 mrad | 9.1 mrad |
| marginal | 21 | 16.5 mrad | 24.3 mrad |
| nonperturbative (WP9 T6-failing branches) | 24 | 369 mrad | 33.9 mrad |

Wherever the chart is perturbatively controlled, \(\phi_v\) tracks the
chart's own CKM angle **an order of magnitude more closely** than the
nearest lattice point.  The nonperturbative cores
(\(\phi\approx0.75,0.77,0.82\)) fit neither carrier nor lattice — they
are branch artifacts of the fit, with no clean invariant meaning, exactly
as WP9's T6 flagged.  The raw vote count (carrier 31, lattice 30) is
deliberately reported as a *non*-result: lattice wins occur only in
cores where neither hypothesis is meaningful.

**T4 — the clustering is exhausted by inheritance plus the measured
angles' own lattice proximity.**  The physical CKM angles at the fitted
point sit near the lattice by themselves: \(\beta\) is 5.25 mrad from
\(\pi/8\), \(\gamma\) 8.30 mrad from \(3\pi/8\), \(\alpha\) 13.55 mrad
from \(\pi/2\).  Hence "fitted \(\phi\) clusters near \(\pi/8\)
multiples" factors as (angle inheritance in clean charts) \(\times\)
(the empirical near-lattice position of the CKM angles).  No independent
lattice attractor is visible in the map.

## Interpretation

Claim (1) of the audit is thereby reduced to claim (2) plus a fact about
the measured CKM angles; claim (3) — a UV symmetry selecting the simple
phase — receives **no support from the texture map**: if a fundamental
mechanism quantized \(\phi\) at the lattice, the clean charts would sit
on the lattice, not on the CKM angles.  They do the opposite, by an
order of magnitude.  The open question is thereby relocated, honestly,
to where the paper itself leaves it: why are the *measured CKM angles*
near \(\pi/8\) multiples — a question about the physical point, not
about sparse presentations of it.  For the Marici typing this completes
the phase-line arc: chart loop data reaches the invariant ring through
exactly one channel (\(J^2=\rho_v\sin^2\phi_v\), WP12/13 + T1), the
channel's chart split is unphysical (WP11 + T1), and the empirically
conspicuous lattice structure of the fitted phases is exhausted by
inheritance (T3/T4).

## Verification

- Q1 gates: identity rel err \(4.2\times10^{-41}\); \(K_v\) imaginary
  residual \(\le6\times10^{-60}\); \(|J|\) quartet vs commutator
  \(1.9\times10^{-40}\) — all 61 charts.
- Q2: \(|J|\), masses, CKM moduli constant across the groupoid
  (spreads \(5.7\times10^{-13}\), \(10^{-10}\), \(4\times10^{-10}\)).
- Regression: rebuilt per-chart UT angles match the atlas's stored
  `ut_angles` (doubles) within input precision.
- Bug disclosed: first run mis-extracted \(J_{\rm comm}\) (`im` for
  `re`); cross-check caught it; fixed and re-run.
- Runtime \(<1\) s; mpmath dps=40.

## Relations

- Closes the brief's fourth work package at groupoid level, sharpening
  WP7 (numeric ensemble inheritance) and WP9 (core classification) into
  the exact viability identity plus regime-resolved residual hierarchy.
- Rests on WP12 (entry 1903) T3 and WP13 (entry 1907): the first-harmonic
  theorem is what makes \(\rho_v\) CP-even and the identity exact.
- Confirms WP10's one-physical-point premise independently (T2).
- Supports the WP6 admission posture: nothing in the phase spectrum
  forces a UV quantization law; the conspicuous lattice is inherited.
