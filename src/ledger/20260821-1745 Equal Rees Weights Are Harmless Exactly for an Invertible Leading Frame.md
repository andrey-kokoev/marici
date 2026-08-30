# 1745 — Equal Rees Weights Are Harmless Exactly for an Invertible Leading Frame

## Repeated-weight test

Let both labelled reference columns vanish to first order:

\[
F_\varepsilon=\varepsilon F_0.
\]

When the leading frame (F_0) is invertible,

\[
\boxed{F_\varepsilon^{-1}HF_\varepsilon=F_0^{-1}HF_0.}
\]

The common Rees factor cancels. Therefore repeated weight does not itself
produce a singular matrix readout, a flag, or an excess class. The labelled
leading frame recovers the full based holonomy.

If the leading labels are discarded, a frame change (F_0\mapsto F_0S)
acts by

\[
F_0^{-1}HF_0\longmapsto S^{-1}(F_0^{-1}HF_0)S.
\]

Only the conjugacy class then descends. This loss is caused by forgetting
occurrence data, not by the repeated Rees weight.

## Rank-deficient contrast

Consider instead

\[
F_\varepsilon=
\varepsilon\begin{pmatrix}1&1\\0&\varepsilon\end{pmatrix}.
\]

Both columns have first valuation one, but the leading frame has rank one.
The source-derived operation (c_2\leftarrow c_2-c_1) yields

\[
(c_1,c_2-c_1)
=
\left(
\varepsilon\binom10,
\varepsilon^2\binom01
\right),
\]

so the complete valuation filtration has weights ((1,2)). The next jet
canonically refines the apparently repeated grade; choosing a split inside
the rank-one leading image would be post hoc.

## Narrow result

\[
\boxed{
\text{Repeated reference weight is harmless iff the labelled leading frame is invertible.}
}
\]

At rank drop, the correct object is the higher-jet/Smith filtration of the
source frame. This remains coefficient/readout data over the existing Cut
carrier. No new carrier stratum is indicated.

## Durable artifacts

- `research/benincasa/checkers/equal_weight_leading_frame.rs`
- `research/benincasa/results/equal-weight-leading-frame.json`
- `research/benincasa/equal-weight-leading-frame.md`

## Next falsifier

Test a rank-one leading frame whose second jet rotates along a loop. Determine
whether its refined line has intrinsic monodromy and whether the full labelled
jet packet recovers it without choosing a local Smith basis.
