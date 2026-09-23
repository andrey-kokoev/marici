# Four-mass quartic secant uniqueness rules out history 9 in any two-term sum

The previous residual rank-one test excluded coefficients ±1 for the only two nine-point histories whose explicit endpoints match the four-pair support. A stronger obstruction excludes **any** scalar coefficient of ordinary history 9 in a representation with only one other sourced R×R history, even if that coefficient varies with kinematics.

At generic four-dimensional external data, restrict the complete four-mass Grassmann polynomial to two ordered η-pairs, `X=(1,5)` and `Y=(2,6)`, independently for each of four supersymmetry flavors. The five flavor-selected coefficients form a binary quartic moment sequence

    F_j = Σ_{i=1,2} s_i x_i^(4−j) y_i^j,    j=0,…,4,

where `C_i` are the TWO algebraic fibre sheets, `x_i=Δ_i(1,5)`, `y_i=Δ_i(2,6)`, and `s_i=source_density(C_i)/J_z(C_i)`. The associated three-by-three Hankel matrix `H_(a,b)=F_(a+b)` has rank two. Its one-dimensional kernel is the quadratic `(r−r₁)(r−r₂)`, with `r_i=y_i/x_i`. **Any** representation by only two flavor-blind products of fermionic δ⁴ factors has the SAME Hankel kernel and thus must use the SAME two pair ratios (up to permutation); this follows directly because the two geometric-series columns span H. It is not an assumption about a particular generalized-R momentum-twistor formula.

For ordinary history 9, the complete two-five-bracket numerator gives pair ratio

    r₉ = [⟨3,4,8,1⟩⟨7,8,4,5⟩] / [⟨2,3,4,8⟩⟨6,7,8,4⟩]

in retained local labels. Two independently generated generic rational `z` in positive four-pair source nullspaces have simple, reconstructible fibre sheets, nonzero histories' denominators, rank-two Hankel matrices, and **nonzero** `(r₉−r₁)(r₉−r₂)`. Hence history 9 is not one of the two rank-one summands, whatever scalar weight it carries. The complete four-mass invariant CANNOT be history 9 plus ANY single other authored R×R history (including transported-spinor history 27), even with kinematic-dependent coefficients. If history 9 participates in such a decomposition, it needs at least THREE nonzero decomposable terms.

This does not exclude a three-or-more-history representation, cancellations of physical label 3 across additional terms, or a full-amplitude equality. The next source question is which larger authored history subset, if any, reproduces the full fermionic tensor AND the independently verified external four-bracket residue.

Checker: `research/nima/checkers/check_nine_point_four_mass_secant_uniqueness.py`; result: `research/nima/results/nine-point-four-mass-secant-uniqueness.json`.
