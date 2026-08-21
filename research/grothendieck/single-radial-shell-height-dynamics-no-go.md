# One radial mode per shell cannot retain prime height dynamics

The quarter-shifted shell correspondence matches the quadratic covariance,
but it compresses each logarithmic shell to one radial vector. We now test
whether the discarded within-shell sector is determinant-class after height
evolution.

Write a prime in shell `k` as

```
log p=k+r,                    -1/4<=r<3/4.             (1)
```

The reciprocal-prime measure in a large shell is asymptotically

```
(dr)/(k+r)=(1/k)dr+O(k^-2)dr.                          (2)
```

After removing the common shell phase `exp(-iTk)`, the exact prime height
phase is `exp(-iTr)`. The normalized overlap with the constant radial mode is

```
phi(T)=integral_(-1/4)^(3/4) exp(-iTr)dr
      =exp(-iT/4) 2 sin(T/2)/T.                        (3)
```

Hence the relative mass left in the fluctuation sector is

```
1-|phi(T)|^2=1-[sin(T/2)/(T/2)]^2.                    (4)
```

For every fixed generic nonzero `T`, this is a positive constant independent
of `k`. Since the shell mass is asymptotic to `1/k`, the total discarded norm
contains

```
[1-|phi(T)|^2] sum_k 1/k=infinity.                    (5)
```

Thus the fixed radial compression does not leave a Hilbert--Schmidt
fluctuation coupling at nonzero height. Trace-class covariance matching at
`T=0` is insufficient for the analytic determinant family.

## A moving radial vector also fails smooth implementability

One may instead choose the shell radial vector itself to be
`eta_k(T,r)=exp(-iTr)`, which captures the single Euler source vector at each
fixed `T`. After optimizing the scalar Berry-phase gauge, its squared
derivative norm is the variance of `r` on an interval of length one:

```
Var(r)=1/12.                                           (6)
```

Weighted by shell mass, the global projective derivative norm contains

```
(1/12)sum_k1/k=infinity.                               (7)
```

Therefore the moving radial subspace is not differentiable in the global
Hilbert--Schmidt/implementable topology required for an analytic Fredholm
family. Letting the basis depend on `T` hides rather than removes the
within-shell phase rank.

## Consequence

Each logarithmic shell needs more than one archimedean comparison mode. The
natural asymptotic fiber is

```
L2([-1/4,3/4],dr),                                    (8)
```

on which height acts by multiplication with `exp(-iTr)`. The constant mode
controls the trace-class radial covariance; nonconstant Fourier/moment modes
carry prime fluctuations.

This does not mean every shell must contribute an uncontrolled infinite
gamma multiplicity. A viable construction must grade the nonconstant modes
so their relative determinant is regularized or cancels in a Krein null
sector while leaving the quarter-shifted constant-mode determinant equal to
the gamma factor.

## Falsifiers and next target

A proposal fails if it compresses each shell to one fixed mode and claims to
retain exact height phases, or uses a `T`-dependent radial basis without
checking its divergent projective derivative.

The next target is the two-mode hostile shell: retain the constant and first
centered moment in `r`, compute the exact `2x2` compressed phase matrix, and
test whether the residual improves from order `T^2/k` to `T^4/k` but still
diverges. This will decide whether any fixed number of shell moments suffices
or an infinite fiber is forced.

This is a height-dynamics no-go for rank-one shell compression, not for the
quarter-shifted covariance theorem or RH.
