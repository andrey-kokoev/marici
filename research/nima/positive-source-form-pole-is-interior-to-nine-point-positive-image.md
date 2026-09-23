# A positive four-mass source pole maps to the **interior** of the nine-point image

The sourced four-mass two-sheet contour has a genuine nonzero simple pole at the **positive source-cell boundary** `w₄=0` on the rational target slice `ε=485/12278`. That is not sufficient to make it a boundary pole of the **full** `n=9,k=2,m=4` positive image. Here the distinction is resolved at that exact target.

Take the positive nine-point moment-curve external matrix `Z₉`, apply a positive-determinant `GL(6)` change of basis, and let `C_boundary` be the sourced four-mass matrix with zero physical column 3 at that `w₄=0` sheet. Its image is the target `Y=C_boundary Z₉`. Choose an exact `3×9` basis `K` of the left kernel of `Z₉` and the explicit rational matrix

```
T = [[ 0.18780, −0.17109,  0.04228],
     [−0.55713,  0.37724, −0.08275]].
```

The checker verifies **without floating-point arithmetic** that `C_top=C_boundary+TK` has ALL **36 ordered `2×2` source minors strictly positive**, while `KZ₉=0` gives `C_top Z₉=Y` as an exact **matrix identity**. All **84 ordered `6×6` external minors** are strictly positive. At this strictly positive full-source preimage, eight independent source-coordinate tangent vectors have a nonzero exact `8×8` target-chart Jacobian. Since positivity is open, the submersion theorem implies that `Y` has an open neighborhood in the positive top-cell image: **it is an interior image point**, not an image-boundary face.

This is a concrete counterexample to promoting a *positive boundary-cell pushforward pole* into a *full positive-image boundary pole*. The complex two-sheet four-mass contour really has the previously certified nonzero scalar and fermionic residues at `Y`, but the image itself extends through the target by other strictly positive source matrices. If a full-image canonical form is regular on its interior as required of a positive-geometry canonical form, that contour pole must not survive as a full-image boundary pole. We have **not computed the full image canonical form or its explicit cancellation mechanism**; the conclusion about image *interiority* is exact and independent of such a calculation.

Checker: `research/nima/checkers/check_nine_point_positive_source_pole_image_interior.py`; certificate: `research/nima/results/nine-point-positive-source-pole-image-interior.json`. Source-contour pole: `research/nima/checkers/check_nine_point_four_mass_positive_source_boundary_pole_slice.py`.
