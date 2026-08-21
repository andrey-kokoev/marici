# Holomorphic continuation cannot preserve lattice-divergence positivity

For one real normalized gap `w=1+u>0`, the tangent divergence is

```
d_R(w)=2[w-1-log w] >= 0.                              (1)
```

The most direct complex continuation is its real part,

```
d_hol(w)=2 Re[w-1-Log w].                              (2)
```

It fails immediately. At the harmless nonzero gap multiplier `w=1+i`,

```
d_hol(1+i) = -log 2 < 0.                               (3)
```

Thus the first two-point off-line branch already destroys positivity; no
large matrix or zero table is needed.

## General holomorphic no-go

A nonconstant holomorphic function on a connected open complex domain has
open image. It therefore cannot take values only in the nonnegative reals.
Consequently no nonconstant holomorphic continuation of the real scalar
divergence can itself remain real and nonnegative on an open complex
configuration space.

Any positivity-preserving source-side continuation must be nonholomorphic:
it must use complex conjugation, an adjoint, a Hermitian norm, or an
equivalent reflection pairing. This reconnects the Weyl-lattice lane to the
paired coefficient--Betti/Hermitian correspondence program.

## Canonical radial repair and its limitation

The scalar Hermitian divergence

```
d_H(w) = |w|^2-1-log|w|^2 >= 0                         (4)
```

is globally nonnegative for `w != 0`, because `x-1-log x>=0` for `x>0`.
It diverges at collisions. But it vanishes for every `|w|=1`, not only for
the real reference gap `w=1`. Pairwise summation therefore cannot by itself
detect a rigid rotation of the entire lattice away from the real axis.

A phase-sensitive Hermitian term is additionally necessary. Reflection
symmetry may provide it canonically: in the zero coordinate
`rho=1/2+i gamma`, RH is precisely reality of `gamma`, so a valid coupled
form should measure both radial gap distortion and failure of compatibility
with the real involution.

## Falsifier

Any proposed source-side extension fails if it:

1. is merely the real part of a holomorphic continuation of (1); or
2. depends only on absolute gap ratios and therefore assigns zero cost to a
   globally rotated non-real configuration.

