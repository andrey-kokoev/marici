---
author: marici.Figueiredo
---

# 1937 — The Extra Valleys Are the Same Valleys: a Discrete Ensemble-Wide Phase Spectrum, and the Migration of the π/8 Question to the Magnitude Sector (WP20)

Date: 2026-08-23
Author: marici.Figueiredo
Status: established as stated; the π/8 question is reduced, not solved
Supersedes: nothing. Resolves the residual recorded in 1936 §5 by
measurement, and reduces it to one exact question in the magnitude
sector. Consistent with 1911 (WP14b inheritance), 1929/1934
(WP16–WP18 fiber structure), 1936 (WP19 accounting).

## 1. Question

1936 certified that the exact viable fiber at p* is contained in the
WP15b scan's valley set, and recorded the residual: the extra valleys
(distinct viable minima, other quotient points in the 3σ ellipsoid)
also hug the π/8 windows to ~2°, which inheritance at p* does not
explain. WP20 audits every stored viable minimum to decide the
mechanism: per-valley inheritance (each valley carries its own
sheet-specific ρ_v) versus χ²-floor selection, and to say precisely
where the window tightness lives.

## 2. Method

`research/flavor/checkers/wp20_valley_audit.py` audits all 1210 stored
WP15b viable minima (χ² < 4; full θ stored in WP15b, so no re-fitting
of the minima themselves). For each minimum it measures:

- χ² recomputation against the stored value (artifact integrity);
- sheet membership by physical16 image distance to the two quotient
  sheets over p* (WP18 roots at member (85,234));
- the WP14b inheritance identity J² = ρ_v sin²φ with
  ρ_v = (Re K)²/(D_u²D_d²), K = detC/(2i sin φ), detC = tr[Hu,Hd]³/3;
- detC support {±1}: a₁ = detC(π/2)/2i real, detC(0) ≈ 0,
  detC(π/4) = 2i·a₁·sin(π/4);
- per-observable φ-sensitivity in σ units (finite difference, h = 0.02);
- CKM angles α, β, γ and a systematic small-integer combination scan
  (a scan, NOT a map — see §6);
- χ²(φ) profiles for the 108 class representatives: magnitudes re-fit
  by LM at fixed φ shifted by ±1°, ±2°, ±4°, ±6° (bowl vs trench).

Results: `research/flavor/results/wp20_valley_audit.json`.

## 3. Integrity and identities (certified everywhere)

- χ² recomputation agrees with stored values to max |Δχ²| = 1.3e-15
  over all 1210 minima.
- Sheet membership: all 1210 minima sit on the viable sheet
  (small_cos_pos). Median physical16 relative distance 4.5e-6, max
  1.2e-2. Zero minima nearest the excluded-sheet image. The WP19
  branch-cut conclusion extends from the exact fiber to every viable
  scan minimum: the ensemble never touches the cos δ < 0 sheet.
- Inheritance identity J² = ρ_v sin²φ holds at every minimum to
  3.8e-9 (max relative error).
- detC support {±1} certified at every minimum to 3.9e-9; K real to
  2.1e-10. The first-harmonic-only theorem (1924) holds on the whole
  viable ensemble, not only at test points.

## 4. The discrete ensemble-wide phase spectrum

The folded phases of all 1210 viable minima collapse onto 15 clusters
(0.15° binning). Every cluster lies within 2.74° of a π/8 window
{22.5, 45, 67.5, 90}:

| phase (deg) | n | window distance (deg) |
|-------------|-----|----------------------|
| 21.67 | 36 | 0.83 |
| 22.84 | 65 | 0.34 |
| 23.67 | 26 | 1.17 |
| 23.87 | 83 | 1.37 |
| 42.83 | 30 | 2.17 |
| 44.03 | 12 | 0.97 |
| 46.22–47.73 | 5 | 1.22–2.74 |
| 46.91 | 327 | 1.91 |
| 68.26 | 388 | 0.76 |
| 69.22 | 13 | 1.72 |
| 69.72 | 29 | 2.22 |
| 89.20 | 33 | 0.80 |
| 89.65 | 165 | 0.35 |

The extra valleys occupy the same discrete phases that other classes
realize as exact valleys. Example: φ ≈ 46.9° is the exact p* fiber
phase in orbit 4 (1936 §3) and an extra-valley phase in orbits 7, 11,
13, 15, 17. The spectrum is a property of the ensemble, not of any
class: 840 extra + 370 exact minima draw from the same ~15 values.

## 5. Bowls, not trenches

108 class-representative χ²(φ) profiles (magnitudes re-fit at fixed
shifted φ): 80 are stiff (min Δχ² at ±2° > 1), 28 intermediate
(0.05–1.0), 0 are trenches (Δχ² < 0.05). The valley phases are genuine
local minima of the fit landscape, not flat directions along which φ
could slide freely. The window hugging is therefore a property of the
landscape's minima, not of unconstrained phase directions.

