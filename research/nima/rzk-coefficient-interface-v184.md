# v184: unique necessary qg12 grade-normalization factor

The known qg1 collision residue and qg2 endpoint residue determine the unique
scalar that would make their oriented node residues cancel. With

`r_g1=-(kappa-3)/(64 p^4 (kappa-1)^2)`

and

`r_g2=-1/(16 p^3 (kappa-1)^2)`,

the equation `r_g1+N r_g2=0` forces

`N=-(kappa-3)/(4p)`.

This predicts both the inverse-p valuation needed for the grade shift and a
nontrivial kappa-dependent normal factor. It is stronger than the earlier
informal suggestion to multiply by x.

The factor is only a necessary target-derived value, not an authorized
normalization. A valid `N_epsilon` must independently recover it from the
parent normal-coordinate Jacobian or regulated chain. Any source computation
producing a different coefficient falsifies the selected road comparison.

Evidence is `results/qg12-required-grade-normalization.json`.
`rzk/212-qg12-required-grade-normalization.rzk.md` passes all eight declarations
without assumptions.
