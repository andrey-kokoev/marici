# The unshifted inverse-n barrier is falsified by signed defect

## Question

Does the truncated Weibull recurrence satisfy

\[
\varepsilon_n\le
\frac1{n+1}-\frac{r_n}{n-1},
\]

as required by the exact \(1/n\) Riccati barrier?

No on the precision-controlled finite grid. A 520-digit calculation through degree sixteen gives negative slack

\[
\varepsilon_n^*-\varepsilon_n<0
\]

at every tested degree. For \(n=8,\ldots,16\), the scaled slack \(n^4(\varepsilon_n^*-\varepsilon_n)\) decreases from \(-0.4154\) to \(-0.4656\), consistent with a nonzero negative fourth-order coefficient.

This does not contradict the observed increase of \(n|P_n(0)|\). The unshifted barrier was sufficient, not necessary: the actual Riccati ratio can remain above \((n-1)/n\) using positive margin accumulated at finite index even when the map sends the exact barrier slightly below itself.

## Disposition

Reject `weibull-critical-defect-barrier`. The next leaf is `weibull-shifted-inverse-barrier`: test comparison profiles

\[
u_n^{(\kappa)}=\frac1{n+\kappa}
\]

and determine a source-compatible \(\kappa\) whose critical defect dominates the Weibull defect with signed margin.

## Claim boundary

Finite negative slack does not prove eventual failure, but its stable \(n^{-4}\) scale falsifies using the available asymptotics to assert the unshifted barrier.
