# Three more positive label-3 cells form an oriented square around E

The known four-cell positive source square `(A,B,C,D)` can be **relabelled** by moving its supported physical column 2 to physical column **3** and making column 2 zero. This produces **four distinct strictly positive label-3-sensitive cells** `(E,E_B,E_C,E_D)`, with E the earlier arbitrary-Y two-sheet cell. Their calibrated source-residue orientations relative to E are `(+,−,−,+)`; relative to original A they are `(−,+,+,−)`.

Crucially, **all four** have the **same nonzero `χ₃⁴χ₅⁴` source minor** `det(C₃,C₅)=w₂w₄`. The three new cells therefore provide **explicit positive sources with the fermionic support required to potentially cancel E's traced label-3 component**. Their opposite signed **equal-coordinate source densities** sum to zero, but their target maps differ; no cancellation of complete pushed forms follows from this source identity.

The square's four common-source edges remain `(E,E_B)` at `w₄=0`, `(E,E_C)` at `t−u=0`, `(E_C,E_D)` at `w₄=0`, and `(E_B,E_D)` at `t−u=0`. Exact positive moment-curve boundary controls have full target rank **8 on both sides of the first three edges**. Both sides of the fourth exceptional edge have target rank **7**, so an ordinary pushed eight-form residue there is not inferred.

This supplies actual candidates beyond the earlier `(A,E,V,F)` four-cell span; it does not compute their arbitrary-Y full traces, select contour weights, prove coverage, or close the nine-point canonical form.

Checker: `research/nima/checkers/check_nine_point_label3_relabelled_four_cell_square.py`; result: `research/nima/results/nine-point-label3-relabelled-four-cell-square.json`.
