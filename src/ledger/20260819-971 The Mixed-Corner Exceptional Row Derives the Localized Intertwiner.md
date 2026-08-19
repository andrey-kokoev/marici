# 971 — The Mixed-Corner Exceptional Row Derives the Localized Intertwiner

## Repairing Entry 970's typing gap

Entry 970 correctly rejects the identity assignment between supported corner
indices and dense six-word character indices.  The repository nevertheless
contains a source-derived comparison: Entries 907--909 construct the exact
mixed-corner exceptional row of

\[
T=M_{\rm block}K_{\rm dense}
\]

over the common conserved kinematic ring and prove its occurrence covariance.

Use that row to locate each composite factor in the dense source frame.  A
dense component belongs to a wall subquotient when it vanishes on both
branches \(U=+1\) and \(U=-1\).

## Exact zero supports

Exact Laurent specialization gives

\[
\begin{array}{c|c}
\text{factor}&\text{dense columns vanishing on both branches}\\ \hline
(ZA_2)^2-1&\{4\}\\
(ZA_2B_{24})^2-1&\{0,1\}\\
(A_3/Z)^2-1&\{5\}\\
(A_3B_{34}/Z)^2-1&\{2,3\}.
\end{array}
\]

These supports reproduce exactly the source character profiles factored in
Entry 970.

Comparing with Entry 969's occurrence blocks derives the localized map

\[
\boxed{
\begin{aligned}
\{0\}_{\rm corner}&\longmapsto\{4\}_{\rm dense},\\
\{1,2\}_{\rm corner}&\longmapsto\{0,1\}_{\rm dense},\\
\{3\}_{\rm corner}&\longmapsto\{5\}_{\rm dense},\\
\{4,5\}_{\rm corner}&\longmapsto\{2,3\}_{\rm dense}.
\end{aligned}
}
\]

The two rank-two maps are canonical as subquotient maps.  Their internal
\(GL_2\) bases remain gauge until the individual occurrence normalization is
transported through the exact mixed-corner matrix.

## Narrow conclusion

Entry 970's mismatch was a basis mismatch, not a failure of the comparison:

\[
\boxed{
\text{the exact mixed-corner exceptional row intertwines all four localized
corner defects with the dense pair-shift subquotients.}
}
\]

This is stronger than determinant agreement and uses no fitted permutation.
The map is derived from the pre-existing dense-to-block transition and tested
on both sheets of every composite wall.

It remains local on the four wall subquotients.  A global six-dimensional
intertwiner, and the internal normalization of the two repeated blocks, are
not yet fixed.

## Next falsifier

Transport the two labelled occurrences inside each rank-two block through
the cyclic/reflection conventions of Entry 909.  Determine the exact
\(2\times2\) block gauges and test their signed cyclic composition.  Then
assemble the four blocks into a global rational intertwiner and verify it
against \(T=M_{\rm block}K_{\rm dense}\).

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_composite_character_blocks.rs`;
- packet:
  `research/benincasa/string-six-point-composite-character-blocks.json`;
- source comparison:
  `research/benincasa/marici-gm/src/bin/string_six_point_mixed_corner_exact.rs`;
- verified command:
  `cargo run --quiet --bin string_six_point_composite_character_blocks`;
- allocator claim:
  `seqclaim-3151cb2be294835b4d23dc67`.
- epistemic event:
  `ev-000000000588-3b50d47b-5ee1-4033-8c2b-3ff0a38851c1`.
