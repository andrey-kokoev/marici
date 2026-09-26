# Three regular label-3 square edges cancel full pushed local superpoles

For the four positive label-3-sensitive cells `(E,E_B,E_C,E_D)`, the three **target-regular** edges `(E,E_B)` at `w₄=0`, `(E,E_C)` at `t−u=0`, and `(E_C,E_D)` at `w₄=0` each have an exact **complete local supersymmetric pushed-pole cancellation**. At **three distinct positive boundary controls per edge**, both 8×8 target Jacobians are nonzero; the full source matrices and hence the complete fermionic boundary numerator coincide. Seven target tangent Jacobian columns agree. Replacing the eighth (normal) column with either of **two transverse target directions** gives equal determinant-normal-speed products on the two cells, while their oriented source residues are opposite. Consequently their nonlinear local pushed simple-pole residues cancel **in every fermionic component** wherever regular.

For the `t−u=0` edge, the correct normal coordinate is **`v=t−u` with tangent `u`**, not the independent old coordinate `t`; differentiating with fixed old `u` would falsely break tangent-column equality. The executable checker uses the boundary-adapted source coordinates.

The **fourth** edge `(E_B,E_D)` at `t−u=0` has rank **7** and is excluded from the regular pushed-residue claim. These three cancellations are local; they do **not** show that the four complete arbitrary-Y traces cancel their label-3 component, that the four cells triangulate the target image, or that the full nine-point amplitude is known.

Checker: `research/nima/checkers/check_nine_point_label3_square_three_regular_pushed_pole_cancellations.py`; result: `research/nima/results/nine-point-label3-square-three-regular-pushed-pole-cancellations.json`.
