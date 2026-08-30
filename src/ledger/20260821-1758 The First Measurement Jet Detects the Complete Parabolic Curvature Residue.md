# 1758 — The First Measurement Jet Detects the Complete Parabolic Curvature Residue

## Typed bi-Rees packet

Keep two normals distinct:

- \(x\): singular calibration/parabolic support;
- \(\delta\): degeneration of the scalar measurement frame.

Entry 1757 constructs

\[
R_{\rm par}
=\left.x[[A_x,B],H]\right|_{x=0}.
\]

Write its entries as \(R_{ij}\). At \(\delta=0\), the rank-three scalar
packet records

\[
R_{00},\qquad R_{11},\qquad R_{01}+R_{10}.
\]

The first measurement grade of the effect

\[
|0\rangle+(1+i\delta)|1\rangle
\]

is

\[
\boxed{
\operatorname{gr}^{(0,1)}_\delta
=i(R_{01}-R_{10}).
}
\]

Therefore

\[
2R_{01}
=(R_{01}+R_{10})-i\bigl(i(R_{01}-R_{10})\bigr),
\]

\[
2R_{10}
=(R_{01}+R_{10})+i\bigl(i(R_{01}-R_{10})\bigr).
\]

All four entries of the supported curvature residue are recovered.

## Narrow result

The supported coefficient class of Entry 1757 remains fully observable even
when the scalar measurement frame degenerates:

\[
\boxed{
\text{ordinary rank-three readout of }R_{\rm par}
+
\text{one first measurement jet}
=
\text{complete supported curvature}.
}
\]

No higher measurement grade and no post hoc splitting are required. The
calibration and measurement normals are retained separately, because they
carry different variance: one locates support, the other restores readout
rank.

This is a bi-filtered coefficient/readout statement over the existing
rank-drop carrier.

## Durable artifacts

- research/benincasa/checkers/parabolic_residue_tomography.rs
- research/benincasa/results/parabolic-residue-tomography.json
- research/benincasa/parabolic-residue-tomography.md

## Next falsifier

Pull the bi-Rees packet to the diagonal \(\delta=x\). Determine whether the
diagonal first coefficient canonically separates measurement-jet detection
of \(R_{\rm par}\) from the finite part of the calibration curvature, or
whether a filtered extension remains.
