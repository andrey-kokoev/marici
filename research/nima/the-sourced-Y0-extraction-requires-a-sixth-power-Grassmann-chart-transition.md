# Sourced Y0 extraction requires a sixth-power Grassmann chart transition

## Question

Can the row-major eight-form coefficient already certified at the positive nine-point target be evaluated at the primary source's localization plane `Y0`?

## Exact result

No: the old target chart fixes `Y=[I2|B_L|B_R]` (pivot in the FIRST two ambient columns), while source `amplituhedron.tex`, section `The Superamplitude`, fixes `Y0=[0_(2x4)|I2]` (pivot in the LAST two). The former chart is undefined at `Y0`. In the appropriate chart write `Y=[U_L|U_M|I2]`, with two-by-two blocks and eight coordinates ordered row-major. On their overlap,

    B_R=U_L^-1,          B_L=U_L^-1 U_M.

The derivative in `U_M` of `B_L` has determinant `(det U_L)^-2`; the derivative in `U_L` of `B_R` has determinant `(det U_L)^-4`. Exchanging the two four-coordinate blocks contributes no sign, so the FULL oriented target eight-form change is

    d^8B = (det U_L)^-6 d^8U,
    omega_U(U;Z) = omega_B(B(U);Z)/(det U_L)^6.

A block-Jacobian derivation and an independent exact numerical eight-by-eight Jacobian at `U_L=[[2,1],[1,3]]`, `U_M=[[1,2],[3,4]]` both give `1/5^6`. A wrong fifth power fails. At sourced `Y0`, `U=0`, so the old `B` chart has no value there. Along `U_L=eps I2,U_M=0`, the transition carries the pole `eps^-12`. A finite `omega_U` requires the transformed `omega_B(B(U);Z)` to cancel this pole; the fixed positive-target evaluations contain no such regularity certificate.

## Disposition

The exact chart normalization is available, but the global FOUR-PAIR traced form is not. Two independent obstructions must be addressed in the correct order: first express and continue the full rational traced target form from rank-six positive external data to the sourced `U=0` chart with the above sixth-power factor; then check regularity under the nilpotent external specialization and perform the source-prescribed Berezin extraction. The earlier pointwise fermion-versus-density scalar comparison has no source authority. No nine-point history or form equality follows from this chart calculation.

Checker: `research/nima/checkers/check_nine_point_Y0_chart_transition.py`; result: `research/nima/results/nine-point-Y0-chart-transition.json`.
