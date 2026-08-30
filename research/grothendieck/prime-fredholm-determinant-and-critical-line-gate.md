# The Euler product is a prime Fredholm determinant only in its convergence half-plane

On `l2(primes)`, define the diagonal operator

```
P_s e_p = p^(-s)e_p.                                   (1)
```

For `Re s>1`, `P_s` is trace class and its Fredholm determinant is

```
det_F(I-P_s)=product_p (1-p^(-s)).                     (2)
```

Therefore

```
zeta(s)=det_F(I-P_s)^(-1).                             (3)
```

Expanding the logarithm gives

```
-log det_F(I-P_s)
 =sum_p sum_(k>=1) p^(-ks)/k,
d/ds log det_F(I-P_s)
 =sum_(n>=2) Lambda(n)n^(-s),                          (4)
```

equivalently `zeta'/zeta=-sum Lambda(n)n^(-s)`.

## Completed determinant architecture

Together with the even-oscillator identity, the completed function has, in
the common convergence region, the schematic factorization

```
xi(s)
 =elementary(s)
  /[det_zeta(A+s/2-1/4) det_F(I-P_s)],                 (5)
```

where `A` has spectrum `k+1/4` and
`elementary(s)=(1/2)s(s-1)pi^(-s/2)sqrt(2pi)` with the
normalization arranged according to the determinant convention.

This realizes both gamma and Euler factors as inverse auxiliary
determinants, but they are parameter-dependent determinant families, not a
single fixed Hilbert--Polya operator.

## Critical-line obstruction

At `Re s=1/2`, the prime operator is not even Hilbert--Schmidt:

```
||P_s||_HS^2=sum_p p^(-1)=infinity.                   (6)
```

It is certainly not trace class. Hence (2) does not define a Fredholm
determinant on the critical line. Analytic continuation of `zeta` cannot be
reinterpreted as silently continuing the same trace-class determinant.

Any determinant construction reaching the critical line needs a genuine
regularization or relative determinant that includes the prime,
archimedean, and endpoint counterterms together. It must prove
regularization independence and preserve the adjoint symmetry.

## Relation to the incidence metric

Expanding (4) over prime powers recovers the von Mangoldt coefficient system.
The prime-exponent Dirichlet metric supplies a finite Euler-box Hilbert
geometry for those coefficients. The unresolved task is to use that metric
to define a relative determinant whose logarithmic derivative analytically
continues (4) without assuming the desired zero geometry.

## Falsifier

A proposed critical-line Fredholm model fails if it uses `P_s=diag(p^-s)` on
ordinary `l2(primes)` and calls `det(I-P_s)` a Fredholm determinant at
`Re s=1/2`. Equation (6) rules this out.

