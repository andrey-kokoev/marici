# Radius-stabilized common-clock cofiber: WP1061

## Question

Does WP790's curvature--flux radius stabilization calibrate WP1060's common
parent clock?

## Joint clock law

WP790 gives the stabilized radius

\[
R_*^2=\frac{3An^2}{2B}.
\]

WP1060's half-twist level-zero clock is

\[
M^2=\frac{1}{4R_*^2}.
\]

Composing them gives

\[
M^2=\frac{B/A}{6n^2}.
\]

Therefore the desired unit clock requires the exact joint condition

\[
\frac BA=6n^2.
\]

## Exact cofiber

The bounded hostile packet is:

\[
\begin{array}{c|c|c|c}
n & B/A & R_*^2 & M^2\\
\hline
1 & 6 & 1/4 & 1\\
1 & 12 & 1/8 & 2\\
2 & 24 & 1/4 & 1\\
2 & 6 & 1 & 1/4
\end{array}
\]

Thus radius stabilization alone does not calibrate the clock. Both
\((n,B/A)=(1,6)\) and \((2,24)\) give \(M^2=1\), while nearby sectors give
\(2\) or \(1/4\). Flux reflection \(n\leftrightarrow-n\) leaves the radius and
clock unchanged.

## Boundary

The next source must derive the flux sector and gauge--gravity ratio from the
same compactification. Only then is the common parent clock absolute. A
physical momentum port must still supply \(p^2/M^2\) in this frame.

## Classification

Conditional radius-clock cofiber. It reduces the absolute-clock blocker to one
exact joint quantization condition, \(B/A=6n^2\), without selecting its
solution.

Checker: `research/flavor/checkers/wp1061_radius_stabilized_common_clock_cofiber.py`

Result: `results/wp1061_radius_stabilized_common_clock_cofiber.json`
