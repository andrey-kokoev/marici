# Both relabelled four-mass cells miss an open positive V sector

Two independently sourced four-mass cells have complete arbitrary-Y quadratic traces: **A** deletes physical label 3; **E** deletes physical label 2. Their union is nevertheless **not** the nine-point positive image.

With positive rank-six moment-curve data at labels 1–9, take the distinct positive **vertical-column-2** cell V at weights `(w₄,w₅,w₆,w₇,w₈,t,u)=(1,1,1,1,1,3,2)`. Its target Jacobian has full rank. At `w₂=1/20`, A's complete fibre consists of **two real nonpositive sheets**, while E's exact fibre has **negative discriminant and no real sheet**. At `w₂=1/40`, both A and E have **two real sheets each**, with **no positive sheet**: E's four reconstructed source weights include `w₂<0` and `w₄<0` on each sheet. All signs are algebraically exact.

A subtle special fibre must not be mistaken for an empty or generic quadratic: at the V targets the E lifted four-minor linear system has rank three and **forces `q=det(T)=0`**. Solving its remaining one-parameter affine line with the determinant quadratic recovers **all** E sheets (zero real at the first target, two nonpositive at the second).

Full-rank V projection and strict A/E sheet-sign and E discriminant controls imply **nonempty open positive target sectors absent from `image(A)∪image(E)`**. Thus even *both* exact arbitrary-Y relabelled four-mass traces are insufficient as complete positive-image coverage. This does not fix the canonical form, V's global multiplicity, or other-cell contour weights.

Checker: `research/nima/checkers/check_nine_point_two_relabelled_cells_miss_vertical_image.py`; result: `research/nima/results/nine-point-two-relabelled-cells-miss-vertical-image.json`.
