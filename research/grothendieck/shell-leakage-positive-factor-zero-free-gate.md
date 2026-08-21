# The shell-leakage Gram factor cannot carry the zero spectrum

For real height `T`, the coupled shell correction is

```
G(T)=det(I+B(T)*B(T)).
```

Whenever `B(T)` is Hilbert--Schmidt, `B(T)*B(T)` is positive trace class and

```
G(T)=product_j(1+s_j(B(T))^2) >= 1.                  (1)
```

Thus `G(T)` has no real zeros. If the family is analytic, its complex
continuation may have zeros away from the real axis, but positivity alone
does not locate or exclude them. On the critical-height axis the factor is
strictly nonvanishing.

Consequently the coupled-positivity theorem cannot itself be the proposed
Hilbert--Polya determinant with Riemann-zero spectrum. In any factorization

```
Xi(T) = D_ret(T) G(T),                               (2)
```

all real zeros of `Xi` must lie in the retained determinant `D_ret`. The Gram
factor can change normalization and logarithmic derivatives, and can certify
that kernel coupling introduces no real zero or sign change, but it cannot
generate the required spectrum.

This sharply types the role of the first universal coupled positivity
theorem:

- it is a stability/no-spurious-real-zero theorem for a mapping-cone defect;
- it is not the spectral realization;
- the spectral burden remains on a source-derived self-adjoint retained
  operator or on a signed determinant not reducible to `I+B*B`.

The next viable attack is therefore not to enlarge the positive Gram factor.
It is to determine whether the quarter-shifted retained moment bundle carries
a canonical self-adjoint generator whose relative determinant is
`D_ret(T)`, while the zero-free Gram factor controls the discarded kernel.

