# 3848 — The Two Active Conductors Span a Rank-Two Residue Plane

## Falsifier

The logarithmic-jet conjecture would weaken substantially if one kinematics-independent linear combination annihilated both active conductor residues. The physical readout could then descend to a canonical scalar combination despite ambiguous individual finite parts.

Test the residue vectors at two exact strict-triangle points.

At ((2,3,4)),

\[
v_{234}=
\left(
\frac{16}{99225}-\frac{\sqrt{46}}{101430},
\frac1{2025}-\frac{\sqrt{94}}{28200}
\right).
\]

At ((3,4,5)),

\[
v_{345}=
\left(
\frac5{124416}-\frac{\sqrt{10}}{311040},
\frac5{55296}-\frac{11\sqrt{17}}{940032}
\right).
\]

Their determinant has the certified strict enclosure

\[
\det(v_{234},v_{345})
=-5.23163832242\ldots\times10^{-10}<0.
\]

The enclosure uses exact thirty-decimal rational bounds for every radical, not floating-point sign inference.

## Result

The residue vectors are linearly independent. No nonzero kinematics-independent linear combination annihilates both active conductor costalks.

Thus the simplest scalar-descending falsifier fails. The source carries a genuine rank-two logarithmic residue plane over generic strict-triangle kinematics.

This does not prove the complete logarithmic-jet conjecture. A nonlinear relation, source-derived renormalization section, or independently normalized physical observable could still reduce the ambiguity.

## Source-normalization audit

The marked wall coordinates are source-normalized linear energy forms, but the primary contour prescription fixes only the signs of their imaginary parts, not their magnitudes. Therefore fixed polynomial normalization alone does not select the finite logarithmic section.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_conductor_residue_plane_rank.py`
- `research/benincasa/results/rank26-conductor-residue-plane-rank.json`

## Next falsifier

Classify the local counterterm or subtraction characters permitted by the primary one-loop source. Determine whether they act transitively on this rank-two residue plane, preserve a nonzero quotient, or are fixed by an independent normalization condition.
