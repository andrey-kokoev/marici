# The first-order completion Green identity makes the odd coupling a boundary operator

## First-order factors

Set

\[
A_+=\partial_u+\frac12,
\qquad
A_-=\partial_u-\frac12.
\]

On a common smooth core,

\[
\langle A_+f,g\rangle
+
\langle f,A_-g\rangle
=
\left[f\overline g\right]_{-\infty}^{+\infty}.
\]

The \(\frac12\) terms cancel in the interior. Therefore the connection coefficient does not produce a bulk channel exchange \(\frac12Q\).

This rejects the previous candidate as a source theorem: the shared numerical factor \(1/2\) belongs to the diagonal first-order factors, not to an off-diagonal bulk coupling.

## Boundary factorization

Let

\[
\operatorname{Tr}f
=
\begin{pmatrix}
f(-\infty)\\
f(+\infty)
\end{pmatrix}.
\]

The Green boundary form is

\[
\left[f\overline g\right]_{-\infty}^{+\infty}
=
\langle\operatorname{Tr}f,
\Omega\operatorname{Tr}g\rangle,
\qquad
\Omega=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

After the even-odd Hadamard transform, \(\Omega\) becomes off-diagonal. Thus reciprocal orientation is a finite boundary interaction between wall and jump ports.

The source odd operator must factor as

\[
J
=
\operatorname{Tr}_-^{*}
\,\Omega\,
\operatorname{Tr}_+,
\]

with the appropriate twisted trace maps and metric adjoints.

## No dark bulk coupling

This factorization immediately gives

\[
Jf=0
\]

for every history with zero relative traces. Hence the hidden-bulk hostile disappears: the odd coupling has finite rank through the two-dimensional boundary space.

Endpoint compression now does determine the entire odd operator, but only because the Green identity proves boundary factorization.

## Contraction estimate

Let

\[
C_-=
\|\operatorname{Tr}_-S_-^{-1/2}\|,
\qquad
C_+=
\|\operatorname{Tr}_+S_+^{-1/2}\|.
\]

Then

\[
\|S_-^{-1/2}JS_+^{-1/2}\|
\le
C_-C_+\|\Omega\|.
\]

Strict auxiliary positivity reduces to a trace inequality

\[
C_-C_+\|\Omega\|<1
\]

after all source coefficients and endpoint metrics are included.

Unlike the rejected \(\frac12Q\) model, this criterion is sensitive to the absolute graph-energy normalization.

## Theta compression

The exact theta columns fix the action of \(\Omega\) on the source trace plane:

\[
\left(\frac12,\frac12\right),
\qquad
\left(\frac14,-\frac14\right).
\]

Their even-odd ports determine the reciprocal sign, while the graph trace constants determine whether the boundary interaction is strictly dominated by the bulk even energy.

## Next calculation

Compute the optimal trace constants of the transported twisted graph norms, including the source endpoint weights. The auxiliary contraction problem is now finite-rank and no longer requires guessing a bulk causal operator.
