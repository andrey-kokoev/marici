---
id: 559
date: 2026-08-18
title: The Resolved Four-Plus-One Boundary Packet Is Not Deck-Character Pure
authors:
  - marici.Benincasa
---

# The Resolved Four-Plus-One Boundary Packet Is Not Deck-Character Pure

Entry 558 constructs a genuine rank-five integer-contiguity residue cone.
Before comparing it with Entry 549's resolved \(4+1\) packet, this entry applies
the square-root deck-character gate required by the physical Cayley--Menger
coefficient.

## Deck action

On the double cover \(w^2=K|_{q_{g1}}\), the deck involution is

\[
\tau:w\longmapsto-w.
\]

It exchanges the two sheet components,

\[
\tau(D_+)=D_-,
\qquad
\tau(D_-)=D_+.
\]

Each exceptional curve over an \(A_1\) point is preserved as a component, so
its component class is invariant. On the \(K_{2,2}\) dual graph, exchanging
the two sheet vertices reverses the unique cycle. Hence

\[
\tau(E_+)=E_+,
\quad
\tau(E_-)=E_-,
\quad
\tau(\gamma)=-\gamma.
\]

In the basis \((D_+,D_-,E_+,E_-,\gamma)\), the character dimensions are

\[
\boxed{
\dim B^+=3,
\qquad
\dim B^-=2.
}
\]

Explicitly,

\[
B^+=\langle D_++D_-,E_+,E_-\rangle,
\qquad
B^-=\langle D_+-D_-,\gamma\rangle.
\]

## Physical coefficient gate

The source square-root residue form has the shape

\[
\Omega=\frac{da\wedge db}{w},
\]

and is anti-invariant:

\[
\tau^*\Omega=-\Omega.
\]

Therefore an equivariant comparison from the physical square-root sector to
the raw boundary packet can land only in \(B^-\), whose rank is two. It cannot
be an isomorphism onto the full rank-five packet:

\[
\boxed{
\text{physical anti-invariant rank-five object}
\not\simeq
B^+\oplus B^-.
}
\]

## Scope and correction

This does not contradict Entry 558's generic integer-contiguity cone. The
finite-field exponent \(5\) used for critical counting is a generic rank
probe, whereas the physical Cayley--Menger realization fixes the square-root
character. Passing from generic rank data to the physical deck sector requires
an equivariant realization functor.

Entry 549's raw \(4+1\) packet therefore cannot itself be the physical
rank-five coefficient object. At best it is an unprojected support associated
grade. The next calculation must construct the deck-equivariant logarithmic
boundary complex, including coefficient twists. If twisting changes the
equivariant structure, that change must be derived from \(1/w\); otherwise the
physical boundary image has rank at most two and the remaining classes are
interior or extension data.

The executable audit is
`research/benincasa/marici-gm/src/bin/generic_lower_boundary_deck_characters.rs`.
