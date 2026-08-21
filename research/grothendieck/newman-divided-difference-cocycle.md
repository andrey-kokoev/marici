# The divided-difference cocycle exactly transports Newman entropy

For an injective differentiable coordinate `f` and distinct roots `r_i`, set

```
J_f(r) = 2 sum_(i<j)
 log |(f(r_i)-f(r_j))/(r_i-r_j)|.                       (1)
```

The Vandermonde identity gives

```
log Delta(f(r)) - J_f(r) = log Delta(r).                (2)
```

Consequently, along any root motion—and in particular closed Newman flow—

```
d/dlambda [log Delta(f(r))-J_f(r)]
 = d/dlambda log Delta(r).                              (3)
```

For Newman flow the right side is `4 sum_i A_i(r)^2`, so the coordinate
anomaly is canceled exactly by `J_f'`.

## Cocycle law

For composable injective coordinates `f` and `g`, divided differences
multiply pairwise. Therefore

```
J_(g o f)(r) = J_f(r) + J_g(f(r)).                      (4)
```

For an affine map `f(r)=a r+b`,

```
J_f(r)=N(N-1) log|a|.                                  (5)
```

Thus `J_f` is the natural correspondence cocycle for discriminant entropy.

## Interpretation and limitation

This solves the coordinate-anomaly bookkeeping problem but not RH. The
corrected functional in (2) is exactly the original discriminant expressed
in another coordinate. A Weyl counting map plus its full cocycle correction
cannot generate a new positivity theorem.

Any genuinely stronger Weyl-renormalized entropy must contain an additional
arithmetic term not forced by coordinate covariance—most naturally the
difference between the exact counting coordinate and its smooth
Riemann--von Mangoldt part, or a canonical exterior-field potential. Such a
term must be independently sign-controlled and falsifiable.

