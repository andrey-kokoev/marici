# The observed flavor ratio is compatible with the t-purity stationary point

Entry 2092 showed that the first two purity limits are hierarchy-forced,
while the third retains a nontrivial dependence on

\[
r=s_{13}/s_{23}.
\]

At fixed OBS17 central inputs and on the stable strict-ray window
\(s_{23}=10^{-4}\), directed one-dimensional optimization gives

\[
r_*=0.0882338,
\qquad
F_t(r_*)=0.99152496,
\qquad
F_t''(r_*)=-22.38.
\]

Independent propagation of the quoted \(V_{ub},V_{cb}\) errors gives

\[
r_{\rm obs}=0.0898305,
\qquad
\sigma_r=0.00272585,
\qquad
\frac{|r_{\rm obs}-r_*|}{\sigma_r}=0.586.
\]

Thus the measured ratio is compatible with the stationary point at one
standard deviation. This promotes extremization of the derived physical
purity function to a viable selector conjecture.

It is not yet a selection theorem. The calculation holds the remaining
inputs fixed, ignores their covariance, and does not derive an operation
whose equations of motion extremize \(F_t\). Moreover the maximum is
strictly below one, so exact purity is not the law.

Verification:

    python research/nima/checkers/check_flavor_t_valley_stationarity.py

The dependency-free checker passes 5/5.
