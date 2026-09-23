# No fixed fibre-linear objective selects the six repaired seven-point cells

The fixed-target positive source fibre is an exact rational polygon in kernel-shift coordinates `(a,b)`. A tempting route to a universal six-cell section is to select one vertex by maximizing ONE fixed linear functional `cx*a+cy*b`. This route is now falsified by three exact strictly-positive source fibres, not just by a finite direction grid.

For a selected repaired vertex `q` and another feasible polygon vertex `p`, maximizing a fixed objective requires `c·(q-p)>=0`. The checked differences include:

- monotone generic top source, selected cell zero: `q-p=(-2231/15360,-9817/7680)`;
- strict positive top lift of sector two: `q-p=(1/85,4/85)`;
- strict positive top lift of sector three: `q-p=(-1/90,0)`.

All six points used in these comparisons are computed from intersections of TWO exact halfspace boundary lines, and each rival vertex satisfies all 21 source-minor inequalities. The three inequalities on `(cx,cy)` imply

    cx+(19634/2231)cy <= 0,
    cx+4cy >= 0,
    cx <= 0.

Since `19634/2231>4`, the first two force `cy<=0`; the latter two force `cy>=0`. Thus `cy=0`, then `cx=0`. The zero functional ties every vertex and cannot specify the repaired choice. **No nonzero fixed linear functional in this common kernel-coordinate frame selects the repaired vertex for all positive fibres.**

This does NOT disprove six-cell coverage or a source-dependent objective. It rules out one unusually cheap generalization of the earlier polygon-selector construction. An exact active-set theorem, piecewise objective, or topological image-gluing argument remains possible. The result also does not touch the independent analytic completion exponent.

Run `python research/nima/checkers/check_seven_point_extremal_selector_probe.py`. Report `research/nima/results/seven-point-extremal-selector-probe.json` includes the three exact obstruction differences and the exploratory small-integer direction census.
