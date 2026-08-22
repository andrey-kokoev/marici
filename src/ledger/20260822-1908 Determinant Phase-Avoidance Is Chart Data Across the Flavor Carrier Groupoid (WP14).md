---
author: marici.Figueiredo
---

# 1908 — Determinant Phase-Avoidance Is Chart Data: the Strong-CP Route Does Not Transport Across the Flavor Carrier Groupoid (WP14)

## Question

Residue of the brief's fifth work package, in the form of its high-value
falsifier #4: *do perfect-matching determinant properties survive allowed
chart changes?*  The paper's App. V route to real \(\det(Y_uY_d)\) rests on
textures where the unique loop phase can avoid every perfect matching of
the Yukawa bipartite graphs, making the determinant a real monomial (up to
sign).  WP5 established this for the four worked textures.  The decisive
groupoid form of the question is new: the 61 fitted charts of the WP9
atlas all lie over **one** physical flavor point (WP10, entry-level
certification via the WP10 permutation gate).  Is phase-avoidance uniform
across them — a property of the physical point — or mixed, hence chart
data?

## Method

Pure combinatorics; no floating point, no fitting.  For each nine-link
support \((\mathrm{mask}_u,\mathrm{mask}_d)\) with the loop phase on a
chosen cycle edge, enumerate the perfect matchings of the two \(3\times3\)
bipartite sector graphs (rows \(Q\), columns \(u^c\) / \(d^c\)).  Each
matching contributes \(\operatorname{sgn}(\pi)\prod m_e\) to
\(\det Y\); the phase edge multiplies its monomial by \(z=e^{i\phi}\) iff
it belongs to that matching.  Three exhaustive classes:

- **real_monomial** — the phase edge is in *no* matching of its sector:
  \(\det(Y_uY_d)\) real monomial, \(\arg\det\in\{0,\pi\}\) structurally;
- **z_times_monomial** — the phase edge is in *every* matching (unique
  matching in all occurring cases): \(\det(Y_uY_d)=z\cdot(\text{real})\),
  so \(\arg\det(Y_uY_d)=\pm\phi\ \mathrm{mod}\ \pi\) *exactly*;
- **A_plus_zB** — mixed membership in a two-matching sector:
  \(\arg\det=\arg(A+Be^{i\phi})\), magnitude-dependent.

Census levels: (a) all 6552 viable connected one-cycle full-rank supports
(the WP13 class), orbit-reduced under \(S_3^3\times\)swap to 18 orbits,
phase placed on each cycle edge — 80 orbit cases; (b) the full
support-level ensemble, 28944 phase placements; (c) the 61 fitted WP9
carrier-groupoid vertices.  Regression gate: the four WP5 worked textures
must reproduce `results/wp5_matching_reality.json`.  Checker:
`research/flavor/checkers/wp14_matching_determinant_census.py`; results:
`research/flavor/results/wp14_matching_determinant_census.json`.

Typing caution, stated once and meant throughout:
\(\arg\det(Y_uY_d)\) is **not** invariant under the \(U(1)^3\) part of the
weak-basis group; the physical combination is
\(\bar\theta=\theta+\arg\det(Y_uY_d)\).  This census measures a
chart-combinatorial property.  It says nothing by itself about
spontaneous CP, radiative stability, or a solution of the strong CP
problem.

## Result

**T1 — exact trichotomy over all one-cycle nine-link topologies.**  The
80 orbit cases split \(31/27/22\) into
real_monomial / z_times_monomial / A_plus_zB.  Every multi-matching
sector in the census has matching counts \((1,2)\) (one matching up-type,
two down-type) with mixed phase membership — the A_plus_zB mechanism is a
single Cauchy–Binet interference, mirroring WP12's \(\cos\phi\) mass-term
mechanism.  At full support level, \(13392/28944\approx46.3\%\) of phase
placements are phase-avoiding.

**T2 — falsifier #4 decided: phase-avoidance does not transport.**  Over
the 61 fitted charts — all above *the same* physical point — the classes
are mixed:

