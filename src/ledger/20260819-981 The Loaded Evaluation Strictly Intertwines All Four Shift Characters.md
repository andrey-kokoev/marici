# 981 — The Loaded Evaluation Strictly Intertwines All Four Shift Characters

## Canonical comparison map

Entry 980 finds the same four pair-shift characters on the exceptional
cochain as on the existing source architecture. Representation type alone
does not identify the modules. The frozen comparison map is right evaluation
by Entry 967's loaded matrix:

\[
\mathcal E_C:\lambda\longmapsto\lambda C.
\]

Every nonzero entry of (C) is one of the composite factors

\[
(ZA_2)^2-1,quad
(ZA_2B_{24})^2-1,quad
(A_3/Z)^2-1,quad
(A_3B_{34}/Z)^2-1.
\]

Consequently (C) is invariant under all four integer sign shifts

\[
A_2, A_3, B_{24}, B_{34}\mapsto
-A_2, -A_3, -B_{24}, -B_{34}.
\]

## Exact intertwining

For each generator (T), exact reduction gives

\[
\boxed{(T\lambda)C=T(\lambda C).}
\]

Project onto each pair-shift character

\[
(++),quad(-+),quad(+-),quad(--).
\]

All four source projectors and all four images are nonzero. In the natural
image bases the four comparison scalars are exactly

\[
\boxed{(1,1,1,1).}
\]

Since (C) is generically invertible by Entry 967, the evaluation is a
generic isomorphism on the full four-character orbit.

## Narrow conclusion

\[
\boxed{
\mathcal E_C
\text{ is a strict deck-equivariant comparison with no characterwise
zero, pole, or extra unit.}
}
\]

Thus the exceptional cochain and its loaded occurrence-source image are the
same discrete coefficient object under a source-derived map.

This does not yet identify that occurrence image with Entry 931's
independently defined normal-symbol row. They have the same character
representation, but equality or a canonical intertwiner remains to be
tested.

## Next falsifier

Compare the four character projectors of \(\lambda C\) with the four
projectors of Entry 931's normal-symbol row in their common six-word ordering.
Test proportionality character by character and factor every scalar. If a
character has rank two rather than one, matching deck representations do not
identify the coefficient objects.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_loaded_evaluation_shift.rs;
- packet:
  research/benincasa/string-six-point-loaded-evaluation-shift.json;
- verified command:
  cargo run --quiet --bin string_six_point_loaded_evaluation_shift;
- allocator claim:
  seqclaim-c315ff06253d76131ca1532b.
- epistemic event:
  ev-000000000598-09717a40-858b-4275-bfde-627e3cc794f6.
