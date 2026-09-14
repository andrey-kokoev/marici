# v213: explicit target detector rows on the physical pullback

Using the labelled basis from v212, the three target restrictions are now forced by their existing normalization and symmetry data:

- generic-Q primary: `sRow=(0,0,1,1,1)`; C3 descent forces equal road values and the primitive Q roof fixes them to one;
- paired-endpoint reciprocal: `WRow=(1,-1,0,0,0)`; the oriented conductor difference and unique unimodular endpoint swap fix this row;
- road relation: `vRow=(0,0,1,1,1)`; `rho0(v)=1` on D03 and Cech/C3 extension force equal values on all three roads.

Each row annihilates all four columns of the Entry-436 `d2`, so each is an actual pullback-homology detector rather than a post hoc scalar signature. All three evaluate `z=(1,0,1,0,0)` to one. Therefore the normalized six-point primitive maps to `s+W+v` in the selected packet.

This is the concrete normalized case `(a,b,c)=(1,1,1)`. It does not yet assert an independently variable symbolic `(a,b,c)` family. The exact row construction and closedness checks are in `check_physical_pullback_target_detector_rows.py`; module 235 records the result.
