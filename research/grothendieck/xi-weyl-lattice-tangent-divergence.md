# A universal coupled positivity theorem for Weyl-lattice fluctuations

Let `z_1<...<z_N` be any ordered real configuration and write

```
z_i = i + epsilon_i,
u_ij = (epsilon_j-epsilon_i)/(j-i).
```

Ordering is exactly the condition `u_ij>-1`. Define the tangent-renormalized
lattice divergence

```
D_N(z) = 2 sum_(i<j) [u_ij-log(1+u_ij)].               (1)
```

Since

```
phi(u)=u-log(1+u) >= 0     for u>-1,                   (2)
```

with equality only at `u=0`, one obtains

```
D_N(z) >= 0,                                           (3)
```

and equality holds exactly when all `epsilon_i` are equal—that is, when the
configuration is a translate of the integer lattice.

Equivalently, if

```
F_N(z)=log[Delta(z)/Delta(1,...,N)],
g_i=2[H_(i-1)-H_(N-i)],
```

then

```
D_N(z) = sum_i g_i epsilon_i - F_N(z).                 (4)
```

Thus `D_N` is the gap between the tangent plane of the concave
log-Vandermonde at the lattice and its actual value. This identifies the
previously troublesome harmonic boundary field as the unique first-order
counterterm selected by concavity, not an adjustable renormalization.

## Arithmetic specialization

For flattened Xi ordinates

```
z_n=n-1/2-S_n,
```

translation by `1/2` drops out and

```
u_ij=-(S_j-S_i)/(j-i).
```

Consequently

```
D_N(S)=2 sum_(i<j)
 [-(S_j-S_i)/(j-i)
  -log(1-(S_j-S_i)/(j-i))] >= 0.                       (5)
```

The ordering of the flattened ordinates supplies the logarithm domain.
Near the lattice,

```
D_N = sum_(i<j) (epsilon_j-epsilon_i)^2/(j-i)^2
      + O(epsilon^3),                                  (6)
```

recovering the positive nonlocal Dirichlet energy. Approaching a flattened
collision sends `D_N` to `+infinity`.

## What this proves—and does not

Equation (3) is a universal coupled positivity theorem, valid for every
ordered real configuration. Applied to Xi it gives a canonical nonnegative
multiscale measure of arithmetic zero-spacing fluctuation. It does not by
itself imply RH, because its definition presupposes an ordered real-zero
configuration. The next hard question is whether `D_N` has a source-side
expression or monotonicity that extends before real-rootedness and detects
the de Bruijn--Newman transition.

