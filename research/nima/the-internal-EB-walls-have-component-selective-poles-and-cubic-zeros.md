# Internal E_B walls have component-selective poles and cubic zeros

At the two exact E_B positive-support endpoints along the strictly positive E target family, `e=44/445` (`w₂(E_B)=0`) and `e=11531/250` (`w₄(E_B)=0`), **both E and E_B target Jacobians and target-frame determinants are nonzero**. The other E_B source weights and `u,t−u` remain nonzero. Thus each wall is an ordinary regular image of one E_B source logarithmic facet lying **inside the regular positive E image**.

The E_B **oriented one-sheet meromorphic eight-form has a simple pole** at **each** endpoint. Crucially, this survives in the **full supersymmetric form**: its `χ₁⁴χ₅⁴` component has order `−1` at the lower `w₂=0` wall, and its `χ₃⁴χ₄⁴` component has order `−1` at the upper `w₄=0` wall. In contrast, the distinguishing `χ₃⁴χ₅⁴` component has **order `+3`—a cubic zero—at both**: its minor `det(C₃,C₅)=w₂w₄` cancels each logarithmic source factor to third order.

This sharpens the contour gate: if a **global canonical form is regular at these interior image loci**, E_B's genuine component-specific poles require cancellation by other contributions. The `χ₃⁴χ₅⁴` projection is **blind** to these obstructions and cannot by itself certify the full superform. No particular cancelling cell, contour coefficient, or full nine-point form is established.

Checker: `research/nima/checkers/check_nine_point_EB_internal_support_walls_fermionic_vanishing.py`; result: `research/nima/results/nine-point-EB-internal-support-walls-fermionic-vanishing.json`.
