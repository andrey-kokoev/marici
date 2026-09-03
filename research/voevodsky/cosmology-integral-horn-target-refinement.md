# Integral horn target refinement

## Question

What is the complete integral target, and can its tame-sign component be canceled independently?

## Claim boundary

Besides the free components `Xi_log` and `-sigma123`, the target contains the primary sign bit

`epsilon_Z=(0,0,1)`

on `(X,Y,Z)`, where `1` denotes the constant unit `-1`. Since this component has order two, reversing the boundary sign does not change it.

Triangle-supported diagonal corrections span

`(0,0,0)`, `(1,0,1)`, `(0,1,1)`, `(1,1,0)`.

Every vector in this span has even parity, while `epsilon_Z` has odd parity. More generally, `{f,-1}` with principal divisor supported only on the three boundary lines has even valuation parity. It cannot cancel `epsilon_Z`.

Adding another divisor can restore even global parity only by creating an additional nonzero boundary component, contrary to the required zero residual unless a separate sourced cancellation is provided.

## Disposition

The free obstruction still rules out the horn. The mod-two projection is an additional integral consistency condition, linked to the free coefficient by parity rather than an independent direct summand. Rationalization forgets the sign decoration and recovers the earlier target. The next leaf combines these data into the minimal bigraded boundary invariant and audits its functoriality.

## Verification

- `research/voevodsky/check_cosmology_integral_horn_target_refinement.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
