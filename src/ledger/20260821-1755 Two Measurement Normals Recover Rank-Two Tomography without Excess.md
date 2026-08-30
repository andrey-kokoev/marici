# 1755 — Two Measurement Normals Recover Rank-Two Tomography without Excess

## Simultaneous rank loss

Let one labelled rank-one effect vary as

\[
|v_{\varepsilon,\eta}\rangle
=|0\rangle+(\varepsilon+i\eta)|1\rangle.
\]

At \((\varepsilon,\eta)=(0,0)\), it coincides with the \(|0\rangle\) effect.
Together with the independent \(|1\rangle\) effect, the ordinary packet has
rank two and retains only \(h_{00},h_{11}\).

The exact two-normal expansion is

\[
\boxed{
q_{\varepsilon,\eta}
=h_{00}
+\varepsilon(h_{01}+h_{10})
+i\eta(h_{01}-h_{10})
+(\varepsilon^2+\eta^2)h_{11}.
}
\]

Hence

\[
\operatorname{gr}^{(1,0)}q=h_{01}+h_{10},
\qquad
\operatorname{gr}^{(0,1)}q=i(h_{01}-h_{10}).
\]

These two labelled first grades recover both off-diagonal entries:

\[
2h_{01}
=\operatorname{gr}^{(1,0)}q
-i\operatorname{gr}^{(0,1)}q,
\]

\[
2h_{10}
=\operatorname{gr}^{(1,0)}q
+i\operatorname{gr}^{(0,1)}q.
\]

## Mixed-grade test

The expansion has no \(\varepsilon\eta\) term:

\[
\boxed{
\operatorname{gr}^{(1,1)}q=0.
}
\]

Therefore the two specialization orders commute. The pure second grades both
contain the already known \(h_{11}\); they introduce no additional
tomographic direction.

## Narrow result

A codimension-two tomographic rank loss closes under the existing labelled
multi-Rees calculus:

\[
\text{rank-two ordinary packet}
+
\text{two independent first grades}
=
\text{complete rank-four readout}.
\]

There is no mixed commutator and no excess coefficient class in this tested
rank-one measurement family. No new carrier stratum is required.

## Durable artifacts

- research/benincasa/checkers/two_normal_tomography.rs
- research/benincasa/results/two-normal-tomography.json
- research/benincasa/two-normal-tomography.md

## Next falsifier

Replace the scalar measurement parameters by a noncommuting matrix-valued
calibration acting on the effect frame. Compute whether the mixed grade is
the calibration commutator and classify it as coefficient curvature rather
than carrier excess.
