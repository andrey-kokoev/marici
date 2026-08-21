# A generic finite transfer determinant has no algebraic Pfaffian lift

Let `R` be an integral domain of characteristic different from two. For every
even skew-symmetric matrix `A` over `R`,

```
det A = Pf(A)^2.                                        (1)
```

Therefore an algebraic skew lift of a transfer Gram determinant

```
D(C) = det(I-C* C)                                     (2)
```

can exist over the same coefficient ring only if `D(C)` is already a square
in that ring. This necessary condition fails at the smallest cutoff.

Take the real scalar transfer `C=[x]`. Then

```
D(x) = 1-x^2.                                          (3)
```

It is positive for `|x|<1`, but it is not a square in `R[x]`: its roots at
`x=1` and `x=-1` have odd multiplicity. Hence there is no polynomial
skew-symmetric matrix `A(x)` of any even size satisfying

```
det A(x) = 1-x^2.                                      (4)
```

Allowing `sqrt(1-x^2)` as an entry produces an analytic skew lift on the open
contractive interval, but that simply adjoins the desired square root. It is
not an entrywise algebraic construction from the original transfer data and
becomes singular at the threshold.

## What doubled structure does provide

For any square matrix `B`, the canonical skew doubling

```
J(B) = [ 0   B ]
       [-B^T 0 ]                                        (5)
```

has

```
Pf(J(B)) = (-1)^(n(n-1)/2) det B,
det J(B) = det(B)^2.                                   (6)
```

Putting `B=I-C*C` therefore gives a canonical Pfaffian equal to the transfer
determinant itself, not a square root of it. If that determinant models
`Xi^2`, skew doubling models `Xi^2` again and its determinant models `Xi^4`.
It does not recover signed Xi.

The missing ingredient must consequently be stronger than skew
symmetrization. The finite transfer determinant must acquire a structural
square factorization

```
det(I-C_P* C_P) = Q_P^2                               (7)
```

from an independent symmetry, polarization, quaternionic pairing, or exact
two-copy decomposition. Only then can `Q_P` be a source-defined candidate
Pfaffian. Generic contractivity supplies no such factorization.

## Falsifier and revised target

A finite-cutoff proposal fails if it claims an algebraic skew lift of
`det(I-C_P* C_P)` without first proving that determinant is a square in the
source coefficient ring. The scalar specialization `C=[x]` is the smallest
hostile test.

The revised constructive target is a source symmetry forcing even divisor
multiplicity for every finite-cutoff transfer determinant, compatibly under
cutoff inclusion. If no such symmetry exists, the Pfaffian route should be
abandoned; the positive determinant may still encode the RH-equivalent zero
set, but not signed Xi by local algebraic square root.
