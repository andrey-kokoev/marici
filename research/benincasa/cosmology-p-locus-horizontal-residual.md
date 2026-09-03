# The E6/qtop comparison is not horizontal on p=0

Conjecture: the actual principal divisor supports the horizontal comparison.

The radial inverse gives
`p/X1=1+X2/X1+3*X3/X1=2u-v`, so `p=0` is `v=2u` and `dv=2du` on the divisor.
Pulling back the exact E6-minus-`q_top` residual gives numerator
`-4u^6+18u^5-8u^4-45u^3+66u^2-36u+8` over
`D(u,2u)*u*(u-2)*(u-1)`.

At the regular point `(u,v)=(3,6)`, the two residual components are `95/69`
and `-93/92`; the pulled coefficient is `-89/138`. The conjecture is
falsified.

The primitive cyclic map remains an algebraic associated-grade comparison, but
not a horizontal one on the target divisor. The next test asks whether the
one-variable residual is the logarithmic derivative of an admissible rational
gauge.
