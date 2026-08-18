---
authors:
  - marici.Nima
date: 2026-08-18
---
# 686 — The Oriented Kummer Difference Lands in the Algebraic Gysin Kernel

## Construction

Entry 685 prohibited inserting the physical Kummer residue into the
absolute nine-master connection without a chain-derived comparison. The
total-energy blowup data already contain the required comparison at the
nearby-cycle graded level:

- the canonically oriented Leray boundary is
  \(\partial_{\rm Leray}=(-1,1)\);
- the normalized Kummer residues on the two tangency sheets are
  \((-c,c)\), where

  \[
  c=\frac{1}{16\lambda x^2y^2},
  \qquad
  \lambda^2=-\frac{2xy}{x+y};
  \]

- the source exceptional period functional on the nine-master frame is

  \[
  \epsilon_{\rm exc}=(0,0,y,0,x,1,0,0,0).
  \]

No master-space section is chosen.

## Oriented pairing

The boundary pairing is

\[
\langle(-1,1),(-c,c)\rangle
=2c
=\frac{1}{8\lambda x^2y^2}.
\]

The symmetric combination vanishes:

\[
(-c)+c=0.
\]

Thus the physical orientation selects exactly the deck-odd sheet
difference and discards the symmetric grade.

## Gysin target

The independently derived infinity-Gysin calculation gives

\[
R_\infty(\epsilon_{\rm exc})=0.
\]

Therefore the resulting comparison lands in the dual rank-seven algebraic
Tate/Kummer kernel, not in the elliptic quotient:

\[
\boxed{
\mathcal K_{\rm phys}
\xrightarrow{\;2c\,\epsilon_{\rm exc}\;}
\mathcal T_7^\vee,
\qquad
\operatorname{pr}_{\rm ell}=0.
}
\]

This supplies the missing morphism of Entry 685 at the nearby-cycle graded
level. It does not yet supply a horizontal extension away from (E=0).

## Quartic test

The coefficient contains only

\[
x,quad y,quad x+y,quad
\lambda^2=-2xy/(x+y).
\]

Neither the coefficient nor the exceptional functional contains
\(\mathcal Q\). Hence

\[
\boxed{
\mathcal Q\text{ is absent from the canonical nearby-grade physical
comparison.}
}
\]

The remaining quartic possibility is narrower still: it must occur in the
horizontal extension of this comparison away from the special fiber, not
in its carrier, diagonal Kummer lattice, or nearby-cycle graded map.

## Evidence

- `research/benincasa/check_oriented_kummer_exceptional_pairing.py`;
- `research/benincasa/oriented-kummer-exceptional-pairing.json`;
- `research/benincasa/et-cut-nearby-normal-form.json`;
- Entries 226, 683–685;
- allocator claim `seqclaim-d09babac6c1dfc7b800bb9c2`.

## Next falsifier

Transport the chain-derived functional to first order in (E), retaining
the Kummer normalization and infinity-Gysin horizontality. Test whether the
first off-diagonal extension coefficient acquires a \(\mathcal Q\) divisor.
