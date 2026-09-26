# Generalized R calibration and first complete50-term component sums

Extended `nine_point_source_r.py` with both inner branches and boundary substitutions. The transported replacement spinor uses the same epsilon convention calibrated by ordinary R. At upper/lower limits it replaces the explicit spinor in both numerator angle brackets and denominator contractions; the theta numerator rows remain sourced.

Independent representation check: construct the shifted momentum supertwistors as line/plane intersections, carrying their full linear chi coefficients. For left nesting the anchor lies on(a1-1,a1) intersecting(9,b1-1,b1); the shared boundary point lies on(b1-1,b1) intersecting(9,a1-1,a1). Compare outer/inner products through all36 two-row wedge coordinates and their bosonic prefactors. All50 histories at each of two rational moment-curve inputs agree exactly, including30 boundary-corrected histories per input. This checks the complete degree-eight tensor product up to the compensated fourth-power row scale at those inputs, not just selected pair ratios.

`check_nine_point_tree_components.py` then evaluates all50 source terms for three components of the normalized ratio P9^NNMHV. At Z_i=(1,i,i^2,i^3), results are:

* chi3^4 chi5^4:10711673/4147200 (24 nonzero terms)
* chi2^4 chi5^4:382363/403200 (33 nonzero terms)
* chi1^4 chi5^4:164505619/18579456000 (22 nonzero terms)

A second nonuniform rational input is recorded in results/nine-point-tree-components.json. Full amplitude includes the sourced MHV prefactor; these are ratio-function coefficients, with flavor-grouped Grassmann convention.

Commands: `uv run --with sympy python research/voevodsky/checkers/check_nine_point_inner_r.py` and the analogous tree-components checker. Both pass fresh.

Do not insert these numbers into the earlier two-family matrix: its data are bosonized target/fibre values, not these newly chosen external4D twistor configurations. Matching requires the same target/frame and correct full-superform map. Next use an independent recursion representation or cyclic re-anchoring of the50-term expression to test the summed amplitude, then explicitly align kinematics with the fork if a geometric comparison is desired. Finite exact agreement does not yet prove an all-target amplitude/contour identity.
