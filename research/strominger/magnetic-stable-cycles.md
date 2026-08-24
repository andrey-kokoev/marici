# Stable magnetic transport is banded, not globally triangular

The triangular theorem for the even alternate-chart core does not extend
literally to every reflection component.

For `q=1`, the preferred Hall minor has a unique determinant term throughout
the tested stable range.  This is the interval/endpoint regime.

For every tested `q>=2`, an alternating support cycle appears already at the
first stable pole-depth step.  The smallest example is

\[
(g,q,k)=(2,2,3).
\]

On columns `(a,sigma)=(2,-),(4,+)` and observations `-4,-3`, its local block is

\[
\begin{pmatrix}
-30&60\\
-10&100
\end{pmatrix}.
\]

Both perfect-matching terms are nonzero:

\[
(-30)(100)=-3000,
\qquad
(60)(-10)=-600,
\]

and the minor is

\[
-3000-(-600)=-2400\ne0.
\]

This is partial cancellation without rank loss.  At the first `q=3` cycle,
the corresponding Leibniz contributions reinforce instead.  Hence raw sign
positivity is parity- and chart-dependent, while nonvanishing is the invariant
question.

The corrected architecture is therefore

\[
\text{ordered interval filtration}
+\text{ finite-width alternating cycles}
+\text{ oriented local transfer}.
\]

Hall endpoints still prevent new support deficiency.  What they do not do is
make the full matrix triangular once `q>1`.  Higher magnetic depth genuinely
retains a bounded overlap state, and its alternating cycles are precisely where
the determinant-orientation theorem must act.

The checker is an exact bounded falsifier, not an all-parameter theorem.  It
tests `q=1..8`, grades through 12, and pole cutoffs through 9.
