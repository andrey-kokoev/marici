# The Li pair is a spectral norm exactly on the critical line

## Exact conditional identity

For a nontrivial zero parameter `rho`, put

`u(rho)=1-1/rho=(rho-1)/rho`.

The functional-equation partner `1-rho` contributes the inverse multiplier
`u(rho)^(-1)`. Their contribution to the `n`th Li coefficient is

`2-u^n-u^(-n)`.

If `rho=1/2+i gamma`, then `|u|=1`, so `u^(-1)=conj(u)` and

`2-u^n-u^(-n)=|1-u^n|^2`.

Summing over critical-line pairs gives the familiar conditional spectral norm
interpretation of Li positivity.

## Exact circularity residual

For `rho=sigma+i gamma`, direct calculation gives

`|u(rho)|^2-1=(1-2 sigma)/(sigma^2+gamma^2)`.

Thus the unitary feature used in the squared norm exists exactly when
`sigma=1/2`. Declaring this spectral expression to be a norm before deriving
unitarity would insert the critical line and therefore beg the RH question.

## Source-side target

Gate C requires a different construction: vectors `v_n` must be obtained
from the theta/prime--gamma source correspondence before the zero fibres are
known, and their Gram values must then be proved equal to the Li coefficients.
The conditional spectral formula specifies the required completed answer but
is not itself the source factorization.

The smallest useful next test is to derive the first several `v_n` from one
uniform source operation and compare their Gram matrix with the derivatives
of `log xi` at `s=1`. Separate fitted vectors for individual `n` do not count.

## Scope

This packet proves the conditional pair identity and identifies its exact
circularity residual. It does not construct source-side Li vectors, prove Li
positivity, or prove RH.
