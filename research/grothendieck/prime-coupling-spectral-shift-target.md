# The remaining prime problem is a spectral-shift construction

Let `H_0` be the quarter-shifted Jacobi reference whose cumulative ranks give
the smooth Riemann--von Mangoldt law. If a self-adjoint arithmetic coupling
produces `H=H_0+V`, then, up to sign convention,

```
N_H(T)-N_H0(T) = -xi_(H,H0)(T),
xi_(H,H0)(T) = (1/pi) arg D(T+i0),
```

where `xi` is the spectral shift and `D` the perturbation determinant.
Therefore the exact target is

```
xi_(H,H0)(T) = -S(T),
```

with `D`, after the separated archimedean normalization, reproducing the zeta
boundary factor.

This yields immediate falsifiers: `V` must be symmetric and domain-controlled;
the resolvent difference must lie in the asserted determinant class; the
determinant phase must equal `S(T)`; and `V` must be derived from primes rather
than reconstructed from known zeros.

There is an equivalence warning. A self-adjoint pair whose perturbation
determinant is the completed zeta factor would already force its divisor onto
the real spectral axis. Its existence is essentially a strengthened
Hilbert--Polya form of RH, not a proof obtained by renaming `S(T)`.

The research content must be a prior construction of `V` from the prime
coefficient--Betti correspondence, followed by proofs of symmetry, domain
control, and the determinant identity. This is the single hard operator gate
left by the shell program.

