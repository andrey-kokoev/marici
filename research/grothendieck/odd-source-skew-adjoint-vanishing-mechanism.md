# Odd source coefficients force skew-adjoint spectral multipliers

Let `G` be an abelian group and let a real convolution kernel satisfy

```
k(-x)=-k(x).                                          (1)
```

Whenever convolution by `k` defines a densely defined closed operator
`T_k` with the standard involutive domain, its adjoint is convolution by

```
k*(x)=conj(k(-x))=-k(x).
```

Therefore

```
T_k*=-T_k.                                             (2)
```

In a unitary Fourier representation, `T_k` is multiplication by `k_hat`,
and (2) says

```
Re k_hat=0.                                            (3)
```

Thus `iT_k` is self-adjoint and the Hermitian reflection-defect operator

```
Re(T_k)(I+T_k*T_k)^(-1/2)
```

vanishes identically.

## Connection to the relative arithmetic cocycle

The quotient-compatible coefficient

```
c(m,n)=log(m/n)                                       (4)
```

is real and reverses sign under swapping the two source legs. Hence the
relative difference geometry contains exactly the involutive symmetry that
could force a critical-line spectral coordinate: source antisymmetry becomes
spectral skew-adjointness.

This is the first candidate vanishing mechanism in the program. It is
structural rather than an assumed positivity statement.

## Why this is not RH

The missing assertion is enormous:

```
Xi zero operator  =  Fourier/correspondence image of T_c.               (5)
```

No such unitary equivalence has been constructed. The ordinary explicit
formula is a trace identity and does not identify operators or domains.

There are also three immediate hostile gates:

1. A finite group admits no nonzero homomorphism to the additive reals, so
   the literal logarithmic cocycle becomes trivial on finite quotients.
2. On a noncompact group, `log`/linear odd kernels generally define
   unbounded or distributional convolution operators.
3. Translation-invariant convolution normally has continuous spectral
   geometry, whereas the Xi divisor is discrete; compactness or confinement
   must enter without destroying skew-adjointness.

## Small C2 audit

On `C_2`, the nonzero element equals its inverse, so oddness forces its
coefficient to vanish. The smallest nontrivial finite odd model is `C_3`,
where `k(1)=-k(2)`. This makes the convolution matrix real skew-symmetric and
its Fourier eigenvalues purely imaginary. The theorem survives, but the
`C_2` branch demonstrates that finite quotient approximations can erase the
logarithmic direction entirely.

## Long-horizon conjecture

Seek an arithmetic Hilbert correspondence in which:

1. divisor incidence transports `Lambda` to the logarithmic relative
   cocycle;
2. leg swap becomes the adjoint involution;
3. the completed archimedean term supplies compactness/confinement; and
4. the resulting skew-adjoint operator has the Xi zero divisor as spectrum.

If all four hold without assuming RH, the critical line follows from (2).

