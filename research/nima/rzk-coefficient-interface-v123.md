# v123: all-degree alternating detector proof

The alternating functional is now proved directly from the column formulas,
without cutoff extrapolation.

Write `lambda(f)=f(0,-1)`. Every p-column has positive a-order. The derivative
part of every q-column also has positive a-order. The only possible zero-a-order
q term occurs for `i=0, eb=1`; it contains `(1+b)^ea` with `ea>=1`, so lambda
annihilates it. Every L2 completion column is multiplied by `a^2` and is likewise
annihilated.

The functional is integral and primitive because `lambda(1)=1`. For
`sa=sb=1, i=0`, the q-columns are `-7 b^j(1+b)`, which span the truncated
`(1+b)` ideal over Q. Consequently evaluation at `b=-1` generates the free
rank-one cokernel in every degree. Integral torsion remains a separate issue.

Evidence is `results/soft-axis-alternating-detector-all-degree.json` from
`checkers/check_soft_axis_alternating_detector_all_degree.py`.
`rzk/151-soft-d1-alternating-detector-all-degree.rzk.md` passes all eight
declarations without assumptions.
