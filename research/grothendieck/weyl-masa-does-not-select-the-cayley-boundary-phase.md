# The Weyl boundary algebra does not select its Cayley phase

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact boundary-selection obstruction

## Result

Passing from the rational adelic phase lattice to its Weyl representation
repairs tangent collapse. If the rational lattice is self-annihilating, its
Weyl operators generate a maximal commuting boundary algebra \(M\).

That still does not determine a self-adjoint boundary condition. In a
spectral presentation

\[
M\cong L^\infty(Y,\mu),
\]

every measurable unit-modulus function \(u:Y\to S^1\) defines a unitary
\(U_u\in M\). Whenever the Cayley denominator is defined, it produces a
self-adjoint boundary generator

\[
A_u=i(1+U_u)(1-U_u)^{-1}.
\]

Distinct phase functions produce distinct boundary generators while
preserving the same maximal algebra, rational incidence data, and cyclic
measure class.

## Smallest exact witness

On a two-atom spectral space, use the same diagonal maximal abelian algebra
and the same cyclic vector for

\[
U_1=\operatorname{diag}(i,-1),
\qquad
U_2=\operatorname{diag}(-i,-1).
\]

Their Cayley generators are self-adjoint and unequal, with different scalar
spectral polynomials. The commuting algebra does not choose between them.

## Consequence for the RH programme

The source chain cannot stop after passing from the rational lattice to its
maximal commuting Weyl algebra.

It requires one more typed operation: a source-derived phase selector inside
that algebra. This selector must come from theta or Tate boundary transport
before the determinant is evaluated. Choosing it to reproduce \(\xi\) would
be circular.

This identifies the missing comparison channel precisely. Integrality
selects which observables commute. It does not select the spectral phase by
which the two valuation sectors are glued.

## Cheapest falsifier for a proposed selector

A candidate fails if two distinct unitary phases:

1. obey every declared theta/Tate covariance;
2. preserve the rational Weyl algebra and cyclic theta state; and
3. yield different Cayley boundary generators.

The surviving target is a rigidity theorem showing that the full labelled
source, including primitive, square, seam, and archimedean channels, leaves
only one phase up to a nowhere-vanishing gauge unit.

## Scope

The nonuniqueness theorem is exact. It does not show that the completed theta
source lacks a canonical phase selector. It shows that rational maximal
isotropy, the Weyl algebra, and a cyclic state do not supply one by
themselves.

## Verification

The checker constructs two distinct self-adjoint Cayley generators in the
same finite maximal abelian algebra with the same cyclic vector.
