---
author: marici.Figueiredo
---

# 1890 — Every Nine-Link Chart Has a Degenerate Leading-Order Unitarity Triangle (WP9 LO Atlas)

## Question

Entry 1092 left the leading-order (LO) identity of the unmatched fiber
cores open: which object does the loop phase \(\varphi\) of a nine-link
chart approach in the hierarchical limit, for each of the 18 exact
fiber values — and what structurally forces the WP4 angle-inheritance
pattern (entry 1084)?  Concretely: driving the fitted texture
magnitudes deeper into the hierarchy (\(m_i \to m_i^\tau\)), what is
the LO behaviour of the three rephasing-invariant CKM quartics whose
arguments are the chart's unitarity-triangle angles, and is that
behaviour a property of the chart, of the core, or of the physical
point?

## Method

For each of the 61 WP8 fiber charts (best-fit physical point,
\(\chi^2 = 3.3628\), \(\alpha = 1.557245\), \(\beta = 0.397949\),
\(\gamma = 1.186398\)): freeze the fitted magnitudes, wind
\(z = e^{i\varphi}\) around \(U(1)\) (1024 samples, \(N\)-halving
certified), and track

\[
R_\alpha=-\tfrac{V_{td}V_{tb}^*}{V_{ud}V_{ub}^*} ,\qquad
R_\beta=-\tfrac{V_{cd}V_{cb}^*}{V_{td}V_{tb}^*} ,\qquad
R_\gamma=-\tfrac{V_{ud}V_{ub}^*}{V_{cd}V_{cb}^*} ,
\qquad
\arg R_x = w_x\varphi + c_x + \mathrm{wobble}_x(\varphi) .
\]

Hierarchy flow \(m_i \to m_i^\tau\): float64 for \(\tau \le 4\); a
pure-mpmath cyclic-Jacobi eigensolver for \(\tau = 8..128\)
(`checkers/jacobi_mp.py`; texture entries and CKM arithmetic never
downconverted — float64 flushes components below \(10^{-308}\) and
corrupts the quartics; validated against `eigh` at \(\tau = 1\) to
\(2.3\times10^{-13}\); working precision
\(\mathrm{dps} = \lfloor 2\tau\,\mathrm{span}/\ln 10 \rfloor + 80\)).
Winding changes along the flow are recorded (`winding_stable`), not
asserted away: for a chart whose path dominance reorganizes, the
\(\tau = 1\) winding need not survive.  T8 cross-checks the windings
against the WP4 symbolic \(\varepsilon\)-series eigensolver at one
integer-power lattice point.

Checker: `checkers/wp9_lo_atlas.py`; results:
`results/wp9_lo_atlas.json`.  Addendum checker:
`checkers/wp9_transition_naturality.py`; results:
`results/wp9_transition_naturality.json`.

## Findings

### 1. Universal winding algebra (all 61 charts)

Every chart's winding vector is a signed permutation of
\((-1, 0, +1)\): exactly two opposite unit windings and one zero, with
\(\sum_x w_x = 0\) — the exact algebraic shadow of
\(\alpha + \beta + \gamma = \pi\).  Offsets \(c_x \in \{0, \pm\pi\}\).
Integer certification: float winding deviation \(< 10^{-9}\);
\(\det[H_u, H_d]\) winding consistent on every chart [T1, T1b, T2, T3,
T7].

Consequence: **every nine-link chart has a degenerate LO unitarity
triangle** — one angle is \(\varphi\)-free at LO (it vanishes in the
hierarchical limit) and the other two are \(\pm\varphi\) and
\(\pi \mp \varphi\).  Angle inheritance is not a property of special
textures; the single-holonomy topology forces it on the whole
nine-link stratum.

### 2. \(\det C\) is first-harmonic pure

\(\arg\det[H_u, H_d]\) carries only the \(m = 1\) Fourier harmonic in
\(\varphi\), higher harmonics \(< 10^{-10}\) of \(a_1\) on every chart
[T4]: the weak-basis-invariant commutator phase is an exact pure
\(U(1)\) character of the loop.  (Flagship chart: higher harmonics
\(\le 10^{-36}\).)

### 3. Three regimes resolve the WP8 unmatched cores

By the residual
\(\lvert \mathrm{angle}_{\rm fit} - (w_x\varphi_{\rm fit} + c_x)\rvert\)
at the fitted point, per distinct folded core:

\[
\begin{array}{c|c|c|l}
\text{core} & \text{regime} & \text{res.\ (mrad)} & \text{carrier; orbits}\\
\hline
0.3983,\ 0.3991 & \text{clean} & 0.36,\ 1.14 & \beta;\ 5,14,10\\
1.1870\text{--}1.1872 & \text{clean} & 0.63\text{--}0.83 & \gamma;\ 9,0,6,16\\
1.5568 & \text{clean} & 0.48 & \alpha;\ 5,14\\
0.3782,\ 0.4170 & \text{moderate} & 19.7,\ 19.0 & \beta;\ 5,14,10\\
1.1960\text{--}1.2169 & \text{moderate} & 9.6\text{--}30.5 & \gamma;\ 2,6,9,16,0\\
1.5640,\ 1.5661 & \text{moderate} & 20.3,\ 18.2 & \alpha;\ 10,4,7,13,15\\
0.7475,\ 0.7684 & \text{nonpert.} & 349.6,\ 370.5 & -;\ 0,2\\
0.8179,\ 0.8193 & \text{nonpert.} & 368.5,\ 367.1 & -;\ 4,7,11,13,15,17
\end{array}
\]

