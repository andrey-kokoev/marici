# Symmetric windows cancel the leading exterior entropy flux

Consider a centered symmetric finite window of real roots and symmetric
exterior pairs `+-y`. Under the full Newman root law, the force on an
interior root `r_i` from one omitted pair is

```
2/(r_i-y) + 2/(r_i+y) = 4 r_i/(r_i^2-y^2).
```

Let the positive exterior ordinates be `y`, put

```
M_2 = sum_y y^(-2),       M_4 = sum_y y^(-4),
X = max_i |r_i|,          Y = min_y y,
```

and assume `X<Y`. The total exterior force decomposes as

```
b_i = -4 M_2 r_i + e_i,
e_i = -4 r_i^3 sum_y [y^(-4)/(1-r_i^2/y^2)].          (1)
```

For the centered-repulsion defect

```
q_i = A_i - [N(N-1)/(2R^2)] r_i,
```

one has the exact scale orthogonality

```
sum_i r_i q_i = 0.                                      (2)
```

Therefore the entire `M_2` exterior force disappears from normalized
discriminant production:

```
sum_i b_i q_i = sum_i e_i q_i.                          (3)
```

Moreover,

```
|e_i| <= 4 |r_i|^3 M_4 / (1-X^2/Y^2),
|sum_i b_i q_i|
  <= 4 M_4 ||(r_i^3)||_2 ||q||_2 / (1-X^2/Y^2).         (4)
```

Hence the Hermite-relative entropy remains decreasing if

```
2 M_4 ||(r_i^3)||_2 / (1-X^2/Y^2) <= ||q||_2.           (5)
```

This criterion is sufficient, not necessary. Its significance is structural:
the apparent second-moment divergence or large tail is irrelevant to the
scale-free entropy; only a fourth-inverse-moment remainder enters.

## Limitation

For a window consisting of the first `N` Xi roots, `X/Y` approaches one at
the boundary, so the crude minimum-gap bound in (4) can be poor. A useful
infinite-rank argument must separate a boundary layer from a distant tail,
or replace the sharp cutoff with a smooth symmetric weight. The theorem
identifies why such a refinement is plausible, but does not supply it.

