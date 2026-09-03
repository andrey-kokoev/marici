# Exact transport theorem for the five-vertex path

## Question

Which inequalities characterize flow on \(P_0-D_0-P_1-D_1-P_2\)?

## Claim boundary

For nonnegative supplies and demands, flow exists exactly when

\[
p_0+p_1\geq d_0,
\qquad p_1+p_2\geq d_1,
\qquad p_0+p_1+p_2\geq d_0+d_1.
\]

Equivalently, the minimum central supply required by the two endpoint deficits obeys

\[
\max(0,d_0-p_0)+\max(0,d_1-p_2)\leq p_1.
\]

In the endpoint-deficit regime \(d_0\geq p_0\), \(d_1\geq p_2\), central-exhausting allocations form

\[
[d_0-p_0,\;p_1+p_2-d_1].
\]

Its width is the collective Hall slack, and its midpoint uniquely equalizes endpoint residuals. Exhaustive testing covers 7,776 integer parameter tuples, including 1,232 feasible endpoint-deficit cases. Separate deliberate failures witness necessity of each cut class.

## Disposition

This theorem is source-independent and reusable, but it proves nothing about decomposing larger Gale cut graphs into path cells. The next test should census fixed-eight minimal two-demand cuts: determine whether every irreducible cell is a five-vertex path in the endpoint-deficit regime or record the first larger topology.
