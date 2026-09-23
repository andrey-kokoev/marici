# NNMHV selector transfer: corrected constructive status

The first inventory audit was **out of date**: `seven-point-positroid-compiler.json` and `seven-point-positroid-rank-tables.json` already compile the six matched seven-point histories to codimension-two positroids. Their status is not `requires_on_shell_graph`, despite the older seed request file retaining that status. Do not cite the earlier missing-cell assertion.

An explicit chart has now been constructed for history zero, whose matched parity simplex is `[1,3,4,6,7]` and whose omitted labels are 2 and 5. Its source columns are `C_i=w_i(1,t_i)` with classes `t=(0,1,1,2,u,u,v)`, `w1=1`, other weights positive and `2<u<v`. This is an eight-parameter positive chart: exactly minors (2,3) and (5,6) vanish, and every other ordered source minor is positive. For positive moment-curve external data `Z_j=(1,j,j²,j³,j⁴,j⁵)` the exact determinant of the target Grassmannian affine-coordinate Jacobian at weights one, `u=3,v=4` is `102400/194481`, nonzero. Thus the chart maps locally to a full-dimensional region of `G(2,6)`.

This **does not** prove the chart canonical form equals the matched generalized-R history, nor establish target overlap or coverage. An eight-dimensional image alone does not select the correct form. The next discriminating test is to compute the pushforward canonical form of this chart (including possible multiple inverse branches), compare its poles and normalization against history zero for the same positive Z, and test intersections with a neighboring compiled chart. Avoid equating a rational-kinematics parity-form match with an all-positive-Z geometric equality.

The analytic `n^-2` law remains fitted selected-component evidence, not a norm-uniform canonical-form bound. A fixed pole-avoiding domain, normalization and uniform-in-n shell estimate are still required for completion transfer.

Reproduce: `uv run --with sympy python research/nima/checkers/check_seven_point_positive_chart.py` and `python research/nima/checkers/check_nnmhv_selector_transfer_gate.py`. Outputs: `results/seven-point-positive-chart.json` and `results/nnmhv-selector-transfer-gate.json`.
