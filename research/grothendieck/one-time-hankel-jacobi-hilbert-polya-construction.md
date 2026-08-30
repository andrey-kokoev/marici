# One-time Hankel positivity canonically constructs the squared Jacobi operator

Fix `t_0>0` and suppose the complete ordinary and shifted Stieltjes Hankel
hierarchy holds for

```
D_k=(-1)^k Theta^(k)(t_0).                             (1)
```

Define on polynomials

```
<x^i,x^j>=D_(i+j).                                     (2)
```

Ordinary Hankel positivity makes this form positive semidefinite. Quotienting
its radical and completing gives a cyclic Hilbert space. Shifted Hankel
positivity gives `<p,xp> >= 0`, so multiplication by `x` is a densely defined
positive symmetric operator.

## Jacobi realization

Gram--Schmidt orthonormalization of `1,x,x^2,...` yields polynomials `p_n` and
the three-term recurrence

```
x p_n=b_(n+1)p_(n+1)+a_n p_n+b_n p_(n-1).             (3)
```

The right-half-plane Taylor radius supplies an exponential moment. Hence the
Stieltjes moment problem is determinate, and multiplication has its canonical
self-adjoint closure `J>=0`.

Untilt the moment measure by

```
dnu(lambda)=e^(t_0 lambda)dmu_(t_0)(lambda).           (4)
```

Then

```
Theta(t)=integral e^(-t lambda)dnu(lambda),
S(x)=integral dnu(lambda)/(x+lambda).                  (5)
```

The known meromorphic function
`S(x)=xi'/xi(1/2+sqrt(x))/(2sqrt(x))` fixes this measure uniquely. Its poles
force atomic support at squared Xi ordinates with positive residues. On a
doubled space,

```
H=diag(sqrt(J),-sqrt(J))                               (6)
```

is self-adjoint and has the signed ordinate support expected by a
Hilbert--Polya model.

## Conditional and multiplicity boundaries

This becomes unconditional only after proving the one-time Hankel hierarchy
from arithmetic source data. That hierarchy is RH-equivalent; this is a
precise construction target, not an RH proof.

A scalar cyclic measure can assign residue `m` to one atom, but its
multiplication eigenspace remains one-dimensional. Thus (6) reproduces
distinct spectral support and resolvent weights, not determinant
multiplicities, unless all zeros are simple. Full Xi multiplicity still
requires the previously identified jet or vector-valued amplification.

The first Jacobi coefficients are

```
a_0=D_1/D_0,
b_1^2=(D_0D_2-D_1^2)/D_0^2.                           (7)
```

Hence the first coupled Hankel determinant is literally the square of the
first Jacobi off-diagonal coefficient. Higher determinants recursively
generate the whole operator.
