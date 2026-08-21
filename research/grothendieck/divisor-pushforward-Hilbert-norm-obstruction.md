# Divisor pushforward is invertible but not a Hilbert-space isometry

On the finite divisibility poset `{1,...,N}`, let the divisor zeta matrix be

```
B_(n,d)=1 if d|n, and 0 otherwise.                     (1)
```

Then `B Lambda=log` and the Möbius matrix is the algebraic inverse `B^-1`.
With the standard Euclidean inner product, however,

```
(B*B)_(d,e)=floor[N/lcm(d,e)].                         (2)
```

This Gram matrix is neither diagonal nor a scalar multiple of the identity.
In particular,

```
B^-1 != B*.                                            (3)
```

Möbius recovery is therefore not adjoint pullback, and the exact arithmetic
transport does not automatically preserve a positive norm.

## No diagonal positive weighting can fix orthogonality

Give the target a positive diagonal weight `W=diag(w_n)` with every
`w_n>0`. For any `d,e` with `lcm(d,e)<=N`,

```
(B* W B)_(d,e)
 = sum_(n<=N; d|n,e|n) w_n > 0.                        (4)
```

Thus distinct divisor columns with a common multiple can never become
orthogonal under a positive diagonal measure. No local reweighting of
integer sites turns `B` into an isometry.

## Available but nonlocal repair

Since finite `B` is invertible, polar normalization gives

```
U=B(B*B)^(-1/2),
U*U=I.                                                 (5)
```

But `(B*B)^(-1/2)` couples many divisibility classes. It is nonlocal in the
integer/divisor basis and has no immediate Euler-product interpretation.
Using it is legitimate algebraically only if this loss of arithmetic
locality is accepted and controlled.

## Consequence

The following must remain separate:

1. `B Lambda=log` and Möbius recovery—exact arithmetic incidence;
2. a Hilbert adjoint/pull--push theorem—currently absent for local positive
   weights; and
3. identification with the positive Hermitian Xi defect—still open.

This blocks any argument that silently treats Möbius inversion as the
adjoint of divisor summation.

