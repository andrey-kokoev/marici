# The retained shell bundle has a canonical self-adjoint Jacobi generator

The slowly growing moment fiber is not merely an approximation space. It
inherits a canonical generator by compressing logarithmic height
multiplication.

On the asymptotic shell coordinate

```
log p = k+r,       r in [-1/4,3/4],
```

write `x=r-1/4 in [-1/2,1/2]`. In the orthonormal Legendre basis, multiplication
by `k+r=k+1/4+x` has the Jacobi matrix

```
(J_k)_(n,n)     = k+1/4,
(J_k)_(n-1,n)   = (J_k)_(n,n-1)
                 = n/[2 sqrt((2n-1)(2n+1))],         (1)
```

for `n>=1`. Its rank-`m_k` truncation is therefore real symmetric without any
spectral fitting. The quarter shift is the diagonal center; the additional
moment channels occur in symmetric pairs around it.

For the exact discrete prime shell, replace Lebesgue measure by

```
mu_k = sum_(p in shell k) (p-1)^(-1) delta_(log p-k).
```

Gram--Schmidt produces the corresponding finite Jacobi matrix, equivalently
`P_k M_(log p) P_k`. It is again self-adjoint and source-derived from the
prime weights. The Legendre matrix is its PNT asymptotic model.

## Compact resolvent

Let

```
H_ret = direct_sum_k J_k^(m_k).
```

Every block is finite, its spectrum lies inside `[k-1/4,k+3/4]`, and these
intervals escape to infinity. Hence `H_ret` is self-adjoint on its maximal
weighted domain and has compact resolvent, even though `m_k` grows, provided
each `m_k` is finite. This gives the shell program a canonical source-derived
self-adjoint operator.

## Spectral identification fails

The eigenvalues of the asymptotic block are the `m_k` Gauss--Legendre nodes
translated by `k+1/4`. The discrete version has Gaussian-quadrature nodes for
the reciprocal-prime shell measure. They are positive, lie one shell at a
time near logarithms of primes, and are not the Riemann-zero ordinates.

Thus self-adjointness and compact resolvent are no longer the central mystery.
The unsolved step is a source-derived transform that turns this arithmetic
Jacobi generator into an operator whose determinant equals completed `Xi`.
Calling `H_ret` the Hilbert--Polya operator would be false: its determinant
zeros occur at its quadrature spectrum, not at the zeta zeros.

The next attack should test whether the coefficient--Betti boundary operator
couples these Jacobi blocks through a nonlocal self-adjoint Schur complement.
A diagonal/direct-sum moment generator cannot perform the required spectral
rearrangement by itself.

