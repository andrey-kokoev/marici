# Two positive zero-label-3 neighbors add a pair beyond the three-sheet cube

At the same exact positive E target used for the three-sheet label-3 cube, a distinct **zero-physical-3**, order-preserving relabelling of its entire eight-cell source cube has been tested. The old source columns are retained in order on physical labels `(1,2,4,5,6,7,8,9)`, and physical column 3 is zero.

The zero-physical-3 **E** four-pair cell had previously been checked: neither of its two real sheets is positive. **Two different adjacent cells do have positive inverse sheets: E_B and F_B.** Their exact rank-four lifted-minor inverses have **all eight strict positive source inequalities** and **nonzero eight-dimensional target Jacobians**, so these are regular geometric positive-sheet witnesses (with local positive neighborhoods). The five other relabelled neighbor cells have one real inverse each but none positive.

Thus the **union of the tested zero-physical-2 cube and this zero-physical-3 relabelled cube has five positive sheets** at this target: the original E,E_B,F_B, plus the newly relabelled E_B,F_B. They enter as **a pair**, not as a uniquely forced fourth “coherencer.” Because both new cells have **physical column 3 identically zero**, they **cannot** repair the nonzero or supported-versus-meromorphic discrepancy of the `χ₃⁴χ₅⁴` component. They may matter for other components, but their physical contour weights and status as sourced nine-point histories are unproved. The earlier exclusion of other *four-pair E embeddings* remains true: these new positive sheets are **neighbor cells**, not E.

Checker: `research/nima/checkers/check_nine_point_zero_phys3_relabelled_cube_neighbors.py`; result: `research/nima/results/nine-point-zero-phys3-relabelled-cube-neighbors.json`.
