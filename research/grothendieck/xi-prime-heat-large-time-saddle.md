# Large-time saddle: PNT cancels endpoint growth but not the spectral scale

## Continuum prime model

Replace the von Mangoldt measure by its prime-number-theorem main density
`dpsi(x)~=dx`. The prime heat kernel becomes

`K_prime^cont(t)`

` =-1/(2sqrt(pi t)) integral_1^infinity`

`   x^(-1/2) exp(-(log x)^2/(4t)) dx`.

With `u=log x`, the exponent is `u/2-u^2/(4t)` and its saddle is at `u=t`,
so the dominant arithmetic scale is `x~=exp(t)`.

The Gaussian integral is exact:

`K_prime^cont(t)`

` =-exp(t/4)[1+erf(sqrt(t)/2)]/2`.

## Endpoint cancellation

Adding `K_endpoint(t)=exp(t/4)` gives

`K_endpoint+K_prime^cont`

` =exp(t/4)erfc(sqrt(t)/2)/2`

` ~1/sqrt(pi t)`.

Thus the PNT main term explains the cancellation of exponential endpoint
growth. It does not produce the exponentially decaying spectral heat trace.

## Scale gap

If the first positive ordinate is `gamma_1`, the true conditional heat trace
has large-time scale

`Theta(t)~m_1 exp(-gamma_1^2 t)`.

The continuum PNT remainder is only algebraic before further gamma and
arithmetic cancellations. Even classical zero-free-region PNT errors, when
sampled at the saddle `x=exp(t)`, are vastly larger than
`exp(-gamma_1^2t)`.

Therefore a direct proof of completed heat positivity for all large `t`
cannot follow from ordinary PNT error bounds. It requires information at the
same scale as the zero spectrum—unsurprising because the statement is
RH-equivalent.

## Explanatory use

This does identify a robust first cancellation mechanism:

- the endpoint pole supplies `exp(t/4)`;
- the mean prime density supplies the matching negative `exp(t/4)` saddle;
- gamma and prime fluctuations determine the much smaller completed heat
  trace.

A successful explanation must organize those fluctuations as a positive
squared-spectrum measure, rather than estimate them independently by size.

## Falsifiers

- Claiming ordinary PNT error bounds suffice for all-time positivity.
- Truncating primes below the moving saddle `n~=exp(t)`.
- Comparing order-one or algebraic errors to the exponentially small heat
  trace without certified cancellation.
- Treating the continuum main term as the completed heat kernel.
