---
author: marici.Figueiredo
---
# 1956 — Exact Sheet Doubling: the Generation-Exchange Map in Closed Form

- Date: 2026-08-23
- Author: marici.Figueiredo
- Status: theorem-form statement, certified at fit precision (35/35 stored pairs)
- Supersedes: sharpens 1955 (WP24c) from existence-by-refit to explicit map

## Scope

WP24c established that the readout fiber over the best-fit point is 2-fold for
all 72 permutation-u diagonal-class textures, with partners exchanged by
generation exchange 1<->2. WP24b gives the map in closed form and shows its
existence is combinatorially forced, not accidental.

## The exact map

For every stored diagonal-class sheet pair (35/35 textures), with sheets
theta_1, theta_2 over the same physical point:

1. **u-side is exact permutation conjugation:**
   Yu_2 = P01 Yu_1 P01, max defect 3.2e-14 (machine precision on stored
   minima). The two light u-magnitudes are interchanged between the two
   off-diagonal (member 266) or diagonal (member 273) slots.

2. **d-side is permutation conjugation up to a diagonal rephasing and a right
   unitary:** Hd_2 = D' P01 Hd_1 P01 D'^dagger with D' diagonal unitary;
   residual 1.2e-12. The magnitude identity |Hd_2| = P01 |Hd_1| P01 holds to
   1.2e-12; the off-diagonal triangle phase arg(h01 h12 h20) holds to 2.5e-8
   (fit precision of the stored minima). Given the Hd identity,
   Yd_2 = D' P01 Yd_1 W with W unitary is an algebraic identity (WW^dagger =
   (Dp P01 Yd1)^-1 Hd2 (Dp P01 Yd1)^-dag = I); numerically W unitarity holds
   to 2.3e-7 for all 35 pairs.

3. **Same physical point:** physical16 agreement <= 2.4e-8 (1955), so the map
   is a genuine weak-basis (U(3)^3) orbit: L = D' P01 on the left, W on the
   right, exact in the limit of exact minima.

4. **The loop phase is exactly the chart monomial:** arg of the App. V.a loop
   monomial reproduces the stored folded phi to 2.8e-14 degrees for all 70
   minima — the WP2 convention identification is exact. The two sheets carry
   loop phases that are chart data through W, not physical data.

## Existence is combinatorially forced

The d-side closure problem for sheet 2 is: find unitary W making
P01 Yd_1 W vanish on the texture's three d-zeros. Columnwise, each zero (i,j)
constrains column w_j to be orthogonal to row p(i) of Yd_1. A generic
obstruction occurs only when all three zeros share one column (w_j would be
orthogonal to three independent rows) or one row (three orthonormal columns
in a 2-dimensional complement). Both patterns make the d-sector singular
(zero column / zero row, hence det Yd = 0) and are excluded by full rank.
Census: all 72 permutation-u diagonal textures have zero-column count type
(2,1,0) — solvable by the explicit construction (w from successive orthogonal
complements). This matches the empirical 72/72 doubling of 1955.

## The loop-phase jump is a zero-pattern invariant

The sheet-to-sheet folded-phase split takes exactly three values, fixed by
the incidence structure of the d-zero pattern alone:

| zero pattern (3 d-zeros)                                | Delta-phi  | n   |
|---------------------------------------------------------|-----------|-----|
| two zeros share a row among rows 0-1                    | 26.8915°  | 19  |
| zeros form a partial transversal (all rows/cols distinct)| 24.5002°  | 8   |
| row-2 zero pair, or two zeros share a column (rows 0-1) | 0 (coincident) | 8 |

The bimodal (1,3)-splitting of 1954 is therefore a combinatorial classification,
not a fit outcome. The values 26.8915° and 24.5002° are differences of
texture-specific chart phases; no simple pi/8 relation is claimed.

## What remains for full exactness

- Symbolic W (rational/symbolic arithmetic) for one representative of each
  Delta-phi family, closing fit-precision to exact arithmetic.
- block21 generalization (WP24d): the (0,4) exchange has the same
  ln(yc/yu) signature but a 4-edge u-sector; the map form is open.
- The oddball 311_273_u01 (6-edge u-support, cluster 0) lies outside the
  permutation-u theorem; its fiber structure is unclassified.

## Durable verification

- Checker: `research/flavor/checkers/wp24b_exact_sheet_doubling.py`
- Results: `research/flavor/results/wp24b_exact_sheet_doubling.json`
- Companion: 1955 (WP24c, results/wp24c_generation_exchange.json)
- Sequence claim: seqclaim-33c8394a2e48390d4d980485 (value 1956)
