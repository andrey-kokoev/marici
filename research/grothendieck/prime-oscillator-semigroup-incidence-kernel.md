# Oscillator semigroup evaluation gives a full-rank Hilbert--Schmidt prime kernel

Let the even gamma oscillator have eigenvalues `lambda_k=k+1/4`, and place
each prime at `u_p=log p`. Evaluating its semigroup gives

```
exp(-u_p lambda_k)=p^(-(k+1/4)).                       (1)
```

Multiplication by the critical prime amplitude defines

```
X_T(k,p)=p^(-1/2-iT)p^(-(k+1/4))
        =p^(-(k+3/4)-iT).                              (2)
```

It uses no Xi zeros: the quarter shift comes from oscillator parity, the
logarithmic coordinate from prime norm, and the half-weight from Euler data.

## Schatten theorem

```
||X_T||_2^2
 =sum_p sum_(k>=0)p^(-2k-3/2)
 =sum_p p^(-3/2)/(1-p^(-2)) < infinity.                (3)
```

The commutator with the oscillator and prime generators is

```
Omega_T=A X_T-X_T L_prime,
Omega_T(k,p)=(k+1/4-log p)X_T(k,p),                    (4)
```

and is also Hilbert--Schmidt: polynomial factors in `k` and `log p` are
dominated by the geometric and `p^(-3/2)` decay. Thus the nonzero commutator
required by the diagonal-intertwiner no-go is determinant class rather than
a formal distribution.

## Full-rank cutoffs

For distinct primes `p_1,...,p_m` and modes `k=0,...,m-1`,

```
det X_T
 =product_j p_j^(-3/4-iT)
  product_(i<j)(1/p_j-1/p_i),                          (5)
```

up to orientation. It is nonzero, so the kernel has growing rank and avoids
the fixed separable-channel obstruction.

Equation (5) also warns that this determinant alone never vanishes at finite
height. `X_T` is only an off-diagonal incidence leg. Zeros must arise after
coupling it to its adjoint, the gamma resolvent, endpoints, and the low-order
anomaly channels in a Schur complement.

The semigroup adds damping beyond the raw Euler amplitude. A completed block
must therefore prove that its Schur complement recovers the unsmoothed prime
Green term in the honest Euler half-plane. Otherwise this is merely a useful
Hilbert--Schmidt regularization.

## Next falsifier

At finite cutoff, test whether an oscillator-resolvent block containing
`X_T` produces

```
sum_n Lambda(n)n^(-1/2)exp(-sqrt(x)log n)/(2sqrt(x))    (6)
```

with the correct sign and prime-power multiplicity. Failure before analytic
continuation kills the candidate.

This is an explicit source-derived full-rank Schatten coupling, not a
completed Xi determinant or RH proof.
