# 3943 — Quotient Projection Restores Local Bockstein Nonhorizontality

## Correction

Entry 3940 is retracted. It correctly replaced sequential relation discovery by the inhomogeneous kernel-lift equation, but formed its right-hand side in the ambient presentation rather than the 26-dimensional free quotient. One displayed obstruction coordinate lay outside the low quotient, exposing the error.

## Repaired calculation

Project every normal form to the free quotient before forming or solving

\[
M_0r_X=-M_Xr_0.
\]

At ((x,y,z)=(2,3,4)), in both (x,y) directions and at primes (32009,32003):

- base relation dimension: (2);
- liftable relation dimension: (2);
- obstruction dimension: (0);
- Bockstein rank: (1);
- Bockstein-plus-mixed rank: (2).

Thus Entry 3933’s local nonhorizontality result is restored, now using the correct kernel-lifting equation and quotient projection. Entry 3940’s rank-two obstruction plane was entirely an ambient-coordinate artifact.

## Epistemic consequence

The two repairs are both necessary:

1. nilpotent-only ambient residuals are not relations;
2. eliminated ambient coordinates are not quotient obstructions.

Only the combination yields the correctly typed result.

## Next falsifier

Recompute the joint (x,y) first saturation with the repaired packets, then parameterize the exact kernel solver for the global Fitting/rank-jump stratification.

Ledger sequence claim: `seqclaim-ef5503b5e63f829a5a6cc940`.
