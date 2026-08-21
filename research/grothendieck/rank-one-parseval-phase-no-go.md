# Rank-one Parseval weighting is only phase encoding

Consider the smallest analytic relative-complement factorization over a real
interval,

```
c(T)^2 + q(T)^2 = 1.                                   (1)
```

Locally, and globally after lifting on a simply connected interval, this is

```
c(T)=cos theta(T),             q(T)=sin theta(T).       (2)
```

The transfer defect is `q(T)^2`, while the oriented first-order determinant
is `q(T)`. Its zeros are precisely the phase-level condition

```
theta(T) in pi Z.                                      (3)
```

This has the desired local multiplicity: a transverse phase crossing gives a
simple zero of `q` and a double zero of `q^2`. But it explains no zero set
unless `theta` is independently derived. Indeed the rational parametrization

```
c=(1-u^2)/(1+u^2),          q=2u/(1+u^2)               (4)
```

turns every chosen analytic function `u` into a Parseval pair with exactly
the prescribed zeros of `u`. Positivity and complementarity alone therefore
have zero discriminatory power over rank-one zero sets.

## Audit of the canonical scalar phases

The archimedean gamma factor supplies the independently derived
Riemann--Siegel phase `vartheta(T)`. Using it in (2) produces the smooth
Gram-type phase levels. It does not include the arithmetic amplitude
interference that distinguishes the Riemann zeros.

The most canonical scalar prime phase does not repair this. On the critical
line, the continued prime scattering ratio and the archimedean scattering
ratio are inverse by the completed functional equation. Their product is
identically one away from zeros and continues as the identity through them.
Thus the corresponding gluing condition is true for every height, not only
at Riemann zeros. Reversing one orientation merely quantizes a smooth doubled
archimedean phase.

So the two obvious source choices fail in opposite ways:

- archimedean phase alone is too sparse and smooth;
- canonical scalar prime--archimedean gluing collapses to an identity.

Choosing `theta(T)=arcsin(normalized Xi(T))`, or any equivalent phase built
from Xi or its zeros, passes the algebraic identity but is tautological.

## Consequence

A rank-one two-branch Parseval correspondence cannot be the explanatory
object. Zero production must survive before scalarization, through at least
one of:

1. a matrix-valued transfer whose determinant records interference among
   independent channels;
2. a nontrivial relative complex whose torsion is not a single phase level;
3. a global regularized determinant coupling prime and archimedean sectors
   without multiplying their reciprocal scalar scattering phases.

The first option is the smallest finite hostile target: a two-channel
oriented `Q(T)` whose entries are independently source-derived and whose
determinant is not reducible to one inserted scalar phase.

## Falsifier

Any rank-one proposal must state its independent derivation of `theta`. It
fails if changing an arbitrary analytic input `u` in (4) can change the zero
set without violating any source axiom, or if its prime and archimedean
phases multiply to the functional-equation identity.

This is a structural no-go, not an assertion that scalar functions cannot
represent Xi. They can do so trivially; the point is that they do not explain
it under the Deutschian noncircularity criterion.
