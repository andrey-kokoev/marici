# Exact entropy balance for a nonlinear Weyl coordinate

Let `z_i=f(r_i)` and define

```
A_i(z) = sum_(j != i) 1/(z_i-z_j),
m_i = f'(r_i)^2,
C_i[f] = 2 sum_(j != i)
 [f'(r_i)/(r_i-r_j)-m_i/(f(r_i)-f(r_j))].
```

The transformed Newman law is

```
z_i' = 2m_i A_i(z)+C_i[f].                             (1)
```

Since `partial_i log Delta(z)=2A_i(z)`, its exact entropy balance is

```
d/dlambda log Delta(z)
 = 4 sum_i m_i A_i(z)^2 + 2 sum_i A_i(z) C_i[f].        (2)
```

The first term is positive mobility-weighted dissipation. The second is the
Weyl-coordinate anomaly flux and has no automatic sign. Positivity survives
precisely when

```
sum_i A_i C_i >= -2 sum_i m_i A_i^2.                   (3)
```

Thus nonlinear flattening does not erase the explanation problem; it moves
it into one explicit scalar inequality.

## Infinitesimal geometry

For `f(r)=r+epsilon h(r)`, expansion of the mobility anomaly gives

```
C_i[f]/(2 epsilon)
 = sum_(j != i)
   [(h(r_i)-h(r_j))/(r_i-r_j)^2-h'(r_i)/(r_i-r_j)]
   + O(epsilon).                                       (4)
```

Affine `h` makes every summand vanish. For a nearby root
`r_j=r_i-delta`, the summand is

```
-h''(r_i)/2 + h'''(r_i) delta/6 + O(delta^2).          (5)
```

Curvature of the counting coordinate, rather than its slope, is therefore
the leading local source of anomaly after mobility is accounted for. For
the smooth Riemann--von Mangoldt density, the relative curvature decreases
at high ordinate; this is encouraging but is not yet a global sign proof.

## Falsifier and next target

A Weyl-renormalized entropy proposal must compute the second term of (2).
Dropping it is valid only for affine coordinates. A successful construction
must either bound it by the positive term, or add a canonical Jacobian or
potential correction whose derivative completes a square with it.

