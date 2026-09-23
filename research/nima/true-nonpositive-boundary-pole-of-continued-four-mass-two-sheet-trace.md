# A genuine boundary pole of the continued trace, distinct from its branch discriminant

On the exact rank-six target slice `Y[0,4]↦Y[0,4]+ε`, the preceding regular-fold analysis showed that the **inverse discriminant is not a trace pole**. To locate *actual* poles, take the resultant of the inverse quadratic `P(q,ε)` with the numerator of each of the eight dlog source factors `w₂,w₄,w₅,w₆,w₇,w₈,u,t−u`. These candidate source-boundary images are disjoint from both discriminant roots. Resultant factors shared by many source factors include chart/leading-degree exceptionalities and are NOT automatically genuine form poles.

One candidate survives a full residue test: at the exact rational value

```
ε = 181/4336,
```
precisely one of the two distinct rational inverse sheets, `q=17/28`, meets `w₈=0`; the other sheet has `q=−585602875/143178188776` and **all** its dlog factors remain nonzero. At the polar sheet, the row gauge, every *other* dlog factor, and the complete `8×8` source-to-target chart Jacobian are nonzero. The implicit derivative `dw₈/dε` along that inverse sheet is nonzero. Therefore its oriented density/Jacobian has a **simple pole** whose residue is computed exactly and is nonzero. The four-flavor `XXXX` coefficient also has a nonzero residue; there is no possible cancellation by the regular conjugate sheet. This distinguishes an actual dlog-image pole of the analytically continued **two-sheet contour** from a spurious square-root branch singularity.

**Positivity warning:** at this target both algebraic inverse sheets have `w₄<0`. The polar sheet is NOT on the positive four-pair source cell. Thus this is a pole of its continued algebraic trace, **not** a demonstrated boundary or pole of the positive source image, the complete nine-point image canonical form, or the physical full amplitude. It illustrates why identifying complex-contour poles with positive geometry requires a separate contour argument.

Checkers: `research/nima/checkers/check_nine_point_four_mass_boundary_norm_slice.py` and `research/nima/checkers/check_nine_point_four_mass_true_boundary_pole_slice.py`. Results: `research/nima/results/nine-point-four-mass-boundary-norm-slice.json`, `research/nima/results/nine-point-four-mass-true-boundary-pole-slice.json`.
