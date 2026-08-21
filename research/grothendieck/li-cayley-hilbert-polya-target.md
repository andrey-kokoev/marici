# The rigid Li phase fixes the conditional Hilbert--Pólya operator

## Exact coordinate

The rigid Möbius phase is

`u=1-1/s`.

Its inverse is `s=1/(1-u)`. Centering at the functional-equation fixed line
gives

`(s-1/2)/i = (1+u)/[2i(1-u)]`.

For `s=1/2+i gamma`, this expression is exactly `gamma`.

## Conditional operator construction

Suppose the arithmetic Toeplitz functional has been proved positive. Its GNS
construction gives a Hilbert space, a cyclic vector for the increment
measure, and a unitary shift `U`. Define the unbounded Cayley transform

`H=(1+U)/[2i(1-U)]`

on the natural domain where the right-hand side is square integrable.

For a unitary `U`, this Cayley transform is self-adjoint provided the domain
and possible spectral mass at `U=1` are handled in the standard way. Under
the conditional zero-phase realization, its spectral values are precisely
the ordinates `gamma`.

## What remains unproved

This does not construct `U`: that requires positivity of the arithmetic
rational-square cone. Nor does it prove that the resulting spectral measure
is purely atomic with exactly the Riemann-zero multiplicities. Required
steps are:

1. prove source positivity and perform GNS;
2. control the null space and prove the shift descends unitarily;
3. establish the Cayley-transform domain and self-adjointness;
4. identify the GNS spectral measure with the completed-zeta divisor through
   the explicit formula;
5. exclude or correctly quotient spectral mass at the singular phase `1`.

## Significance

Once the positive moment functional exists, the Hilbert--Pólya operator is
not guessed. Reflection rigidity fixes `U`, and the inverse Möbius map fixes
`H`. The hard problem has moved entirely into arithmetic positivity and
spectral identification, where it can be finitely falsified.
