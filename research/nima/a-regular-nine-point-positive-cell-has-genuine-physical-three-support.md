# A regular nine-point positive cell has genuine physical-label-3 support

The sourced four-pair cell's **arbitrary-Y rational trace** is independent of physical label 3 because its matrix column 3 vanishes. That property is **not shared by all positive eight-dimensional nine-point cells**. An explicit counterexample is obtained by moving its `w₂ e₁` column from physical position **2** to physical position **3**, leaving column 2 zero and keeping the same eight positive coordinates. This new cell has **24 strictly positive and 12 zero ordered two-minors** on `w₂,w₄,w₅,w₆,w₇,w₈,u,t−u>0`, and meets the old cell at `w₂=0` when both columns vanish.

The new column 3 is `(w₂,0)`, so its full fermionic numerator depends on `χ₃`; in particular, `det(C₃,C₅)=w₂w₄>0` gives a nonzero `χ₃⁴χ₅⁴` component. Its target plane depends nontrivially on the external physical row `Z₃`. For strictly totally positive rank-six moment-curve external data, **three exact positive interior controls** have nonzero `8×8` source-to-target Jacobians. This is a genuine regular positive image cell, not a formal relabelling that collapses under projection.

No cyclic top-cell residue orientation, amplitude contour weight, complete image coverage or pushed canonical-form coefficient for this new cell is claimed. The result does, however, rule out treating the label-3-blind arbitrary-Y **zero-column sourced trace alone** as an inventory of the nine-point positive cells; other label-3-sensitive sectors must be considered by any image-form comparison.

Checker: `research/nima/checkers/check_nine_point_positive_label3_cell_missing_from_zero_column_trace.py`; result: `research/nima/results/nine-point-positive-label3-cell-missing-from-zero-column-trace.json`.
