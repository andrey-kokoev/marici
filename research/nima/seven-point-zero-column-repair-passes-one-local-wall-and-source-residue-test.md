# A zero-column repair passes one local wall and residue test

The zero-column-3 replacement for collapsed history 1 has now been compared with the separated-pair history-zero source cell on a **common seven-dimensional source face**:

    C3=0, Delta_(5,6)=0.

Use strictly positive moment-curve `Z`. At a rational interior face point, the `CZ` image of the shared face has tangent rank seven. Opening the history-zero chart by a positive column 3 parallel to column 2 and opening the zero-column chart by splitting columns 5 and 6 are BOTH transverse to that image. Their oriented target Jacobians in the SAME ordered seven face variables have exact ratio `-14/5`. Thus the two positive images lie on opposite local sides of their common immersed wall. This fixes the defect of the old triple-parallel carrier, whose inward Jacobian was identically zero in this test.

There is also an independent symbolic **source-form** comparison. The history-zero source form is obtained by the earlier double cyclic residue at minors 23 and 56, including the essential nonconstant `2/v` factor. Take its further residue as column 3 vanishes. On the replacement side, use the standard top cyclic form of `G_+(2,6)` on the surviving columns `(1,2,4,5,6,7)` and take its residue at minor 56. Expressed in identical seven face coordinates `(w2,w4,w5,w6,w7,u,v)`, the two source residue coefficients are IDENTICAL as rational functions; their exact quotient simplifies to `1`, not merely at the checked point. The opposite target inward sides supply the expected orientation distinction **if** an oriented target-cell sewing is adopted; equality of unsigned source residues by itself is not a signed cancellation theorem.

This is meaningful progress on a candidate positive-cell compiler: an actual shared face, full transverse images, and exact compatible boundary forms. It is not yet a proof that either pushed-forward eight-form equals the corresponding physical generalized-R history. It proves neither the complete shared wall nor global six-cell coverage, and it says nothing about the other two repaired cells. The same-Z normalized eight-form comparison remains the decisive admission test.

Run:

    uv run --with sympy python research/nima/checkers/check_seven_point_repair_shared_wall.py
    uv run --with sympy python research/nima/checkers/check_seven_point_repair_wall_residue.py

Results: `research/nima/results/seven-point-repair-shared-wall.json` and `research/nima/results/seven-point-repair-wall-residue.json`.
