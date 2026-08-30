# A paired gluing determinant can create global zeros from nonzero local sectors

Let `A` and `B` be positive invertible finite-dimensional local blocks and
let `C` be a coupling correspondence. Form

```
M = [ A   C  ]
    [ C*  B  ].                                         (1)
```

With

```
T=A^(-1/2) C B^(-1/2),                                 (2)
```

the Schur complement gives

```
det M = det A det B det(I-T*T).                         (3)
```

Thus both local determinants may be nonzero while the coupled determinant
vanishes. The zero condition is

```
1 in spec(T*T),                                        (4)
```

equivalently, a singular value of the normalized correspondence reaches
one. Moreover,

```
M>=0 iff ||T||<=1.                                     (5)
```

At equality, the coupled positive system develops a null state.

This gives a concrete global zero-production mechanism compatible with the
Euler-local no-go: zeros are not local factor zeros; they are failures of
invertibility of the gluing correspondence.

## Holomorphic family with critical-line Hermitian restriction

Let `C(s)` be a holomorphic operator family satisfying the real-structure
condition

```
C(conj s)=C(s)*.                                       (6)
```

Define the paired determinant

```
F(s)=det[I-C(1-s)C(s)].                                (7)
```

This is holomorphic where the determinant is defined and is symmetric under
`s -> 1-s` up to the standard `det(I-AB)=det(I-BA)` identity. On the critical
line, `1-s=conj s`, so

```
F(1/2+iT)=det[I-C(s)*C(s)].                            (8)
```

The global function is holomorphic, while its critical-line restriction is
controlled by a Hermitian singular-value problem. This evades the
open-mapping no-go correctly: positivity is asserted only on the fixed line,
not on an open complex domain.

## Candidate arithmetic interpretation

The two local blocks can represent the even-oscillator archimedean sector and
the regularized Euler sector. The coupling `C(s)` should be built from the
relative difference/copy correspondence with the incidence-derived metric.
Then Xi zeros would be global matching resonances where a normalized
prime--archimedean transfer channel has singular value one.

## What remains unproved

No `C(s)` with determinant `xi(s)` has been constructed. Even if (7) matches
Xi, the determinant can have zeros away from the critical line unless an
additional contractivity or index theorem excludes them. The required hard
statement would be something like:

```
I-C(1-s)C(s) invertible for Re(s)!=1/2.                (9)
```

That is an RH-strength assertion and cannot be assumed.

## Infinite-dimensional gate

In a Hilbert-space model, `C(1-s)C(s)` must lie in a determinant class or
carry a canonical regularized determinant. Compactness, domains, and the
reflection-adjoint identity must all be proved. Equation (3) is the finite
theorem guiding that construction.

