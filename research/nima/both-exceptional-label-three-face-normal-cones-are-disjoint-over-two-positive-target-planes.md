# Both exceptional label-3 face normal-ray families are disjoint over exact positive target planes

The exceptional cube edges `E_B/E_D` and `F_B/F_D` both blow down to **six-dimensional images** of seven-dimensional source faces, with **two-dimensional target-normal quotients**. Their opposite source residues cannot be paired as ordinary codimension-one poles. A stronger exact cone comparison now quantifies **all positive source-face preimages** over **two specified positive target planes per edge**.

For `F_B/F_D`, each target-face fibre is an open **one-dimensional positivity interval**. Vary its F_B and F_D parameters **independently** over their complete intervals. The normal-wedge numerator is bilinear; after shifting both interval parameters to positive coordinates `x,y` it takes the form

```
first target:  911547xy − 498232x − 84896y,
second target: 2129793939xy − 9296821450x − 1383591650y.
```

The first positive interval has width `56/159`; the second has exactly the certified width in the result JSON. On **each entire open positivity rectangle**, the exact bound `A·width<B` for `Axy−Bx−Cy` proves the wedge is **strictly negative**. **No pair of positive F_B/F_D face preimages has parallel transverse normal rays over either target plane.**

For `E_B/E_D`, choose the strictly ordered nine-point moment-curve external nodes `(1,3/2,2,4,5,6,7,8,9)`. Deleting its zero physical row 2 recovers **exactly** the original eight-point B/D source matrices and positive external data. The already certified all-positive-face-fibre nonparallel normal-cone inequalities therefore transfer identically to E_B/E_D on its two fixed target planes.

This is **stronger than a single-source-point normal test**, but still restricted to four exact target planes. It does not exclude more complicated nonlinear gluing, other cells or a valid global contour, and it does not construct the nine-point image form.

Checker: `research/nima/checkers/check_nine_point_vertical_label3_exceptional_positive_normal_cones.py`; result: `research/nima/results/nine-point-vertical-label3-exceptional-positive-normal-cones.json`.
