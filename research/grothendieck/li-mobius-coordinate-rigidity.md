# The Li Möbius coordinate is forced by reflection and endpoint normalization

## Rigidity theorem

Let `u(s)=(as+b)/(cs+d)` be a nonconstant Möbius transformation. Require:

1. `u` has its pole at the arithmetic endpoint `s=0`;
2. `u(infinity)=1`;
3. functional reflection becomes inversion: `u(1-s)=u(s)^(-1)`.

Then

`u(s)=(s-1)/s=1-1/s`.

## Proof

The pole condition gives `d=0`. The normalization at infinity gives `a=c`
with `a` nonzero, so `u(s)=(as+b)/(as)`. Substitution into the intertwining
identity and comparison of polynomial coefficients gives `b=-a`. Cancelling
the common scalar yields the claimed coordinate.

Reflection then automatically exchanges the pole at `0` with the zero at
`1`, sends the fixed center `1/2` to the fixed inversion phase `-1`, and maps
the critical line to the unit circle.

## Deutschian significance

The coordinate is not fitted to the zeros or selected for a convenient Li
formula. It is fixed by three independently meaningful pieces of structure:
the endpoint, the normalization of high spectral parameter, and the
functional equation. Varying any coefficient while retaining those
requirements is impossible.

Consequently the rational-square cone

`R_p(s)=p(u(s))p(u(s)^(-1))/[s(1-s)]`

inherits a hard-to-vary status. Its inversion symmetry, critical circle, and
inverse-square coboundary weight all arise from the same rigid coordinate.

This rigidity does not establish positivity of the arithmetic explicit
formula. It prevents coordinate freedom from being used to manufacture that
positivity after the fact.
