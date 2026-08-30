# The raw scale derivative also loses the theta trace angle

## Candidate jet

After raw translates become asymptotically collinear, the next candidate is the scale jet

\[
c'(L)=\partial_L c(L),
\]

paired with the translated trace column

\[
c(L)=
\begin{pmatrix}
M_-(L)\\
M_+(L)
\end{pmatrix}.
\]

For the half-line theta tail, write

\[
c(L)=a(L)
\begin{pmatrix}
1\\
1+\varepsilon(L)
\end{pmatrix},
\qquad
\varepsilon(L)=O(e^{-2L}).
\]

The dominant theta exponent is

\[
x_L=\pi e^{2L},
\]

and the exact negative moment asymptotic implies

\[
\partial_L\log a(L)
=
-2x_L+O(1).
\]

Also

\[
\varepsilon'(L)=O(e^{-2L})=O(x_L^{-1}).
\]

Therefore

\[
c'(L)
=
a'(L)
\left[
\begin{pmatrix}
1\\
1+\varepsilon(L)
\end{pmatrix}
+
\frac{a(L)}{a'(L)}
\begin{pmatrix}
0\\
\varepsilon'(L)
\end{pmatrix}
\right].
\]

The transverse correction relative to the dominant ray is only

\[
\frac{\varepsilon'(L)}
{\partial_L\log a(L)}
=
O(x_L^{-2})
=
O(e^{-4L}).
\]

Hence the normalized scale jet and normalized value column satisfy

\[
\angle\bigl(c(L),c'(L)\bigr)
=
O(e^{-4L}),
\]

and their two-column smallest singular value tends to zero.

## Consequence

Differentiating a rapidly decaying translated tail is dominated by differentiating its scalar amplitude. The raw scale derivative therefore does not create a completion-stable second trace direction. It is even more tightly aligned with the endpoint-localized ray than two separated translates.

A scalar normalization applied after differentiation does not repair the angle. One would have to remove the amplitude connection first:

\[
\nabla_L c
=
c'
-
(\partial_L\log a)c.
\]

This covariant derivative isolates the shape variation, but the coefficient \(\partial_L\log a\sim-2\pi e^{2L}\) is large and source-dependent. Introducing it merely to force transversality would be circular.

## Source-authority gate

A renormalized scale jet is admissible only if the source constructor independently supplies:

1. a canonical line metric or connection on the translated theta ray;
2. the corresponding covariant derivative;
3. compatibility with reciprocal reflection and wall subtraction;
4. a uniform norm for the residual shape direction.

Without this data, neither raw translation nor raw scale differentiation supplies the second relative trace coordinate.

## Remaining minimal route

The first non-circular candidate is now a genuinely reciprocal two-sided packet. It must retain information from the opposite theta tail rather than repeatedly localizing at the same half-line endpoint. Its two trace columns should be tested before any Schur or positivity construction.
