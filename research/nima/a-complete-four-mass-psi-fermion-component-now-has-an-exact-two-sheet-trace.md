# A complete four-mass ψ fermion component has an exact two-sheet trace

## Question

Can the sourced starred four-mass ψ expression be evaluated beyond its isolated prefactor, on the SAME four-dimensional quotient by the certified rational nine-point target?

## Claim boundary

Yes, for ONE specified Grassmann monomial. The primary source `positive_grassmannian_update.tex`, equations `r-invariant` (line 1527), `g2n_yangian_invariants` starred row (line 1538) and `four_mass_explicit_solution` (line 1543) fixes `ψ[A,1,2,3,4][B,5,6,7,8]`. For the component `χ_1^4 χ_5^4` in the ordered retained-eight labels, `A=z_7+αz_8` involves only `χ_7,χ_8` and `B=z_3+βz_4` only `χ_3,χ_4`. Hence auxiliary fermions cannot enter this component. Its complete branch coefficient is

    ψ × <2,3,4,A>^4 / product_cyclic_5(<A,1,2,3,4>)
      × <6,7,8,B>^4 / product_cyclic_5(<B,5,6,7,8>).

Every four-bracket is the exact six-dimensional determinant of `(Y1,Y2,Z_i,Z_j,Z_k,Z_l)` for the same rational target and positive moment-curve external data. The checker substitutes the SOURCED coupled auxiliary equations, reduces the whole product in the quadratic field of `α`, and stores its nonzero exact two-branch trace as a 290-character rational in `nine-point-complete-four-mass-psi-component-trace.json`. Its reduced ψ prefactor independently agrees with the prior `Tr(ψ)=1` packet. A separate 110-digit check evaluates the RAW ψ and BOTH five-bracket factors at each root and reproduces the exact trace; omitting ψ or reversing the second branch fails.

This is a complete sourced SUPERFUNCTION COMPONENT at one external and target datum, NOT an equality with the separately certified traced TARGET eight-form density. Such an equality requires a source-derived bosonization/component-to-volume map fixing fermionic conventions, target-chart Jacobian and orientation; equal algebraic fields or raw scalars do not supply it. Inclusion as a nine-point generalized-R history also remains unverified.

## Disposition

The specified complete source component trace is exact at this one target. Next falsifier: construct the typed map from this `χ_1^4 χ_5^4` coefficient to a row-major `B=(CZ)[:,0:2]^-1 CZ[:,2:6]` volume coefficient at identical external data, then compare to the certified two-sheet target trace, including normalization and one pole residue. If no sourced map exists, close ONLY this comparison branch with that typed blocker, not the programme.

Checkers: `research/nima/checkers/check_nine_point_complete_psi_component_trace.py`, `research/nima/checkers/verify_nine_point_complete_psi_component_trace.py`.
