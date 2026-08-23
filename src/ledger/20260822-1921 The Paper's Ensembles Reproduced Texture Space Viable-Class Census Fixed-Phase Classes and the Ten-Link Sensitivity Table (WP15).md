---
author: marici.Figueiredo
---

# 1921 — The Paper's Ensembles Reproduced: Texture Space, Viable-Class Census, Fixed-Phase Classes, and the Ten-Link Sensitivity Table (WP15)

## Question

The fourth work package's census obligation: reproduce the ensembles of
arXiv:2607.27315v1 (App. V.a free-phase scan -> 2398 fits / 156 classes;
App. V.b fixed-phase scan -> 1412 fits / 99 permutation classes / 32
rotation classes; App. II.a ten-link sensitivity, Fig. S2) inside the
exact census of WP5/WP13, so that the pi/8 clustering and the texture
counting rest on reproduced — not quoted — numbers.

## Method

WP15a. The paper's texture space (full-rank pairs, nine links, splits
4+5/5+4/6+3/3+6, (3,3) nonzero in both matrices, one 4- or 6-link loop)
is exactly the WP5 census restricted by the (3,3) rule: 1592 supports,
36 S3^3 orbits, 18 exchange orbits.  Splits and loop lengths are not
independent hypotheses: full rank forces >= 3 links per sector, and
bipartiteness (Q vs u^c/d^c) forces cycle length in {4, 6}.
Checker `wp15a_texture_space_audit.py`.

WP15b. Dense free-phase scan: every (3,3)-filtered member of every
orbit, BOTH sector identifications (the paper does not identify sectors
at texture level, so the swapped half carries independent physics),
24 starts/member (16 phase anchors + 8 random), two-stage bounded LM,
same 17-observable chi2 (Tab. S2 at M_Z) and 3-sigma cut as the paper;
unioned with the WP7 ensemble.  Class reduction by the paper's rule
(App. V.a): identify fits related by S3^3 row/column permutations with
all nine entry magnitudes matching to 5% and |phi| to 0.1 deg.  Per the
paper's stated policy ("for a given texture, our scan looks for the best
possible chi2 solution", distinct viable fits arise from the pi/8 phase
windows), only the best-chi2 minimum per (member, window) enters the
reduction.  Checkers `wp15b_dense_scan.py`, `wp15b_dense_reduce.py`.

WP15c. Fixed-phase scan: phi pinned at the paper's ten values
{+-pi/8, +-3pi/8, +-pi/2, +-5pi/8, +-7pi/8}, 9 free magnitudes, on two
representatives per S3^3 orbit (canonical member + second member;
attainable fit sets are permutation-invariant within an orbit),
starts = hierarchy-aware random plus transported free-phase minima
from the same orbit.  Permutation classes via the
paper rule (folded phase: the paper does not distinguish +-phi or
pi+-phi); rotation classes via the paper's practical rule (fits
converging to the same minimum to ~10 significant figures in chi2).
Checkers `wp15c_fixed_phase.py`, `wp15c_reduce.py`.

WP15d. Ten-link sensitivity (Eq. S37): the Fig.-2 texture is class 4 of
the phi = pi/2 fixed-phase classes — NOT App. III's Example I (the
sensitivity text flags Y^u_21 as vanishing; Example I has u21 != 0).
Constraints from the text (loop = {u12, d12, u22, d22} cross-matrix
4-cycle; u21 = d11 = d13 = d32 = 0; R_alpha ~ D12/U12) isolate two
census candidates, members (275, 314) [orbit 17] and (275, 370)
[orbit 15].  Fit at pinned phi = pi/2, then switch on each vanishing
entry at its hierarchical size sqrt(m_i m_j)/v and differentiate alpha
numerically, purely real / purely imaginary, smaller sign retained.
Checker `wp15d_sensitivity.py`.

## Result

T1 (texture space).  App. V.a's space = 1592 supports / 36 S3^3 orbits
inside the exact census; no additional texture hypotheses are needed
beyond the (3,3) rule.

T2 (free-phase ensemble).  1658 viable minima (1486 dense + 172 WP7)
over all 1592 textures x both halves; best-per-(texture, window) policy
-> 1071 fits -> **134 classes** at the paper's tolerances (paper: 2398
fits -> 156 classes).  Tolerance audit: 153 classes at (2%, 0.05 deg),
134 at (5%, 0.1 deg), 125 at (10%, 0.2 deg) — the count brackets 156 and
is limited by fit convergence and scan density, not by missing texture
space.  The folded class histogram has support ONLY at multiples of
pi/8: 32 (pi/8), 30 (pi/4), 49 (3pi/8), 23 (pi/2).  The pi/8 lattice of
viable classes is reproduced from the census end to end.

