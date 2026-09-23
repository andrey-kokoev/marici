# Two previously found positive neighbors also cancel the `w₆=0` and `w₈=0` facets

No additional source cell is needed to cancel two further zero-column facets of the sourced four-mass eight-cell:

* At **`w₆=0`**, physical column 7 vanishes. The previously constructed **slope-merge neighbor**, which uses physical column 7 with lower entry `w₆u` rather than `w₆t`, becomes exactly the original matrix. Its sixfold cyclic top-form residue has the independently established opposite orientation.
* At **`w₈=0`**, physical column 9 vanishes. The previously constructed **cyclic-endpoint neighbor**, which keeps physical column 9 at `(-w₈,0)` rather than `(-w₈,w₈u)`, also becomes exactly the original matrix. Its top-residue orientation is opposite as well.

On each common positive boundary the **entire source matrix and fermionic numerator agree**. The two `8×8` source-to-target Jacobians share seven tangent columns and differ only in the corresponding zero-column weight's normal direction. Cramer's cofactor identity then makes the oriented local pushed-form residues **equal and opposite for every fermionic component** wherever regular. Three exact positive boundary points per facet, each with two transverse target directions, verify the nonzero Jacobians and cancellation (**six** new exact controls).

This raises the screened local polar facets from four to **six of the eight** basic source-form factors (`w₂,w₄,w₅,w₆,w₇,w₈,u,t−u`): the still-unscreened factors are `w₂` and `w₇`. Six local cancellation relations do **not** prove an exhaustive nine-point image triangulation or full canonical form, especially at intersections of facets.

Checker: `research/nima/checkers/check_nine_point_reused_neighbor_zero_column_cancellations.py`; certificate: `research/nima/results/nine-point-reused-neighbor-zero-column-cancellations.json`.
