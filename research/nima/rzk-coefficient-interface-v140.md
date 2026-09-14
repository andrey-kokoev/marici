# v140: unit-cone pushout condition

The contractible cone construction is now stated with the necessary gluing
qualification. The standalone complex `Z<c> -> Z<1>` is contractible, but the
road correction is its pushout along a map sending the cone unit to the
existing residual `r`.

In the pushout the new cell has differential `-r`. Closure of `r` gives
`d^2=0`; `lambda(r)=1` gives detector pairing `-1`; and the new column kills the
free detector class. The pushout itself need not be contractible—it kills the
class of r—and the previously identified integral torsion remains.

Thus the exact geometric datum is a map from the cone's unit line to the closed
soft nearby-cycle residual, not merely existence of an abstract contractible
pair. This prevents overclaiming from module 167.

Evidence is `results/soft-axis-unit-cone-pushout.json` from
`checkers/check_soft_axis_unit_cone_pushout.py`.
`rzk/168-soft-d1-unit-cone-pushout.rzk.md` passes all eight declarations without
assumptions.
