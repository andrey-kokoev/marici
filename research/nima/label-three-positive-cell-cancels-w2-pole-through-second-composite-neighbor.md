# Label-3-sensitive positive cell is a second composite neighbor of the same `w₂=0` facet

The regular positive eight-cell with physical column **3** equal to `(w₂,0)` and physical column **2** zero is not merely additional label-3 support: it is a **second** explicit positive neighbor of the sourced four-pair cell A along `w₂=0`. It is **distinct** from the previously found *vertical-column-2* composite neighbor; both share the original matrix at that same source facet.

A common nine-dimensional positive cell has physical columns 2 and 3 equal to `(x,0)` and `(y,0)`. Taking five cyclic top-form poles `(12),(23),(45),(67),(89)` produces a density proportional to `dx∧dy/[xy w₄w₅w₆w₇w₈u(t−u)]`. Its `y=0` residue is A, while the **induced composite `x=0`** residue is the label-3-sensitive cell E. Calibrating the cyclic ordering to A's independently computed sixfold top residue fixes E's complete oriented density to **exactly minus A's**.

At their shared positive `w₂=0` boundary, the full source matrices and fermionic numerators coincide and seven target-Jacobian tangent columns agree. Three exact positive rank-eight boundary controls, each checked in two transverse target directions, certify **full nonlinear local pushed-pole cancellation** for every fermionic component wherever regular.

**Contour-selection warning:** A now has **two distinct positive composite neighbors** that separately cancel the *same* local `w₂` pole. Adding A and both neighbors with their individually computed orientations would generally overcount rather than triangulate. Local positivity and incidence do not specify which contour/cell combination represents the complete nine-point image form; the independent arbitrary-Y form and multiplicity constraints remain essential.

Checker: `research/nima/checkers/check_nine_point_label3_cell_composite_local_cancellation.py`; result: `research/nima/results/nine-point-label3-cell-composite-local-cancellation.json`.
