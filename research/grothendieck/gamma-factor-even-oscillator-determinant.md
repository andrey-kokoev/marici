# The full archimedean gamma factor is an even-oscillator determinant

Let

```
H_osc=-d^2/dx^2+x^2
```

on `L2(R)`. Its eigenvalues are `2n+1`. Restricting to even parity selects
`n=2k`, hence eigenvalues `4k+1`. Define the scaled even operator

```
A=(1/4) H_osc |_(even),
spec(A)={k+1/4 : k=0,1,2,...}.                         (1)
```

This is self-adjoint, positive, and has compact resolvent.

For a complex shift `z`, its spectral zeta function is the Hurwitz zeta

```
zeta_(A+z)(w)=sum_(k>=0)(k+1/4+z)^(-w)
             =zeta_H(w,1/4+z).                        (2)
```

Using

```
zeta_H'(0,a)=log Gamma(a)-(1/2)log(2pi),               (3)
```

the zeta-regularized determinant is

```
det_zeta(A+z)
 =exp[-zeta_(A+z)'(0)]
 =sqrt(2pi)/Gamma(1/4+z).                              (4)
```

Therefore the completed-zeta archimedean factor on the critical coordinate
is exactly

```
Gamma(1/4+iT/2)
 =sqrt(2pi)/det_zeta(A+iT/2).                          (5)
```

The quarter shift is no longer an adjustable boundary phase: it is selected
by even parity and oscillator zero-point energy.

## Relation to the Maslov phase

The harmonic oscillator is the basic metaplectic system. Its half-integer
zero-point shift, followed by even-parity restriction and scaling by four,
produces `1/4`. Stirling asymptotics of its determinant then produce the
`-pi/8` phase and the `7/8` counting constant already isolated.

This supplies a concrete candidate origin for both the compact archimedean
sector and the eighth-phase correction.

## Important limitation

`A` is an auxiliary determinant operator, not the Hilbert--Polya operator.
Its eigenvalues grow linearly and are not the Xi zero ordinates. The
`T log T` zero count comes from the phase of the shifted determinant, not
from the eigenvalue counting function of `A`.

Moreover, the completed factor also contains `pi^(-s/2)` and the endpoint
factor `s(s-1)`, while the prime Euler product must be coupled through a
separate determinant or relative determinant. No single operator whose
determinant is completed `xi` has yet been constructed.

## Next target

Seek a relative determinant

```
det_rel(A + arithmetic interaction + z, A+z)           (6)
```

whose logarithmic derivative produces `zeta'/zeta` and whose interaction is
symmetric under the incidence-derived Hilbert metric. This would couple the
now-concrete gamma operator to the prime correspondence without altering its
canonical parity shift.

