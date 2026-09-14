# v159: all-degree L2 filtered projection

The finite cutoff-projection checks are now upgraded to an all-degree support
argument.

Expanding every p/q operator case shows that each nonzero labelled column
raises `a+b` degree by one of `2,3,4,5,6,7`; no column preserves or lowers
source degree. These shifts are independent of the source exponents: translating
a monomial shifts input and output degrees equally, while the derivative and
fixed L1/L2/k multipliers determine the listed offset.

Consequently a source introduced above cutoff D has no output in target degrees
at most D. The labelled matrices therefore form a strict filtered projection
system in all degrees, not merely through the five computed cutoffs.

This supplies canonical global chain-level transition maps for a derived tower.
Compatibility of chosen torsion-saturation cells remains open, but the base
filtered system they must lift is now proved.

Evidence is `results/L2-all-degree-filtration-shift.json` from
`checkers/check_L2_all_degree_filtration_shift.py`.
`rzk/187-l2-all-degree-filtration-projection.rzk.md` passes all six declarations
without assumptions.
