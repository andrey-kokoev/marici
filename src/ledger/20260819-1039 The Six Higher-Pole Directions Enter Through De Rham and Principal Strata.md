# The Six Higher-Pole Directions Enter Through De Rham and Principal Strata

## Intrinsic source filtration

Entry 1035 gives the exact short rank census

\[
E_2^{(2)}\hookrightarrow E_2^{(3)},
\qquad
\dim E_2^{(2)}=7,
\qquad
\dim E_2^{(3)}=13.
\]

To type the six-dimensional cokernel without using elimination-family
witnesses, the depth-three source presentation was ordered by genuine nested
source strata:

\[
F_0=C^{k\le2},
\]

followed by

\[
d_{\rm dR}^{k=2},
\quad
K^{k=2},
\quad
q_1^{k=3},q_2^{k=3},q_3^{k=3},q_{23}^{k=3},q_{31}^{k=3}.
\]

The ambient depth-three columns are retained at every stage, so this is a
filtration by labelled source relation submodules rather than a sequence of
projected quotient bases.

## Cumulative exact ranks

The exact cumulative ranks over \(\mathbf F_{32003}\) are

\[
\begin{array}{c|c|c|c}
\text{stage}&R_0&n_1&n_2\\
\hline
F_0&6305&5&7\\
+d_{\rm dR}^{k=2}&6410&15&8\\
+K^{k=2}&7290&7&13\\
+q_1^{k=3}&7834&7&13\\
+q_2^{k=3}&8138&7&13\\
+q_3^{k=3}&8306&7&13\\
+q_{23}^{k=3}&8398&7&13\\
+q_{31}^{k=3}&8448&7&13.
\end{array}
\]

Thus the exact-valuation-two rank evolves as

\[
\boxed{
7\xrightarrow{d_{\rm dR}^{k=2}}8
\xrightarrow{K^{k=2}}13
\xrightarrow{q_i^{k=3}}13.
}
\]

One new direction first appears when the higher-\(K\)-pole de Rham relations
are admitted.  Five more appear when the higher-\(K\)-pole principal
relations are admitted.  None of the new marked-pole strata changes the
exact-valuation-two rank.

## Meaning

The six-dimensional cokernel is not new marked-divisor data.  It is exposed
entirely by extending the Cayley--Menger pole resolution while the complete
depth-two marked packet is already present.  Its intrinsic source filtration
has candidate associated ranks

\[
\boxed{1+5}.
\]

This is compatible with a de Rham boundary direction followed by five
principal descendants, but that interpretation is not yet proved.  The
first-normal rank temporarily rises from five to fifteen at the de Rham
stage and falls to seven after the principal relations enter, showing that
the two strata participate in a nontrivial coherence cancellation rather
than two independent direct summands.

## Boundary

Only the cumulative dimensions have been computed at the two intermediate
stages.  Entry 1035 proves injection from the initial seven-plane into the
final thirteen-plane, but the maps

\[
E_2(F_0)\to E_2(F_1)\to E_2(F_2)
\]

have not separately been reduced.  Therefore \(1+5\) is an intrinsic
filtration profile, not yet a split cokernel decomposition.

The next finite test is to compute those two transition maps.  If both are
injective, the cokernel has associated graded dimensions \((1,5)\).  If the
middle map has kernel, the transient class is replaced during principal
coherence and the final six-plane has a different extension structure.

## Durable verification

- filtration exporter:
  `research/nima/export_triangle_wall_dual_rows.py`;
- sparse rank engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- result packet:
  `research/nima/triangle-wall-kdepth3-rank.json`;
- allocator claim: `seqclaim-8a65ff4701a88b0a2d46c384`.
