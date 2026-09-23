# The nine-point four-pair source form has an exact zero-column normalization

The minimum-eight-support nine-point candidate now has a **source-derived canonical-form candidate**, not merely positive geometry and image rank.

For retained labels `(1,2,4,5,6,7,8,9)`, the intrinsic eight-column top cyclic Grassmannian form has been restricted by four disjoint pair conditions `(1,2),(4,5),(6,7),(8,9)`. In a positive chart with six weights `w2,w4,w5,w6,w7,w8>0` and angular variables `t>u>0`, its exact FOURFOLD oriented source residue is

    - dw2 dw4 dw5 dw6 dw7 dw8 dt du
      / [w2 w4 w5 w6 w7 w8 * u * (t-u)]

in the declared coordinate ordering. The apparent simple six-weight `dlog` guess alone would miss the angular factor `1/[u(t-u)]`. The checker derives the coefficient from the 12-coordinate gauge Jacobian and all eight cyclic minors, then checks positive source-chart instances. This is the intrinsic source form, not yet its pushforward to `CZ`.

Deleting physical column 3 must not silently replace the NINE-column source top form with an eight-column one. A separate GENERIC source normalization calculation now closes that step. Gauge physical columns 1 and 4 to `(1,0),(0,1)`, let column 2 be `(x,y)` and the vanishing column 3 be `(alpha,beta)`. The two source normal minors are

    S=Delta34=alpha,
    T=Delta23=x*beta-y*alpha,

while the new adjacency in the retained eight-column cyclic product is `Delta24=x`. Since

    d(alpha) wedge d(beta) = (1/x) dS wedge dT,

this Jacobian cancels EXACTLY against the replacement adjacency. Taking residues in the declared `(S,T)` order gives the intrinsic eight-column top form with coefficient ratio **one**. Reversing the two normal directions reverses orientation; omitting `Delta24` leaves an invalid `1/x` factor. The normalization holds generically where `x!=0`, not only at the earlier algebraic point.

Together, these give a normalized source-side four-pair residue inside the nine-label ambient carrier. A subsequent check computed TWO exact rational local pushforward coefficients and counted positive algebraic branches at each sampled target; see `the-nine-point-four-pair-form-has-two-exact-local-pushforward-values.md`. What remains unresolved is a GLOBAL pushforward identity, its value on the earlier algebraic minimum-eight-support target, and comparison with a **sourced nine-point generalized-R history at the same external data**. Source-form agreement, full image rank at one point and minimum eight-label support do not establish that match or a global triangulation.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_paired_source_form.py
    uv run --with sympy python research/nima/checkers/check_nine_point_zero_column_residue.py

Artifacts: `research/nima/results/nine-point-paired-source-form.json` and `nine-point-zero-column-residue.json`.
