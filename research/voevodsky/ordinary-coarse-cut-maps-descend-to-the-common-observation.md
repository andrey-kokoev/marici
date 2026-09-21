# Ordinary coarse cut maps descend to the common observation

## Result and boundary

There are explicit cut-defined extensions of the ordinary observation in `ordinary-middle-history-observation-descends.md` to both coarse coefficient spaces. They descend through the four-event product quotient. This is a source-coordinate construction with conditional transfer through the admitted function-valued carrier, not an isometry theorem for independently prescribed coarse Green forms.

## Cut formulas

On a four-event path cut uniquely after two events, retain its intermediate vertex l. Write the resulting paths u,v and define, linearly,

    A_L(uv) = D(u) tensor rho(v),
    A_R(uv) = rho(u) tensor D(v).

The targets are direct sums over l. D is the actual local seam derivative and rho is the terminal history record. These formulas are defined on the full four-event path space, then restricted to I4.

At this critical length every element of P4=I4^2 is a sum of products ab of two local relations. Therefore

    A_L(ab)=D(a) tensor rho(b)=0,
    A_R(ab)=rho(a) tensor D(b)=0.

Thus both maps descend to C4=I4/P4. No complement, quotient metric, or assumption that P4 is Green-radical is needed.

On L0=direct_sum C4 tensor R2 and R0=direct_sum R2 tensor C4 define

    F_L([v] tensor c)=A_L(v) tensor D(c),
    F_R(a tensor [v])=D(a) tensor A_R(v).

Use the canonical ordered tensor reassociation to put both outputs in the same labelled seam/history/seam target. Preserve the root carrier once. The displayed formulas concern ordinary coefficient maps; no new suspension convention is being asserted.

For the common ordinary cell, f_L(a tensor [w] tensor c)=[aw] tensor c and f_R(a tensor [w] tensor c)=a tensor [wc]. Consequently

    F_L f_L = D(a) tensor rho(w) tensor D(c) = F_R f_R.

This equality holds before pairing and is independent of all middle lifts. It gives equality against any shared target observer whenever that target pairing is admitted. It does not identify these newly specified cut observations with a pre-existing coarse Green observation.

## Analytical boundary

The history and derivative formulas are linear combinations of retained source features. Their equality transfers under the existing faithful function-valued feature construction with the same typed labels and slot order. In a prescribed common tensor target, paired equality follows without numerical spectral ranks or division by an aggregated spectral denominator.

What is still needed for a claim about inherited coarse forms is a comparison between each coarse carrier's prescribed form and the pullback through A_L or A_R, including actual memory/seam weights, root state dependence, and cross terms. Equality in a shared refined target does not prove those maps are isometries. Nor is a map of the full derived complexes, including the previously constructed shifted observation, supplied here.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_ordinary_coarse_cut_descent.py`

The checker uses the existing actual path derivative and terminal history records. Across all 15 four-event subsets of six events, at root and complementary-prefix starts, it checks 1440 product-basis cut vanishings and 5760 restriction identities. No analytical trace evaluation, independent source-equivariance proof, full complex extension, or coarse metric identification is claimed.
