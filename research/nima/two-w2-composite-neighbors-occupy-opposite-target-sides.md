# Two composite `w₂` neighbors occupy opposite target-normal sides

Three distinct positive boundary controls classify the **target-normal geometry** of the sourced cell A and its two positive composite `w₂=0` neighbors. Denote by **V** the previously found vertical physical-column-2 neighbor, and by **E** the new label-3-sensitive neighbor with physical column 2 zero and column 3 `(w₂,0)`. All three have the **same complete boundary matrix**, the same seven target-Jacobian tangent columns, and **nonzero rank-eight Jacobians** at the controls. Their source-residue orientations are A negative, V positive, E positive.

Quotienting the eight-dimensional target tangent chart by the common seven-dimensional boundary tangent image gives one target-normal coordinate. In **all three** exact positive controls:

```
relative normal side:  V/A = negative,    E/A = positive,    E/V = negative.
```

Thus **A and V occupy opposite local target sides** of the shared facet, while **A and E occupy the same side**; V and E are opposite. Both pairs A/V and A/E have algebraically canceling oriented local pole residues, but they realize **different positive image geometry**—one as opposite-side adjacency, the other as overlapping-image cancellation. This is a concrete reason not to infer a unique target triangulation or contour from source-facet cancellation alone.

Checker: `research/nima/checkers/check_nine_point_two_composite_neighbors_target_sides.py`; certificate: `research/nima/results/nine-point-two-composite-neighbors-target-sides.json`.
