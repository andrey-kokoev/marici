# The full four-mass Berezin map and a selective source-pole residue

## A full-superfunction statement, not another component fit

Let `X_(i,A)=(Cη)_(i,A)` for `i=1,2` and `A=1..4`. At generic `z`, the previously proved Y0 polynomial is `Σ_i [source_density(C_i)/J_z(C_i)] det(C_i h)^4`, and `h=φη` is well-defined even Grassmann data. Extracting the eight ordered `φ` generators from `det(Σ_A φ_j^A X_(i,A))^4` produces exterior degree eight in the **eight independent odd X generators**. Their top exterior space is one-dimensional. Computing that one scalar in a freely generated ordered exterior algebra gives the universal identity

    [φ1^1⋯φ1^4 φ2^1⋯φ2^4] det(Σ_A φ_j^A X_(i,A))^4
      = 2880 X_(1,1)⋯X_(1,4) X_(2,1)⋯X_(2,4).

Thus dividing the RAW ordered Berezin extraction by 2880 identifies the **complete fermionic polynomial**, not just `η1⁴η5⁴`, with the bosonic-delta-localized Grassmannian super-integral of the same oriented cell on the generic simple-fibre locus. This is an algebraic normalization in the DECLARED φ/X order, not a claim about an unspoken convention of the cited source. The published α-coordinate dlog order differs from our raw cyclic-residue orientation by `-1`; a plus-starred-ψ label still needs that sign reconciled.

## Independent boundary control

At the intrinsic cell pole `w2=0`, the raw source-form residue is

    Res_(w2=0) Ω_source = -dw4⋯du/[w4 w5 w6 w7 w8 u(t-u)]

in the declared remaining coordinate order. The `η1⁴η5⁴` fermionic numerator is `det(C_1,C_5)^4=(w5 t)^4`, so the nonzero residue coefficient before the universal 2880 factor is

    -w5³ t⁴/[w4 w6 w7 w8 u(t-u)].

At the positive exact control point `(w4,w5,w6,w7,w8,t,u)=(1,1,1,1,1,3,2)` it equals `-81/2`. Conversely, for `η2⁴η5⁴`, `det(C_2,C_5)^4=(w2 w5 t)^4`; it cancels the `1/w2` source pole and the residue is exactly zero. The authored α1-first dlog orientation reverses the displayed raw sign. **This is a source-coordinate dlog pole, not yet an independently identified momentum-twistor `z`-pole** of the global traced function; no such external pole is claimed here.

Remaining: locate/compare an external four-bracket pole with independent sourced ψ, compute an explicit `Y`-dependent global bosonic trace, and settle nine-point generalized-R history/coverage separately.

Checker: `research/nima/checkers/check_four_mass_full_superfunction_and_source_residue.py`; result: `research/nima/results/four-mass-full-superfunction-source-residue.json`.