T3 (excluded orbits).  Four exchange-orbits are nonviable in BOTH sector
identifications (best chi2 3835-6669, cut 20.28): census orbits 1, 3, 8,
12 — canonical (84,119), (84,238), (85,118), (85,220).  Orbits 1, 8 and
12 are the WP13 CP-trivial (J identically zero) orbits, which must fail
a CP-odd readout — the exclusion is structural, not numerical.  Orbit 3 ((84,238), split 3+6, monomial anti-diagonal
up-texture) is excluded at best chi2 = 3835; the mechanism (a monomial
Yu cannot source realistic CKM mixing in this pairing) is recorded as a
conjecture.  14 of 18 exchange-orbits are viable.

T4 (sector identification matters).  Viability is NOT symmetric under
u <-> d exchange at fixed support: orbit 2's swapped half has zero
viable minima (best chi2 76.3), orbit 0's swapped half has one
(chi2 3.50).  The paper's silent sector assignment is a genuine physical
choice, visible only because both halves were scanned.

T5 (ten-link sensitivity).  Both Fig.-2 candidates fit viably at pinned
phi = pi/2 (chi2 = 3.38, alpha0 = 88.95 deg; |R_alpha| = 2.40 vs
|D12/U12| = 2.51, arg -90.00 deg — the LO Yukawa-triangle relation
holds at the fitted point).  The S37 table (degrees per unit epsilon,
hierarchical size sqrt(m_i m_j)/v, eps-converged 1e-6..1e-8):
Y^u_13 (+41 imag / -17 real), Y^d_13 (+469 / -198), Y^d_32 (-22 / +8)
are the phase-independent dangerous entries requiring 1-2 orders of
suppression; Y^d_11 is dangerous only for the real perturbation (+3.3);
all other zeros are sub-degree.  This reproduces Fig. S2's qualitative
content entry by entry, for BOTH candidate members — the sensitivity
pattern is a class property, not a presentation artifact.

T6 (fixed-phase ensemble).  Union of two per-orbit representative
variants (canonical + second member), ten phase pins: 280 viable pinned
fits (90 + 157 + 33 across |phi| = pi/8, 3pi/8, pi/2) ->
permutation classes 14 / 16 / 11 = 41 (paper 35/35/29 = 99);
rotation classes 9 / 7 / 3 = 19 (paper 10/13/9 = 32).  All three
pinned families are viable on the shared orbits, the pi/8 rotation
count matches within one (9 vs 10), and the class support mirrors the
free-phase pi/8 lattice.  The permutation-class shortfall is
demonstrably scan-density limited, not structural: doubling the pinned
fit count (142 -> 280 via the second representative) added exactly one
permutation class (40 -> 41), so the paper's 99 classes require far
denser seeding than 24 starts/member — and the paper states its own
scan is incomplete.  Variant-1 representatives independently reproduce
the WP15b viability pattern (e.g. orbit 3's canonical half yields zero
pinned minima, consistent with its free-phase exclusion).

## Caveats

- Class counts are scan-density and fit-convergence limited on both
  sides; the paper states its own scan is incomplete.  The reproduced
  quantities are the *structure* (pi/8-only support, excluded orbits,
  sensitivity pattern), not the exact integers 156/99/32.
- The Fig.-2 member identification has a residual twofold ambiguity
  ((275,314) vs (275,370)) not resolved by the printed text; all
  reported conclusions hold for both.
- Sign conventions: the viable basin selects the phase sign through the
  paper's phase-placement rule; +-phi and pi+-phi are identified per the
  paper.

## Consequence for the program

WP15 closes the census obligation of WP4: the pi/8 clustering, the
class census, and the ten-link robustness are now reproduced inside the
exact groupoid machinery rather than quoted.  Combined with WP14b (the
clustering is exhausted by CKM-angle inheritance) and WP11-13 (the loop
phase is chart data), the empirical core of the paper stands as:
a sparse-chart mechanism whose physical content is exactly its
weak-basis-invariant image.  No new sector admission evidence arises
from the ensembles themselves.

Artifacts: research/flavor/checkers/wp15{a,b_dense_scan,b_dense_reduce,c_fixed_phase,c_reduce,d_sensitivity}.py;
research/flavor/results/wp15{a_texture_space_audit,b_dense_orbit01..18,b_dense_class_reduction,c_fixed_phase,c_class_reduction,d_sensitivity}.json.
