# The sourced two-sheet contour is a transverse section of a six-dimensional n=9 fibre

The full `k=2,m=4,n=9` positive source has dimension `2(9−2)=14`; its Grassmannian image target has dimension `2·4=8`, so a regular full-source fibre has dimension **6**. The sourced four-mass cell has eight parameters and is a codimension-six *loop/parallel-pair* source boundary. Its two-sheet intersection with a fixed target is therefore a potential transverse **localization of a full six-dimensional fibre**, not an image-boundary face.

Here the localization is checked rather than assumed. At each of the **four exact boundary source sheets** (two per positive rank-six external data set), choose a `3×9` left-kernel basis `K` for the n=9 external matrix and six variables in a `2×3` matrix `T`. In the local source gauge with columns at physical `(1,4)` equal to `I₂`, the 14 variables are the eight four-mass source parameters together with the six kernel parameters in `D₉(s)+TK`. The eight target coordinates are the first four columns in a `Y[:,5:6]` chart of `Gr(2,6)`; the six source normals are the two missing-column entries and four vanished parallel-pair minors `(1,2),(4,5),(6,7),(8,9)`.

The local `14×14` derivative is **block diagonal** at the boundary:

    d(target, normals)/d(source8, kernel6) = diag(J₈, M₆).

Indeed `K Z₉=0` makes the upper-right block exactly zero, while the normals vanish *identically* along the sourced eight-parameter cell, making the lower-left block zero. Both `det(J₈)` and `det(M₆)` are exact nonzero rationals at **all four sheets**, including the algebraically continued nonpositive sheet. Thus the full coordinate determinant factors as `det(J₈)det(M₆)≠0`: the sourced cell is locally transverse to the full fibre. For each external witness only **one** of the two source sheets is positive, while the other is its rational continuation; the full positive fibre near the positive sheet is six-dimensional.

This clarifies the earlier scalar-history obstruction and image-interior result without resolving the form problem. A pushforward of the **eight-dimensional contour form** localizes a selected fibre intersection. The canonical pushforward of a **14-dimensional top-cell form** requires an independent six-dimensional fibre integration/contour prescription; its value cannot be identified with the two-sheet boundary form merely from their common target. Top-cell canonical orientation, all preimages, arbitrary-`Y` trace, and global positive image coverage remain open.

Checker: `research/nima/checkers/check_nine_point_loop_fibre_transverse_factorization.py`; certificate: `research/nima/results/nine-point-loop-fibre-transverse-factorization.json`.
