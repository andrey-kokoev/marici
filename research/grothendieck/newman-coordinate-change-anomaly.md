# Nonlinear Weyl coordinates necessarily create a Newman-flow anomaly

Let `z_i=f(r_i)` for a differentiable injective coordinate change. Starting
from the closed Newman root law gives

```
z_i' = 2 f'(r_i) sum_(j != i) 1/(r_i-r_j).             (1)
```

In the new coordinate, the canonical inverse-gap force would be

```
2 sum_(j != i) 1/(z_i-z_j).
```

Their exact difference is the coordinate anomaly

```
B_i[f] = 2 sum_(j != i)
  [ f'(r_i)/(r_i-r_j) - 1/(f(r_i)-f(r_j)) ].           (2)
```

Thus

```
z_i' = 2 A_i(z) + B_i[f].                              (3)
```

One may instead use the natural position-dependent mobility
`m_i=f'(r_i)^2`; then

```
z_i' = 2 m_i A_i(z) + C_i[f],
C_i[f] = 2 sum_(j != i)
 [f'(r_i)/(r_i-r_j)-f'(r_i)^2/(f(r_i)-f(r_j))].        (4)
```

Neither anomaly vanishes for a genuine Weyl-counting transformation.

## Affine-conjugacy rigidity

Suppose a coordinate change conjugates every two-root inverse-gap system to
the same form up to one global time factor `kappa`:

```
f'(x)/(x-y) = kappa/(f(x)-f(y))                        (5)
```

for every distinct `x,y`. Symmetry of the divided difference gives

```
kappa/f'(x) = [f(x)-f(y)]/(x-y) = kappa/f'(y).
```

Hence `f'` is constant and `f` is affine. Conversely, affine maps do satisfy
(5) with the corresponding constant time rescaling.

Therefore a nonlinear counting coordinate can flatten Xi density, but it
cannot preserve closed Newman dynamics. The anomaly is not an error term to
discard: it is precisely where the arithmetic Weyl density enters the
transformed entropy balance.

## Next gate

For a proposed smooth counting map `f`, derive the contribution of `B[f]`
to discriminant production and test whether its leading continuum part is
the uniform-equilibrium potential

```
V_U'(x)=log((1+x)/(1-x)).
```

Any proof that simply replaces ordinates by counting coordinates while
retaining the unmodified Calogero/Newman law fails equation (2).

