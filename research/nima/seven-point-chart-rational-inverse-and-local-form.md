# Seven-point chart: rational inverse and local form

For history zero's positive rank-two source cell (cyclic minors 23 and 56 vanish), the external moment-curve matrix `Z` has rank six and its left kernel is the line `(1,-6,15,-20,15,-6,1)`. Fix a target representative `Y` and a rational linear left inverse `R=(Z^T Z)^-1 Z^T`. All source representatives satisfying `CZ=Y` have the form

    C=YR+[a,b]^T k.

Each source 2x2 minor is **linear** in `(a,b)` because the quadratic rank-one update cancels. The equations `Delta23=Delta56=0` are therefore a 2x2 linear system. Its determinant is nonzero at two exact positive source points (`-882`, `-7344`), and the unique solution reconstructs both source matrices. This proves a rational **generic** inverse on the history-zero cell's image, beyond the previously checked nonzero differential at one point. It does not establish global injectivity at the vanishing determinant locus.

In the chart `C_i=w_i(1,t_i)`, with `t=(0,1,1,2,u,u,v)`, `w1=1`, `w2..w7>0`, `2<u<v`, the **initial, now falsified** positive coordinate top-form guess was

    (dw2/w2) ^ ... ^ (dw7/w7) ^ du/(u-2) ^ dv/(v-u).

A subsequent symbolic cyclic top-form double-residue calculation finds that this guess misses a NONCONSTANT factor `2/v`; see `seven-point-chart-boundary-residue-corrects-the-naive-form.md`. The two coefficients below are therefore NOT the source-derived form coefficients.

Writing the target affine Grassmannian coordinates as `B=Y[:,0:2]^-1 Y[:,2:6]` (row-major), its local pushforward coefficient is the reciprocal of the product of `w2..w7 (u-2)(v-u)` and the exact 8x8 Jacobian determinant of `B` with respect to the eight source variables. At the two checked points it equals `194481/102400` and `144215816802121/27722671718400`, respectively. These are **superseded candidate** form coefficients: the coordinate form has not been independently derived from a source-approved on-shell boundary-measure prescription, nor compared with the history's canonical form for these SAME external data. In particular these numerical coefficients are not physical amplitude evaluations.

This test removes two specific obstacles: the fibre is not intrinsically multivalued on a generic open set, and exact local pushforward coefficients can be calculated. Remaining is the decisive same-Z comparison of eight-forms, including their orientation and residues. A rational kinematic matching recorded elsewhere cannot be silently transplanted to the moment-curve `Z` used here.

Reproduce: `uv run --with sympy python research/nima/checkers/check_seven_point_chart_pushforward.py`; packet `research/nima/results/seven-point-chart-pushforward.json`.
