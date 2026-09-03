# High-order frequency refinement enters the Arb radius

## Question

Does fixed-spatial-grid frequency refinement reduce the aligned rank-\(25\) Schur-entry change below the \(10^{-5}\) Arb perturbation radius?

## Claim boundary

Yes empirically. At fixed spatial order \(700\), both successive high-order frequency comparisons are below \(10^{-5}\), and the finest comparison is below \(10^{-6}\). This satisfies the numerical acceptance test but is not an analytic quadrature remainder bound.

## Refinement results

From frequency order \(2800\) to \(3600\), the maximum aligned entry change is

\[
2.14385\times10^{-6},
\]

with spectral-norm change

\[
9.17991\times10^{-6}.
\]

From order \(3600\) to \(4400\), the maximum entry change is

\[
8.22456\times10^{-7},
\]

with spectral-norm change

\[
1.09547\times10^{-6}.
\]

The aggregate \(2800\)-to-\(4400\) maximum entry change is

\[
2.22302\times10^{-6}.
\]

The common-grid basis overlap has minimum singular value above \(0.9999999999991\), and orthogonality errors remain below \(9\times10^{-13}\).

## Comparison with the interval matrix radius

Arb \(LDL^*\) proves the target margin for arbitrary independent entry perturbations of radius \(10^{-5}\). The finest observed frequency increment is smaller by a factor greater than twelve. Previously isolated spatial changes are below \(4.1\times10^{-7}\).

## Residual

Successive Gauss--Legendre differences are empirical convergence evidence, not enclosures of the integral remainder. They also do not certify the concentration eigenvectors. A promotion requires a theorem bounding the continuum-minus-order-\(4400\) frequency quadrature error and the continuum-minus-order-\(700\) Nyström projection error, with their sum below \(10^{-5}\) entrywise.

## Disposition

The numerical resolution now fits inside the Arb matrix-algebra radius. The only remaining first-prime certification defect is the missing analytic enclosure arrow from continuum operators to the computed interval matrix. Positivity and RH are not promoted.

## Verification

- `research/voevodsky/checkers/scout_aligned_schur_entry_difference.py`
- `research/voevodsky/results/aligned_schur_entry_difference.json`
