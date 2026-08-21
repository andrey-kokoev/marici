# Explicit archimedean heat kernel for the squared xi resolvent

## Archimedean resolvent term

Set `y=sqrt(x)` and `s=1/2+y`. The gamma and pi factors contribute

`G(x)=[psi(y/2+1/4)-log(pi)]/(4y)`

to the squared resolvent `B'(x)`.

Use the standard integral representation

`psi(z)=-EulerGamma`

` +integral_0^infinity [exp(-r)-exp(-zr)]/(1-exp(-r)) dr`.

Together with the square-root Laplace transform, this gives

`K_gamma(t)=1/(4sqrt(pi t)) * [`

` -EulerGamma-log(pi)`

` +integral_0^infinity`

`   [exp(-r)-exp(-r/4-r^2/(16t))]/[1-exp(-r)] dr ]`.

The apparent singularity at `r=0` is removable; its limiting integrand value
is `-3/4`.

## Completed source heat kernel

The three canonical pieces are now

`K_endpoint(t)=exp(t/4)`,

`K_prime(t)=-1/(2sqrt(pi t)) sum_n Lambda(n)n^(-1/2)`

`             *exp(-(log n)^2/(4t))`,

and `K_gamma(t)` above.

Their Laplace sum agrees with

`B'(x)=[xi'/xi(1/2+sqrt(x))]/[2sqrt(x)]`

initially for `x>1/4`, where the Euler product is valid and each transform is
controlled. Analytic continuation then identifies the completed expression.

## Pointwise RH-equivalent target

The source-positive Lévy-density conjecture becomes the explicit inequality

`K_endpoint(t)+K_gamma(t)+K_prime(t) >= 0`

for every `t>0`, together with the transform and continuation conditions.

If proved, the left side is the positive heat trace `Theta(t)`, its Laplace
transform is Stieltjes, and the complete-Bernstein program follows.

## Coupling behavior

Neither the endpoint nor gamma nor prime term should be interpreted alone:

- the endpoint term grows as `exp(t/4)`;
- the prime term is negative and has a moving large-time saddle;
- the gamma integral carries the archimedean completion needed for exact
  cancellation and the short-time Weyl law.

The next attack is to analyze this completed kernel directly, beginning with
small- and large-time asymptotics and hostile numerical sign searches under
controlled truncation error.

## Proof-status boundary

The transform normalization and digamma representation are exact classical
identities. The checker performs symbolic normalization and high-precision
sample regression; its numerical residuals are not interval-certified. A
full theorem must justify exchanging the Laplace, digamma, and prime sums and
must control analytic continuation.
