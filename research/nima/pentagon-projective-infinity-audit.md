# Projective-infinity audit for cyclic pentagon forms

## Question

Does absence of a pole on the projective line at infinity select the reference pentagon slice from its common-Jacobian rivals?

## Claim boundary

The cancellation below applies to every cyclic five-tuple of affine facet functions. It says nothing about positivity, boundedness, source selection, or physical normalization.

Write `a_i=c_i+p_i x+q_i y` and pass to the projective chart

\[
x=z^{-1},\qquad y=wz^{-1}.
\]

Then `a_i=l_i(w,z)/z` and

\[
dx\wedge dy=-z^{-3}dz\wedge dw.
\]

For the cyclic logarithmic form, the possible residue on `z=0` is

\[
-\sum_i\frac{\det(v_i,v_{i+1})}
 {l_i(w,0)l_{i+1}(w,0)}\,dw.
\]

Let `l_i(w,0)=p_i+q_iw`. Each scalar summand satisfies

\[
\frac{\det(v_i,v_{i+1})}{l_i l_{i+1}}
=\frac{d}{dw}\log\frac{l_{i+1}}{l_i}.
\]

The cyclic sum telescopes identically, so the apparent `dz/z` pole cancels. This does not require equal Jacobians. Removing the closing cyclic term leaves a symbolic nonzero residual, verifying that closure—not positivity or the reference fan—is the operative condition.

The homogenized facet hyperplanes still meet the infinity line at isolated projective points. Those intersections belong to the closures of the facet divisors; the result only excludes the infinity line itself as an additional pole divisor.

## Disposition

Absence of an infinity-divisor pole is generic cyclic algebra. Combined with interval boundary recursion it still leaves the affine fan and support moduli unresolved, so these canonical-form properties cannot supply source selection.
