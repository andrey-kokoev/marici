# Independent-block Cut coproduct of the cubic cumulant generator

For independent centered Gaussian blocks, set

\[
Q=\sum_iw_iQ_i,
\qquad
A=\sum_iw_i^2a_i.
\]

The collective centered cubic shear decomposes exactly as

\[
-t(Q^2-A)
=-t\sum_iw_i^2(Q_i^2-a_i)
-2t\sum_{i<j}w_iw_jQ_iQ_j.
\]

The first term is obtained by evolving block `i` for time `tw_i` before the
weighted merge.  The second is the labelled mixed cocycle of Entries
1694--1695.

Since `Q` is Gaussian with variance `A`, this operator identity reconstructs
Entry 1708's complete generating germ with `a` replaced by `A`.  Multinomial
expansion of powers of `A` supplies every pure and mixed labelled cumulant
slot; no coefficientwise fitting is needed.
