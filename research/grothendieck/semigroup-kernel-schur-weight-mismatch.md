# The semigroup incidence kernel fails the Euler Schur-complement weight test

For a self-adjoint block operator

```
H=[A V; V* D],                                         (1)
```

eliminating the `A` channel produces the Schur correction

```
V*(A-z)^(-1)V.                                         (2)
```

This expression is necessarily quadratic in the coupling amplitudes. Its
diagonal trace contains absolute squares; its off-diagonal entries contain
products of two source weights.

For the proposed semigroup incidence kernel

```
X_T(k,p)=p^(-(k+3/4)-iT),                              (3)
```

the diagonal quadratic weight at the lowest oscillator mode is `p^(-3/2)`,
and the full oscillator contraction is built from

```
p^(-3/4+iT)q^(-3/4-iT)
sum_(k>=0)(pq)^(-k)r_k(z).                             (4)
```

It is a product/difference-correlation kernel. By contrast, the exact
Euler-region prime Green term is linear:

```
R_prime(y^2)
=-(1/(2y))sum_(n>=2)Lambda(n)n^(-1/2-y),              (5)
```

and includes every prime power. Equations (4) and (5) have different
coefficient degree, exponent, support, and height dependence. No scalar
normalization independent of `p,q,y` can identify them.

Thus the explicit kernel passes rank and Schatten tests but fails its first
proposed identification as the direct Schur leg producing the Euler trace.

## Square-root coupling does not solve the boundary problem

One can force a quadratic form to reproduce the positive magnitude of (5)
in the honest Euler domain by choosing amplitudes

```
v_y(n)=sqrt(Lambda(n)) n^(-1/4-y/2).                  (6)
```

Then `sum_n |v_y(n)|^2=sum_n Lambda(n)n^(-1/2-y)` for
real `y>1/2`. But this construction:

- is not defined as a Hilbert vector at the critical boundary;
- loses the negative Euler orientation in a positive norm;
- does not by itself produce the off-diagonal free Green propagation;
- changes the source type from von Mangoldt coefficients to chosen square
  roots and requires an orientation for every prime power.

It is therefore a useful factorization control, not the completed solution.

## Correct typing: paired cross-resolvent

The Euler term is already known exactly as an off-diagonal Green matrix
element between the boundary distribution at `u=0` and the von Mangoldt
source supported at `u=log n`:

```
<delta_0,(H_0+y^2)^(-1)q_prime>.                       (7)
```

Unlike a diagonal Schur correction, a cross-resolvent is linear in the prime
source and retains its sign. This is precisely why the coefficient--Betti
double must preserve distinct source and readout legs until the final
two-channel determinant.

The role of `X_T` must consequently be reduced. It may provide a
Hilbert--Schmidt regularizing transform or comparison kernel between prime
and oscillator modules, but it cannot replace the linear prime source in
(7). A valid completed block must contain both:

1. the linear boundary-to-prime Green entry (7);
2. a separate determinant-class prime--oscillator comparison leg.

## Falsifier and revised target

A proposal fails if it claims that a quadratic self-adjoint Schur correction
with coupling weights `p^(-3/4-iT)` equals the linear von Mangoldt trace.
Finite-cutoff coefficient comparison already disproves it.

The revised target is a self-adjoint two-boundary-channel resolvent matrix
whose off-diagonal entry is exactly (7), while its diagonal relative
covariances are renormalized by the gamma oscillator. Zeros may then arise
from the determinant of the full `2x2` boundary Weyl matrix, not from turning
the linear prime term into a positive norm.

This is a hostile rejection of one use of the semigroup kernel, not of the
kernel's rank/Schatten theorem, and it is not an RH proof.
