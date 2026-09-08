# Five-point associahedral slice and form dimension

## Question

Which two-dimensional slice turns the five-channel Laurent weighted sum into a candidate pentagon canonical form, and where do its Jacobians enter?

## Claim boundary

The following affine slice has pentagon combinatorics and unit facet Jacobians. It is not claimed to be selected by scattering sources, positive geometry, or a physical normalization theorem.

In the five-dimensional channel space choose

\[
a_0=x,\quad a_1=y,\quad a_2=1-x,\quad
 a_3=\tfrac32-x-y,\quad a_4=1-y.
\]

Equivalently impose three affine constraints

\[
a_0+a_2=1,\qquad a_1+a_4=1,\qquad
 a_0+a_1+a_3=\tfrac32.
\]

The positive region `a_i>=0` is the pentagon with vertices

\[
(0,0),(1,0),(1,\tfrac12),(\tfrac12,1),(0,1).
\]

For the cyclic compatible pairs `(0,1),(1,2),(2,3),(3,4),(4,0)`, every oriented gradient determinant

\[
\det\frac{\partial(a_i,a_j)}{\partial(x,y)}
\]

equals one. Therefore

\[
\sum_{(i,j)}d\log a_i\wedge d\log a_j
 =\left(\sum_{(i,j)}\frac1{a_i a_j}\right)dx\wedge dy.
\]

Thus the Laurent weighted sum is the scalar coefficient of the logarithmic pentagon form after pullback to this slice. The equality would fail or acquire term-dependent Jacobians on a generic two-plane.

## Disposition

The prior five-channel top-form candidate was overdimensional for associahedral geometry. A declared codimension-three affine slice repairs the dimension, and its unit Jacobians explain when the weighted sum becomes a form coefficient. The remaining authority question is whether these affine constraints and constants arise from the ABHY/source construction rather than being chosen to fit the desired form.
