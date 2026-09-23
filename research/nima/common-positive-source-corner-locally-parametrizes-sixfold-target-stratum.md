# The shared positive source corner locally parametrizes a six-dimensional target stratum

Two exact strictly positive B/D `t=u` face points have complete weight fibres that reach the common **`w₄=0,t=u` source corner** with all remaining weights positive. A new exact rank check at both corner representatives finds:

* The six corner-tangent source parameters `(w₂,w₅,w₆,w₇,w₈,u)` have a **nonzero `6×6` target minor**. Their shared map immerses the corner into a six-dimensional target stratum.
* At those corner representatives, full source-to-target Jacobian ranks remain **A=8, B=7, C=8, D=7**. B/D restricted to the seven-dimensional slope face have rank **six**, and their one-dimensional collapsed weight kernels have **nonzero `w₄` component**, transverse to the `w₄=0` corner section.
* The B/D face points and their corner representatives have **exactly the same target plane**. Along that section all four complete source matrices agree.

The rank and transverse-kernel statements supply local coordinates: near either certified target, the common corner image is a **six-dimensional local section** of the B/D slope-face image (by the ordinary inverse/constant-rank theorem). They do **not** compute a singular pushed differential form, target multiplicity, face coverage away from these neighborhoods or the full nine-point canonical form. In particular, A/C have full rank at the corner even though their strictly positive slope-face interior images are separate from the B/D slope-face interior.

Checker: `research/nima/checkers/check_nine_point_shared_corner_local_sixfold_image.py`; certificate: `research/nima/results/nine-point-shared-corner-local-sixfold-image.json`.
