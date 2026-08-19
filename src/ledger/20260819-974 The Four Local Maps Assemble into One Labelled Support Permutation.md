# 974 — The Four Local Maps Assemble into One Labelled Support Permutation

## Frozen local data

Entry 971 fixes the two singleton support maps and the unordered repeated
blocks.  Entry 973 fixes each repeated block to the swap (J) by preserving
its unique common source label.  No further ordering choice remains.

In corner-occurrence order

\[
(123456,124356,142356,132456,134256,143256)
\]

and dense six-word order

\[
(123456,124356,132456,134256,142356,143256),
\]

the assembled index map is

\[
\boxed{p=(4,1,0,5,3,2).}
\]

Equivalently, its four factor blocks are

\[
\begin{array}{c|c}
(ZA_2)^2-1 & 0\mapsto4\\
(ZA_2B_{24})^2-1 & (1,2)\mapsto(1,0)\\
(A_3/Z)^2-1 & 3\mapsto5\\
(A_3B_{34}/Z)^2-1 & (4,5)\mapsto(3,2).
\end{array}
\]

## Exact assembly check

The six images are distinct and exhaust the dense basis, so they define a
permutation matrix (P_{m lab}).  Its cycle decomposition is

\[
(0\ 4\ 3\ 5\ 2)(1),
\]

hence

\[
\det P_{m lab}=+1.
\]

Restricting (P_{m lab}) to each of the four factor blocks reproduces the
singleton maps of Entry 971 and the two (J)-normalized maps of Entry 973.
Thus the local maps have no obstruction at the level of labelled support and
integral orientation.

## Narrow conclusion

\[
\boxed{
\text{The four localized maps assemble uniquely into one labelled,
orientation-preserving support permutation.}
}
\]

This is not yet equality with the complete rational mixed-corner/dense
transition.  The calculation fixes only support and basis ordering; rational
unit factors and possible off-support entries remain to be derived.

## Next falsifier

Pull the exact exceptional row through (P_{m lab}).  For every occurrence
(i), divide its assigned dense component by the corresponding source wall
factor and determine whether the quotient is a regular unit on the generic
localized wall.  Failure at any component blocks rational assembly even
though support assembly succeeds.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_global_support_permutation.rs`;
- packet:
  `research/benincasa/string-six-point-global-support-permutation.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_global_support_permutation`;
- allocator claim:
  `seqclaim-de28f2d295945d73b338c5af`.
- epistemic event:
  `ev-000000000591-8196633c-5751-453d-9a18-9b8ca6b3df96`.
