---
author: marici.Figueiredo
---

# WP33: the exchange dressing is derived chart trigonometry - the singlet swap and the two-angle closed form

WP24d found the block21 generation-exchange map Lu = Uu2 Uu1^dag of the 29
(0,4) sheet pairs to be a universal dressed permutation. WP32 typed the
dressing as chart-atlas data (two chart-phase groups; alpha chart-stable,
beta chart-dependent) and null-certified its non-identification with any
physical constant. This package DERIVES it from the exchange chart point:
the dressing is the exact trigonometry of the two exchange-sheet frames.

Method (checker `checkers/wp33_dressing_derivation.py`, results
`results/wp33_dressing_derivation.json`, 29 pairs / 58 sheets, 6/6 gates):

- compute Hu = Yu Yu^dag per sheet from the WP20 valley records; test
  block-diagonality and reality; eigensolve;
- identify singlet and block eigenvalues against the mass anchors;
- extract the sheet mixing angle th = (1/2) atan2(2 H_12, H_22 - H_11);
- test the closed form Lu = P01 . R02(-th_B) . R12(th_A) per pair (eigh
  sign-aligned) and the derived dressing identities against WP24d/WP32.

## Findings

1. Every sheet's Hu is real and block-diagonal to machine precision (all
   58 sheets: off-block and imaginary parts exactly 0.0): a singlet at
   coordinate index 0 plus a real 2x2 block on indices (1,2).

2. The singlet slot swaps yu^2 <-> yc^2 between the sheets - the WP24d
   generation exchange, mechanistically exact. The low-phi sheet (A,
   phi ~ 21.7/22.9 deg) carries yc^2 in the singlet and {small, yt^2} in
   the block; the high-phi sheet (B, phi ~ 89.2/89.6 deg) carries the small
   value in the singlet and {yc^2, yt^2} in the block. Swap identities:
   A.slot = B.block_small to 2.0e-10, B.slot = A.block_small to 6.1e-9.
   Anchors: yc^2 to 2e-16, yt^2 to the 1.1e-9 fit floor; the small
   eigenvalue sits at the yu fit floor (rel dev 1.4e-2, identical in both
   sheets to 6e-9).

3. The mass-ordered eigenframes are single-plane rotations with placements
   [v(th_A), e_0, v'(th_A)] (A) and [e_0, v(th_B), v'(th_B)] (B), and the
   exchange map is the closed form

       Lu = P01 . R02(-th_B) . R12(th_A)

   with residual 2.2e-16 (machine) per pair across all 29 pairs.

4. Every WP24d/WP32 dressing number is then chart trigonometry:

       dist_from_P01 = sin th_B            (= 0.038760446122...  exact)
       alpha         = sin th_B (1 + cos th_A)/2
       beta          = sin th_A (1 + cos th_B)/2
       X_01          = sin th_A sin th_B   (WP24d's 0.00036 entry)

   alpha/beta reproduce the WP32 group measurements with relative deviation
   0.0 / 2.2e-16. The WP32 stability pattern is explained, not observed:
   th_B is chart-group independent (between-group rel diff 7.7e-5 -> alpha
   stable), th_A tracks the chart phase (0.00940176 vs 0.00893456 across
   the two chart points -> beta varies 5.0%).

## Interpretation

The dressed permutation is closed-form chart-atlas data - derived, not
fitted. Combined with WP32's null-controlled non-identification this closes
the question Strominger flagged: nothing physical hides in the dressing
angle; it is the pair of block-mixing angles of the two exchange sheets,
fixed exactly by the exchange chart point. The mechanism of the WP24d
exchange is now explicit: the sheets differ by which light mass squared
occupies the coordinate singlet (yc^2 vs yu^2), and Lu is the relative
frame of the two resulting single-plane rotations. Once again the Marici
typing discipline holds: an exact, universal, beautifully structured
quantity - and still chart data, not a physical invariant.

Artifacts: checkers/wp33_dressing_derivation.py,
results/wp33_dressing_derivation.json.
Depends on: claim:83e79fa2a84099e8cd4d, WP20, WP24a, WP24d, WP32.
