# 973 — Source Labels Fix Both Repeated-Block Orderings

## Residual gauge from Entry 972

Occurrence covariance leaves the unsigned choices \(I\) and \(J\) in each
repeated rank-two wall block.  This ambiguity may be resolved only by data
already present before the comparison.  Use the source chamber labels carried
by the corner occurrences and by the dense zero supports of Entry 971.

## The \(ZA_2B_{24}\) block

The two corner occurrences are ordered by their host chambers as

\[
(124356,142356),
\]

while the dense zero support is

\[
(123456,124356).
\]

Their intersection contains exactly one labelled occurrence:

\[
\{124356,142356\}\cap\{123456,124356\}
=\{124356\}.
\]

The identity gauge matches no label.  The swap gauge \(J\) sends the first
corner occurrence to the uniquely common dense label \(124356\).

## The \(A_3B_{34}/Z\) block

Here the corner hosts and dense support are

\[
(134256,143256),
\qquad
(132456,134256).
\]

Again the intersection is a singleton,

\[
\{134256\},
\]

and only the swap gauge preserves it.

Therefore the source-labelled internal gauges are

\[
\boxed{(P_{24},P_{34})=(J,J).}
\]

## Narrow conclusion

The residual unsigned \((\mathbb Z/2)^2\) of Entry 972 becomes trivial once
the source occurrence labels are retained.  This is not a host-maximization
fit: each block has one and only one common labelled occurrence, and the
allowed covariance centralizer contains one and only one unsigned gauge that
preserves it.

Overall residue orientations remain conventional signs, already classified
as unimodular gauges in Entry 968.

Thus the four localized subquotient maps now have source-derived internal
orderings.  What remains is their global rational assembly and equality with
the complete dense-to-block transition.

## Next falsifier

Assemble the singleton maps and the two \(J\)-normalized repeated blocks into
a global six-by-six permutation/intertwiner.  Compose it with Entry 967's
loaded diagonal normal form and compare with the exact mixed-corner/dense
transition over the common conserved kinematic ring.  Verify every component,
not only determinant and zero support.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_repeated_block_gauge.rs`;
- packet:
  `research/benincasa/string-six-point-repeated-block-gauge.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_repeated_block_gauge`;
- allocator claim:
  `seqclaim-9bce0c9e7bcce8100adb96d7`.
- epistemic event:
  `ev-000000000590-1414f83d-c76f-4390-a624-76edf3c8eaf1`.
