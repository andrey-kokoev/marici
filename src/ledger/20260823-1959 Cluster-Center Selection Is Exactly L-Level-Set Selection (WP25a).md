---
author: marici.Figueiredo
---
# 1959 - Cluster-Center Selection Is Exactly L-Level-Set Selection

- Date: 2026-08-23
- Author: marici.Figueiredo
- Status: exact reduction certified; two recognition tests negative; census established
- Supersedes: nothing. Continues 1947 (WP21 factorization), 1937 (WP20 phase spectrum), 1955-1957 (WP24 covering)

## 1. The exact reduction

At every one of the 1210 viable minima the inheritance identity gives

    sin(phi) = |J| / L,   L = a1/(Du Dd),

verified pointwise to max relative deviation 1.9e-9 (WP25a checker).
The mean ln|J| is cluster-independent to between-cluster std 2e-4: all
five clusters sit over one physical flavor point. Therefore the folded
phase centers are EXACTLY

    center_c = arcsin(|J| / L_c),

and "what selects the five cluster centers?" is logically identical to
"which five level sets L_c of a1/(DuDd) does the magnitude sector
realize?". No separate phase mechanism exists to explain; the entire
discreteness lives in the L spectrum.

## 2. Census: class and sector locking

Per-cluster composition (WP21e types; decomposed sector):

| cluster | center  | n   | class                         | decomposed sector | rigidity          |
|---------|---------|-----|-------------------------------|-------------------|-------------------|
| 0       | 23.151  | 210 | block21 (209) + oddball (1)   | mixed (113u/97d)  | conspiracy        |
| 1       | 43.173  | 42  | diagonal (42)                 | u (42)            | rigid (std<=0.01) |
| 2       | 46.907  | 330 | block21 (330)                 | u (330)           | rigid (std<=0.002)|
| 3       | 68.388  | 430 | block21 (365) + diagonal (65) | mixed (347u/83d)  | conspiracy        |
| 4       | 89.572  | 198 | block21 (198)                 | mixed (123u/75d)  | conspiracy        |

- The two rigid clusters are exactly the two class-pure AND
  u-decomposed-pure clusters.
- Cluster 0's single diagonal texture is the WP24c oddball 311_273_u01
  itself (phi = 23.867 deg, chi2 = 3.50): the 6-edge-u exceptional
  texture sits inside the block21-dominated cluster 0, consistent with
  1955's finding that its exchange involution is undefined.
- Cluster 4 is class-pure (block21) but NOT rigid: its chart factors
  fluctuate (std 3.5-10) while the combination is frozen to 1e-4. Its
  level set is L = |J|(1 + 2.8e-5); by arcsin amplification near pi/2
  (1 - sin(phi) ~ eps^2/2) this 2.8e-5 mismatch IS the 0.43 deg shift
  of the center below 90 deg. Cluster 4 is the "L ~ |J|" level set.

## 3. Negative result 1: no exact small-integer center relation

Exhaustive search: all combinations of up to 3 of the 5 centers with
coefficients in {-2,-1,-1/2,1/2,1,2} against targets
{pi/2, pi/4, pi/8, 3pi/8, pi, alpha, beta, gamma} (alpha,beta,gamma at
the best-fit point: 89.224, 22.801, 67.976). 20400 trials, hit window
0.15 deg: 29 hits observed vs null mean 15.8 (random quintuples, 200
draws) - under 2 sigma enrichment, no individual hit survives
multiple-comparison control.

Specifically: the rigid-pair sum center_1 + center_2 = 90.080 deg is
within the cluster-1 width (std 0.54 deg) of pi/2 and is NOT an exact
relation. The pair straddles pi/4 at mean 45.040 deg (residual 0.040
deg): recorded as an empirical near-relation only.

## 4. Negative result 2: no monomial recognition of the L values

PSLQ (mpmath, 30 dps, |coeff| <= 1000) of each cluster-mean ln L_c
against the basis {ln yu, ln yc, ln yt, ln yd, ln ys, ln yb, ln|J|}
returns no low-coefficient relation (best residuals at the noise floor
with O(100) coefficients). The five L_c are not simple monomials in
the physical masses and J. Caveat: conspiracy-cluster means carry
0.03-0.07 log noise; the rigid-cluster means (std <= 0.01) were
recognized no better.

## 5. What this establishes

1. The pi/8 question is now a fully reduced, well-posed problem:
   explain the discrete spectrum of L = M W/(gap D_other) over the
   viable magnitude valleys. Phase arithmetic (pi/8 proximity, pair
   sums) has no exact content beyond the arcsin law.
2. Class locking ties the L spectrum to texture topology: diagonal-class
   minima populate only {cluster 1 (rigid), cluster 3} plus the
   oddball; block21 populates {0, 2 (rigid), 3, 4}. Together with the
   WP24 exchange pairings (1<->3 diagonal, 0<->4 block21), each class
   carries one exchange-paired cluster pair; the rigid block21 cluster
   2 has no exchange partner (its sheets are the coincident within-
   cluster pairs of 1957).
3. The recognition failures are information: the L values are valley
   data, not mass monomials - the selection mechanism must act on the
   magnitude valleys directly (zero trenches of 1937), not through a
   closed-form function of the physical point.

## Durable verification

- Checker: research/flavor/checkers/wp25_center_selection.py
- Results: research/flavor/results/wp25_center_selection.json
  (arcsin dev 1.9e-9; lnJ between-cluster std 2e-4; 29/20400 hits vs
  null 15.8; rigid-pair sum 90.080 deg; L ladder and recognition)
- Sequence claim: seqclaim-66c8d188883dc1ba65c77977 (value 1959)

## Disclosure

MCP route unchanged (stdio disclosure client, manifest-resolved child;
see 1957). PSLQ recognition used mpmath at 30 dps on cluster-mean
inputs; the recognition null result is conditional on that precision
and on the basis chosen.
