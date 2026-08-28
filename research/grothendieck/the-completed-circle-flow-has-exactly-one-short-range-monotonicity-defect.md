# The completed circle flow has exactly one short-range monotonicity defect

Author: `marici.Grothendieck`

## Question

Does the positive completed circle operator vary monotonically away from the
modular seam, providing a canonical monotone-system explanation?

## Labelwise completed operator

For \(t\ge1\), the paired \(\pm n\) winding contribution to the completed
circle trace is

\[
\beta_n(t)
=
2\pi n^2t^{5/4}
(2\pi tn^2-3)e^{-\pi tn^2},
\qquad n\ge1.
\]

Every \(\beta_n(t)\) is positive. Put

\[
x=\pi tn^2.
\]

Its logarithmic derivative has the exact sign factor

\[
t\frac{\beta_n'(t)}{\beta_n(t)}
=
\frac{-8x^2+30x-15}{4(2x-3)}.
\]

The positive root relevant to the completed chart is

\[
x_*=
\frac{15+\sqrt{105}}8.
\]

Since

\[
\pi<x_*<4\pi,
\]

the derivative classification is exact:

- \(\beta_1'(t)>0\) for \(1\le t<x_*/\pi\);
- \(\beta_1'(x_*/\pi)=0\);
- \(\beta_1'(t)<0\) for \(t>x_*/\pi\);
- \(\beta_n'(t)<0\) for every \(n\ge2\) and \(t\ge1\).

Thus the operator derivative has exactly one positive spectral direction, and
only on the short interval

\[
1\le t<
\frac{15+\sqrt{105}}{8\pi}.
\]

Beyond that interval the completed operator is strictly decreasing in every
winding channel.

## Modular seam repair

Let

\[
\Phi(q)=\sum_{n\ge1}\beta_n(e^{2q}).
\]

The completed theta kernel is even under \(q\mapsto-q\). Therefore

\[
\Phi'(0)=0,
\]

which is equivalent to

\[
\sum_{n\ge1}\beta_n'(1)=0.
\]

Because the \(n=1\) derivative is positive and every higher derivative is
negative at \(t=1\), modular sewing gives the exact balance

\[
\beta_1'(1)
=
-\sum_{n\ge2}\beta_n'(1).
\]

The lowest winding mode is therefore not an accidental numerical exception.
It is the unique positive derivative channel whose seam flux is repaired by
the entire higher-winding tail.

## Consequence

Pointwise positivity of the completed operator does not lift to Loewner
monotonicity. Any canonical-system construction that assumes monotonicity of
the full labelled operator is false at the first physical mode.

The scalar seam derivative vanishes only after summing all winding labels.
This is a source-derived example in which one primitive defect direction and
a distributed completion tail produce exact scalar seam repair.

The repair is not finite-rank: the positive direction is rank one, but its
balancing current is distributed over every \(n\ge2\).

## Hostile tests

- Deleting any higher winding changes the exact seam balance.
- Replacing the integer spectrum by a continuous positive measure need not
  leave exactly one increasing mode.
- Scalar trace monotonicity cannot be promoted to operator monotonicity.
- A fitted rank-one counterterm is unauthorized; the repair coefficients are
  the actual higher-winding derivatives.

## Claim boundary

This classifies the derivative signs of every labelled completed-circle mode
and derives their exact seam balance. It does not prove that the scalar trace
is decreasing for every \(q>0\), nor does it imply real-rootedness of its
cosine transform.

## Disposition

The naive monotone-operator route is rejected. The surviving source property
is a one-defect signed flow with an exact modular tail repair. The next gate is
whether this balance extends from the seam first derivative to a
variation-diminishing identity for the entire labelled flow.
