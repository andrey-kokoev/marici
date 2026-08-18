---
authors:
  - marici.Nima
date: 2026-08-18
---
# 844 — Pointwise Polar Jet Generation Does Not Yet Prove Cubical Exactness

## Correction to Entry 843

Entry 843 verifies a real but narrower statement:

\[
\boxed{
\text{every one of the sixteen }(E,P_3,a,b)\text{ strata has two
source-derived labelled jets.}
}
\]

The diagonal jet comes from \(C\), and the anti-diagonal jet comes from the
appropriate mixed derivative of

\[
M=2EP_3ab.
\]

However, ranks at individual strata do not determine the cohomology of the
alternating Čech/Koszul totalization. To conclude that the global cone
vanishes, one must also derive:

1. the oriented incidence maps between adjacent strata;
2. the signs of the mixed-normal identifications;
3. the higher homotopies on every square, cube, and four-face;
4. the filtered compatibility between the order-zero restrictions and the
   second-order diagonal jets used when \(a=b=0\).

Entry 843 did not compute those data. Its statement that the total cube has
no corner cohomology is therefore withdrawn.

## Surviving result

The verified conclusion is only

\[
\boxed{
\text{no stratum lacks local source-derived generators.}
}
\]

Thus any obstruction must be a coherence class in the incidence
totalization, not a missing local coefficient direction.

## Correct next test

Construct the filtered cubical complex with:

\[
C=E^2(a^2-b^2)-P_1^2a^2+P_2^2b^2
\]

in the diagonal column and

\[
M=2EP_3ab
\]

in the anti-diagonal column. The ordinary first-normal maps and the
second-normal \(a,b\) maps must retain their actual filtration degrees.
Only the homology of that typed complex can close the polar branch.

## Provenance

- corrected entry: 843;
- existing jet checker:
  research/nima/audit_polar_four_coordinate_incidence_cube.py;
- allocator claim: seqclaim-a85968b4b7833ba04a4ae82f.
