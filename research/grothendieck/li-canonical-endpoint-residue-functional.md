# Canonical endpoint extension by the completed-xi logarithmic derivative

## Definition

Let `L(s)=xi'(s)/xi(s)` for the completed entire xi function. Since
`xi(0)=xi(1)` is nonzero, `L` is holomorphic at both endpoints. For a
rational-square test `R_p`, define its full-divisor endpoint functional by

`D(R_p)=-Res_(s=0) R_p(s)L(s)-Res_(s=1) R_p(s)L(s)`.

The signs are those obtained by moving the endpoint poles to the other side
of the argument-principle contour identity. Under the usual symmetric
contour limit, this equals the sum of `R_p` over the full completed-xi
divisor. The Li Toeplitz energy uses one representative per reflection pair,
so its normalized source functional is `E(p)=D(R_p)/2`.

## Reflection rigidity

The functional equation gives

`L(1-s)=-L(s)`.

Since `R_p(1-s)=R_p(s)`, the two endpoint residues are equal. Therefore

`D(R_p)=-2 Res_(s=0) R_p(s)L(s)`,

and consequently `E(p)=-Res_(s=0) R_p(s)L(s)`.

No cutoff, coordinate-dependent constant term, or rank-dependent subtraction
is introduced.

## Finite-jet property

For `deg(p)=d`, `R_p` has endpoint pole order `d+1`. Its residue against the
holomorphic `L` depends exactly on the jets

`L(0),L'(0),...,L^(d)(0)`.

These are completed-zeta endpoint data. Reflection supplies the other
endpoint automatically. This explains why the degree-`d` Toeplitz energy is
controlled by finitely many completed-zeta derivatives while all degrees are
governed by one common functional.

## Status of the contour step

The local residue prescription is canonical and exact. A full theorem still
must specify an exhausting symmetric contour, prove the boundary integral
vanishes or identify its limit, and justify convergence of the divisor sum
for every rational-square test. The `s^(-2)` decay of `R_p` at infinity is
favorable, but these analytic estimates must not be replaced by formal
residue notation.

## Remaining positivity problem

The residue functional is not manifestly positive on the arithmetic side.
It makes the question well-defined and eliminates counterterm freedom:

`E(p) >= 0 for every polynomial p`.

Proving this remains RH-equivalent. Splitting `L` into zeta, gamma, and
endpoint pieces must preserve the already-fixed residue prescription.

This is a scalar meromorphic-contour construction and makes no claim about a
physical relative-chain pushforward.
