# Quaternionic symmetry forces a square but over-doubles positive zeros

The finite-cutoff Pfaffian obstruction asks for a source reason that

```
det(I-C_P* C_P)
```

is a square before any Xi identification. There is a standard sufficient
mechanism: an antiunitary symmetry of quaternionic type.

Let `B` be a finite-dimensional Hermitian operator and let `Theta` be
antiunitary with

```
Theta^2 = -I,                 Theta B = B Theta.         (1)
```

If `Bv=lambda v`, then `B(Theta v)=lambda Theta v`. Moreover `v` and
`Theta v` are orthogonal: antiunitarity and `Theta^2=-I` imply
`<Theta v,v>=-<Theta v,v>`. Thus every eigenspace has even complex
dimension. Consequently

```
det B = product_j lambda_j^2.                           (2)
```

For a quaternionic-Hermitian family, the one-copy product is the Moore
determinant; its square is the ordinary complex determinant. This supplies
exactly the structural square missing from a generic transfer Gram matrix.

Applied to

```
B_P(T)=I-C_P(T)* C_P(T),                               (3)
```

a cutoff-compatible quaternionic structure commuting with `B_P(T)` would
produce a source-defined square root. But positivity now causes a stronger
obstruction. Each Kramers eigenvalue `lambda(T)>=0` that vanishes at an
interior point has even analytic order. Its paired contribution
`lambda(T)^2` to the complex determinant therefore has order divisible by
four. Thus a positive quaternionic Gram determinant cannot model `Xi(T)^2`
at a simple Xi zero, where the required order is two. Its Moore determinant
is also nonnegative and cannot recover the sign change of Xi.

## The known Xi involution is insufficient

Complex conjugation and the functional-equation reflection pair `s` with
`1-conjugate(s)`. On the critical line this is a real structure of square
`+I`, not a quaternionic structure of square `-I`. An antiunitary involution
with square `+I` does not force paired eigenvalues: a real diagonal family

```
B(x,y)=diag(x,y)                                       (4)
```

commutes with conjugation but has determinant `xy`, which is not a square in
`R[x,y]`.

Therefore the Riemann functional equation by itself cannot supply the
required finite-cutoff square. Twisting it to `Theta^2=-I` would force a
square, but while the Gram operator remains positive it forces too much
multiplicity. A viable symplectic construction would have to live before the
positive quotient, in an indefinite or oriented complex, rather than as a
Kramers symmetry of the final positive Gram operator.

## Hostile tests

A proposed quaternionic repair must pass four tests:

1. `Theta_P` is constructed from prime and archimedean source data, without
   Xi zeros;
2. `Theta_P^2=-I` exactly, not only after imposing RH or at the limit;
3. `[Theta_P,B_P(T)]=0` for every real `T` and every cutoff;
4. cutoff inclusions intertwine `Theta_P` and the resulting square roots;
5. the construction avoids the order-four zero forced by positivity plus
   Kramers degeneracy.

Failure of any one leaves the scalar `1-x^2` obstruction intact. The two
immediate falsifiers are that the available reflection squares to `+I`, and
that imposing a minus-square symmetry on the positive Gram space
over-doubles a generic zero.

## Revised conjectural target

Search, if at all, for a source-derived symplectic polarization on the
indefinite pre-quotient complex whose oriented section squares to the final
Gram determinant without imposing Kramers doubling on that positive
determinant. This is substantially more specific—and more falsifiable—than
asking for an unspecified determinant-line orientation.
