# Multiprecision collapse of sub-cutoff candidates

## Question

Do the eight WP529 sub-cutoff candidates stabilize as nonzero physical
couplings when the eigensystem is reconstructed independently at arbitrary
precision?

They do not. Every candidate tracks the eigensolver residual and collapses
toward zero as working precision rises.

## Independent reconstruction

WP530 rebuilds the explicit WP507 tangent matrix and WP508 canonical mass
matrix using arbitrary-precision arithmetic. It does not import the WP516 or
WP529 eigenvectors. The same eight ordered triples are evaluated at 50, 80,
and 120 decimal digits.

The largest candidate coupling at each precision is approximately

\[
4.68\times10^{-46},\qquad
2.27\times10^{-76},\qquad
1.45\times10^{-115}.
\]

The corresponding eigenpair residuals are approximately

\[
8.55\times10^{-50},\qquad
6.75\times10^{-80},\qquad
1.55\times10^{-119}.
\]

At each precision the largest candidate remains within \(10^4\) times the
eigenpair residual. It does not approach a precision-independent nonzero
value.

The summed candidate width collapses as

\[
1.76\times10^{-88},\qquad
4.14\times10^{-149},\qquad
1.69\times10^{-227}.
\]

Widths here are measured in GeV.

## Correction to WP529

WP529 correctly showed that double precision placed eight entries above its
chosen numerical-zero floor. Its provisional interpretation of them as
candidate channels is superseded by the multiprecision test.

The eight entries are numerical basis artifacts consistent with structural
zeros. Their apparent double-precision width sum of
\(3.13\times10^{-16}\) GeV is not a physical correction to WP517.

This is still a numerical collapse certificate, not a formal algebraic proof.
Arbitrary precision does not supply directed rounding, and exact zero is not
deduced merely from many leading zero digits.

## Structural route to exactness

Every collapsing triple contains two eigenstates from one four-generator
sector and one state from another sector. The WP508 mass matrix is exactly
block diagonal. The next checker can therefore decide the issue without
eigenvectors:

1. freeze the exact gauge-basis support of each WP508 block;
2. restrict the exact \(SU(3)_F\), \(SO(3)_P\), and \(SO(3)_E\) structure
   tensors to each candidate block triple;
3. prove the restricted tensor is identically zero;
4. infer that every mass-basis contraction vanishes for arbitrary rotations
   within those blocks.

This avoids the exact-degeneracy and small-gap basis problem entirely.

## Disposition

- Domain: the eight WP529 candidate triples.
- Result: all eight collapse with working precision and track solver error.
- Classification: corrective numerical collapse certificate, neither
  selector nor rigidifier.
- Width authority: the numerical census returns to the 34 WP517 channels.
- Smallest falsifier: one candidate stabilizes away from zero or its exact
  block-restricted structure tensor is nonzero.
- Remaining gate: prove exact block-support zeros, then promote the
  34-channel sum on WP527's nonquark-closed witness and transport it through
  WP525.

WP530 supersedes the candidate-channel interpretation of WP529 while
preserving WP529's lightweight reconstruction method.
