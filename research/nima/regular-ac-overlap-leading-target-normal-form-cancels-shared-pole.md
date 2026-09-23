# Regular A/C overlap cancels its shared target-normal pole at leading order

At two exact positive common corners, A and C have regular `8×8` target maps and **overlapping**, rather than disjoint, positive target-normal cones. In A's local normal target coordinates `(X,Y)`, its positive source normals are `(w₄,v)=(X,Y)`, where `v=t−u`. C's slope-gap ray lies inside A's cone, so its normal map has the form

```
(X,Y) = (w₄,C+α v_C, β v_C),       α,β>0,
c=α/β.
```

The exact oriented source signs are A negative and C positive. Factoring out their common regular six-dimensional corner density and **full common fermionic numerator**, the leading homogeneous pushed **normal two-form** on their overlap `X>cY>0` has densities

```
A:   −1/(XY),
C:   +1/[Y(X−cY)],
A+C: c/[X(X−cY)].
```

Thus the **shared `Y=0` pole cancels** in this local common-target leading term, even though the full two-forms do not cancel. The exact positive ratios are `c=3822/4169` and `c=37170/26531` at the two certified corners. This supplies an explicit target-chart counterpart of the regular A/C adjacency cancellation and illustrates why overlapping source-cell images need careful oriented addition rather than a disjoint triangulation assumption.

The calculation is a **linearized leading normal-form model** around two corners—not a complete nonlinear pushed eight-form, a treatment of singular B/D sectors, or the global nine-point canonical form.

Checker: `research/nima/checkers/check_nine_point_regular_ac_corner_leading_image_form.py`; result: `research/nima/results/nine-point-regular-ac-corner-leading-image-form.json`.
