# Aligned entry convergence misses the Arb radius at current resolution

## Question

Do the two cutoff-\(250\) discretizations agree entrywise within the \(10^{-5}\) Arb perturbation radius after their concentration bases are aligned?

## Claim boundary

No. Common-grid Procrustes alignment is numerically well conditioned, but the largest aligned Schur-entry difference is about \(1.02\times10^{-4}\), ten times the certified radius. Eigenvalue stability therefore does not yet imply entrywise enclosure.

## Alignment test

The rank-\(25\) Nyström eigenfunctions from the \((480,1800)\) and \((560,2200)\) calculations were extended to a common 700-point Gauss grid. The overlap matrix had minimum singular value

\[
0.99999999999994,
\]

and both common-grid orthogonality errors were below \(1.4\times10^{-12}\). Thus subspace mismatch and failed alignment are not visible at displayed precision.

After polar alignment, the maximum entry difference was

\[
1.01657\times10^{-4},
\]

and the spectral-norm difference was

\[
4.16643\times10^{-4}.
\]

## Disposition

The current pair does not fit inside the Arb-certified uniform entry radius \(10^{-5}\). This is a failed acceptance test, not evidence against positivity: both aligned matrices remain positive above the target margin. The next test separates spatial Nyström error from frequency quadrature error by varying each resolution independently before another joint refinement.

## Verification

- `research/voevodsky/checkers/scout_aligned_schur_entry_difference.py`
- `research/voevodsky/results/aligned_schur_entry_difference.json`
