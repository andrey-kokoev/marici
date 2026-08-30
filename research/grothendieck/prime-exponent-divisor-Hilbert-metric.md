# Prime-exponent coordinates give a canonical Hilbert metric for divisor pushforward

Fix finitely many primes and exponent caps. The corresponding Euler box is

```
E={product_p p^(a_p) : 0<=a_p<=K_p}.
```

Divisibility is coordinatewise order on the exponent vectors. For one chain
`0,...,K`, its zeta matrix is

```
L_(a,b)=1 if b<=a, and 0 otherwise.                    (1)
```

Its inverse is the first-difference matrix

```
D=L^-1,
(Df)_0=f_0,
(Df)_a=f_a-f_(a-1).                                   (2)
```

For the full Euler box,

```
B = tensor_p L_p,
B^-1 = tensor_p D_p.                                  (3)
```

Define the positive target metric

```
M_E=(B^-1)* B^-1
   =tensor_p (D_p* D_p).                               (4)
```

Then divisor pushforward is exactly unitary from the standard coefficient
space to the potential space equipped with `M_E`:

```
B* M_E B = I,
<Bf,Bg>_(M_E)=<f,g>.                                  (5)
```

For one prime-exponent chain, `D*D` is a tridiagonal positive discrete
Dirichlet metric. Thus the required correction is not diagonal in integer
sites, but it is nearest-neighbor in each prime valuation and factors as an
Euler tensor product.

## Coefficient--potential interpretation

On an Euler box, von Mangoldt coefficients and logarithmic potentials obey

```
B Lambda=log.
```

Equation (5) therefore gives the exact norm identity

```
||log||_(M_E)^2=||Lambda||_2^2.                        (6)
```

Möbius inversion is now the unitary inverse relative to this target metric,
even though it was not the adjoint under the naïve counting metric.

## What this repairs

This repairs the finite coefficient-side Hilbert structure without an
arbitrary polar square root. The metric is determined by incidence, positive,
and Euler-factorized. It also explains why no diagonal integer weighting
worked: the correct energy measures discrete differences along valuation
chains.

## Infinite and physical gates

The infinite prime/exponent limit is not automatic. It requires an incomplete
tensor-product reference vector or trace, convergence weights, and
compatibility with the archimedean factor. Moreover, (4) is an arithmetic
incidence metric, not the unavailable physical relative-chain pushforward.
Finally, no equality with the Hermitian Xi reflection-defect norm is yet
proved.

