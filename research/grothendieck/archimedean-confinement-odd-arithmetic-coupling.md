# Archimedean confinement can coexist with odd-arithmetic skew-adjointness

Let `H_0` be a self-adjoint operator with compact resolvent, representing an
archimedean confining sector. Let `V` be a symmetric arithmetic interaction
that is `H_0`-bounded with relative bound strictly below one. By
Kato--Rellich,

```
H=H_0+V                                             (1)
```

is self-adjoint on `Dom(H_0)`. Its resolvent remains compact: at a common
resolvent point, the resolvent identity factors `(H-z)^(-1)` as the compact
resolvent of `H_0` times a bounded correction. Therefore

```
Z=iH                                                (2)
```

is skew-adjoint with discrete imaginary spectrum of finite multiplicity.

This is the first abstract mechanism satisfying both requirements isolated
by the previous no-go:

```
archimedean compact resolvent  +  symmetric arithmetic interaction
              => discrete skew-adjoint spectral coordinate.             (3)
```

The source-leg oddness theorem supplies a reason the arithmetic interaction
could become symmetric after multiplication by `-i`; the gamma sector must
supply `H_0`.

## Classical archimedean Weyl geometry

There is a simple phase-space explanation for the two leading
Riemann--von Mangoldt terms. In the positive quadrant with cutoffs `x>=a`,
`p>=b`, the region `xp<=E` has area

```
A(E)=integral_a^(E/b) (E/x-b) dx
    =E log(E/(ab))-E+ab.                              (4)
```

Dividing by the Planck cell `2pi` and choosing `ab=2pi` gives

```
A(E)/(2pi)
 =E/(2pi) log(E/(2pi))-E/(2pi)+1.                    (5)
```

The logarithmic and linear terms match the smooth zero-counting law. The
constant is `1`, not the Xi constant `7/8`; a boundary/Maslov correction of
`-1/8` is still required. More importantly, the energy-dependent phase-space
cutoff in (4) is not yet a fixed self-adjoint operator domain.

## Exact operator target

A successful construction must provide:

1. a fixed archimedean Hilbert space and self-adjoint `H_0` with compact
   resolvent and the completed Xi Weyl law, including the constant term;
2. a prime interaction `V` obtained from the divisor/difference
   correspondence;
3. symmetry and relative-bound estimates for `V`; and
4. a determinant or trace identity identifying `spec(H_0+V)` with Xi
   ordinates without assuming RH.

The abstract perturbation theorem proves that these requirements are
compatible. It does not construct any of them for Xi.

## Falsifier

If the transported prime interaction has a nonsymmetric component, then
`i(H_0+V)` need not be skew-adjoint and eigenvalues may leave the imaginary
axis. If `V` destroys compact resolvent, discreteness is also lost. Both
properties require separate proofs.

