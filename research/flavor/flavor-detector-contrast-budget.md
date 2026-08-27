# Detector contrast budget: WP699

## Pointwise contrast is not uniform faithfulness

WP698 gives the ideal branch rate ratio

\[
\rho(t)=\left(\frac{t-1}{t+1}\right)^2.
\]

Its ideal contrast is

\[
C(t)=1-\rho(t)=\frac{4t}{(t+1)^2}.
\]

This is positive for every finite \(t>0\), but tends to zero as \(t\to0\) or
\(t\to\infty\). Pointwise branch separation therefore does not imply a
uniformly faithful instrument over the unrestricted source domain.

## Compact-support detector budget

Assume the source independently supplies the reciprocal support bound

\[
\frac1T\leq t\leq T,
\qquad T\geq1.
\]

Then the exact uniform contrast floor is

\[
C_{\min}=\frac{4T}{(T+1)^2}.
\]

For a declared detector model with common efficiency \(\epsilon\), ideal
positive-branch signal \(S\), common background \(B\), per-yield absolute
error \(\eta\), and residual branch-differential background uncertainty
\(\beta\), the common background cancels and robust separation requires

\[
\epsilon S C_{\min}>2\eta+\beta.
\]

Equivalently,

\[
S>
\frac{(2\eta+\beta)(T+1)^2}{4\epsilon T}.
\]

## Authority boundary

WP699 is an exact conditional detector budget, not a calibration and not a
selector. The compact bound on \(t\) must come from the complete source rather
than the desired discrimination. The common efficiency and background model
must be replaced by a calibrated channel response including widths, loops,
resolution, and correlated uncertainties.

The smallest exact falsifier is absence of finite source support: as
\(T\to\infty\), the uniform contrast floor vanishes.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp699_detector_contrast_budget.py

Generated result: results/wp699_detector_contrast_budget.json.
