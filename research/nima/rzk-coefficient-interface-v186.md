# v186: conductor cell has the selected primitive normalization

The source-derived qg2 conductor coefficient

`c=-1/(32 p^4 (kappa-1)^2)`

is a unit in the physical localized coefficient ring where p and kappa-minus-one
are inverted. Its inverse is

`c^-1=-32 p^4 (kappa-1)^2`.

Stripping this unit from the conductor connecting cell produces a primitive
orientation generator with detector value one. This matches the explicit L2
normalization `rho0(v)=1` for `v=a^3+a^3b` and the primitive logarithmic normal
link generator.

Thus there is no remaining scalar or denominator mismatch among the three
selected rank-one lines. The remaining comparison is geometric: identify the
normalized conductor orientation line with the log orientation line and
construct its ambient relative cut-chain transport. Scalar matching alone does
not supply that identification.

Evidence is `results/qg2-conductor-primitive-normalization.json`.
`rzk/214-qg2-conductor-primitive-normalization.rzk.md` passes all eight
declarations without assumptions.
