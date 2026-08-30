# Global contour closure for the rational Li test cone

## Universal decay

For every polynomial `p`, the rational-square test satisfies

`R_p(s)=-p(1)^2/s^2+O_p(s^(-3))`

as `s` tends to infinity away from the finite endpoints. The leading decay
is independent of `deg(p)`. If `p(1)=0`, the decay improves further.

This follows by `u(s)=1-1/s=1+O(1/s)`,
`u(s)^(-1)=1+O(1/s)`, and
`1/[s(1-s)]=-s^(-2)+O(s^(-3))`. The exact checker verifies the expansion for
generic polynomials through degree eight.

## Absolute divisor convergence

All nontrivial completed-zeta zeros lie in a fixed vertical strip, and the
standard counting estimate is

`N(T)=O(T log T)`.

Since `R_p(rho)=O_p(|rho|^(-2))`, dyadic summation gives

`sum_(|Im rho|>T) |R_p(rho)| = O_p(log(T)/T)`.

Thus the divisor evaluation is absolutely convergent, including
multiplicities. No symmetric summation convention is needed for this
rational-square class.

## Contour identity

Choose expanding rectangles whose horizontal sides avoid zero ordinates and
on which the standard logarithmic-derivative bounds for completed xi hold.
The `s^(-2)` test decay beats the boundary length and logarithmic growth of
`xi'/xi`, so the boundary integral tends to zero. The residue theorem then
gives

`sum_rho R_p(rho)`

` = -Res_0(R_p xi'/xi)-Res_1(R_p xi'/xi)`.

This is the full-divisor sum. Because `R_p(1-rho)=R_p(rho)`, the Li Toeplitz
energy normalized by functional pairs is half of it:

`E(p)=1/2 sum_rho R_p(rho)=-Res_0(R_p xi'/xi)`.

Accordingly the canonical endpoint residue functional is the global divisor
functional on this cone.

## Proof-status boundary

The algebraic decay and dyadic implication are elementary. A publication
proof must cite or reproduce the precise zero-counting and zero-avoiding
logarithmic-derivative estimates used to select the contours. This packet
records the reduction and does not claim those classical analytic estimates
were reproved here.

## Consequence for the attack

Endpoint admissibility and divisor convergence no longer supply adjustable
choices. The remaining hard theorem is exactly positivity of this fixed
completed-xi residue functional on every rational square `R_p`, derived from
the arithmetic source side rather than from the zero divisor.
