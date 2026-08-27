# Weyl intertwining uniquely selects the Fourier phase

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact finite metaplectic rigidity theorem

## Correct typing of the selector

A Fourier–Tate selector does not commute with the two Weyl polarizations. It
intertwines them. For a clock \(Z\), shift \(X\), and selector \(F\), the
native relations are

\[
FX=ZF,
\qquad
FZ=X^{-1}F.
\]

Suppose \(F_1\) and \(F_2\) are invertible selectors satisfying the same
relations. Their ratio \(F_2^{-1}F_1\) commutes with both \(X\) and \(Z\).
If the Weyl representation is irreducible, Schur rigidity gives

\[
F_1=cF_2.
\]

Thus polarization exchange selects the Fourier transform up to one scalar
phase.

## Source normalization removes the scalar

The finite Fourier transform sends the position delta vacuum to the uniform
momentum vacuum. Requiring this exact source normalization fixes \(c=1\).
No determinant or zero data enter.

This is stronger and better typed than requiring a boundary selector to
commute with the full Weyl pair. Commutation would erase the polarization
exchange. Intertwining expresses it.

## Adelic consequence

The adelic Schwartz–Bruhat representation already carries translations,
modulations, and the Fourier transform. The plausible source selector is
therefore the unique normalized metaplectic intertwiner between the two
polarizations, not an arbitrary unitary chosen inside one boundary algebra.

The remaining infinite-dimensional gates are:

1. formulate the uniqueness theorem on the adelic rigged test space;
2. retain the self-dual Haar and additive-character normalization;
3. prove that the rational comb normalization fixes the projective scalar;
4. show that the resulting Fourier graph is the boundary relation required
   by the doubled Dirac carrier; and
5. derive the relative determinant as the completed theta transform.

The first three are representation-theoretic. The fourth is the operator
bridge. The fifth is the RH readout bridge.

## New location of the obstacle

Phase selection is no longer mysterious at the Weyl-representation level.
The unresolved step is whether the normalized Fourier intertwiner is the
same object as the self-adjoint Lagrangian boundary relation of the proposed
Dirac system. A representation intertwiner is not automatically a boundary
condition.

## Falsifier

The route fails if either:

- two nonproportional continuous adelic intertwiners obey the complete Weyl
  exchange relations; or
- the normalized Fourier graph does not make the doubled Green boundary form
  vanish maximally.

The second test is now the cheapest decisive calculation.

## Scope

Uniqueness of the normalized intertwiner is exact in the finite irreducible
Weyl model. Its adelic rigged-space analogue is expected from the
Stone–von Neumann mechanism but has not been established here. No boundary
self-adjointness or determinant identity follows yet.

## Verification

The checker solves the exact order-three clock–shift intertwining equations,
finds a one-dimensional solution space, and verifies the vacuum
normalization of the discrete Fourier transform.
