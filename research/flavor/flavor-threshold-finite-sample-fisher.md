# Threshold finite-sample Fisher gate (WP371)

## Bounded statistical model

Let \(\gamma=1-2\beta>0\) be WP370's calibrated detector contrast. For \(N\)
independent effective samples, take per-channel statistical variance
\(\sigma^2/N\). Model an independently calibrated differential-background
uncertainty with variance \(\tau^2\) along \((1,-1)^T\). The record covariance
is

\[
\Sigma=\frac{\sigma^2}{N}I
+\tau^2
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\]

Its common- and difference-channel variances are respectively
\(\sigma^2/N\) and \(\sigma^2/N+2\tau^2\).

## Exact information determinant

Let \(J_{\mathrm{det}}\) be the WP369 threshold Jacobian composed with the
WP370 confusion matrix. The local Gaussian Fisher matrix for \((L,\Omega)\)
is

\[
F=J_{\mathrm{det}}^T\Sigma^{-1}J_{\mathrm{det}}.
\]

Its determinant is

\[
\det F=
\frac{N^2\gamma^2\mu^8}
{16(L^2+\Omega^2)^4\sigma^2(\sigma^2+2N\tau^2)}.
\]

It is strictly positive for finite admitted parameters and \(\gamma>0\).
Thus finite sample size and calibrated background uncertainty degrade
precision but do not create a contextual kernel.

At \(\tau=0\), information volume scales as \(N^2\gamma^2\). With a nonzero
calibrated differential floor, it scales only linearly in \(N\) asymptotically:
one eigenchannel continues improving while the other saturates.

## Unknown nuisance versus calibrated uncertainty

A fixed unknown differential background is different from a calibrated random
uncertainty. Adding its amplitude \(\delta\) as a third parameter produces a
two-by-three response Jacobian. Its rank is at most two, leaving a nontrivial
local kernel at one scan point. More samples at the same point do not remove
that structural ambiguity; an independent background control or additional
source-supported scan point is required.

## Disposition

The finite-sample detector remains locally faithful for the two pole
coordinates only under positive calibrated contrast and a declared covariance
model. This is an identification theorem, not flavor selection. The smallest
exact falsifier is \(\gamma=0\), where \(\det F=0\). The remaining instrument
gate is a justified likelihood, effective sample count, background support,
and scan design rather than covariance alone.

Run `uv run --with sympy python
research/flavor/checkers/wp371_threshold_finite_sample_fisher.py` to regenerate
the exact result.
