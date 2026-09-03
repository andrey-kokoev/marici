# Sharp two-grade Green return margin

## Question

When primitive and square grades genuinely mix, what is the exact replacement for impossible one-way triangularity of the positive normalized Green return?

## Positive return

On the strict two-grade plane, write the positive self-adjoint normalized return as

\[
K=
\begin{pmatrix}
a&z\\
\bar z&b
\end{pmatrix},
\qquad
0\le K.
\]

Positivity requires

\[
a\ge0,
\qquad
b\ge0,
\qquad
|z|^2\le ab.
\]

The effective arithmetic form is \(I-K\). Strong survival of the arithmetic frame requires

\[
I-K>0,
\]

equivalently \(\|K\|<1\).

## Sharp criterion

By the two principal minors of \(I-K\), strict contraction holds exactly when

\[
a<1,
\qquad
b<1,
\qquad
|z|^2<(1-a)(1-b).
\]

The largest eigenvalue is

\[
\lambda_{\max}(K)
=
\frac{a+b+\sqrt{(a-b)^2+4|z|^2}}{2},
\]

so the exact return margin is

\[
\delta_{\rm ext}
=1-\lambda_{\max}(K).
\]

This criterion permits nonzero primitive-square mixing. It separates three failure mechanisms:

1. primitive diagonal saturation \(a\to1\);
2. square diagonal saturation \(b\to1\);
3. mixed return saturation \(|z|^2\to(1-a)(1-b)\).

## Why separate diagonal bounds are insufficient

Even with \(a,b<1\), the mixed entry can produce a unit eigenvalue. For

\[
a=b=\frac12,
\qquad
|z|=\frac12,
\]

one has \(|z|^2=(1-a)(1-b)\), and the eigenvalues are \(1,0\). Thus terminal cancellation occurs exactly at zero mixed slack.

Likewise, eliminating all mixing is unnecessary. The strict example

\[
a=\frac12,
\qquad
b=\frac13,
\qquad
|z|^2=\frac1{16}
\]

has positive mixed slack and a nonzero admissible cross-grade return.

## Uniform source target

For a prime-indexed physical family \(K_p\), the required theorem is not merely the pointwise inequalities. It is one uniform margin

\[
\inf_p
\left[
1-rac{a_p+b_p+\sqrt{(a_p-b_p)^2+4|z_p|^2}}{2}
\right]
>0.
\]

Equivalently, the diagonal deficits and mixed determinant slack must remain jointly separated from zero. Finite-cutoff positivity does not provide this infimum.

## Verification

`research/aspect/checkers/check_sharp_two_grade_return_margin.py` checks the exact principal-minor criterion on strict, unit-boundary, diagonal-failure, and mixed-failure rational cases.

## Disposition

Reverse triangularity is replaced by the sharp quantitative two-grade margin. The physical source audit must now compute three normalized quantities \((a_p,b_p,|z_p|^2)\). Without the physical return constructor, these remain undefined; no parity or filtration theorem supplies them.
