# K2 integral Tate lattice

## Question

Do the normalized period and Parshin residue detect the same primitive integral class?

## Claim boundary

Yes. The complex torus `(C*)^2` deformation retracts to `T^2`, so its second homology and cohomology are each `Z`. The class

`c=(2 pi i)^(-2) dlog(u) wedge dlog(v)`

pairs to one with the ordered positive torus. Under Betti-de Rham comparison, `Xi_log` therefore represents the generator of the rank-one Tate lattice `Z(-2)`, equivalently the corresponding generator in `H^2(U,Z(2))` after fixing the twist convention.

For the three-line SNC compactification, the top-weight comparison identifies this lattice with first homology of the dual triangle. The oriented vector `(1,1,1)` is primitive, and the comparison matrix is `(1)` up to orientation sign. There is no torsion or hidden divisibility.

## Disposition

The period and Parshin flags detect one primitive integral class. Rational rescaling or finite-index lattice enlargement cannot remove the obstruction. The next leaf tests whether any mixed-Hodge extension data exists that could mimic a degree-one Bockstein despite this pure Tate class.

## Verification

- `research/voevodsky/check_cosmology_K2_integral_Tate_lattice.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
