# The full four-pair Y0 trace is polynomial in bosonized external directions

## Resolved nilpotent-domain gate

Write the external data as `Z=[z|h]`, with `z` eight-by-four of generic rank four and `h` eight-by-two. In the sourced `Y0=[0_(2x4)|I2]` target chart, `U=(C(v)h)^-1 C(v)z`. Therefore the fibre equation at `U=0` is **exactly `C(v)z=0`**, independent of `h` whenever `det(C(v)h)≠0`. For the four-pair eight-dimensional cell there are two simple solutions on the verified generic open set. Set `J_z(v)=det(∂(C(v)z)/∂v)` in the declared row-major target and source-coordinate orders. At a fibre root, the derivative of `(Ch)^-1` multiplies `Cz=0` and vanishes, yielding

    J_U(v) = det(C(v)h)^(-4) J_z(v),
    omega_U(Y0;z,h) = Σ_{two roots v_i} [source_density(v_i)/J_z(v_i)] det(C(v_i)h)^4.

The coefficients and roots depend on `z` only. Thus the COMPLETE two-sheet Y0 coefficient is a genuine homogeneous degree-eight POLYNOMIAL in ordinary commuting `h` (equivalently in the eight quotient coordinates modulo `h→h+zM`). There are no uncanceled `h` denominators on this simple-fibre generic-`z` open set. One can therefore substitute the even nilpotent `h=φ·η` BEFORE the sourced Berezin operation; **the previously unresolved nilpotent regularity gate at Y0 is resolved on that open set without constructing the global Y-dependent rational numerator**. This does not assert regularity across a discriminant or a singular `z`-pole.

## Exact checks and remaining work

At two distinct rational `z` obtained from the positive rank-six witnesses, the checker reconstructs both source roots, verifies `Cz=0` and nonzero `J_z` on each sheet, independently computes the full eight-by-eight `J_U`, and verifies the fourth-power factorization. It constructs the two-sheet polynomial in eight quotient variables, certifies every monomial has degree eight, matches the independently frozen Y0 trace, and checks a second bottom-data deformation not equivalent to `h→h+zM`.

The primary source `1312.2007`, section `The Superamplitude`, maps this now-well-defined polynomial/Berezin operation to the complete on-shell Grassmann integral. Still open: independently evaluate the full `χ1⁴χ5⁴` coefficient and a pole residue with the audited orientation `-1`; derive an explicit global bosonic coefficient away from Y0; assign any nine-point generalized-R history and establish image coverage. No fixed positive target scalar is identified pointwise with a supercomponent.

Checker: `research/nima/checkers/check_four_mass_Y0_polynomial_trace.py`; result: `research/nima/results/four-mass-Y0-polynomial-trace.json`.
