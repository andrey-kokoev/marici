# C2 channel data generates the right-angle symmetry group

## Question

Can channel parity, reversal, and the right-angle metric be constructed from the explicit \(C_2\) 2-Segal model rather than appended independently?

## Parity from the coefficient group

The group \(C_2\) has one nontrivial real character:

\[
\chi(g)=(-1)^g.
\]

On the two-channel normal representation it acts as

\[
S=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Thus sign parity comes from the nontrivial character of the chosen plane-label group.

## Reversal from simplex order

The simplicial reversal reverses simplex order and inverts labels. Inversion is trivial in \(C_2\). Combined with exchange of the initial and final path-space channels, its normal action is

\[
J=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix}.
\]

Both \(S\) and \(J\) are involutions. Their product is a quarter-turn, and the matrix group they generate has order eight: it is the standard two-dimensional representation of \(D_4\).

## Metric by finite averaging

Start from any positive metric \(G_0\). Average it over the generated symmetry group:

\[
\overline G
=
\frac1{8}
\sum_{g\in D_4}g^TG_0g.
\]

The resulting metric is invariant under both parity and reversal. Direct matrix calculation gives

\[
\overline G
=
\frac{\operatorname{tr}(G_0)}2 I.
\]

Therefore the two channels are orthogonal and equally normalized up to one positive scale.

## Disposition

Within the explicit \(C_2\) model, the nontrivial character and simplicial reversal generate the \(D_4\) channel action. Averaging over that action produces the invariant metric up to scale.

The metric is no longer independent model data. The remaining model choice is the use of \(C_2\)-labelled channel geometry itself. No result currently forces arbitrary coherence-pyramid planes to carry that coefficient group.

## Verification

```text
python research/voevodsky/checkers/check_C2_source_derived_channel_symmetry.py
```

The checker verifies the character law, generates all eight symmetry matrices, and averages three exact positive seed metrics to scalar metrics.

Artifacts:

- `research/voevodsky/checkers/check_C2_source_derived_channel_symmetry.py`
- `research/voevodsky/results/C2_source_derived_channel_symmetry.json`
