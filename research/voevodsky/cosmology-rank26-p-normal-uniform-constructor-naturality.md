# Uniform source-constructor naturality

## Claim

For either monomial axis and every admissible exponent e, multiplication by the corresponding square monomial commutes with the `T`, `S_K`, and `Q` source constructors. Ambient degree controls only which exponents are admitted.

## Derivation

Every `S_K` row consists of a unit term at e and K-coefficient terms at e+t. Every `Q` row has the same form with q coefficients. Shifting e by twice an axis unit commutes with adding every polynomial-support exponent t, so these rows commute termwise with ambient multiplication.

The raw IBP row contains one coefficient depending only on e and further K/q coefficient terms at e+t. `T` is parameter differentiation of raw rows. Parameter differentiation kills the exponent-only coefficient and differentiates only the K/q coefficients; it does not alter e or t. Thus each `T` term also commutes with the monomial shift. The same argument applies directly to parameter derivatives of K and q relation rows.

No step depends on a numerical ambient degree except the cutoff inequalities ensuring that the shifted descriptor and columns occur in the higher presentation.

## Disposition

P5d3b1 is completed. Constructor naturality is an algebraic arbitrary-degree identity under the frozen relation definitions, not a finite extrapolation.

P5d3b2 becomes active: establish the exact ambient threshold at which the two square-monomial images cover every top-three-degree boundary exponent.

This result does not prove contraction existence at untested degrees; it proves only that any admitted contraction transports through either source map.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_uniform_constructor_law.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_uniform_constructor_law.json`
