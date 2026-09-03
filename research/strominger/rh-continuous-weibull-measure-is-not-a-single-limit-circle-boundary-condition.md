# The continuous Weibull measure is not a single limit-circle boundary condition

## Question

Can the selected continuous truncated Weibull measure be identified with one self-adjoint Weyl boundary parameter of the limit-circle Jacobi operator?

No. The measure

\[
d\nu_X(x)=\mathbf 1_{[X,\infty)}e^{-2x^{1/4}}dx
\]

has strictly positive density on every nonempty interval inside \([X,\infty)\), hence is non-atomic. In an indeterminate Jacobi moment problem, the spectral measure of a single canonical self-adjoint extension is an extremal representing measure; such measures are discrete. Therefore \(\nu_X\) cannot be the spectral measure of one constant boundary parameter.

The moment sequence of \(\nu_X\) still determines the Jacobi coefficients and the polynomial solution from its finite-index initial conditions. Different representing measures with the same moments produce the same polynomial recurrence. Consequently the coefficient of the \(p=-1\) asymptotic branch is a connection coefficient of that fixed polynomial solution, not a choice made by selecting one continuous representing measure at the limit-circle endpoint.

A continuous representing measure may instead be described through a generalized resolvent or a nonconstant Nevanlinna parameter, but that representation adds no branch-selection shortcut: the polynomial connection problem remains.

## Disposition

Reject `weibull-weyl-boundary-coefficient` as a single-boundary-parameter construction. The next leaf is `weibull-polynomial-connection-coefficient`: construct a normalized asymptotic basis for the recurrence and express the polynomial solution’s \(p=-1\) coefficient as a discrete Wronskian limit.

## Claim boundary

This does not determine whether that coefficient vanishes. It corrects the type of object that must be computed.
