# The direct Y0 four-pair residue matches the independent sourced four-mass pole

## Independent calculation on the same external family

For the exact `⟨5678⟩=-10ε` family in the sourced-ψ Laurent checker, a NEW elimination starts directly from the four-pair bosonic cell `C(w2,w4,w5,w6,w7,w8,t,u)z=0`, not from ψ's auxiliary variables. Because `z1..z4` are the standard four-dimensional basis, the first row fixes `(w5,w6,w7,w8)` linearly in `x=w2` using the inverse of the last-four-row matrix `H=[z5;z6;z7;z8]`. Write `V=w5 z5+w6 z6`, `W=w7 z7+w8 z8`. The first two coordinates of the second row impose the independent quadratic

    -2(3ε+8)x² + 11(ε+6)x - 65 = 0,
    discriminant = 121ε² - 108ε + 196.

The remaining coordinates determine `t,u,w4` rationally in `(x,ε)`. At two explicit rational off-wall parameters (rational points on the discriminant conic), both fibre sheets reconstruct exact `Cz=0` solutions. Direct **eight-by-eight** source-to-`Cz` Jacobians agree sheetwise with the separately derived factorization `J_z=det(H) det[∂(C₂z)/∂(x,w4,t,u)]`. Their complete `η1⁴η5⁴` source-pushforward component equals an independent full starred-ψ quadratic-field trace at both parameters.

More decisively, the direct Y0 checker forms the source density times `det(C_1,C_5)^4/J_z` as an exact rational function of `(x,ε)`, substitutes **both** roots of this independent quadratic, performs their Laurent expansions BEFORE the wall limit, and sums. It finds

    complete normalized Y0 component = (2/325) ε^-1 + O(1)
                                     = (-4/65) ⟨5678⟩^-1 + O(1).

This **exactly matches** the separately implemented sourced-ψ companion-matrix local Laurent computation. The direct Y0 result is stated AFTER dividing the raw ordered eight-φ coefficient by its independently proved factor 2880. The earlier source-coordinate orientation `-1` relative to the authored ordered α chart remains an explicit convention and is not silently changed.

This closes the selected **external four-bracket residue comparison** on the simple-fibre rational family, without constructing the arbitrary-`Y` global rank-six bosonic eight-form, proving positive image coverage or assigning an authored nine-point generalized-R history. Those remain independent research leaves.

Checkers: `research/nima/checkers/check_four_mass_5678_direct_Y0_fibre.py`, `research/nima/checkers/check_four_mass_5678_direct_Y0_residue.py`; results: `research/nima/results/four-mass-5678-direct-Y0-fibre.json`, `research/nima/results/four-mass-5678-direct-Y0-residue.json`.
