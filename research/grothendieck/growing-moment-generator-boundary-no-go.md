# Growing moment rank does not make the full height generator implementable

Let `P_m` project onto the first `m` orthonormal Legendre moments on a shell.
Multiplication by the centered coordinate `x` obeys the Jacobi recurrence.
The only leakage from the retained polynomial space is its top boundary:

```
(1-P_m) M_x P_m e_(m-1) = a_m e_m,
a_m = m/[2 sqrt((2m-1)(2m+1))].                     (1)
```

But

```
a_m^2 = m^2/[4(2m-1)(2m+1)] -> 1/16.                (2)
```

Increasing the rank moves the boundary outward; it does not weaken the
boundary matrix element. With reciprocal-prime shell mass asymptotic to
`1/k`, the global squared leakage contains

```
sum_k a_(m_k)^2/k,
```

which diverges for every rank schedule `m_k>=1`, including logarithmic Weyl
rank. Without the shell-mass weighting it diverges even more strongly.

## Scope correction

The previous factorial estimate remains correct for approximating the single
distinguished phase vector `exp(-iTx)` by its first `m_k` moments. It does not
control the operator commutator `(1-P)M_xP` on the whole retained moment
bundle. Consequently it does not by itself produce a Hilbert--Schmidt
operator leakage, an analytic Fredholm family, or the `B` required by the
coupled-positivity determinant.

This distinguishes two tasks:

- supported-current preservation: slowly growing rank suffices;
- natural operator-level height dynamics: every hard polynomial cutoff has a
  nonsummable moving boundary.

A full operator construction needs a soft moment cutoff, a weighted Sobolev
metric damping the top Jacobi coefficient, or a mapping-cone cancellation
between adjacent ranks. Any such repair must be source-derived and must retain
the Weyl counting law.

