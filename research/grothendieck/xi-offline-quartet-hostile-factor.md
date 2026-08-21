# Hostile quartet: symmetry and boundary sign do not exclude off-line zeros

## Construction

Use the centered coordinate `w=s-1/2`. For `a=alpha+i beta` with
`alpha!=0`, define

`Q_a(w)=(w^2-a^2)(w^2-conjugate(a)^2)`.

This polynomial inserts the quartet

`a,-a,conjugate(a),-conjugate(a)`

in centered coordinates, corresponding to the usual functional/reflection
quartet of off-critical-line zeros.

## Structures preserved

The factor is even:

`Q_a(-w)=Q_a(w)`.

It has real structure:

`Q_a(conjugate(w))=conjugate(Q_a(w))`.

On the critical boundary `w=it`,

`Q_a(it)=|t^2+a^2|^2`,

which is nonnegative and is strictly positive away from accidental boundary
collisions. Multiplying an even real entire candidate by `Q_a` therefore
preserves:

- the functional reflection symmetry;
- critical-boundary reality;
- critical-boundary sign away from zeros;
- pure-imaginary logarithmic derivative on the boundary.

Yet it introduces off-line zeros.

## Falsified explanation class

No argument using only functional symmetry, real structure, boundary sign,
or boundary skewness can prove RH. All those properties survive this hostile
deformation.

Likewise, the maximum-principle picture does not independently rule out the
quartet: the added zeros create precisely the interior poles that invalidate
the harmonic extension.

## What must reject the factor

A successful arithmetic explanation must use structure changed by `Q_a`,
such as:

- the exact Euler product or prime coefficients;
- completed growth and normalization beyond symmetry alone;
- a source-positive Herglotz representation fixed before the divisor;
- an arithmetic determinant identity that cannot absorb an arbitrary even
  positive-boundary factor.

This is a strong Deutschian falsifier. It isolates the missing content as
arithmetic rigidity rather than analytic reflection.

## Harder hostile family

Finite products of such `Q_a` factors insert any finite collection of
off-line quartets while preserving the same boundary properties. Therefore
the failure is not confined to a single exceptional deformation.
