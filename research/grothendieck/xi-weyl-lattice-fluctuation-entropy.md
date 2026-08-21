# Weyl flattening isolates an arithmetic lattice-fluctuation entropy

Use the smooth Riemann--von Mangoldt coordinate

```
W(t) = theta(t)/pi + 1.
```

With midpoint conventions at a zero ordinate `gamma_n`, the exact counting
identity reads

```
n-1/2 = W(gamma_n)+S(gamma_n),
```

so the flattened ordinate is

```
z_n = W(gamma_n) = n-1/2-S_n.                          (1)
```

Translation by `1/2` is irrelevant to differences. Relative to the integer
lattice, define the finite arithmetic fluctuation functional

```
F_N = log[Delta(z_1,...,z_N)/Delta(1,...,N)]
    = 2 sum_(i<j) log |1-(S_j-S_i)/(j-i)|.             (2)
```

This is the first candidate in the current lane that depends only on the
fluctuating argument term after the smooth Weyl geometry has been removed.
It is therefore genuinely arithmetic rather than a coordinate rewrite of
the original discriminant.

## Sign and boundary obstruction

For a general increasing perturbed lattice, `F_N` has no fixed sign. Exact
three-point examples give both larger and smaller discriminant than the
integer lattice. Moreover, for `z_i=i+epsilon_i`,

```
F_N = 2 sum_(i<j) (epsilon_j-epsilon_i)/(j-i)
      - sum_(i<j) (epsilon_j-epsilon_i)^2/(j-i)^2
      + O(epsilon^3).                                  (3)
```

The linear term is a finite-window boundary field. Its coefficient at site
`i` is

```
2[H_(i-1)-H_(N-i)].                                    (4)
```

It vanishes only at the center (or in a symmetric principal-value infinite
lattice). Once this boundary term is removed, the quadratic fluctuation is
the negative nonlocal Dirichlet form

```
-sum_(i<j) (epsilon_j-epsilon_i)^2/(j-i)^2.             (5)
```

Thus the uniform lattice is locally discriminant-maximizing in the bulk,
but not a stationary configuration of a sharp one-sided finite window.

## Research consequence

A canonical renormalization should subtract the harmonic boundary field in
(4), preferably using symmetric windows or a smooth cutoff. The remaining
quadratic form is structurally promising: it measures arithmetic rigidity
across every index scale. However, the logarithmic functional has no global
sign without a bound preventing near-collisions or controlling higher
orders. This is a theorem-shaped target, not yet an RH criterion.

