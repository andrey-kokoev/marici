# Riemann zero density forces logarithmic shell rank

The retained Jacobi operator has `m_k` eigenvalues in a bounded interval near
height `k`. Its counting function therefore satisfies

```
N_ret(T) = sum_(k<=T) m_k + O(m_T).                  (1)
```

The Riemann--von Mangoldt law is

```
N_zeta(T) = T/(2 pi) log(T/(2 pi)) - T/(2 pi)
            + O(log T).                              (2)
```

Consequently, any shell-local operator intended to realize the zero spectrum
with multiplicity must have average shell rank

```
m_k ~ (1/(2 pi)) log(k/(2 pi)).                      (3)
```

The minimal Hilbert--Schmidt schedule

```
m_k ~ c log log k / log log log k
```

is far too sparse: its counting function is
`o(T log T)`. It solves the phase-approximation summability problem but cannot
solve the spectral multiplicity problem.

## Forced architecture

The logarithmic rank schedule is compatible with, and much stronger than,
the approximation requirement. Factorial moment convergence then makes the
discarded phase leakage extremely summable on compact height sets. More
importantly, the rank is no longer a tunable regularization parameter: the
Riemann--von Mangoldt law fixes its leading coefficient `1/(2 pi)`.

This produces a clean separation:

- the quarter shift `1/4` fixes the center of each archimedean shell block;
- the Weyl law fixes the leading number of moment channels per block;
- the Jacobi recurrence fixes the local self-adjoint matrix;
- a still-missing nonlocal coefficient--Betti coupling must move the local
  quadrature nodes to the actual Riemann ordinates without changing their
  global density.

A construction with the minimal sublogarithmic rank is therefore falsified
as a Hilbert--Polya spectral model even though it remains a valid
determinant-class compression. Conversely, simply choosing logarithmic ranks
does not prove spectral identification; it only passes the necessary density
gate.

