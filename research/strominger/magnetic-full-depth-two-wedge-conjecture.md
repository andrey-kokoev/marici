# The consecutive-depth current cokernel has two width-two wedges

For the hostile consecutive-depth extension with native source parameter
\(\beta=4\), the stable current quotient appears to have dimension

\[
W_{g,q}=
\begin{cases}
2,&q\ge2g+1,\\
2,&g\ge4\text{ and }\min(3,g-3)\le q\le g-3,\\
1,&\text{otherwise}.
\end{cases}
\]

This classification passes 220 exact rational-rank cases over
\(2\le g\le12\), \(1\le q\le20\), using consecutive depths through
\(N=30\).

## Two failure mechanisms

The width-two locus is not one exceptional curve.

The high-excess wedge

\[
q\ge2g+1
\]

is consistent with branch separation: reflected route supports are too far
apart for the available local path relations to identify their current
classes.

The low wedge

\[
\min(3,g-3)\le qle g-3
\]

lies inside the overlap region. Its second class must therefore arise from
collision degeneracy, not geometric separation. For \(g\ge6\), this becomes

\[
3\le qle g-3.
\]

Between these wedges, the quotient is one-dimensional and all consecutive
current classes sew to one intrinsic class.

## Prediction for the local minor

A correct local Fitting determinant should have two qualitatively different
failure factors:

- a support-separation factor controlling the high wedge;
- a collision factor controlling the low wedge.

They should not be compressed into one unexplained polynomial zero set.

The present statement is a bounded exact conjecture. An unbounded proof still
requires a fixed-size local reduction of the augmented packet
\([M\mid K_0\mid K_1]\).

Replay with: python research/strominger/checkers/magnetic_full_depth_two_wedge_checks.py