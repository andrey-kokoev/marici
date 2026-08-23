# Complex theta saddle critical-value reconnaissance

## Search object

For the completed source, saddle degeneracy is equivalent to

\[
N(u):=\Phi(u)\Phi''(u)-\Phi'(u)^2=0.
\]

At a zero with \(\Phi(u)\ne0\), its critical parameter is

\[
z=-\frac{\Phi'(u)}{\Phi(u)}.
\]

The labelled derivative recurrence was evaluated only after summation into
the completed jets. Newton searches used a dense seed grid in

\[
0\leq\Re u\leq1.5,\qquad 0.025\leq\Im u\leq0.725,
\]

inside the natural series strip \(|\Im u|<\pi/4\).

## First two critical values

The nearest candidate lies on the imaginary source axis:

\[
u_0\approx0.4152735637211994\,i,\qquad
z_0\approx5.701318127533996\,i.
\]

It belongs to the critical boundary \(\Re z=0\).

The first candidate mapping into the open outer quadrant is

\[
u_1\approx0.23586044848965584+0.5575783460166387\,i,
\]

\[
\boxed{z_1\approx0.47991051323739475+9.62457962286267\,i.}
\]

Its image in the Pick variable is

\[
t_1=z_1^2\approx-92.40221881610758+9.23787389300439\,i,
\qquad |t_1|\approx92.8628470175391.
\]

This is far beyond the existing certified central disk \(|t|\leq8.5\).

## Stability checks

For \(u_1\):

- the relative curvature-numerator residual is \(6.03\times10^{-16}\);
- \(|\Phi(u_1)|\approx11.4028\);
- \(|N'(u_1)|\approx70167.9\), so the root is numerically simple; and
- label cutoffs 28 and 36 give identical displayed critical values.

The denser grid found ten candidates. None maps to an open-quadrant critical
value with smaller \(|z|\) than \(z_1\).

## Interpretation

This is evidence for a large nondegenerate saddle chart, not a proof of one:

- the Newton search does not certify the number of roots;
- no argument-principle enclosure was performed;
- a Stokes transition can occur without saddle degeneracy; and
- common-phase and thimble-barycenter conditions remain unchecked.

The first observed outer collision is at \(|t|\approx92.86\), not near the
current certified disk.

## Next gate

1. Use the argument principle on a complex-\(u\) rectangle to certify that no
   zero of \(N\) was missed below the first outer candidate.
2. Trace steepest-descent phases from the positive Mellin contour to detect
   any earlier Stokes equality.

Either an omitted critical value or an earlier Stokes equality is the sharp
falsifier.

## Boundary-winding upgrade

A numerical argument-principle audit was run on two rectangles with
`0.001<=Re(u)<=1.5` and `0.001<=Im(u)<=h`. For `h=0.55`, the winding number is
zero at 400, 800, and 1,600 points per edge. For `h=0.60`, it is one at all
three resolutions. The minimum normalized boundary modulus remains above
`0.00264`, while the maximum adjacent phase increment falls below `0.37`
radians at the finest resolution.

This topologically isolates the first outer candidate between the two upper
edges, subject to numerical evaluation. It is not a certified argument-
principle enclosure because transcendental and boundary interpolation errors
have not been bounded.

Artifacts:

- checkers/theta_complex_log_curvature_roots.py
- results/theta-complex-log-curvature-roots.json
- checkers/theta_curvature_argument_principle_scan.py
- results/theta-curvature-argument-principle-scan.json
