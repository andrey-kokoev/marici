# A latent log-time measure positively completes every squarefree cube

Let `(Omega,mu)` be a probability space and let each visible prime direction
carry a real feature `x_j(u)` with `|x_j(u)|<=1`. Given diagonal energy `D>0`,
define the correlation attached to a squarefree subset `S` by

```
f(S) = D integral_Omega product_(j in S) x_j(u) dmu(u). (1)
```

The convolution kernel `K(a,b)=f(a+b)` on `(C2)^d` is positive
semidefinite. Indeed, its Walsh eigenvalues are

```
lambda_eta
 = D integral_Omega product_j [1+(-1)^(eta_j)x_j(u)] dmu(u) >= 0. (2)
```

Every factor in the integrand is nonnegative. This is an exact positive
completion theorem, not a numerical criterion.

## Log-time specialization

For `u>=0`, choose

```
x_p(u)=p^(-u).                                          (3)
```

Then

```
f(S)=D integral (product_(p in S)p)^(-u) dmu(u).        (4)
```

The mixed coefficient at `{p,q}` is a continuous-sector correlation
`D integral (pq)^(-u)dmu(u)`. It is not a von Mangoldt atom and does not
contradict `Lambda(pq)=0`. Shared `u` generally makes it different from the
independent product `f({p})f({q})/D`.

This geometry is suggested directly by the gamma resolvent bridge:

```
1/(a+iT/2)=2 integral_0^infinity e^(-2au)e^(-iTu)du,
```

and the digamma sum produces the positive formal density
`2e^(-u/2)/(1-e^(-2u))du`. At any bounded cutoff
`epsilon<=u<=R`, normalizing that density gives exactly a measure of the form
used above, so its squarefree mixed correlations are automatically positive.

## The remaining source obstruction

The cutoff theorem does not prove completed Weil positivity. The digamma
density diverges like `1/u` at `u=0`; its finite part is tied to polar and
endpoint subtractions. The prime-power term enters the completed logarithmic
derivative with a negative sign. Consequently one may not normalize the
uncut gamma density as a probability measure and then append primes as an
orthogonal positive sector.

The next exact gate is therefore narrower:

> Show that the common endpoint finite part and the negative prime evaluation
> maps arise as a Schur compression of a positive latent-scale dilation.

Such a dilation would generate the needed mixed correlations without
inventing squarefree arithmetic support. A failure of positivity after the
same endpoint subtraction on any finite prime cube is the corresponding
finite falsifier.
