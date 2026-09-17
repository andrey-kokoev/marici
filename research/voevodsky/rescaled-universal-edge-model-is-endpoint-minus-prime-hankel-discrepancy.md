# The rescaled universal edge model is an endpoint--prime Hankel discrepancy

Let `N=e^{2L}` and consider the two endpoint layers

\[
x=-L+\delta s,
\qquad x=L-\delta t,
\qquad s,t\ge0,
\]

with the unitary rescaling `f(x)=delta^{-1/2}g_-(s)` on the left and similarly
`g_+(t)` on the right.

A prime-power shift `log n=2L-delta r` maps the left coordinate `s` to the
right coordinate

\[
t=r-s.
\]

Thus the edge-to-edge arithmetic term is a Hankel operator whose measure is

\[
d\mu_{N,\delta}(r)
=
\sum_{n\le N}
 \frac{\Lambda(n)}{\sqrt n}
 \delta_{(\log(N/n))/\delta}(dr).
\]

The endpoint rank-two term has leading cross contribution

\[
\delta\sqrt N\,
\Re\left(
 \overline{\int g_-(s)ds}
 \int g_+(t)dt
\right).
\]

On the other hand, replacing `d psi(x)` by its prime-number-theorem main term
`dx` gives

\[
\frac{d x}{\sqrt x}
=
\delta\sqrt N e^{-\delta r/2}dr.
\]

The resulting Hankel integral has the same leading rank-one term as the
endpoint contribution, with the opposite sign. Therefore the large
`delta sqrt(N)` pieces cancel. The universal rescaled edge operator is not the
single entering prime-power translation; it is

\[
\mathcal E_{N,\delta}
=
\text{endpoint main term}
-
	ext{Hankel}(d\mu_{N,\delta}),
\]

or, after subtracting the continuum density,

\[
\mathcal E_{N,\delta}
=
-\operatorname{Hankel}
\left(
 d\mu_{N,\delta}
-
 \delta\sqrt N e^{-\delta r/2}dr
\right)
+	ext{lower-order endpoint terms}.
\]

## Consequence for the proposed uniform proof

An isolated-prime edge estimate is not asymptotically valid: the endpoint term
on the pair of edges has norm of order `delta sqrt(N)`, and it is cancelled by
the aggregate of all prime powers in the logarithmic boundary layer.
Controlling the remaining Hankel discrepancy uniformly is a weighted short-
interval prime-number theorem problem.

An unconditional PNT remainder is insufficient after division by `sqrt x`:
its absolute error can still grow much faster than the logarithmic
archimedean confinement. Square-root-scale control of this discrepancy is of
the same strength as zero-free information on the critical line. Hence a
uniform positivity proof cannot be obtained by discarding signed prime
cancellation or by treating thresholds independently; that would hide the
central RH-equivalent arithmetic input.
