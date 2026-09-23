# Cyclic boundary residue corrects the seven-point chart form

The previously proposed local product of six weight `dlog`s with `du/(u-2) ∧ dv/(v-u)` was **wrong** as a Grassmannian canonical form. An independent symbolic double residue of the standard rank-two top-cell cyclic form finds an exact nonconstant factor `2/v`.

Choose the GL(2) gauge fixing columns 1 and 4 of the 2x7 source matrix to the identity. The remaining five columns supply ten affine coordinates, ordered column-major. The top-cell form is their wedge divided by the product of seven cyclic minors. Resolve the two sourced boundary conditions by `t3=1+e`, `t6=u+f`, and extract the double logarithmic residue at `e=f=0`. Compute the ten-coordinate gauge Jacobian and the product-of-minors coefficient of `e*f` independently. Exact symbolic simplification yields, in the declared coordinate order,

    Res_23 Res_56 Omega_top
      = (2/v) (dw2/w2 ∧ ... ∧ dw7/w7)
          ∧ du/(u-2) ∧ dv/(v-u).

The `2/v` factor is NOT a constant normalization: it changes from `1/2` to `1/3` at the two exact points previously used to quote target pushforward coefficients. In the same target affine-coordinate orientation, the corrected coefficients are respectively `194481/204800` and `144215816802121/83168015155200` (previous candidates times `1/2` and `1/3`). These are source cyclic-form coefficients transported via the earlier nonzero chart Jacobians. The absolute overall sign depends on the ordering of the two transverse residues; that ordering is explicitly frozen by the checker.

This is a substantive falsification of an appealing but unjustified positive-coordinate `dlog` ansatz. It also shows why a cell chart and rational inverse cannot by themselves supply its normalized canonical form. The source cyclic-form residue now supplies a testable normalized eight-form on this **one** positive chart. A comparison to history zero at the SAME positive external data and a proof of its global pushforward remain open; neither is inferred from the earlier rational-kinematics parity match.

Run `uv run --with sympy python research/nima/checkers/check_seven_point_boundary_residue.py`. Exact artifact: `research/nima/results/seven-point-boundary-residue.json`.
