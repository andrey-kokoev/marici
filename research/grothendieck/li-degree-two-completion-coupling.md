# Degree-two positivity is carried by completion cross-terms

## Canonical germ split

Write

`log xi(1+t)=constant+E(t)+G(t)+P(t)`,

where

`E(t)=log(1+t)` is the endpoint germ,

`G(t)=-(1+t)log(pi)/2+log Gamma((1+t)/2)` is archimedean,

and

`P(t)=log(t zeta(1+t))` is the Abel-renormalized prime germ.

Let the first three Taylor coefficients of these germs be vectors `e,g,p`,
so the completed jet vector is `a=e+g+p`.

## First two channels

The reflection-odd channel is linear:

`A_2(a)=a_1-a_2-3a_3/2`.

The coupled determinant is the quadratic form

`D_2(a)=a_1^2+a_1a_2+3a_1a_3/2-2a_2^2`.

Therefore

`D_2(e+g+p)=D_2(e)+D_2(g)+D_2(p)`

` +B(e,g)+B(e,p)+B(g,p)`,

where the polarization is

`B(x,y)=2x_1y_1+x_1y_2+x_2y_1`

`       +3(x_1y_3+x_3y_1)/2-4x_2y_2`.

This identity is exact. The checker evaluates its six pieces at high
precision to expose their signs and scales.

## Interpretation rule

No self-piece or cross-piece is separately invariant under arbitrary
redistribution of analytic germs. Here the split is admitted only because
endpoint, gamma, and `log(t zeta(1+t))` were fixed independently by the
completed factorization and Abel pole cancellation.

The purpose is diagnostic, not to claim that each component is an observable
positive energy. If the small positive total results from cancellation among
large mixed-sign pieces, then any proof based on separate coarse lower bounds
is structurally mismatched. A viable proof must preserve the polarization
coupling or find a new identity that packages it as a square.

The numerical values in the result are reconnaissance without interval
certification. The polarization formula itself is exact.
