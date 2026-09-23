# Full nonlinear C/D pushed pole cancels on the regular `w₄=0` facet

The leading common-target C/D ray cancellation extends to the **full nonlinear pushed eight-forms** on the generic positive boundary `w₄=0`, **provided `t>u>0`**. This is the boundary *away from* the further singular corner `t=u`.

C and D are two explicitly positive eight-cells of the four-cell square. Their intrinsic top-cell residue eight-forms have **exactly opposite orientations**. At `w₄=0` their **entire source matrices and fermionic numerators agree**. Seven source-to-target Jacobian columns tangent to the shared boundary are identical. Wherever both `8×8` target Jacobians are nonzero, Cramer's cofactor identity makes the pushed simple-pole residues **equal and opposite for any regular transverse target direction and every SU(4) component**.

Three distinct exact positive boundary points, each tested in two transverse target directions, have nonzero Jacobians and pass the cancellation. Hence this is a **generic-open full nonlinear local target-facet statement**, stronger than the preceding leading corner normal-form check. It does **not** extend the ordinary inverse-Jacobian argument through `t=u`, where D's rank drops, or assemble the full nine-point image form.

Checker: `research/nima/checkers/check_nine_point_regular_cd_full_boundary_pole_cancellation.py`; certificate: `research/nima/results/nine-point-regular-cd-full-boundary-pole-cancellation.json`.
