# 1589 — The Independent Cubic Dyson Kernel Has Three Statistical Placements

## Hostile correction to Entry 1588

Entry 1588 identified the left Dyson leg, middle self-energy kernel, and
right Dyson leg.  Restore independent CTP matrices

\[
G_L,qquad G_M,qquad G_R
\]

subject only to their separate largest-time identities.

## Exact result

The signed cubic composition still has zero CTP defect.  In the
retarded/advanced/statistical basis, Symbolica gives

\[
\boxed{
R_{\rm out}=2R_LR_MR_R,
\qquad
A_{\rm out}=2A_LA_MA_R,
}
\]

\[
\boxed{
F_{\rm out}
=2(F_LA_MA_R+R_LF_MA_R+R_LR_MF_R).
}
\]

Therefore the rank-three Gaussian/Keldysh coefficient object is preserved
without collapsing the three kernel labels.

## Occurrence interpretation

The statistical coordinate occurs in exactly one of three labelled
positions: left, middle, or right.  Their sum is forced by contour matrix
composition.  No unlabelled multiplicity was inserted.

The generic occupation ratio is not fixed.  Entry 1588's ratio preservation
is recovered only after identifying all three kernels and is narrowed to that
diagonal specialization.

## Classification

\[
\boxed{
\text{existing doubled contour carrier}
+\text{three occurrence-resolved coefficient placements};
\quad\text{no new coefficient rank or carrier cell}.
}
\]

## Next falsifier

Substitute the source Wightman functions and restore one actual internal-time
domain.  Test endpoint orientation and ultraviolet order separately for the
three statistical placements after Bunch--Davies subtraction.

## Artifacts

- `research/benincasa/marici-gm/src/bin/gaussian_cubic_dyson_contour.rs`
- `research/benincasa/three-placement-keldysh-dyson.md`
- `research/benincasa/results/three-placement-keldysh-dyson.json`

Ledger sequence claim: `seqclaim-7a8f932e51eca0e7eb3cf99d`.
