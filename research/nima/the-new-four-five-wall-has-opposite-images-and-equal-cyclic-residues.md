# The newly detected 4/5 wall passes both local gates

The multichamber fibre test found a strict-positive source target lying on a wall common to repaired candidates 4 and 5. The wall is not an open-cell coverage failure. It is the source face

    C5=0, Delta_(7,1)=0.

An independent local chart now verifies the proposed gluing at a rational point with strictly positive moment-curve external data. The face image has tangent rank seven; opening cell 4 by adding a column 5 parallel to column 6 and opening cell 5 by separating columns 7 and 1 give nonzero target inward Jacobians with exact ratio `-2/15`. Thus their local images lie on opposite sides of the same immersed wall.

A separate symbolic cyclic-form check compares the DOUBLE residue of the seven-column top form on cell 4 (minors 56 and 71), followed by its `C5=0` residue, with the minor-71 residue of the six-column top form on the zero-column-5 replacement. In a common seven-coordinate wall chart, both coefficients simplify to

    2/[v*w1*w3*w4*w6*w7*(u-2)*(u-v)].

The exact quotient is `1`. Orientation of a sewn TARGET form is not inferred from this unsigned source coefficient alone; the independently checked opposite inward sides supply the local orientation datum.

At the time of this calculation, four local edges were checked. The later 1/2 and 3/4 checks now close the local cycle; see `the-repaired-seven-point-cells-close-a-local-six-wall-residue-cycle.md`. Global coverage and same-Z physical history-form equality remain open; no arbitrary-n compiler or analytic completion law follows.

Run `uv run --with sympy python research/nima/checkers/check_seven_point_four_five_wall.py`; report `research/nima/results/seven-point-four-five-wall.json`.
