# H-minus binding with retained parent and distinct orbital roles

## Question

Give the nested construction [[P,e1],e2] a conditional physical benchmark: can distinct compact/diffuse orbital roles demonstrate binding of the second electron without treating electrons as distinguishable? The retained parent is the original hydrogen state. Active obligation: physical readout under full electron exchange, with source assumptions explicit.

## Claim boundary

Supply the standard fixed-proton, nonrelativistic Coulomb Hamiltonian

\[
H=\sum_{i=1}^2\left(-\frac12\nabla_i^2-\frac1{r_i}\right)+\frac1{r_{12}}.
\]

Use the Chandrasekhar-type symmetric spatial trial

\[
\Psi_{a,b}=\mathcal N\left[e^{-ar_1-br_2}+e^{-br_1-ar_2}\right],
\]

with antisymmetric spin singlet. The orbital roles may have a different radial scale while numbered electron marginals remain identical. Neither the Hamiltonian nor this trial family is derived by the nested syntax. Retaining the parent state means storing its construction, not freezing its orbital in the final state.

All integrals are rational functions of positive a,b after common pi factors cancel. With n_a=1/a^3, n_b=1/b^3, and s=8/(a+b)^3, the common normalization denominator is n_a*n_b+s^2. The kinetic numerator is (a^2+b^2)n_a*n_b/2+ab*s^2; the nuclear-attraction numerator is -(a+b)n_a*n_b-8s/(a+b)^2. Direct and exchange repulsion numerators are

\[
J=\frac{a^2+3ab+b^2}{a^2b^2(a+b)^3},\qquad K=\frac{20}{(a+b)^5}.
\]

The checker independently evaluates the split-domain radial integrals for J and K. It checks the equal-exponent limit against the prior product-state energy.

Freeze b/a=j/1000, j=1,...,1000. For each ratio optimize the common scale exactly through E(lambda)=lambda^2*T+lambda*V. No H-minus affinity input enters selection. The selected ratio is 273/1000, with a approximately 1.0391553 and b approximately 0.2836894.

## Results

| Trial or threshold | Energy in model atomic units |
|---|---:|
| Equal-exponent optimized trial | -0.47265625 |
| Hydrogen plus free electron threshold | -0.5 |
| Unequal-role, exchange-symmetric trial | -0.5133027718 |

The equal-exponent trial does not demonstrate binding; its position above threshold is not a proof of nonbinding. The unequal-role trial is below the dissociation threshold and thus demonstrates variational binding in the supplied Coulomb model. A fixed-parent-exponent trial a=1 also lies below threshold; relaxing the compact orbital lowers energy further. This distinguishes retaining a record from constraining present physics to remain equal to it.

Using only the earlier hydrogen calibration 1 model atomic unit=27.1968 eV:

- first attachment binding: 13.5984 eV, supplied calibration;
- second attachment binding: approximately 0.3617928244 eV, calculated;
- total electronic binding: approximately 13.9601928244 eV.

These are approximate model values, not a precision comparison with measured electron affinity. The finite ratio grid and restricted ansatz are explicit. Finite nuclear mass, relativity and a separately measured energy unit are not incorporated.

## Disposition and verification

A hierarchy-compatible orbital representation can demonstrate second-electron binding while maintaining exact exchange symmetry. The result does not establish a permanent identity of one electron as the inner particle, nor that physical preparation order uniquely selects these orbital roles. It supplies a concrete observable benchmark for the proposed hierarchy; the WG rule selecting the physical interaction and trial class remains absent.

`python research/nima/checkers/check_hminus_nested_orbitals.py` passed via `structured_command_execution:e_32876_1791226257281471100_37`. Exact rational controls include independent radial-integral formulas, exchange invariance, analytic scale stationarity, virial balance, equal-exponent recovery, nonzero repulsion and fixed-parent comparison. Results: `results/hminus-nested-orbitals.json`. No commit or publication is claimed.
