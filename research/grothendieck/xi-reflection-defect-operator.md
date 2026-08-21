# A canonical self-adjoint Hilbert--Schmidt RH defect operator

Let `D_Xi` be the nontrivial zero divisor with multiplicity and let

```
H_D = l^2(D_Xi).
```

On its maximal domain define the normal diagonal zero operator

```
Z e_rho = (rho-1/2)e_rho.
```

Its real part

```
X = (Z+Z*)/2
```

is diagonal with eigenvalue `Re(rho)-1/2`. Since `X` commutes with `Z*Z`,
define the bounded self-adjoint reflection-defect operator

```
A_Xi = X (I+Z*Z)^(-1/2).                               (1)
```

Its eigenvalues are

```
a_rho = (Re(rho)-1/2)/sqrt(1+|rho-1/2|^2).             (2)
```

The critical-strip bound and Riemann--von Mangoldt counting imply that
`A_Xi` is Hilbert--Schmidt, with

```
||A_Xi||_HS^2
 = sum_rho (Re(rho)-1/2)^2/[1+|rho-1/2|^2]
 = H_Xi.                                               (3)
```

Therefore

```
RH  iff  A_Xi=0  iff  ||A_Xi||_HS=0.                  (4)
```

This is an exact self-adjoint operator formulation, but not a
Hilbert--Polya solution: the operator is constructed from the zeros, and RH
corresponds to its vanishing rather than to a prescribed real spectrum.

## Real-structure formulation

Complex conjugation of zeros induces an antiunitary involution `J` on
`H_D`. The diagonal adjoint is recovered through this real structure, and
`X` is the component of the zero coordinate fixed by conjugation. Thus
`A_Xi` measures failure of the zero coordinate to be anti-self-adjoint:
under RH, `Z*=-Z`.

This identifies the source-side target more sharply:

> Construct a normal source operator `Z_src` with the Xi divisor model and a
> canonical real structure `J_src`, then prove that the bounded real-part
> defect `Re(Z_src)(I+Z_src*Z_src)^(-1/2)` is Hilbert--Schmidt and vanishes.

The last word, “vanishes,” is exactly RH and cannot be assumed. A useful
arithmetic construction must make its norm computable or force it to zero
by an independent correspondence identity.

## Quartet test

For the off-line quartet `beta+-iT`, `1-beta+-iT`, the spectrum of `A_Xi`
on the quartet is

```
{+a,+a,-a,-a},
a=(beta-1/2)/sqrt(1+(beta-1/2)^2+T^2),                 (5)
```

and its squared Hilbert--Schmidt norm is the hostile-quartet defect already
computed. Hence the operator does not lose the smallest off-line branch.

