# Two-setting conditioning gate

Work package: WP578  
Owner: marici.Figueiredo

## From identification to robust calibration

WP577 proves that an invertible two-setting design \(X\) identifies a local
affine detector transport through \(K=YX^{-1}\). Exact invertibility is not a
robustness certificate. If the calibrated response has error \(E\), then

\[
\widehat K-K=EX^{-1},
\qquad
\|\widehat K-K\|_2
\le {\|E\|_2\over\sigma_{\min}(X)}.
\]

The design singular value is therefore part of the physical calibration
contract.

## Smallest near-collinear hostile

Take

\[
X_\varepsilon=
\begin{pmatrix}
1&1\\
0&\varepsilon
\end{pmatrix},
\qquad
\det X_\varepsilon=\varepsilon\ne0.
\]

Let a completed-record calibration error affect only the second setting,

\[
E=(0\ \delta w),
\qquad
\mathbf1^Tw=0.
\]

Then

\[
EX_\varepsilon^{-1}
=
(0\ {\delta\over\varepsilon}w).
\]

Thus the reconstruction-error norm is amplified exactly by
\(1/|\varepsilon|\). At \(\varepsilon=1/10\), a response error of scale
\(1/100\) creates a transport error of scale \(1/10\). The design is exactly
identifiable and practically fragile.

## Optimal frozen geometry

Freeze the total two-setting energy

\[
\operatorname{tr}(X^TX)=2.
\]

If the singular values are \(s_1\ge s_2\ge0\), then
\(s_1^2+s_2^2=2\), so \(s_2\le1\). Equality requires
\(s_1=s_2=1\), equivalently \(X^TX=I\). Orthogonal equal-norm settings
therefore maximize the worst calibrated direction and attain
\(\sigma_{\min}(X)=1\).

This optimality is conditional on the frozen Euclidean source metric and
energy budget. Detector cost, source feasibility, support, or asymmetric
uncertainty can change the optimal design and must be declared before response
data are examined.

## Portal consequence

The two invariant portal perturbations required by WP577 must be chosen with a
published source metric, feasible setting domain, and lower confidence bound
on \(\sigma_{\min}(X)\). After transport reconstruction, WP568--WP569 must be
applied again to the composed response with detector and interface uncertainty.

The design is an instrument compiler, not a selector or rigidifier. It
descends under the weak-basis groupoid only when its metric and perturbations
are defined on invariant \((r,q)\) coordinates. A reference exposure port may
be part of the detector metric, but it does not repair a near-collinear source
design.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp578_two_setting_conditioning_gate.py

The generated result is
`research/flavor/results/wp578_two_setting_conditioning_gate.json`.
