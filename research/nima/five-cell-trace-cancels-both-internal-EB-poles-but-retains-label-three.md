# Five-cell trace cancels both internal E_B poles but retains label-3 support

The five-cell meromorphic sum `(E,E_B,E_C,E_D,F_B)` passes **both** component-sensitive interior E_B wall tests on the fixed positive E target family:

* At lower `e=44/445`, the complete unique F_B inverse lies on the same regular `w₂=0` source facet as E_B, and their full supersymmetric simple-pole residues cancel. The other three cells' inverse sheets are regular there.
* At upper `e=11531/250`, F_B's unique inverse has **finite nonzero source weights and target Jacobian**. E_B's `w₄=0` superpole cancels instead against E's **nonpositive second algebraic sheet**, already certified regular as a paired local residue. Hence F_B does not reintroduce the upper pole.

Nevertheless, the complete five-cell **arbitrary-Y rational `χ₃⁴χ₅⁴` field trace is nonzero** at an exact shared positive rank-six moment-curve target `e=1`. F_B itself has `det(C₃,C₅)=w₂w₄/t`, so it contributes genuinely to this component; adding its exact one-sheet coefficient does **not** cancel the previous nonzero four-cell trace. A nonzero exact rational witness proves generic nonvanishing on a simple-fibre open.

This is a useful distinction: cancelling **two identified internal spurious superpoles** is neither a vanishing theorem for the complete five-cell form nor a proof of a correct physical contour. Other target poles, label-3 cells, multiplicities and the global nine-point image canonical form remain open.

Checker: `research/nima/checkers/check_nine_point_five_cell_two_internal_walls_and_label3_remainder.py`; result: `research/nima/results/nine-point-five-cell-two-internal-walls-and-label3-remainder.json`.
