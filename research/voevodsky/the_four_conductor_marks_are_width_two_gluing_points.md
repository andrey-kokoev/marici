# The four conductor marks are width-two gluing points

Let

\[
X=W-Q,
\qquad
Y=W+Q.
\]

Then the total-energy degeneration is locally expressed as

\[
XY=G_E-Q^2.
\]

At any of the four conductor points

\[
p_{\sigma\tau}:
\quad a=\sigma y h,
\quad b=\tau x h,
\qquad \sigma,\tau\in\{\pm1\},
\]

put \(h=1\), \(a=\sigma y+u\), and \(b=\tau x+v\). The conductor has linear equation

\[
Q_{\rm lin}=-2xy(\sigma u+\tau v).
\]

Its tangent can be parametrized by

\[
u=\tau s,
\qquad
v=-\sigma s.
\]

The quadratic leading term of the first smoothing coefficient restricts universally to

\[
\left.\partial_EG_E\right|_{E=0,\mathcal C}
=8xy(x+y)s^2+O(s^3).
\]

Thus the smoothing section has a **double zero** at each of the four marked points. After multiplication by units and analytic coordinate changes, the local model is

\[
XY=E s^2+	ext{higher }E\text{-order terms}.
\]

This is the geometric origin of width two. Generic points of the conductor have \(XY=E\), but the four marked points contribute \(s^2\), so their gluing cannot be represented by four unrelated ordinary nodes.

The sign dependence disappears after restricting to the oriented conductor tangent: all four points have the same local coefficient

\[
8xy(x+y).
\]

Hence their distinction is global—where they sit on the conductor and how paths pair them—not a local multiplicity or local orientation difference.

This also explains why local Picard--Lefschetz calculations repeatedly found identical width-two data while failing to determine the global two-bit class. The missing information lives in the resolution and global pairing of four identical \(XY=Es^2\) neighborhoods.

The next calculation is the explicit blow-up of this model and its integral specialization boundary matrix.

Certificate:

- `research/voevodsky/checkers/localize_four_conductor_smoothing_points.py`;
- `research/voevodsky/results/four_conductor_local_smoothing.json`.
