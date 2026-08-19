# 989 — Two Pairwise Source-Wall Fibers Recombine the Character Lines

## Pairwise fiber census

Entry 988 showed that the global (+1/-1) character splitting survives every generic single source wall.  Intersect the four distinct wall equations pairwise, retain all four signed-sheet choices, and compute the exact rank of the two specialized eigendirections.

This is a fiber calculation.  It does not yet compare two ordered residue or Gysin maps.

## Result

Four of the six pair types preserve rank two for both characters and every sign choice.  Exactly two character-selective intersections collapse to rank one:

\[
\boxed{
\chi=++:
\quad
(ZA_2)^2=1,
\qquad
(A_3/Z)^2=1,
}
\]

and

\[
\boxed{
\chi=--:
\quad
(ZA_2B_{24})^2=1,
\qquad
(A_3B_{34}/Z)^2=1.
}
\]

The collapse is independent of the two signed-sheet choices.

At the (++) intersection,

\[
\mathcal L_{++,-}
=
\frac{1+A_2^2}{A_2^2-1}
\mathcal L_{++,+}.
\]

At the (--) intersection,

\[
\mathcal L_{--,-}
=
\frac{1+A_2^2B_{24}^2}{A_2^2B_{24}^2-1}
\mathcal L_{--,+}.
\]

These identities hold as exact six-word vector identities on the corresponding generic intersection fibers.

## Interpretation

The global interior splitting and every single-wall specialization are valid, but the two line lattices are not transverse on two existing codimension-two carrier strata.

\[
\boxed{
\text{first supported recombination occurs at two pairwise source-wall intersections.}
}
\]

No new carrier stratum is indicated: both loci are intersections of already frozen source walls.  What fails is extension of the direct-sum splitting as two everywhere-transverse boundary line lattices.

This is not yet a Beck--Chevalley obstruction.  A rank-one common fiber can be compatible with commuting ordered residues, or can support a nontrivial excess/extension class.  The ordered maps and their orientations must be derived before deciding.

## Next falsifier

At each of the two recombination loci, derive the two ordered source residue maps and compare them in the common rank-one fiber.  Compute the excess scalar, orientation sign, and any Tor class.  Only a nonzero typed commutator or excess class constitutes a localization/Gysin obstruction.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_character_plane_reflection.rs`
- `research/benincasa/string-six-point-character-plane-reflection.json`

The checker parametrizes all six pair types on every signed sheet, substitutes into both exact eigendirections, computes all projective minors, and derives the collapse scalar when rank one occurs.

Epistemic graph event: `ev-000000000606-c1da9378-191c-45d0-a83d-509d11afa5d9`.
