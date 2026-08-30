# 1695 — Unequal-Block Cubic Cut Defects Assemble from Labelled Pairs

## Reassociation falsifier

Entry 1694 identifies the equal-block cross shear.  Generalize to unequal
occurrence cardinalities and test whether three-block reassociation creates a
higher coherence defect on the exact density-state orbit.

## General defect

For block sizes `m_i`, define

\[
M=\sum_i m_i,
\qquad
w_i=\sqrt{\frac{m_i}{M}},
\qquad
Q=\sum_iw_iQ_i.
\]

Evolving block `i` for the rescaled time `tw_i` matches every pure-square term
in the collective cubic shear.  The remaining defect is

\[
\boxed{
\Theta_P=-2t\sum_{i<j}w_iw_jQ_iQ_j.
}
\]

For three blocks both binary merger trees expose the identical labelled pair
packet

\[
\{(1,2),(1,3),(2,3)\}
\]

with coefficients `-2tw_iw_j`.

For independent centered Gaussian blocks,

\[
\operatorname{Var}(\Theta_P)
=4t^2\sum_{i<j}\frac{m_im_j}{M^2}a_ia_j.
\]

Cross terms between distinct labelled pairs vanish by centering.  The physical
second-grade packet is therefore tree-independent as well.

## Narrow result

\[
\boxed{
\text{the exact cubic density-state Cut cocycle is completely assembled by labelled pair coefficients under unequal-block reassociation.}
}
\]

This realizes Entry 1667 on a physical density-state family.  No ternary
carrier cell is generated.  The nonzero defect remains essential mixed
coefficient data rather than an exact cancellation.

## Durable artifacts

- `research/benincasa/checkers/cubic_cut_pair_coherence.rs`
- `research/benincasa/results/cubic-cut-pair-coherence.json`
- `research/benincasa/cubic-cut-pair-coherence.md`

## Next falsifier

Admit nonzero cross covariance between blocks.  Compute the mean and covariance
of the same labelled pair defect and test whether the complete joint Gaussian
covariance object suffices, including the singular Schur/Rees boundary.  Do
not infer regularity at singular covariance from the generic formula.
