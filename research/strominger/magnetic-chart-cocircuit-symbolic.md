# The even magnetic cocircuit holds at every grade

Companion to `checkers/magnetic_chart_cocircuit_symbolic_checks.py` (8/8,
exit 0) and `results/magnetic_chart_cocircuit_symbolic.json`.

Fix an even grade (g\ge2) on the chart divisor

\[
q=2g+8,qquad k=\frac g2+4,qquad a_{\max}=g+8.
\]

The two reflected branches at pole depth (a) have target supports

\[
I_-(a)=[-a-g,-a+1],
\qquad
I_+(a)=[g+8-a,2g+9-a].
\]

Since admitted pole depths are nonnegative and even, only one column from
each branch can meet target rows (0,1):

\[
(a,m)=(0,-3g-7)quad\text{on }I_-,
\qquad
(a,m)=(g+8,1)quad\text{on }I_+.
\]

All other columns vanish on both rows.  It therefore suffices to calculate
two endpoints.

For the minus endpoint (a=0), only the last path coefficient
(c_g=(4)^{\overline g}) survives.  Hence

\[
R_0=-(2g+7)(4)^{\overline g},
\qquad
R_1=-(3g+7)(4)^{\overline g}.
\]

For the plus endpoint (a=g+8,m=1),

\[
\frac{c_1}{c_0}=\frac{g(g+4)}{2g+7},
\]

and the first mixed path coefficient gives

\[
\frac{R_1}{R_0}
=2\frac{c_1}{c_0}+1-g
=\frac{3g+7}{2g+7}.
\]

The common reflection sign cancels in this ratio.  Thus every source column,
including those vanishing on both rows, obeys

\[
\boxed{(2g+7)R_1-(3g+7)R_0=0.}
\]

This proves the preferred-chart cocircuit for every even grade.  The chart
divisor is forced by support geometry: exactly at (a_{\max}=g+8), the two
opposite reflected endpoints become competing observations on rows (0,1)
with the same source-derived ratio.

## Scope

The theorem proves the cocircuit and hence vanishing of the preferred maximal
minor for all even (g\ge2).  It does not yet prove that the row-(3)
alternate minor is nonzero for arbitrary grade.  That remaining statement is
the invariant determinant-line continuation problem.