The moderate cores are the same UT-angle carriers with NLO wobble at
the fitted point: along the flow their wobble decays below
\(5\times10^{-3}\) with \(c \in \{0, \pm\pi\}\) to \(10^{-3}\) [T6b].
**This resolves the WP8 "unmatched" cores \(0.378, 0.417,\)
\(1.20\)–\(1.22\): they are NLO-deformed angle cores, not new objects.**
The nonperturbative cores admit no LO identity at the fitted point;
\(\varphi\) there is a non-perturbative chart coordinate.

### 4. Revision of a WP8 remark

WP8 noted \(0.768414 \simeq \pi - 2\gamma\) at \(0.38\) mrad.  WP9
finds no carrier law behind that core (nonperturbative regime,
residual \(370\) mrad): the match is a numerical coincidence at the
fitted point, not an LO relation.  The WP8 core table is narrowed
accordingly.

### 5. Flow convergence is orbit-dependent, with exactly two mixed cores

The \(\tau\)-flow verdict is not a function of the core alone.  All
six \(0.817882\) orbits converge (final wobble \(\le 1.1\times10^{-5}\));
exactly two cores split by orbit: \(0.819271\) (converges on orbits 11,
13; winding-unstable on 4, 7, 15, 17) and \(1.566129\) (converges on
13, 15; unstable on 4, 7).  The clean cores \(0.3983, 1.5568\) are
winding-*unstable* on their (5, 14) orbits — a chart whose fitted
point sits on a clean angle carrier can still reorganize its path
dominance under the flow.  A single universal hierarchy-flow collapse
is thereby falsified [T6 false, honestly]; every converged
representative is winding-stable with \(c \in \{0,\pm\pi\}\) [T6b, T6c
true].  Graph record: `marici:claim:flavor-wp9-two-mixed-cores-v1`
(ev-000000000870), `marici:claim:flavor-wp9-mixed-verdict-v1`
(ev-000000000860).

### 6. Canonical holonomy transport across orbit boundaries — inside the atlas

Within the \(0.817882\) cluster the full wobble functions
\(\arg R_x(\varphi)\) agree across six orbits to
\(1.2\times10^{-9}\); within \(0.819271\) across four orbits to
\(7.0\times10^{-10}\) [curve_identity]: the loop phase transports
canonically across those chart boundaries.  This is atlas-internal
evidence on falsifier 1 of the flavor brief; it sharpens and does not
contradict the WP6 non-descent verdict (entry 1077), which concerns
the full \(U(3)^3\) quotient.

### 7. Symbolic validation (T8)

The WP4 \(\varepsilon\)-series eigensolver at the integer-power lattice
point of chart (orbit 6, member \((417,342)\), edge \((d,0,1)\)) yields
\(z\)-powers \((w_\alpha, w_\beta, w_\gamma) = (+1, 0, -1)\), matching
the certified numeric winding at the same lattice point exactly
[T8 true].  The winding algebra is therefore not a numerical-fit
artifact: the symbolic eigensolver sees the same two-leg structure.

### 8. Transition naturality: base agreement, flow divergence, no verdict typed

The addendum (`wp9_transition_naturality`) compares repeated cores
across orbits: base (\(\tau = 1\)) loop readouts agree to
\(2.2\times10^{-9}\), while later-flow readouts diverge (spread
\(1.9\times10^{-2}\) by \(\tau = 4\) on the worst core); the mixed
cores are exactly the WP9 pair of \S5 [its T1–T4 true].  Because the
tolerance-selected fiber points are not certified identical physical
points, **no chart-transition naturality verdict is typed**: the flow
is coherent on the physical base, but sparse exponent rescaling does
not descend to a natural flow on the physical quotient.  Graph
records: `marici:claim:flavor-wp9-readout-divergence-only-v1`
(ev-000000000881), `marici:claim:flavor-wp9-flow-mistyped-v1`
(ev-000000000871).

## Scope

Statements concern the WP7/WP8 best-fit fiber, the nine-link stratum,
and the LO limit as defined by the magnitude flow.  The transport
statement of \S6 is internal to the sparse atlas, not a descent claim.
The entry strengthens 1084 (angle inheritance is universal on the
stratum), narrows 1092 (moderate cores resolved; the
\(\pi - 2\gamma\) remark revised), and leaves the 1077 admission
verdict unchanged.  T6 is false by design of the honest recording:
nonperturbative and winding-unstable charts are classified, not
forced.

## Verification

- `research/flavor/checkers/wp9_lo_atlas.py` reproduces every number
  from `results/wp7_ensemble.json`; output
  `results/wp9_lo_atlas.json` (tests T1–T8 as reported above; T8 with
  `--t8`).
- `research/flavor/checkers/wp9_transition_naturality.py`; output
  `results/wp9_transition_naturality.json` (T1–T4 true).
- `research/flavor/checkers/jacobi_mp.py` validated against
  `numpy.linalg.eigh` at \(\tau = 1\) (max \(|\,V\,|\) deviation
  \(2.3\times10^{-13}\)).
- Epistemic graph: WP9 claims at ev-000000000860, ev-000000000870,
  ev-000000000871, ev-000000000881; refines the WP8 claim
  (`claim:7db3b744dc01f91c79fb`, entry 1092).
