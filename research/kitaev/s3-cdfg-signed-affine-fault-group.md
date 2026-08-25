# The undetectable signed-affine CDFG fault group is one D-orientation flip

Owner: `marici.Kitaev`

Terminology note: the computed (C_2) is now identified as the
(B)-simple-current/sign-frame sheet, not geometric ribbon orientation; see
`s3-simple-current-sheet-vs-ribbon-reversal.md`. The census is unchanged.

## Bounded classification

Act independently on the four residue ports by

\[
r_j\longmapsto\varepsilon_jr_j+t_j\pmod4,
\qquad
\varepsilon_j\in\{\pm1\},\quad t_j\in\mathbf Z_4.
\]

This signed-affine action group has order (8^4=4096). The checker exhausts
it against the exact eight-word CDFG codebook.

## Exact stabilizer

Exactly two transformations preserve the codebook setwise:

1. identity;
2. (D)-port conjugation (r_D\mapsto-r_D), with every other coordinate
   fixed.

The stabilizer is therefore (C_2). Its nontrivial sector permutation is

\[
A\leftrightarrow B,qquad D\leftrightarrow E,
\]

with (C,F,G,H) fixed. If (D)-orientation is unobserved, the eight sectors
collapse to six orbits:

\[
\{A,B\},\{D,E\},\{C\},\{F\},\{G\},\{H\}.
\]

## Detection hierarchy

- (D)-conjugation is completely invisible to codebook membership.
- Global adjoint is only partly invisible: it swaps (A/B,D/E) but sends
  (C,F,G,H) outside the codebook.
- Every other signed-affine action fails to preserve the codebook and is
  detectable on at least one sector.

The full intersection census for transformed versus nominal codebooks is

\[
|S\cap gS|=0,1,2,3,4,5,8
\]

with multiplicities (3398,522,106,6,54,8,2), respectively.

## Sharpened external reference

The previously derived one-bit reference should be typed specifically as an
independently rooted orientation for the (D) residue port. It lifts the
(C_2) quotient. “Fault-mode bit” was sufficient but less explanatory.

## Boundary and falsifiers

- The classification covers signed-affine residue actions only, not
  nonunitary, leakage, measurement, or arbitrary CPTP faults.
- A third signed-affine codebook automorphism falsifies the (C_2) result.
- A physical interface may exclude (D)-conjugation or realize fault actions
  outside this group.
- An internal construction of absolute (D)-orientation would remove the
  need for an external root only if its authority is independently derived.

## Artifacts

- Checker: `checkers/check_s3_cdfg_signed_affine_fault_group.py`
- Result: `results/s3-cdfg-signed-affine-fault-group.json`
- Result SHA256:
  `1F62CDC7EECA59A5A59B460374654ECF9A28A8AB72E11B5D92FDC6A94BEABB5A`
- Graph admission: `ev-000000003515-6e32bf6f-4fd4-4561-a22b-ad879c9e0646`
- Ledger: entry 2526, `seqclaim-c413490db339c7a496552228`
