# 970 — Determinant Agreement Does Not Identify the Pair-Shift Subquotients

## Frozen character blocks

The dense source checker decomposes the six-word columns into pair-shift
character supports

\[
\chi_{--}:\{0,2\},\qquad
\chi_{-+}:\{1\},\qquad
\chi_{+-}:\{3\},\qquad
\chi_{++}:\{4,5\}.
\]

To compare Entry 969 with this source object, factor the four source block
minors separately rather than reading only their product.

## Source wall profiles

In character order

\[
(\chi_{--},\chi_{-+},\chi_{+-},\chi_{++}),
\]

the composite factors occur in the frozen source minors with profiles

\[
\begin{array}{c|c}
(ZA_2)^2-1&(0,0,0,1)\\
(ZA_2B_{24})^2-1&(1,1,0,0)\\
(A_3/Z)^2-1&(0,0,0,1)\\
(A_3B_{34}/Z)^2-1&(1,0,1,0).
\end{array}
\]

By contrast, assigning Entry 969's six occurrence indices directly to the
six-word character supports gives

\[
\begin{array}{c|c}
(ZA_2)^2-1&(1,0,0,0)\\
(ZA_2B_{24})^2-1&(1,1,0,0)\\
(A_3/Z)^2-1&(0,0,1,0)\\
(A_3B_{34}/Z)^2-1&(0,0,0,2).
\end{array}
\]

Only the \(ZA_2B_{24}\) profile agrees.

## Correction

The occurrence basis of Entry 967 is a supported corner basis.  It was not
derived as the pair-shift character basis of the dense six-word source.  The
profile mismatch proves that identifying their column indices is invalid:

\[
\boxed{
\text{determinant and corank agreement do not identify the localized
pair-shift subquotients.}
}
\]

Entries 967--969 remain valid as statements about the loaded corner
comparison and its determinant.  They do not yet establish equality with the
dense source transition as a character-equivariant map.

This is a comparison-basis defect, not new carrier support.  No wall or
coefficient summand should be added to force the profiles to agree.

## Next falsifier

Derive an actual intertwiner

\[
J:\mathcal L_{\rm corner}\longrightarrow\mathcal L_{\rm dense}
\]

from source residue/period data.  Require it to conjugate the pair-shift
action and transport each localized kernel into the source block carrying
the same factor.  If no such source-derived \(J\) exists, retain the loaded
corner object and dense source object as determinant-equivalent but
nonidentified coefficient lattices.

Do not solve for an arbitrary rational matrix from the four desired profiles.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_composite_character_blocks.rs`;
- packet:
  `research/benincasa/string-six-point-composite-character-blocks.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_composite_character_blocks`;
- allocator claim:
  `seqclaim-0140e5fd7c826f8e552525aa`.
- epistemic event:
  `ev-000000000587-04673314-1619-4c68-8224-28734df56835`.
