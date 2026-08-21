# The endpoint is reflection-positive but carries a forbidden negative-energy atom

The elementary completed endpoint heat term is

```
Theta_endpoint(t)=e^(t/4)=e^[-t(-1/4)].                (1)
```

As a bilateral Laplace atom, it has positive weight at

```
lambda_endpoint=-1/4.                                 (2)
```

Its ordinary time-addition kernel factors as

```
K_endpoint(s,u)
=e^[(t_0+s+u)/4]
=e^(t_0/4)e^(s/4)e^(u/4),                             (3)
```

so it is rank-one positive semidefinite. Ordinary reflection positivity alone
therefore permits spectral support on the negative real axis.

## Shifted-kernel rejection

The generator-shifted kernel is

```
K_endpoint^+(s,u)
=-partial_t e^[(t_0+s+u)/4]
=-(1/4)e^[(t_0+s+u)/4],                               (4)
```

which is negative semidefinite and already fails on every diagonal entry.
This is exactly the support condition: multiplying the atom by `lambda`
reveals `lambda_endpoint<0`.

Hence both kernels in the time-addition theorem are necessary:

- `K>=0` reconstructs a positive bilateral Laplace measure;
- `K^+>=0` forces that measure onto `[0,infinity)`, making the transform
  Stieltjes.

## Completed cancellation meaning

The endpoint atom cannot be discarded, because it is canonically paired with
the zeta pole and is essential to the exact source formula. Nor can it survive
as an orthogonal sector of the final positive generator. Gamma and prime terms
must couple with it before the shifted Gram is formed, canceling the forbidden
negative-energy contribution in the completed measure.

This gives an operator-level interpretation of the large-time endpoint--prime
cancellation: it is the removal of a rank-one negative generator direction.
Any proposed source factorization that treats the endpoint as an independent
positive summand can satisfy ordinary reflection positivity while failing the
actual Stieltjes/Hilbert--Polya support gate.

## Smallest hostile test

One time increment suffices. The ordinary `1x1` Gram value is positive, while
the shifted `1x1` value is negative. This is the smallest possible example
showing that positivity of `Theta`, or even of the full ordinary
time-addition kernel, does not imply a nonnegative spectral generator.
