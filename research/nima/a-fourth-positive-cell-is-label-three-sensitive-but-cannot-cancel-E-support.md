# A fourth positive cell is label-3-sensitive but cannot cancel E's distinguishing component

Alongside A (horizontal physical column 2, physical column 3 zero), V (vertical physical column 2, physical column 3 zero), and E (physical column 2 zero, **horizontal** physical column 3), there is an explicit fourth strictly positive cell **F**: physical column 2 zero and **vertical** physical column 3 `(0,w₂)`. Every ordered source 2×2 minor is nonnegative. Deleting physical column 2 identifies F with the same **birational V source chart**, relabelled onto physical labels `(1,3,4,5,6,7,8,9)`. At two exact positive moment-curve controls its target Jacobian is nonzero and the five-minor kernel-lift has a unique algebraic inverse.

F has real `χ₃` dependence: `det(C₁,C₃)=w₂`. But physical columns **3 and 5 are parallel** in F, so `det(C₃,C₅)=0` and its complete pushed `χ₃⁴χ₅⁴` coefficient vanishes **identically**. A and V have zero physical column 3, and their same coefficient also vanishes. By contrast E has `det(C₃,C₅)=w₂w₄`, and its **complete arbitrary-Y two-sheet `χ₃⁴χ₅⁴` trace is generically nonzero**.

Consequently, among the explicit four-cell rational span `(A,E,V,F)`, **E alone carries this fermionic coordinate**. No bosonic reweighting of A, V or F can cancel it. A `χ₃`-independent *four-cell* combination would require E's weight to vanish unless **additional distinct cells** contribute the same component. The **full nine-point amplitude is not claimed to be `χ₃`-independent**; this is a necessary span constraint, not a contour determination or coverage theorem.

Checker: `research/nima/checkers/check_nine_point_vertical_label3_cell_fermionic_support.py`; result: `research/nima/results/nine-point-vertical-label3-cell-fermionic-support.json`.
