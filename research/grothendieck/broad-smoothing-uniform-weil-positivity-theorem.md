# Sufficiently broad Gaussian smoothing is uniformly positive

Let `Theta(t,xi)` be the explicit completed shifted-Gaussian Weil kernel, with
variance `sigma=1/(4t)`. Then there exists `t_0>0` such that

```
Theta(t,xi)>0             for every 0<t<t_0 and xi in R. (1)
```

Equivalently, the Weil Gaussian smoothing threshold is finite.

## Uniform archimedean lower bound

Rescale the gamma integral by

```
u=y/sqrt(t),       z=sqrt(t) xi.
```

The vertical digamma asymptotic and a fixed compact lower bound give,
uniformly in `z`,

```
K_gamma(t,xi)
 >= log(1/t)/(8 sqrt(pi t)) - C/sqrt(t)                (2)
```

for some absolute `C` and all sufficiently small `t`. The key uniform fact is
that

```
J(z)=integral_R e^[-(y-z)^2] log|y| dy                (3)
```

has a finite global minimum: it is continuous, the logarithmic singularity
is integrable, and `J(z)->+infinity` as `|z|->infinity`. Thus translating the
broad Gaussian cannot evade the universal `-(1/2)log t` growth.

The `-log(pi)/(4sqrt(pi t))` term is absorbed into `C/sqrt(t)`. Since
`log(1/t)` diverges, the positive leading term eventually dominates every
archimedean constant.

## Uniform arithmetic and endpoint bounds

The endpoint satisfies

```
|K_endpoint(t,xi)|<=e^(t/4).                           (4)
```

The prime cosine is bounded by its zero character. For small `t`, the first
allowed displacement is `log 2`, and comparison with the corresponding
logarithmic integral yields

```
sup_xi |K_prime(t,xi)|
 <= C_1 t^(-1/2) exp[-c_1/t]                           (5)
```

for positive constants `C_1,c_1`. This is negligible relative to (2).
Combining (2)--(5) proves (1).

## Threshold consequence

Broad positivity, Gaussian-semigroup monotonicity, character coercivity, and
first-contact rigidity now give the following dichotomy:

1. the positivity threshold is zero, which is Weil positivity and hence RH;
2. a finite positive threshold exists and is attained at a finite double
   contact satisfying `Theta=partial_xi Theta=0`.

The active conjecture has therefore become a zero-contact exclusion theorem
for one explicit two-variable source function. This is still RH-equivalent;
the reduction is explanatory, not a proof.

## Proof-status note

The argument uses only standard uniform digamma bounds, the integrability of
`log|y|`, and elementary domination of the log-Gaussian von Mangoldt series.
A publication proof should record explicit constants and a concrete `t_0`.
No zero locations or RH assumption enter the broad-regime argument.
