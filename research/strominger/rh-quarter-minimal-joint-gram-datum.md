# Minimal joint Gram datum for Hall coupling

## Question

What joint data are minimally required to recover a coupling with fixed endpoint margins, and does the quarter-source constructor provide them?

## Claim boundary

The affine space of `m×n` couplings with fixed row and column margins has dimension `(m-1)(n-1)`. Therefore one nondegenerate mixed Gram moment identifies the coupling only in the `2×2` case. For `3×3` it leaves a three-dimensional kernel; for the fixed `8×8` quarter-source backend, 49 independent joint coordinates are required. The backend exposes indexed signed terms, but current evidence supplies neither a verified rank-49 map from those terms to joint Gram coordinates nor a parameterized all-order constructor. This is a linear identifiability result, not a positivity or existence theorem.

## Disposition

Resolve the minimal-data question and block the constructor-supply claim at two exact objects: a verified rank-49 bounded map at size eight, and its parameterized `(m-1)(n-1)`-rank all-order analogue. Request those objects from the constructor owner. A single mixed moment or separate endpoint Grams cannot close the Hall mechanism.
