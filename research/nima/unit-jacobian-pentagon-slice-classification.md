# Classification of common-Jacobian pentagon slices

## Question

Does requiring every cyclic dlog term to have one common pullback Jacobian select the five-point associahedral slice?

## Claim boundary

The classification concerns affine facet gradients up to a chosen `GL(2)` frame and common scale. It does not classify bounded support constants or establish an ABHY/source-selected slice.

Normalize the first two gradients to `v0=(1,0)` and `v1=(0,1)`, so their determinant is one. Solving

\[
\det(v_i,v_{i+1})=1
\]

cyclically gives the generic two-parameter family

\[
\begin{aligned}
v_2&=(-1,a),\\
v_3&=\left(\frac{1-b}{ab-1},\frac{1-a}{ab-1}\right),\\
v_4&=(b,-1),
\end{aligned}
\]

for `ab != 1`. On `ab=1` the equations are inconsistent except at `a=b=1`, where they collapse to `u+v=-1` and give a degenerate exceptional family. The previously used gradients are the member `a=b=0`.

Therefore equal cyclic Jacobians do not select one pentagon fan. After quotienting by coordinate frame and common scale, two gradient moduli remain. Facet constants add independent support data; translation removes two combinations, leaving the affine shape parameters that determine whether the positive intersection is a bounded pentagon.

For any admitted member with common determinant `J`,

\[
\sum_i d\log a_i\wedge d\log a_{i+1}
 =J\,m_5(a(x,y))\,dx\wedge dy.
\]

A coordinate change rescales `J`; it does not select the gradient moduli or support constants.

## Disposition

Unit Jacobians explain a normalization once a slice is declared, but they do not derive the slice. Source selection must independently provide the affine fan and support constants, such as an ABHY-type constraint map. Treating the reference member as canonical without that map would insert positive geometry.
