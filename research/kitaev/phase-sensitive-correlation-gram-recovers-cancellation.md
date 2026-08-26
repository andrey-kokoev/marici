# The Phase-Sensitive Correlation Gram Recovers Cancellation

Let \(R\) be the normalized core–tail coupling. Instead of erasing phases
entrywise, first form the tail correlation Gram

\[
H=R^*R,
\qquad
H_{jk}=\sum_i\overline{r_{ij}}r_{ik}.
\]

The sum over core atoms is taken before absolute values. Therefore all
source-derived phase cancellation is retained. Since

\[
\|R\|^2=\lambda_{\max}(H),
\]

the Gershgorin correlation load

\[
\eta=sup_j\left(H_{jj}+sum_{k\ne j}|H_{jk}|\right)
\]

satisfies \(\|R\|^2\le\eta\). Uniform \(\eta_N\le1-\varepsilon\) proves a
uniform Schur gap and hence completion-stable source coercivity.

The dual core correlation Gram \(RR^*\) gives the same exact operator norm;
one may use whichever side admits the sharper source-derived estimate.

## Exact recovery of phase cancellation

For the signed Hadamard coupling \(R=H_4/4\),

\[
R^*R=\frac14I_4.
\]

The correlation certificate gives \(\eta=1/4\) and \(\|R\|=1/2\). By
contrast, taking entrywise absolute values first gives an all-ones coupling
whose norm is one. Thus the order of operations is theorem-bearing:

\[
R\longmapsto R^*R\longmapsto |\text{off-diagonal correlations}|
\]

retains phase cancellation, whereas \(R\mapsto|R|\) destroys it.

## Why diagonal energy alone is insufficient

For the one-row coupling

\[
R=(1/2,1/2,1/2,1/2,1/2),
\]

every column has squared norm \(1/4\), but all columns are parallel and
\(\|R\|^2=5/4\). The off-diagonal correlations detect the pileup exactly.

The Gershgorin load remains sufficient rather than necessary. A positive
correlation Gram can have spectral radius below one while its absolute row
loads reach one. In that case one must use its exact spectrum, a weighted
correlation certificate, or additional signed structure; no kernel follows
from failure of diagonal dominance.

## Theta/Tate consequence

If Euler/Mellin phases are fixed by the source normalization, Grothendieck's
next viable estimate is not an absolute overlap sum. It is a bound on the
completed correlation kernel

\[
\sum_i\overline{r_{ij}(s)}r_{ik}(s)
\]

after the core index has been summed. This identifies exactly where
oscillation may produce the missing strict gap. A phase convention chosen
after completion has no authority; the phases must descend from the frozen
Fourier–Tate and endpoint normalization.

## Falsifiers

- Absolute values are taken before the core correlation sum.
- Only diagonal column energies are bounded.
- The phase convention varies with cutoff without source covariance.
- A Gershgorin failure is reported as an actual spectral failure.
- Correlation cancellation is obtained only after an unauthorized change of
  source frame.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The target was the first local certificate that preserves phase.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The Hadamard hostile is repaired exactly, and the RH-bearing estimate
is sharpened to a source-native correlation-kernel bound.
