# 1756 — Noncommuting Measurement Calibrations Produce Coefficient Curvature

## Matrix-valued normals

Replace Entry 1755's commuting scalar normal directions by infinitesimal
frame calibrations \(A,B\in\mathfrak{gl}_2\). Their action on a holonomy
matrix is the adjoint action

\[
D_A(H)=[A,H],
\qquad D_B(H)=[B,H].
\]

The two iterated mixed grades are

\[
D_AD_B(H)
\qquad\text{and}\qquad
D_BD_A(H).
\]

Their difference is fixed by the Jacobi identity:

\[
\boxed{
[D_A,D_B](H)
=D_{[A,B]}(H)
=[[A,B],H].
}
\]

Thus a nonzero mixed grade is neither an incidence defect nor an arbitrary
failure of specialization. It is the curvature of the matrix-valued
coefficient calibration.

## Scalar observability

Apply Entry 1753's four labelled scalar effects to the defect matrix

\[
C=[[A,B],H].
\]

The two diagonal evaluations recover \(C_{00},C_{11}\), while the real and
imaginary superposition effects recover

\[
C_{01}+C_{10},
\qquad
i(C_{01}-C_{10}).
\]

Therefore the same scalar tomography packet reconstructs the complete
coefficient-curvature matrix.

## Narrow result

\[
\boxed{
\text{mixed measurement grade}
=
\text{coefficient curvature } \operatorname{ad}_{[A,B]},
}
\]

for the tested adjoint calibration model.

Commuting scalar normals are the flat special case of Entry 1755.
Noncommuting normals produce a real mixed class, but its type and origin are
already determined inside the sector-specific coefficient local system.
No new Cut carrier stratum is required.

## Durable artifacts

- research/benincasa/checkers/noncommuting_calibration_curvature.rs
- research/benincasa/results/noncommuting-calibration-curvature.json
- research/benincasa/noncommuting-calibration-curvature.md

## Next falsifier

Let one calibration become singular so that its commutator curvature has a
parabolic pole. Test whether the source-derived Hom/Rees weights regularize
the curvature and whether a supported residue remains on the rank-drop
locus.
