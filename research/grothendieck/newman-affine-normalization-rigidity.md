# Affine normalization rigidly selects Hermite equilibrium

Let `r_1,...,r_N` be a closed real simple-root Newman system

```
r_i' = 2 A_i(r),
A_i(r) = sum_(j != i) 1/(r_i-r_j).
```

After removing the conserved center, put

```
R^2 = sum_i r_i^2,
p = N(N-1)/2,
x_i = r_i/R,
d tau/d lambda = 2/R^2.
```

The standard identities

```
sum_i r_i A_i(r) = p,
dR^2/dlambda = 4p
```

give the exact normalized flow

```
dx_i/dtau = A_i(x)-p x_i.                              (1)
```

It stays on the unit sphere and is the constrained gradient ascent of the
logarithmic discriminant. Indeed, with

```
q_i = A_i(x)-p x_i,
```

one has

```
d/dtau log Delta(x) = 2 sum_i q_i^2 >= 0.              (2)
```

Equality requires

```
A_i(x)=p x_i,                                          (3)
```

the Stieltjes electrostatic equations. Their unique ordered solution is the
appropriately normalized Hermite-root configuration.

## Rigidity consequence

Affine centering and radius normalization cannot make a uniform limiting
root density stationary under the closed Newman flow. The quadratic drift
`-p x_i` in (1) is forced by the radius chain rule, and its continuum
log-gas equilibrium is semicircular.

Therefore the uniform Xi window law and the finite closed Newman Lyapunov
law describe different asymptotic regimes. A Weyl-adapted entropy cannot be
obtained by merely replacing the Hermite reference inside the existing
formula. It must include at least one genuinely new ingredient:

1. a nonlinear counting-coordinate transformation;
2. the exterior-root field before taking the window limit; or
3. a non-affine, density-dependent normalization.

This is a useful impossibility theorem: any proposed uniform-reference
functional derived using only center and radius normalization is falsified
by (1).

