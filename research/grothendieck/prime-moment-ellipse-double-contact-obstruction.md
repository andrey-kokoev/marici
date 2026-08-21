# Prime moment geometry constrains every Gaussian double contact

For fixed `t>0`, put

```
c_n(t)=Lambda(n)n^(-1/2) exp[-(log n)^2/(4t)] >= 0,
M_j(t)=sum_(n>=2)c_n(t)(log n)^j.                       (1)
```

Define the prime cosine value and sine derivative moment

```
R(t,xi)=sum_n c_n cos(xi log n),
I_1(t,xi)=sum_n c_n log(n) sin(xi log n).              (2)
```

All moments converge at positive `t`.

## Moment ellipse

Weighted Cauchy--Schwarz gives

```
I_1^2 <= M_2 sum_n c_n sin^2(xi log n).                (3)
```

Weighted Jensen gives

```
sum_n c_n sin^2(xi log n)
 <= M_0-R^2/M_0.                                       (4)
```

Therefore every prime character lies in the exact ellipse

```
R^2/M_0^2 + I_1^2/(M_0 M_2) <= 1.                    (5)
```

This uses only positivity of the von Mangoldt coefficients after common
Gaussian smoothing. No independence of prime phases is assumed.

## Substitution of the contact equations

Write the completed source kernel as

```
Theta(t,xi)=A(t,xi)-C(t)R(t,xi),
C(t)=1/(2sqrt(pi t)),                                  (6)
```

where `A=K_endpoint+K_gamma`. Since
`partial_xi R=-I_1`, a double contact requires

```
R=2sqrt(pi t) A,
I_1=-2sqrt(pi t) partial_xi A.                         (7)
```

Combining (5) and (7) yields the necessary archimedean contact inequality

```
[2sqrt(pi t)A/M_0]^2
 +[2sqrt(pi t)partial_xi A]^2/(M_0 M_2) <= 1.          (8)
```

If the left side exceeds one at `(t,xi)`, no choice of the actual prime
phases can produce a double contact there. This is a rigorous exclusion test
using only the three positive scalar prime moments `M_0,M_2` and the explicit
archimedean value and slope.

## Equality and the zero character

Equality in (5) requires simultaneous equality in Cauchy--Schwarz and Jensen,
forcing strong alignment of the sampled sines and cosines. At `xi=0`, however,
`R=M_0` and `I_1=0`, so the ellipse is automatically saturated. The criterion
cannot by itself exclude a zero-character contact; that is the original
scalar heat-positivity gate.

For nonzero characters, (8) can sharply shrink the contact region before any
full prime sum is evaluated. Higher moment matrices can strengthen it by
including curvature
`partial_xi^2 Theta=partial_xi^2 A+C R_2>=0`, where
`R_2=sum c_n(log n)^2 cos(xi log n)`.

## Curvature covariance bound

Put `M_4=sum c_n(log n)^4`. Weighted covariance of `(log n)^2` and the
cosine, followed by Cauchy--Schwarz, gives

```
[R_2-(M_2/M_0)R]^2
 <= [M_4-M_2^2/M_0][M_0-R^2/M_0].                     (9)
```

At first contact, heat curvature requires

```
R_2 >= -2sqrt(pi t) partial_xi^2 A.                   (10)
```

If the right side of (10) lies above the upper endpoint allowed by (9), a
first contact is impossible even when the value--slope ellipse (8) survives.
Thus moments through order four provide a nested source-only filter:
value, slope, then curvature.

## Falsifier protocol

Obtain certified enclosures for `A`, its first two character derivatives,
and `M_0,M_2,M_4`. An
interval lower bound greater than one for the left side of (8) excludes that
region. Otherwise (9)--(10) may exclude it by curvature. A surviving point is
only a candidate; the exact phase sums must still be checked.
