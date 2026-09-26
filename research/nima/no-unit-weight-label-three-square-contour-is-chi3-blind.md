# No unit-weight label-3 square contour is χ₃⁴χ₅⁴-blind

The four **complete** arbitrary-Y rational traces `(E,E_B,E_C,E_D)` have been evaluated on **two identical common positive external/target controls**, including both E sheets and each neighbor's unique sheet. An exact exhaustive check finds that **none of the 15 nonempty subsets** of their calibrated oriented traces cancels the `χ₃⁴χ₅⁴` coefficient. Even allowing an independent coefficient from **`{−1,0,+1}` for each cell**, **none of the 80 nonzero choices** cancels at either target. Therefore no such fixed unit-weight selection can make the rational label-3 square contribution generically `χ₃⁴χ₅⁴`-blind.

Adding any cells from the original **zero-physical-3 four-cell square** or the vertical label-3 cell F does not affect this particular coefficient: all have identically vanishing `χ₃⁴χ₅⁴` source minors. This is an exact, bounded **contour-support constraint**. It is **not** a requirement that the true nine-point amplitude be `χ₃`-blind; additional label-3-sensitive cells, target-dependent weights, or a physically nonzero label-3 component may be appropriate.

The label-3 square is the exact relabelling of the original zero-column square at arbitrary first-pivot Y, with an overall reversed calibrated source orientation; the original square's analogous `χ₂⁴χ₅⁴` form can be compared by the same map. Neither source incidence nor local pole cancellation determines the full contour.

Checker: `research/nima/checkers/check_nine_point_label3_square_unit_contour_support_sieve.py`; result: `research/nima/results/nine-point-label3-square-unit-contour-support-sieve.json`.