\[
24\ \text{real}\quad/\quad
31\ \arg\det=\pm\phi\ \text{exactly}\quad/\quad
6\ \arg\det=\arg(A+Be^{i\phi})\ (\text{all orbit 2}).
\]

The same physical flavor point is presented by charts whose
\(\det(Y_uY_d)\) is structurally real, charts whose determinant carries
the *entire* loop phase, and charts whose determinant phase is a
magnitude-dependent interpolation.  Determinant phase-avoidance is
therefore **chart data, not physical data**: no statement about
\(\arg\det\) per chart descends through the carrier groupoid.  (55 of 61
fitted charts have matching counts \((1,1)\) — both determinants
monomials — so the classification there is purely the combinatorics of
which edge the unique matching uses.)

**T3 — the existential refinement survives.**  What *can* descend is a
fiber-level existential: *the fiber over the fitted physical point
contains phase-avoiding charts* (24 of them, spanning orbits
0, 6, 10, 11, 13, 14, 15, 16, 17).  Whether every physical point in the
viable region admits a phase-avoiding chart is open — the
support-general 46% avoidance rate does not by itself survive the
viability selection, which is known to correlate with chart structure
(WP7/WP9).

**T4 — disjoint from the WP13 zero dichotomy.**  All 12 phase cases in
WP13's CP-trivial orbits \((84,119),(85,118),(85,220)\) — where
\(\det[H_u,H_d]\equiv0\) identically — are phase-in-det cases.  No
real_monomial orbit case is CP-trivial.  Structural determinant reality
and structural CP-triviality are disjoint chart properties in this
census.

Ensemble reconciliation with the paper: App. V's "5 of 99 fixed-phase
textures do not allow the phase to avoid all determinant matchings"
concerns the paper's fitted fixed-phase ensemble (including ten-link
classes); our 24/61 counts the nine-link LO atlas over one physical
point.  Different ensembles, no contradiction; the qualitative paper
statement ("most viable textures allow avoidance") survives in the
existential form T3.

## Interpretation

This is the WP6/WP11 pattern recurring at the determinant layer: a
conspicuous chart quantity that organizes presentations without
descending to the physical quotient.  The strong-CP-friendliness of the
framework types precisely as: *if* a UV completion sets \(\theta=0\)
(spontaneous CP or otherwise, with radiative stability addressed
separately) *and* the Yukawa sector is realized in a phase-avoiding
presentation, *then* \(\bar\theta=0\) at tree level — and T3 says such a
presentation exists over the fitted point.  But T2 says nature selecting
"a nine-link texture" does not select that presentation: 37 of 61 fitted
charts over the same physics fail it, 31 of them maximally
(\(\arg\det=\pm\phi\)).  For the H2LR typing: determinant
phase-membership belongs to the chart atlas
\(\mathfrak F_9^{\mathrm{sparse}}\), not to
\(\mathcal O_{\mathrm{flavor}}\); the only candidate physical statement
is the existential fiber property, which is exactly the kind of
"chart-existence" clause WP6 already isolated for the flavor admission
verdict.

## Verification

- WP5 regression: all four worked textures (S38/S43/S48/S53) reproduce
  the prior phase-membership booleans and per-sector matching counts —
  pass.
- Exhaustiveness: all 6552 viable supports enumerated (matches WP13's
  independent count); 18 orbits, 80 orbit phase cases; 61/61 fitted
  charts classified, class counts sum to 61.
- The A_plus_zB label was audited for the theoretical subcase "phase in
  all of \(\ge2\) matchings" (which would be \(z\cdot\)real polynomial,
  arg \(=\pm\phi\)): zero occurrences in the census.
- Runtime \(\sim2\) s; stdlib only.

## Relations

- Closes the brief's fifth work package residue and decides falsifier #4.
- Extends WP5 (`wp5_matching_reality.json`, four worked textures) to all
  topologies and to the full fitted groupoid.
- Cross-references WP13 (entry 1907): T4 is the disjointness statement
  against its zero dichotomy.
- Depends on WP10's certification that the 61 charts lie over one
  physical point (the premise that makes T2 decisive).
- Repeats the WP6 (ev-758) admission-verdict pattern at the determinant
  layer: presentation property, existential fiber residue.
