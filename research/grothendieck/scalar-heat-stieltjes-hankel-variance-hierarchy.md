# Scalar heat derivatives obey coupled Stieltjes Hankel positivity

Define the alternating completed heat derivatives

```
D_k(t)=(-1)^k partial_t^k Theta(t).                    (1)
```

If the scalar Stieltjes/RH representation exists, then

```
D_k(t)=integral_[0,infinity) lambda^k e^(-t lambda)
        dmu(lambda).                                   (2)
```

For every order `r`, both Hankel matrices

```
H_r(t)=(D_(i+j))_(0<=i,j<=r),
H_r^+(t)=(D_(i+j+1))_(0<=i,j<=r)                     (3)
```

are positive semidefinite. They are Gram matrices of the monomials
`1,lambda,...,lambda^r` in `L2(e^(-t lambda)dmu)`; the shifted matrix inserts
the nonnegative multiplier `lambda`.

## First coupled inequalities

At order one,

```
D_0 D_2-D_1^2 >=0,
D_1 D_3-D_2^2 >=0.                                    (4)
```

The first is log-convexity of the completed heat trace. If
`nu_t=e^(-t lambda)dmu/D_0`, then

```
(D_0D_2-D_1^2)/D_0^2=Var_(nu_t)(lambda).              (5)
```

Consequently the effective squared spectral energy

```
E(t)=D_1/D_0=-partial_t log Theta(t)                  (6)
```

obeys

```
E'(t)=-Var_(nu_t)(lambda)<=0.                          (7)
```

This is the completed spectral analogue of the prime variance-dissipation
identity, but it is conditional on precisely the positive measure that RH
asks us to derive.

## Why signs alone are insufficient

All entries `D_k` can be individually nonnegative while a Hankel determinant
is negative. For example `D_0=1,D_1=1,D_2=1/2` violates the first inequality.
Thus finite derivative-sign checks discard correlations required of one
common spectral measure.

## Source formulation

Each `D_k` is already an explicit completed endpoint--gamma--prime Laguerre
sum. Substituting those expressions into (3) produces a nested nonlinear
source hierarchy. A negative principal minor at any `(r,t)` falsifies the
Stieltjes representation and RH. Positive finite minors remain necessary
only.

The first credible coupled scalar target is therefore not merely `D_1>=0`,
but

```
Theta(t) partial_t^2 Theta(t)-[partial_t Theta(t)]^2>=0 (8)
```

for every `t>0`, proved from the completed arithmetic formula. Equality would
force the tilted spectral measure to a single squared ordinate, incompatible
with the full Xi Weyl law; the actual target should be strict.
