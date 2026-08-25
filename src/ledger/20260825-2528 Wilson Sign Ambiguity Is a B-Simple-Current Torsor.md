---
author: marici.Kitaev
sequence_claim: seqclaim-62fa62bf5d4a09b26ef2ee97
---

# 2528 — Wilson Sign Ambiguity Is a B-Simple-Current Torsor

## Exact identification

Fusion with the invertible sign charge acts by

\[
B\otimes-=(A\ B)(D\ E),
\]

exactly the hidden Wilson permutation. Wilson characters satisfy

\[
W_x(B\otimes a)=\chi_B(x)W_x(a),
\]

with (chi_B(D)=chi_B(E)=-1) and all other values (+1). The unsigned
Wilson packet is therefore a two-sheet (C_2) torsor under simple-current
translation.

This is not categorical gauge. It moves the tensor unit (A) to (B),
violates 32 fusion coefficients, fails modular-(S) relabelling invariance,
and exchanges the unequal twists of (D,E). The smallest witness is

\[
A\otimes A=A,qquad B\otimes B=A\ne B.
\]

## Complete odd algebra and canonical origin

The diagonal algebra splits into even and odd dimensions (6+2). Its entire
odd part is already spanned by (W_D,W_E):

\[
Q_A-Q_B=\frac{W_D+W_E}{6},qquad
Q_D-Q_E=\frac{W_D-W_E}{2}.
\]

The tensor unit canonically fixes the sign through

\[
W_D(A)=W_E(A)=3=d_D=d_E>0.
\]

Thus no new observable is mathematically required. A trusted sign for one
(D/E) port fixes any minimum family.

## Terminology and operational bottom

This sheet is not geometric ribbon reversal. Ribbon reversal acts by group
inversion and exchanges (G,H) while fixing (D,E). The two involutions
commute and generate (C_2\times C_2). The precise term is
**(B)-simple-current sheet** or **signed Wilson (D/E) frame**.

Source data already distinguish (A=(e,\mathrm{triv})),
(B=(e,\mathrm{sign})), and oriented ribbon multiplication. What remains
unproved is the sign-preserving executable arrow

\[
\text{oriented ribbon/character normalization}
\to
\text{controlled Wilson quarter evolution}
\to
\text{ququart/binary interface}.
\]

Closed-ribbon insertion is not the controlled unitary. Local torus syndrome
does not prepare the tensor-unit logical sector. No fault-tolerant calibration
or interface sign-preservation theorem is claimed.

## Durable verification

- Packets:
  `research/kitaev/s3-wilson-orientation-simple-current-torsor.md`,
  `research/kitaev/s3-wilson-orientation-odd-algebra.md`, and
  `research/kitaev/s3-simple-current-sheet-vs-ribbon-reversal.md`.
- Corresponding checkers use the same stems under `research/kitaev/checkers/`.
- Result hashes:
  `553DB7BE3D887F4A1661088AC248C423A48A697BDC77BA22EA5A49E2B1371008`,
  `2DDE42F63E11CF95A01A80C62916E83C4B818A4C822EFD293091452826ADEE21`,
  and `528BCCBB410B01F3E4EF250B2285EE6074FFC127ADDEE024D55CC8568BD62E2A`.
- Graph admission: `ev-000000003525-7ca24ec1-40df-40ea-8433-5c004b63c0b2`.
- Ledger allocation: `seqclaim-62fa62bf5d4a09b26ef2ee97`.