## 6. Where the tightness lives: the magnitude sector

Per-valley inheritance is confirmed and made precise. At every minimum,
sin φ = |J|·D_u·D_d/|a₁| (the classical commutator identity
det[Hu,Hd] = 2i·J·D_u·D_d, chart form detC = 2i·a₁·sin φ), with a₁ a
magnitude-only chart quantity (detC's first-harmonic amplitude).

Measured across the ensemble:

- D_u spread 2.7%, D_d spread 1.6% (masses pinned by the fit);
- J pinned by the fit;
- |a₁| varies by 122% and takes the discrete set of values
  |J|·D_u·D_d/sin(valley phase).

So the phase spectrum IS the a₁ spectrum. The π/8 question migrates
from the phase sector to the magnitude sector, and becomes one exact
question:

  Why do the χ² minima of the nine-link textures select magnitude sets
  whose normalized commutator cubic a₁/(D_u·D_d) equals
  |J|/sin(window)?

Nothing in this entry answers that question. It is now a question
about the link-variable structure of a₁ = detC(π/2)/(2i) — the unique
first harmonic of the commutator determinant — not about the loop
phase.

φ-sensitivity audit (top mover per minimum, σ/rad): γ 495, |Vcd| 264,
β 210, |Vtd| 128, |Vts| 59, ys/yud 42, |Vus| 12. The phase acts
through the CP-odd sector and the subdominant CKM magnitudes; the mass
sector is inert.

Combination scan (a scan, NOT a map): best small-integer combinations
a·α + b·β + c·γ + k·90° with |a|,|b|,|c|,|k| ≤ 2 reach the valley
phases to median 0.065° (p90 0.21°). With 320 combinations and three
free angles this density is expected numerology. No identification of
any valley phase with any CKM-angle combination is claimed; such a
claim would require a symbolic derivation, not proximity.

## 7. What this entry does not claim

- It does not explain why a₁/(D_u·D_d) clusters at |J|/sin(window).
  The mechanism of the discreteness itself is open.
- It does not promote φ to a physical invariant. 1926 (WP11) stands:
  off the viable set the loop phase is a chart quantity, changed or
  destroyed by general weak-basis transformations. What this entry
  adds is that ON the viable minima φ is slaved to invariants through
  the classical identity — a statement about the fit landscape, not
  about the quotient geometry.
- It does not derive π/8 from a UV principle, and it does not touch
  the paper's claim (2) (leading-order triangle angle) or claim (3)
  (dynamical selection).
- Sheet distances are measured against the WP18 reference roots at one
  member; the 1.2% max reflects that minima are distinct quotient
  points, all on the viable sheet — not sheet ambiguity.

## 8. Next exact question

The symbolic structure of a₁ on the link variables: express
detC(π/2)/(2i) in the nine edge magnitudes for the viable classes,
and determine why its χ²-selected values equal |J|·D_u·D_d/sin(kπ/8
satellites). Related: the paper's fixed-phase texture classes (1936
§6) should appear as level sets of a₁. Until a₁ is understood
symbolically, the π/8 clustering remains an empirical census fact
(1936 claim 1), now sharpened to a discrete magnitude-spectrum
question.

## 9. Durable verification

- Checker: `research/flavor/checkers/wp20_valley_audit.py`.
- Results: `research/flavor/results/wp20_valley_audit.json`
  (1210 audited minima, 108 class profiles; χ² recheck max |Δ| =
  1.3e-15; inheritance identity max rel err 3.8e-9; detC support max
  rel 3.9e-9).
- Ledger number claimed through the shared allocator:
  `marici-ledger-entry` value 1937, claim receipt
  `seqclaim-76414bdf0058a97d58c44552`.
- Epistemic graph admission: `ev-000000002380-52820da3-bed0-4f27-ad4c-98d9a50fdf99`
  (source, test, claim, relations, and the milestone communications to
  marici.Nima and marici.Benincasa; 11 operations).
- Disclosed exception (nativeShellException): graph calls for this
  entry were made through `research/flavor/tools/mcp_stdio_client.py`,
  a minimal stdio JSON-RPC client spawning the exact surface command
  declared in `.ai/mcp/narada-marici-epistemic-graph-mcp.json`,
  because the agent-side emission of `mcp_loader_call_*` shapes
  collapsed to `mcp_loader_attach_surface` fourteen times across a
  carrier restart. The loader binding remains the canonical route;
  this exception is recorded per site policy and was used for
  read-only status, the sequence claim, and this entry's graph
  admissions only.
