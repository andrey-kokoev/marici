# The Nyström scout rejects the forty-times-leakage certificate

## Problem

Does the sufficient finite form

\[
G=PAP-40\left(PA^2P-(PAP)^2\right)
\]

remain positive on the threshold concentration subspace?

## Bold conjecture

The coarse inverse bound \(C^{-1}\leq40Q\) might already be sharp enough to certify the first-prime finite block.

## Named rivals

1. The factor \(40\) overestimates the exact tail resolvent enough to destroy an otherwise positive Schur complement.
2. Frequency truncation creates the negative directions.
3. Spatial Nyström resolution or the concentration nullspace creates the negative directions.

## Risky consequences

The conjecture predicts a nonnegative least eigenvalue stable under spatial refinement and increased frequency cutoff. A valid discretization also requires

\[
PA^2P-(PAP)^2\geq0.
\]

## Strongest falsification attempt

The projection was selected by the proved threshold \(\lambda>1/130\), not by taking \(190\) numerically unresolved modes. All runs selected rank \(25\), with stable separating values

\[
\lambda_{25}\approx0.0315675,
\qquad
\lambda_{26}\approx0.00532731.
\]

At cutoff \(150\), increasing the spatial and frequency quadratures from \((320,1000)\) to \((400,1400)\) changed the least eigenvalue only from approximately

\[
-8.6023151
\]

to

\[
-8.6023335.
\]

Both runs had exactly two negative eigenvalues. At cutoff \(250\), the least eigenvalue remained negative at approximately

\[
-7.381245
\]

with two negative eigenvalues. The leakage matrix was positive semidefinite up to roundoff in every run; its least reported values were between \(-3.3\times10^{-16}\) and \(-2.2\times10^{-15}\).

The cutoff-\(100\) positive value is not stable under enlargement of the frequency window and is rejected as truncation evidence.

## Exact residual

The scout does not include the infinite frequency tail and is not interval certified. It therefore does not prove that \(G\) has a negative eigenvalue. However, the matched cutoff-\(150\) refinements eliminate concentration-nullspace and spatial-resolution instability as explanations at displayed precision. The surviving residual is two negative directions in the coarse sufficient form.

## Disposition

The conjecture that the universal factor \(40\) suffices is rejected at the numerical-scout level. This does not refute local Weil positivity: failure of \(G\geq0\) is inconclusive because

\[
40BB^*
\]

is only an upper bound for the exact Schur correction. The next discriminating object is a sharper tail-resolvent estimate or a converged approximation to

\[
F-BC^{-1}B^*.
\]

The finite compression itself remains encouraging but non-evidential: the reported least eigenvalue of \(PAP\) was positive in every run. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/scout_finite_schur_nystrom.py`
- `research/voevodsky/results/finite_schur_nystrom.json`
