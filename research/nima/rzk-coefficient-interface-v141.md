# v141: L2 residual/free-detector separation correction

A provenance audit catches an important distinction. The labelled L2 residual
from source `s11:minus:q` is `3a^3+3a^3b`. The all-degree alternating detector
restricts to `a=0`, so its value on this residual is zero. By contrast its value
on the chosen free complement `1` is one.

Therefore the s11 L2 residual is not the unit-detected free cokernel class. The
unit-cone construction of modules 152--168 is mathematically valid only as a
conditional extension if the eventual geometric road residual has unit
detector value; it is not a realization of the known s11 residual.

This restores the correct frontier: L2 addresses the rank-one Bockstein defect,
while the constant unit describes a separate free complement of the completed
plus matrix. A global road computation must identify which class the physical
Cech residual actually occupies before attaching the cone.

Evidence is `results/L2-residual-vs-free-detector.json` from
`checkers/check_L2_residual_vs_free_detector.py`.
`rzk/169-l2-residual-free-detector-separation.rzk.md` passes all eight
declarations without assumptions.
