# Decorated boundary column lattice

## Question

What replaces the integer column-lattice criterion when primary tame signs are retained?

## Claim boundary

For general degree-one columns write

`c_j=(n_j,r_j,s_j,other_j)`

with `s_j` in `(Z/2)^3`. Exact chain-level membership in the target `(1,-1,(0,0,1),0,...)` requires integers `a_j` satisfying

- `sum a_j n_j=1`;
- `sum a_j r_j=-1`;
- `sum (a_j mod 2)s_j=(0,0,1)` in all three sign coordinates;
- every other component vanishes.

If diagonal Milnor boundaries spanning the even-parity plane are explicitly admitted, the three sign equations reduce in the cohomological quotient to the single parity equation `sum (a_j mod 2) parity(s_j)=1`. They do not reduce to the two equations stated previously; that claim incorrectly treated the monomial-symbol fiber product as the full chain group.

Mod-two equations can be lifted with auxiliary integer variables and included in an augmented integer lattice test.

## Disposition

The column criterion is corrected: three sign equations govern exact chains, while one parity equation governs the quotient by admitted diagonal boundaries. The free condition still excludes every rank-26 column with zero `Xi_log` coefficient.

## Verification

- `research/voevodsky/check_cosmology_bigraded_boundary_column_lattice.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
