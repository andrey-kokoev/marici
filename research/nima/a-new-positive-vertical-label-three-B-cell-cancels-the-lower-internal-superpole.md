# A positive vertical label-3 B-cell cancels the lower interior superpole locally

The four-cell label-3 square's **uncancelled** lower interior pole at `e=44/445` (`E_B` source `w₂=0`) has an explicit **fifth positive-cell neighbor**: `F_B`, obtained from `E_B` by replacing physical column 3 `(w₂,0)` with `(0,w₂)`, while physical column 2 remains zero and all later columns stay unchanged. All its ordered source minors are nonnegative. At `w₂=0`, `F_B` and `E_B` have **identical complete source matrices**, hence identical fermionic boundary numerators.

Their oriented intrinsic source densities have **opposite signs**. This follows by taking the two opposite `x=0`/`y=0` composite residues of a common horizontal/vertical positive column-3 cell and applying the same `w₄` pole-shift Jacobian to both: `E_B` has `−1/[w₂w₄w₅w₆w₇w₈u(t−u)]` and `F_B` the opposite. At **three exact positive boundary controls**, including the precise lower wall target **inside E's regular positive image**, both full target Jacobians have rank 8 and seven tangent columns agree. Two transverse target directions per control give **exact cancellation of the full locally pushed simple superpole**, including the `χ₁⁴χ₅⁴` pole which survived the original four-cell meromorphic sum.

This supplies a concrete **additional positive-cell cancellation candidate** for the lower internal obstruction. It does **not** compute F_B's complete arbitrary-Y field trace, establish its global contour coefficient, or prove full nine-point image coverage/canonical form.

Checker: `research/nima/checkers/check_nine_point_vertical_label3_B_neighbor_cancels_lower_EB_pole.py`; result: `research/nima/results/nine-point-vertical-label3-B-neighbor-cancels-lower-EB-pole.json`.
