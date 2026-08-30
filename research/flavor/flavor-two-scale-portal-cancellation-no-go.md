# Two-scale portal cancellation no-go: WP689

## Affine comparison theorem

On the WP688 domain, the source-generated additive running coefficient (b)
is positive. Write the leading-log portal transport as

\[
\lambda_p(L)=a+bL,
\]

where (a) is an independent boundary value and (L) denotes an abstract physical
context coordinate.

At two distinct contexts (L_1,L_2), the response Jacobian is

\[
\frac{\partial(\lambda_p(L_1),\lambda_p(L_2))}
{\partial(a,b)}
=\begin{pmatrix}1&L_1\\1&L_2\end{pmatrix},
\qquad
\det=L_2-L_1.
\]

Thus a boundary term can cancel the response in one context but not in two
distinct contexts when (b\neq0).

## Uniform two-context floor

Optimizing over every boundary value gives

\[
\min_a\max
\left(|\lambda_p(L_1)|,|\lambda_p(L_2)|\right)
=\frac{b|L_2-L_1|}{2}.
\]

The optimum is (a=-b(L_1+L_2)/2), which leaves equal and opposite residuals.
This is an exact lower bound independent of the unknown boundary coupling.

## Corrected authority boundary

WP690 corrects the earlier interpretation of two renormalization-scale choices
as physical contexts. Changing the renormalization scale at fixed physical
momentum is a coordinate change and supplies only one physical record.
Algebraically the theorem removes the cancellation fiber only when (L_1,L_2)
label distinct source-authorized physical contexts, such as distinct momenta.
No calibrated pair of such measurements is currently admitted.

This is a complementary-probe theorem, not yet a physical instrument or a
numerical flavor selector.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp689_two_scale_portal_cancellation_no_go.py

Generated result: results/wp689_two_scale_portal_cancellation_no_go.json.
