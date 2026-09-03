# Algebraic first-jet zero theorem

## Theorem

Let `C1 -> C0` be the labelled IBP/K/q relation presentation at any even ambient degree at least 12. For every relation generator `R` and every rational direction `v` in the declared `(x,y,z)` parameter space,

\[
[D_vR]=0\quad\text{in }C_0/\operatorname{im}(d_1).
\]

The verified directions

\[
n_x=(1,0,0),\qquad t_1=(1,-1,0),\qquad t_2=(3,0,-1)
\]

form a unimodular basis. Explicitly, for `v=(x,y,z)`,

\[
v=(x+y+3z)n_x-y t_1-z t_2.
\]

Exact absorption of the three basis derivatives and linearity prove the claim. Integral directions have integral coefficients in this decomposition.

## Corollary

Every rational or integral normal satisfying `dp(n)=1` has the same zero quotient class. More strongly, no first-derivative direction inside the declared three-dimensional parameter space can produce a nonzero algebraic Bockstein while the quotient remains unchanged.

## Claim boundary

The maximal sourced scope is the characteristic-zero labelled algebraic first-jet presentation with squared-axis transport over all even degrees at least 12. The theorem does not supply a geometric normal bundle, DNC or support filtration, exceptional specialization, external deformation parameter, higher jet, or physical class.

## Verification

- `research/voevodsky/check_cosmology_algebraic_first_jet_zero_theorem.py` — exit 0
- `research/voevodsky/results/cosmology_algebraic_first_jet_zero_theorem.json`
