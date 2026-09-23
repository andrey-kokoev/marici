# Y0-stabilizer covariance does not supply bosonization

For any ambient right action `W=[[L,M],[0,R]]∈SL(6)`, the plane `Y0=[0|I2]` is preserved. In its chart `Y=[U|I2]`, the transformed chart coordinate is `U'=(UM+R)^-1 U L`. Setting `H=UM+R`, direct differentiation gives `dU'=H^-1 dU (L-MU')`. Its row-major target eight-coordinate Jacobian is

    det(dU'/dU) = det(H)^-4 det(L-MU')^2 = det(H)^-6,

using the block determinant `det(L-MU')=det(W)/det(H)` and `det W=1`. Hence the SAME global eight-form, if it exists, transforms as `ω_U(U';ZW)=det(H)^6 ω_U(U;Z)` and at sourced `Y0` scales as `det(R)^6`. The sixth power independently agrees with the previously audited first-pivot/last-pivot chart exponent. Exact eight-by-eight derivative at a nonzero rational `U` verifies the determinant; nontrivial rational `W` with nonzero upper-right `M`, `det(R)=1/2` gives sheetwise Jacobian multiplier 64 and complete two-sheet density multiplier 1/64 for BOTH distinct positive rank-six Y0 witnesses.

This establishes exact covariance along a high-dimensional orbit of rank-six positive external data, not merely an isolated value. Its boundary is sharp: every external six-bracket of the rank-four body `Z=(z,φη)` is zero, while `SL(6)` preserves the nonzero positive ordered six-brackets of the witnesses. No invertible constant ambient transformation in this family reaches the nilpotent bosonization locus. Formal continuation of a GLOBAL rational target coefficient, with denominator cancellation checked in the relevant local ring, remains necessary before the sourced Berezin operation.

Checker: `research/nima/checkers/check_four_mass_Y0_parabolic_covariance.py`; result: `research/nima/results/four-mass-Y0-parabolic-covariance.json`.
