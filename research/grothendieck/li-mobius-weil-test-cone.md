# Möbius pullback identifies the arithmetic Li test cone

## Exact intertwining

Define

`u(s)=1-1/s=(s-1)/s`.

The functional-equation reflection acts by

`u(1-s)=u(s)^(-1)`.

Also

`(1-u(s))(1-u(s)^(-1))=1/[s(1-s)]`.

These identities are algebraic and do not assume RH.

## Rational square cone

For a polynomial `p`, define the reflection-invariant rational test

`R_p(s)=p(u(s))p(u(s)^(-1))/[s(1-s)]`.

Then `R_p(1-s)=R_p(s)`. On the critical line, inversion of `u` is complex
conjugation and `s(1-s)=|s|^2`, so

`R_p(s)=|p(u(s))|^2/|s|^2 >= 0`.

Summing `R_p` over one representative from each functional zero pair gives
the Toeplitz energy whose moments are the second differences of the Li
coefficients. Equivalently, it is half the sum over the full divisor.

## Source formulation of Gate C

Let `W` denote the pair-normalized arithmetic explicit-formula functional
(half the full-divisor evaluation) on this rational test class. The gate is

`W(R_p) >= 0 for every polynomial p`.

This is the source-side statement corresponding to positivity of the Li
Toeplitz functional. It is now expressed entirely through a fixed Möbius
pullback and a degree-independent cone of rational squares.

The construction has three desirable rigidities:

1. the center `1/2` is forced because reflection must become inversion;
2. the inverse-square weight is forced by the coboundary factor
   `(1-u)(1-u^(-1))`;
3. multiplication of polynomials stays inside one test algebra, so higher
   Toeplitz ranks require no new test family.

## Remaining theorem

Derive `W(R_p)` explicitly from endpoint, gamma, and prime-power data and
prove it nonnegative on the entire rational square cone. Under a spectral
zero evaluation, positivity is immediate only after RH; using that evaluation
would be circular. The required proof must act on the arithmetic side.

## Falsifier

A single polynomial `p` with certified `W(R_p)<0` disproves positivity of the
cone and hence falsifies the proposed source construction. A derivation that
changes the test family with `deg(p)` or inserts zero phases is not admitted.
