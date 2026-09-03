# Ratio-line-bundle triviality

## Question

Do the intended wall equations trivialize the ratio line bundles controlling integral descent?

## Claim boundary

They do on the affine normal slice: `U,V,P` are coordinates, so all three conormal lines and both ratios are trivial.

Globally, if `l1,l2,l3` are sections of one line bundle `L` and identify the three conormal summands with `L|C`, then

`L1 L3^-1` and `L2 L3^-1`

are canonically trivial. The ratios `u=l1/l3` and `v=l2/l3` are global rational functions and the Cech K2 obstruction vanishes.

A global equation `l3=l1+l2+p` is itself typed only when all terms lie in a common additive line or module. Thus any global carrier realizing the displayed equation automatically passes this ratio gate.

The current artifacts do not materialize those global sections or their common line bundle; they prove only the local statement.

## Disposition

Ratio triviality adds no obstruction after a common-line carrier constructor exists. The next leaf builds the universal full integral horn over that category and proves base-change naturality.

## Verification

- `research/voevodsky/check_cosmology_ratio_line_bundle_triviality.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
